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
EXPECTED_TAG = "v2.2.6"


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

    if any(ord(char) < 32 and char != "\n" for char in tex + bib):
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
        "first proof that WOW-284 is false",
        "first Lean formalization",
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
    if re.search(r"n\s*(?:\\leq?|<=|≤)\s*49", tex):
        raise AssertionError("unsupported positive order-49 bound")

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
        "thm:integral-slack": "scripts/verify_integral_optimal_slack_collapse.py",
        "thm:three-to-one": "scripts/verify_three_to_one_excess_bound.py",
        "cor:three-to-one-equality": "scripts/verify_three_to_one_equality_rigidity.py",
        "prop:signed-complement": "scripts/verify_signed_complement_bridge.py",
        "prop:order50-minus-two": "scripts/verify_order50_minus_two_multiplicity.py",
        "thm:order50-disconnected": "scripts/verify_order50_signed_complement_disconnected.py",
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
        if label not in labels or not (ROOT / verifier).is_file():
            raise AssertionError(f"theorem/verifier mapping missing: {label} -> {verifier}")

    lean_claim_markers = (
        "the analytic LP optimum and rigidity for every integer \\(k\\ge4\\)",
        "proves that it is admissible and attains equality",
        "both as a polynomial and at coefficient level",
        "This LP formalization is deliberately graph-independent",
        r"the trace interpretation of the \(F_i(A)\)",
        "This is the precise scope of the Lean claims in the paper.",
    )
    normalized_tex = " ".join(tex.split())
    for marker in lean_claim_markers:
        if marker not in tex and marker not in normalized_tex:
            raise AssertionError(f"Lean claim or scope marker missing: {marker}")
    if "The public Lean development is sorry-free and kernel-checked by Lean 4.31" not in normalized_tex:
        raise AssertionError("Lean verification statement missing")
    if (
        r"\newcommand{\resultbox}[1]{\boxed{#1}}" not in tex
        or tex.count(r"\boxed{") != 1
        or tex.count(r"\resultbox{") != 17
    ):
        raise AssertionError("principal-result box style is not uniform")
    exact_exposition_markers = (
        r"(-k+1)^2-(2k-2)=(k-1)(k-3)\ge0",
        r"5n=2|E(G)|",
        r"5\nmid 1683",
        r"\int f\,d\mu\le0",
        r"\mathcal E_k=g_k(A)-(h_k+1)J+I",
        r"r=2\varepsilon-n-2",
        r"\frac{3(k+2)^2(k^2+3)}{18k+41}",
        r"A(X)=-I-E+J",
        r"\det(xI-D(R-v))=P_{39}(x)",
        r"\det(xI-D(R-\{u,v\}))=P_{38}(x)",
    )
    for marker in exact_exposition_markers:
        if marker not in tex:
            raise AssertionError(f"exact proof-exposition marker missing: {marker}")
    removed_ai_sentence = "No AI system is " + "an author"
    if r"\appendix" in tex or removed_ai_sentence in tex:
        raise AssertionError("removed appendix or AI-authorship sentence returned")

    report = {
        "labels": len(labels),
        "references": len(referenced_labels(tex)),
        "citation_occurrences": len(citations),
        "cited_sources": len(set(citations)),
        "bibliography_entries": len(bib_keys),
        "repository_paths_checked": len(paths),
        "theorem_verifier_mappings": len(theorem_verifiers),
    }
    print("v2.2.6 integrated manuscript audit: PASS")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
