#!/usr/bin/env python3
"""Validate release metadata, generated certificates, and package topology."""

from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> None:
    expected = [
        "main.tex",
        "main.pdf",
        "main.bbl",
        "manuscript.md",
        "references.bib",
        "CITATION.cff",
        "LICENSE",
        "LICENSE_SCOPE.md",
        "README.md",
        "REVIEW.md",
        "SOURCE_LEDGER.md",
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
        "supplement/extended_2026-07-23/SHA256SUMS",
        "archive/main_2026-07-19.tex",
    ]
    missing = [relative for relative in expected if not (ROOT / relative).is_file()]
    require(not missing, f"missing release files: {missing}")

    tex = (ROOT / "main.tex").read_text(encoding="utf-8")
    require(r"\usepackage[margin=1in]{geometry}" in tex, "one-inch margins not fixed")
    require(r"\date{}" in tex, "active manuscript date must be suppressed")
    require(r"\author{Samuil Petkov}" in tex, "author mismatch")
    require(r"\title[Exact counterexamples to WOW-284]" in tex, "title mismatch")
    require("Howlader and Panigrahi" in tex, "prior distance-spectrum attribution missing")
    require("No claim is made" in tex, "scope limitation missing")
    require("OpenAI ChatGPT assisted" in tex, "generic AI disclosure missing")
    require("OpenAI ChatGPT-5.6" not in tex, "stale AI system designation present")
    require("A graph6 string in this fixed" in tex, "fixed-label graph6 wording missing")
    require("canonical graph6 string" not in tex, "unsupported graph6 canonicality claim")
    require(r"V(-\infty)=26" in tex and r"V(-28/5)=25" in tex,
            "exact order-38 Sturm variation certificate missing")
    require(r"vertices at distance two from \(P_{0,0}\)" in tex,
            "explicit order-42 base vertex missing")
    require(r"\texttt{v2.0.2-arxiv}" in tex, "fixed release tag missing")
    require(r"\delta^*(H_v)" in tex, "order-39 graph quantifier is not explicit")
    require(r"\mathbb R^{V(X)}" in tex, "Moore invariant-space decomposition missing")
    require(r"2K-7-\sqrt{4K-3}" in tex, "Moore threshold calculation missing")
    require(r"m_2+m_{-3}=35" in tex, "order-42 multiplicity calculation missing")
    require(r"V(M)=U\sqcup S" in tex, "generic equitable-deletion notation not fixed")
    require("permitting byte-for-byte integrity" in tex,
            "checksum integrity wording missing")
    require("python scripts/explore_generalizations.py" in tex,
            "generalization verifier command missing")
    require("runs every extended exact certificate" not in tex,
            "verify_extended.py scope is overstated")
    require("authenticates it and every other archived" not in tex,
            "unsigned checksum manifest is described as authentication")
    require("The explicit 50-vertex counterexample is fully formalized and verified" in tex,
            "completed explicit Lean verification status missing")
    require("Lean 4.31 also kernel-checks finite spectral certificates" in tex,
            "non-50 finite spectral certificate status missing")
    require("The scope of these non-50 results is deliberately finite and spectral" in tex,
            "non-50 formal claim boundary missing")
    require(r"\section{A 40-vertex induced counterexample}" in tex,
            "40-vertex counterexample section missing")
    require(r"\Spec(D(R))=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}" in tex,
            "40-vertex distance spectrum missing")
    require(r"\today" not in tex, "arXiv-unsafe dynamic date present")
    archived_tex = (ROOT / "archive" / "main_2026-07-19.tex").read_text(encoding="utf-8")
    require(r"\date{19 July 2026}" in archived_tex,
            "historical 19 July manuscript snapshot is not dated correctly")

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

    bibliography = (ROOT / "references.bib").read_text(encoding="utf-8")
    for doi in [
        "10.1016/j.laa.2014.06.010",
        "10.1147/rd.45.0497",
        "10.1016/j.laa.2021.11.014",
        "10.7717/peerj-cs.103",
        "10.3390/axioms15050332",
        "10.1016/0095-8956(79)90052-2",
        "10.1002/jgt.3190030413",
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

    with (ROOT / "results" / "edges.csv").open(encoding="utf-8", newline="") as handle:
        require(sum(1 for _ in csv.reader(handle)) == 176, "edge CSV row count mismatch")
    for name in ["adjacency_matrix.csv", "distance_matrix.csv"]:
        with (ROOT / "results" / name).open(encoding="utf-8", newline="") as handle:
            rows = list(csv.reader(handle))
        require(len(rows) == 51, f"{name} row count mismatch")
        require(all(len(row) == 51 for row in rows), f"{name} column count mismatch")

    with zipfile.ZipFile(ROOT / "arxiv" / "wow284_arxiv_source.zip") as archive:
        require(
            archive.namelist() == ["main.tex", "references.bib", "main.bbl"],
            "arXiv archive contains unexpected files",
        )

    supplement = ROOT / "supplement" / "extended_2026-07-23"
    for line in (supplement / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line)
        require(match is not None, f"invalid supplement checksum line: {line!r}")
        expected_hash, relative = match.groups()
        payload = supplement / Path(relative)
        require(payload.is_file(), f"missing supplement payload: {relative}")
        actual_hash = hashlib.sha256(payload.read_bytes()).hexdigest()
        require(actual_hash.lower() == expected_hash.lower(),
                f"supplement checksum mismatch: {relative}")

    text_extensions = {".tex", ".bib", ".md", ".py", ".toml", ".txt", ".yml", ".cff", ".sh", ".ps1"}
    mojibake_markers = ("\ufffd", "\u00e2\u20ac", "\u00c3")
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in text_extensions:
            continue
        if any(part in {".git", ".lake", ".venv", "tmp", "__pycache__"} for part in path.relative_to(ROOT).parts):
            continue
        text = path.read_text(encoding="utf-8")
        require(not any(marker in text for marker in mojibake_markers), f"mojibake marker in {path}")

    require((ROOT / "main.pdf").stat().st_size > 25_000, "compiled PDF is unexpectedly small")
    print("repository release validation: PASS")


if __name__ == "__main__":
    main()
