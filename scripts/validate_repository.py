#!/usr/bin/env python3
"""Validate release metadata, generated certificates, and package topology."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
RELEASE_TITLE = "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284"
RELEASE_TAG = "v2.2.8"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def pdf_page_count(path: Path) -> int:
    result = subprocess.run(
        ["pdfinfo", str(path)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, flags=re.MULTILINE)
    require(match is not None, f"pdfinfo did not report a page count for {path}")
    return int(match.group(1))


HISTORICAL_LEDGER_MARKER = (
    "# HISTORICAL JULY 2026 SNAPSHOT; not the current manuscript inventory."
)
ARXIV_SOURCES = ("main.tex", "main.bbl", "references.bib", "petkov-preprint.sty")


def validate_arxiv_package() -> None:
    """Check the current manuscript package in arxiv/ against its own records.

    The root manuscript and root SHA256SUMS are a historical July snapshot. The
    current manuscript, PDF, source ZIP and ancillary files live in arxiv/,
    with their own MANIFEST.txt and SHA256SUMS.
    """
    arxiv = ROOT / "arxiv"
    manifest = [
        line
        for line in (arxiv / "MANIFEST.txt").read_text(encoding="utf-8").splitlines()
        if line
    ]
    require(manifest == sorted(set(manifest)),
            "arxiv/MANIFEST.txt is not a sorted list of unique paths")
    actual = sorted(
        path.relative_to(arxiv).as_posix() for path in arxiv.rglob("*") if path.is_file()
    )
    require(
        actual == manifest,
        "arxiv/ inventory differs from arxiv/MANIFEST.txt: "
        f"missing={sorted(set(manifest) - set(actual))}, "
        f"unlisted={sorted(set(actual) - set(manifest))}",
    )

    def digest(relative: str) -> str:
        return hashlib.sha256((arxiv / relative).read_bytes()).hexdigest()

    ledger = (arxiv / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    require(
        ledger == [f"{digest(name)}  {name}" for name in manifest if name != "SHA256SUMS"],
        "arxiv/SHA256SUMS does not match the files listed in arxiv/MANIFEST.txt",
    )

    ancillary = [name for name in manifest if name.startswith("anc/")]
    with zipfile.ZipFile(arxiv / "wow284_arxiv_source.zip") as archive:
        members = archive.namelist()
        require(
            len(members) == len(set(members))
            and sorted(members) == sorted([*ARXIV_SOURCES, *ancillary]),
            f"unexpected arXiv ZIP members: {members}",
        )
        for name in members:
            require(archive.read(name) == (arxiv / name).read_bytes(),
                    f"arXiv ZIP member differs from arxiv/{name}")
    require(r"\today" not in (arxiv / "main.tex").read_text(encoding="utf-8"),
            "arXiv-unsafe dynamic date present in arxiv/main.tex")


def main() -> None:
    expected = [
        "main.tex",
        "main.pdf",
        "main.bbl",
        "references.bib",
        "CITATION.cff",
        "LICENSE",
        "LICENSE_SCOPE.md",
        "README.md",
        "BUILD_VERIFICATION.txt",
        "SHA256SUMS",
        "results/verification.json",
        "results/verification_40.json",
        "results/edges.csv",
        "results/adjacency_matrix.csv",
        "results/distance_matrix.csv",
        "arxiv/wow284_arxiv_source.zip",
        "src/wow284_induced40.py",
        "scripts/verify_40.py",
        "scripts/verify_extended.py",
        "scripts/verify_wow284_38_40_42.py",
        "scripts/verify_38_graph6_independent.py",
        "scripts/verify_descendant_families.py",
        "data/graphs/G38.graph6",
        "data/graphs/G39.graph6",
        "data/graphs/G40.graph6",
        "data/graphs/G42.graph6",
        "data/graphs/G50.graph6",
        "scripts/verify_proof_audit_11_diameter_four.py",
        "scripts/verify_proof_audit_12_small_puncture.py",
        "scripts/verify_proof_audit_13_hs_robustness.py",
        "scripts/verify_optimal_slack_gram_unification.py",
        "scripts/verify_integral_optimal_slack_collapse.py",
        "scripts/verify_optimal_slack_excess_matrix.py",
        "scripts/verify_two_gram_hierarchies.py",
        "scripts/verify_three_to_one_excess_bound.py",
        "scripts/verify_three_to_one_equality_rigidity.py",
        "scripts/verify_proof_audit_14_three_to_one.py",
        "scripts/verify_signed_complement_bridge.py",
        "scripts/verify_order50_minus_two_multiplicity.py",
        "scripts/verify_order50_signed_complement_disconnected.py",
        "scripts/verify_component_indicator_noninvariance.py",
        "lean/Wow284/LPDefinitions.lean",
        "lean/Wow284/LPRecurrence.lean",
        "lean/Wow284/LPPrimal.lean",
        "lean/Wow284/LPDualFinite.lean",
        "lean/Wow284/LPChebyshevTail.lean",
        "lean/Wow284/LPWeakDuality.lean",
        "lean/Wow284/LPRigidity.lean",
        "lean/Wow284/LPCeiling.lean",
        "lean/Wow284LPAudit.lean",
        "scripts/validate_lp_formalization.py",
    ]
    missing = [relative for relative in expected if not (ROOT / relative).is_file()]
    require(not missing, f"missing release files: {missing}")

    tex = (ROOT / "main.tex").read_text(encoding="utf-8")
    require(r"\usepackage[margin=1in]{geometry}" in tex, "one-inch margins not fixed")
    require(
        r"\keywords{distance spectrum, dual degree, Moore graph}" in tex,
        "manuscript keywords are not the requested focused three",
    )
    require(
        "pdfkeywords={distance spectrum, dual degree, Moore graph}" in tex,
        "PDF metadata keywords are not synchronized",
    )
    require(r"\date{}" in tex, "active manuscript date must be suppressed")
    require(r"\author{Samuil Petkov}" in tex, "author mismatch")
    require(r"\email{samuil.petkov@phys.ens.psl.eu}" in tex, "email mismatch")
    require(
        r"\title[Counterexamples and obstructions for WOW-284]" in tex
        and RELEASE_TITLE in tex,
        "expanded manuscript title mismatch",
    )
    require(
        rf"\newcommand{{\RepoTag}}{{{RELEASE_TAG}}}" in tex,
        "v2.2.8 release tag missing",
    )
    require("WOW-284 asserts" in tex, "conjecture verb is not the requested wording")
    require(
        "OpenAI ChatGPT-5.6 Sol Pro assisted" in tex,
        "requested AI disclosure missing",
    )
    lower_tex = tex.lower()
    for phrase in (
        "first counterexample",
        "first proof that wow-284 is false",
        "first lean formalization",
        "smallest counterexample",
        "previously unknown",
    ):
        require(phrase not in lower_tex, f"unsupported claim returned: {phrase}")
    require(
        re.search(r"n\s*(?:\\leq?|<=|≤)\s*49", tex) is None,
        "unsupported positive order-49 bound returned",
    )
    require(
        r"\label{cor:edge-cycle-sieve}" in tex
        and r"\label{cor:uniform-deletion}" in tex
        and r"\label{thm:integral-slack}" in tex,
        "structural results are missing",
    )
    require(
        r"\label{thm:three-to-one}" in tex
        and r"\frac{3(k+2)^2(k^2+3)}{18k+41}" in tex
        and r"\label{prop:signed-complement}" in tex
        and r"\label{prop:order50-minus-two}" in tex,
        "three-to-one excess or signed-complement results are missing",
    )
    require(
        r"correspond to release \texttt{\RepoTag}" in tex,
        "manuscript-to-release correspondence statement missing",
    )
    require(
        all(
            stale not in tex
            for stale in (
                "v2.0.5-arxiv",
                "v2.1.0",
                "The earlier arXiv submission was withdrawn",
                "Exact Counterexamples and Spectral Mechanisms for WOW-284",
            )
        ),
        "submission source mentions superseded release history",
    )
    normalized_tex = " ".join(tex.split())
    for marker, message in (
        (
            r"\section{Moment bounds and the exact LP ceiling}",
            "expanded LP section missing",
        ),
        (
            r"\begin{theorem}[Exact LP ceiling and rigidity]",
            "exact LP theorem missing",
        ),
        (
            "the analytic LP optimum and rigidity for every integer \\(k\\ge4\\)",
            "LP formalization claim missing from abstract",
        ),
        (
            "proves that it is admissible and attains equality",
            "formalized optimizer-attainment claim missing",
        ),
        (
            "both as polynomials and at coefficient level",
            "coefficient-level uniqueness claim missing",
        ),
        (
            "This LP formalization is deliberately graph-independent",
            "LP graph-independence boundary missing",
        ),
        (
            r"the trace interpretation of the \(F_i(A)\)",
            "graph trace bridge exclusion missing",
        ),
        (
            r"\section{Distance spectra of punctured Moore graphs}",
            "punctured-Moore section missing",
        ),
        (
            r"\section{Small punctures and exact Hoffman--Singleton robustness}",
            "deletion-robustness section missing",
        ),
    ):
        require(marker in tex or marker in normalized_tex, message)
    require(r"\clearpage" in tex, "references do not start on a new page")
    require(r"\today" not in tex, "arXiv-unsafe dynamic date present")

    pages = pdf_page_count(ROOT / "main.pdf")
    build_report = (ROOT / "BUILD_VERIFICATION.txt").read_text(encoding="utf-8")
    require(f"PASS  PDF page count: {pages}." in build_report,
            "build report page count does not match main.pdf")
    require(
        "The authoritative SHA-256 digests for main.pdf and\n"
        "      arxiv/wow284_arxiv_source.zip are recorded in SHA256SUMS."
        in build_report,
        "build report does not identify SHA256SUMS as the authoritative digest ledger",
    )
    require(
        re.search(r"[0-9a-f]{64}\s+main\.pdf", build_report) is None,
        "build report duplicates the main.pdf digest",
    )
    require(
        re.search(
            r"[0-9a-f]{64}\s+arxiv/wow284_arxiv_source\.zip",
            build_report,
        )
        is None,
        "build report duplicates the arXiv ZIP digest",
    )

    require((ROOT / "lean" / "lean-toolchain").read_text(encoding="utf-8").strip() ==
            "leanprover/lean4:v4.31.0", "Lean toolchain is not pinned to 4.31.0")
    lakefile = (ROOT / "lean" / "lakefile.lean").read_text(encoding="utf-8")
    require('@ "v4.31.0"' in lakefile, "Mathlib is not pinned to 4.31.0")
    require("package Wow284" in lakefile,
            "Lake package name must match the root module for external checking")
    lake_manifest = json.loads((ROOT / "lean" / "lake-manifest.json").read_text(encoding="utf-8"))
    mathlib_locks = [package for package in lake_manifest["packages"] if package["name"] == "mathlib"]
    require(len(mathlib_locks) == 1 and mathlib_locks[0]["inputRev"] == "v4.31.0",
            "Lake manifest does not resolve Mathlib v4.31.0")
    forbidden_lean = re.compile(r"\b(sorry|admit|native_decide|bv_decide|unsafe|axiom)\b")
    for path in (ROOT / "lean").rglob("*.lean"):
        if ".lake" in path.parts:
            continue
        require(not forbidden_lean.search(path.read_text(encoding="utf-8")),
                f"forbidden Lean token in {path}")
    dispatcher = (ROOT / "lean" / "Wow284.lean").read_text(encoding="utf-8")
    require("import Wow284.LPCeiling" in dispatcher,
            "root Lean dispatcher does not import the LP closure")
    lp_ceiling = (ROOT / "lean" / "Wow284" / "LPCeiling.lean").read_text(
        encoding="utf-8"
    )
    require("theorem twoSidedLP_optimal_and_rigid" in lp_ceiling,
            "frozen all-degree LP endpoint is missing")
    lp_closure = "\n".join(
        (ROOT / relative).read_text(encoding="utf-8")
        for relative in (
            "lean/Wow284/LPDefinitions.lean",
            "lean/Wow284/LPPrimal.lean",
            "lean/Wow284/LPRigidity.lean",
            "lean/Wow284/LPCeiling.lean",
        )
    )
    require(
        "Coefficients" in lp_closure
        and "Admissible" in lp_closure
        and "extremal" in lp_closure
        and "attain" in lp_closure.lower(),
        "LP closure does not expose the coefficient witness and attainment layer",
    )
    lp_audit = (ROOT / "lean" / "Wow284LPAudit.lean").read_text(encoding="utf-8")
    require("twoSidedLP_optimal_and_rigid" in lp_audit and "#print axioms" in lp_audit,
            "LP public endpoint is absent from the axiom audit")

    bibliography = (ROOT / "references.bib").read_text(encoding="utf-8")
    for doi in [
        "10.1016/j.laa.2014.06.010",
        "10.1147/rd.45.0497",
        "10.1016/j.laa.2021.11.014",
        "10.7717/peerj-cs.103",
        "10.3390/axioms15050332",
        "10.1016/0095-8956(79)90052-2",
        "10.1002/jgt.3190030413",
        "10.1002/(SICI)1097-0118(199902)30:2<137::AID-JGT7>3.0.CO;2-G",
        "10.1307/mmj/1242071692",
        "10.1016/S0024-3795(03)00483-X",
        "10.25080/TCWV9851",
    ]:
        require(doi in bibliography, f"missing DOI: {doi}")

    certificate = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
    require(certificate["graph"]["order"] == 50, "certificate order mismatch")
    require(certificate["graph"]["girth"] == 5, "certificate girth mismatch")
    require(certificate["spectra"]["least_distance_eigenvalue"] == -4, "certificate spectrum mismatch")
    require(certificate["wow284"]["strict_gap"] == 3, "certificate gap mismatch")

    certificate_40 = json.loads(
        (ROOT / "results" / "verification_40.json").read_text(encoding="utf-8")
    )
    require(certificate_40["graph"]["order"] == 40, "40-certificate order mismatch")
    require(certificate_40["graph"]["girth"] == 5, "40-certificate girth mismatch")
    require(certificate_40["graph"]["diameter"] == 3, "40-certificate diameter mismatch")
    require(certificate_40["spectra"]["least_distance_eigenvalue"] == -5,
            "40-certificate spectrum mismatch")
    require(certificate_40["wow284"]["strict_gap"] == 1,
            "40-certificate gap mismatch")
    require(
        "Lean 4.31" in certificate_40["formalization_scope"]
        and "not currently Lean-formalized"
        not in certificate_40["formalization_scope"],
        "40-certificate formalization scope is stale",
    )

    with (ROOT / "results" / "edges.csv").open(encoding="utf-8", newline="") as handle:
        require(sum(1 for _ in csv.reader(handle)) == 176, "edge CSV row count mismatch")
    for name in ["adjacency_matrix.csv", "distance_matrix.csv"]:
        with (ROOT / "results" / name).open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        require(len(rows) == 51, f"{name} row count mismatch")
        require(all(len(row) == 51 for row in rows), f"{name} column count mismatch")

    validate_arxiv_package()

    cited_keys: set[str] = set()
    for match in re.finditer(r"\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]*)\}", tex):
        cited_keys.update(key.strip() for key in match.group(1).split(","))
    bbl = (ROOT / "main.bbl").read_text(encoding="utf-8")
    bbl_keys = set(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", bbl))
    require(bbl_keys == cited_keys,
            f"BBL/citation key mismatch: missing={sorted(cited_keys - bbl_keys)}, "
            f"stale={sorted(bbl_keys - cited_keys)}")

    text_extensions = {".tex", ".bib", ".md", ".py", ".toml", ".txt", ".yml", ".cff", ".sh", ".ps1"}
    mojibake_markers = ("\ufffd", "\u00e2\u20ac", "\u00c3")
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_extensions:
            continue
        if any(part in {".git", ".lake", ".venv", "tmp", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        raw = path.read_bytes()
        if path.suffix.lower() in {".md", ".tex"}:
            require(b"\t" not in raw, f"tab control byte in prose source {path}")
            require(b"\r" not in raw, f"carriage-return control byte in prose source {path}")
        text = path.read_text(encoding="utf-8")
        require(not any(marker in text for marker in mojibake_markers), f"mojibake marker in {path}")

    # The root SHA256SUMS is the historical July 2026 snapshot (published by the
    # project site) and says so in its first line. The current integrity records
    # are arxiv/MANIFEST.txt and arxiv/SHA256SUMS, checked by validate_arxiv_package().
    first_line = (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines()[0]
    require(
        first_line == HISTORICAL_LEDGER_MARKER,
        "root SHA256SUMS is not marked as the historical July snapshot",
    )

    require((ROOT / "main.pdf").stat().st_size > 25_000, "compiled PDF is unexpectedly small")
    print("repository release validation: PASS")


if __name__ == "__main__":
    main()
