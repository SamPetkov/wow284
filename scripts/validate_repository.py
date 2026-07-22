#!/usr/bin/env python3
"""Validate release metadata, generated certificates, and package topology."""

from __future__ import annotations

import csv
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
        "results/edges.csv",
        "results/adjacency_matrix.csv",
        "results/distance_matrix.csv",
        "arxiv/wow284_arxiv_source.zip",
    ]
    missing = [relative for relative in expected if not (ROOT / relative).is_file()]
    require(not missing, f"missing release files: {missing}")

    tex = (ROOT / "main.tex").read_text(encoding="utf-8")
    require(r"\usepackage[margin=1in]{geometry}" in tex, "one-inch margins not fixed")
    require(r"\date{19 July 2026}" in tex, "manuscript date mismatch")
    require(r"\author{Samuil Petkov}" in tex, "author mismatch")
    require(r"\title[Moore graphs and the failure of WOW-284]" in tex, "title mismatch")
    require("Howlader and Panigrahi" in tex, "prior distance-spectrum attribution missing")
    require("No claim is made" in tex, "scope limitation missing")
    require("The explicit 50-vertex counterexample is fully formalized and verified" in tex,
            "completed explicit Lean verification status missing")
    require("formal verification claim here is deliberately limited" in
            " ".join(tex.split()),
            "formal verification scope limitation missing")
    require(r"\today" not in tex, "arXiv-unsafe dynamic date present")

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
    ]:
        require(doi in bibliography, f"missing DOI: {doi}")

    certificate = json.loads((ROOT / "results" / "verification.json").read_text(encoding="utf-8"))
    require(certificate["graph"]["order"] == 50, "certificate order mismatch")
    require(certificate["graph"]["girth"] == 5, "certificate girth mismatch")
    require(certificate["spectra"]["least_distance_eigenvalue"] == -4, "certificate spectrum mismatch")
    require(certificate["wow284"]["strict_gap"] == 3, "certificate gap mismatch")

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
