#!/usr/bin/env python3
"""Fail-closed source audit for the expanded WOW-284 manuscript."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
TEX_PATH = ROOT / "v22" / "main.tex"
BIB_PATH = ROOT / "v22" / "references.bib"

EXPECTED_TITLE = "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284"
EXPECTED_EMAIL = "samuil.petkov@phys.ens.psl.eu"
EXPECTED_TAG = "v2.2.2"


def citation_keys(tex: str) -> list[str]:
    output: list[str] = []
    pattern = re.compile(r"\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]*)\}")
    for match in pattern.finditer(tex):
        output.extend(item.strip() for item in match.group(1).split(",") if item.strip())
    return output


def bibliography_keys(bib: str) -> list[str]:
    return re.findall(r"@[A-Za-z]+\{([^,]+),", bib)


def referenced_labels(tex: str) -> list[str]:
    return re.findall(r"\\(?:ref|eqref|pageref|autoref)\{([^}]+)\}", tex)


def check_theorem_labels(tex: str) -> None:
    for environment in ("theorem", "proposition", "lemma", "corollary", "conjecture"):
        pattern = re.compile(
            rf"\\begin\{{{environment}\}}(?:\[[^\]]*\])?(.*?)\\end\{{{environment}\}}",
            re.DOTALL,
        )
        for index, block in enumerate(pattern.findall(tex), start=1):
            if "\\label{" not in block:
                raise AssertionError(f"unlabelled {environment} block #{index}")


def check_repository_paths(tex: str) -> list[str]:
    checked: list[str] = []
    for command in ("codefile", "datafile"):
        for value in re.findall(r"\\" + command + r"\{([^}]+)\}", tex):
            path = ROOT / value
            if not path.is_file():
                raise AssertionError(f"missing {command} target: {value}")
            if value.startswith(".agent-coordination") or "private" in value.lower():
                raise AssertionError(f"private/internal path exposed in manuscript: {value}")
            checked.append(value)
    for value in re.findall(r"\\path\{([^}]+)\}", tex):
        # The command definitions contain the literal macro argument
        # ``\path{#1}``; only concrete manuscript paths are repository targets.
        if value == "#1":
            continue
        path = ROOT / value.rstrip("/")
        if not path.exists():
            raise AssertionError(f"missing path target: {value}")
        checked.append(value)
    return checked


def main() -> None:
    tex = TEX_PATH.read_text(encoding="utf-8")
    bib = BIB_PATH.read_text(encoding="utf-8")

    if any(ord(char) < 32 and char not in "\t\n" for char in tex + bib):
        raise AssertionError("forbidden control byte")
    if "\ufffd" in tex + bib:
        raise AssertionError("Unicode replacement character")

    for required in (
        EXPECTED_TITLE,
        rf"\email{{{EXPECTED_EMAIL}}}",
        rf"\newcommand{{\RepoTag}}{{{EXPECTED_TAG}}}",
        r"\(N(v)\) for its open neighbourhood",
        r"If \(\delta\) is the ordinary minimum degree",
        r"average row quotient is similar to the",
        r"symmetric compression on normalized layer indicators",
    ):
        if required not in tex:
            raise AssertionError(f"required manuscript marker missing: {required}")

    forbidden_phrases = (
        "Exact Counterexamples and Spectral Mechanisms for WOW-284",
        "v2.1.0",
        "first counterexample",
        "smallest counterexample",
        "previously unknown",
        "new distance spectrum",
        "all Lean is done",
        "fully formalized LP ceiling",
        "proof sketch",
        "TODO",
        "FIXME",
    )
    lower_tex = tex.lower()
    for phrase in forbidden_phrases:
        if phrase.lower() in lower_tex:
            raise AssertionError(f"forbidden or stale phrase: {phrase}")

    labels = re.findall(r"\\label\{([^}]+)\}", tex)
    duplicates = sorted(key for key, count in Counter(labels).items() if count != 1)
    if duplicates:
        raise AssertionError(f"duplicate labels: {duplicates}")
    missing_labels = sorted(set(referenced_labels(tex)) - set(labels))
    if missing_labels:
        raise AssertionError(f"undefined cross-references: {missing_labels}")
    check_theorem_labels(tex)

    bib_keys = bibliography_keys(bib)
    duplicate_bib = sorted(key for key, count in Counter(bib_keys).items() if count != 1)
    if duplicate_bib:
        raise AssertionError(f"duplicate bibliography keys: {duplicate_bib}")
    citations = citation_keys(tex)
    missing_citations = sorted(set(citations) - set(bib_keys))
    if missing_citations:
        raise AssertionError(f"undefined citations: {missing_citations}")

    paths = check_repository_paths(tex)

    theorem_verifiers = {
        "thm:regular-degree-six": "scripts/verify_proof_audit_04_regular_low_degree.py",
        "thm:endpoint-diameter": "scripts/verify_proof_audit_10_endpoint_diameter.py",
        "thm:diameter-four": "scripts/verify_proof_audit_11_diameter_four.py",
        "thm:lp-ceiling": "scripts/verify_proof_audit_02_two_sided_lp.py",
        "thm:degree-six-fifty": "scripts/verify_proof_audit_01_edge_local.py",
        "thm:order50-feasibility": "scripts/verify_proof_audit_06_order50_feasibility.py",
        "thm:one-puncture": "scripts/verify_proof_audit_05_small_moore_punctures.py",
        "thm:edge-puncture": "scripts/verify_proof_audit_05_small_moore_punctures.py",
        "thm:nonadjacent-puncture": "scripts/verify_proof_audit_03_nonadjacent_puncture.py",
        "thm:small-puncture": "scripts/verify_proof_audit_12_small_puncture.py",
        "thm:hs-radius": "scripts/verify_proof_audit_13_hs_robustness.py",
        "thm:prime-field": "scripts/verify_proof_audit_08_prime_field.py",
        "thm:matching-deletions": "scripts/verify_proof_audit_07_layer_matchings.py",
    }
    for label, verifier in theorem_verifiers.items():
        if label not in labels or verifier not in tex:
            raise AssertionError(f"theorem/verifier mapping missing: {label} -> {verifier}")

    lean_claim_markers = (
        "the analytic LP\noptimum and rigidity for every integer \\(k\\ge4\\)",
        "proves that it is admissible and attains equality",
        "both as a\npolynomial and at coefficient level",
        "This LP formalization is deliberately graph-independent",
        r"the trace interpretation of the \(F_i(A)\)",
        "are likewise analytic results supported by exact Python audits; they are not",
        "part of the Lean claim",
    )
    for marker in lean_claim_markers:
        if marker not in tex:
            raise AssertionError(f"Lean claim or scope marker missing: {marker}")
    if (
        "The public endpoint axiom reports contain only" not in tex
        or r"\texttt{propext}, \texttt{Classical.choice}, and \texttt{Quot.sound}"
        not in tex
    ):
        raise AssertionError("axiom-scope statement missing")

    report = {
        "labels": len(labels),
        "references": len(referenced_labels(tex)),
        "citation_occurrences": len(citations),
        "cited_sources": len(set(citations)),
        "bibliography_entries": len(bib_keys),
        "repository_paths_checked": len(paths),
        "theorem_verifier_mappings": len(theorem_verifiers),
    }
    print("v2.2 integrated manuscript audit: PASS")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
