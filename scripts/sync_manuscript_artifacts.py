#!/usr/bin/env python3
"""Build and synchronize the public WOW-284 manuscript artifacts.

The authoritative manuscript source is ``main.tex``.  A normal run compiles
the PDF in an ASCII-only temporary directory, regenerates the readable
Markdown copy, mirrors the arXiv-facing files, creates a deterministic source
ZIP, and refreshes the manifest and SHA-256 ledger.  ``--check`` is read-only.
"""

from __future__ import annotations

import argparse
import hashlib
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_TEX = ROOT / "main.tex"
CANONICAL_BIB = ROOT / "references.bib"
CANONICAL_BBL = ROOT / "main.bbl"
CANONICAL_PDF = ROOT / "main.pdf"
CANONICAL_MD = ROOT / "manuscript.md"
ARXIV_DIR = ROOT / "arxiv"
ARXIV_ZIP = ARXIV_DIR / "wow284_arxiv_source.zip"

ARXIV_MIRRORS = {
    CANONICAL_TEX: ARXIV_DIR / "main.tex",
    CANONICAL_BIB: ARXIV_DIR / "references.bib",
    CANONICAL_BBL: ARXIV_DIR / "main.bbl",
    CANONICAL_PDF: ARXIV_DIR / "main.pdf",
    CANONICAL_MD: ARXIV_DIR / "main.md",
}

EXCLUDED_DIRECTORIES = {
    ".git",
    ".lake",
    ".venv",
    ".pytest_cache",
    "__pycache__",
    "tmp",
}


def run(command: list[str], *, cwd: Path, env: dict[str, str] | None = None) -> None:
    subprocess.run(command, cwd=cwd, env=env, check=True)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def arxiv_member_bytes(source: Path) -> bytes:
    """Serialize arXiv text members with deterministic LF line endings."""

    text = source.read_text(encoding="utf-8")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def compile_manuscript() -> None:
    """Compile in a short temporary path and copy back the PDF and BBL."""

    with tempfile.TemporaryDirectory(prefix="wow284-latex-") as temporary:
        build = Path(temporary)
        shutil.copy2(CANONICAL_TEX, build / "main.tex")
        shutil.copy2(CANONICAL_BIB, build / "references.bib")
        environment = os.environ.copy()
        environment.update(
            {
                "TZ": "UTC",
                "SOURCE_DATE_EPOCH": "1784894400",
                "FORCE_SOURCE_DATE": "1",
            }
        )
        run(
            [
                "latexmk",
                "-pdf",
                "-bibtex",
                "-interaction=nonstopmode",
                "-halt-on-error",
                "-file-line-error",
                "main.tex",
            ],
            cwd=build,
            env=environment,
        )
        shutil.copy2(build / "main.pdf", CANONICAL_PDF)
        CANONICAL_BBL.write_text(
            (build / "main.bbl").read_text(encoding="utf-8"),
            encoding="utf-8",
            newline="\n",
        )
        log_target = ROOT / "tmp" / "main.log"
        log_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(build / "main.log", log_target)


def generate_markdown() -> None:
    """Generate a readable, explicitly noncanonical GitHub Markdown copy."""

    with tempfile.TemporaryDirectory(prefix="wow284-pandoc-") as temporary:
        pandoc_source = Path(temporary) / "main-for-pandoc.tex"
        raw = Path(temporary) / "raw.md"
        latex = CANONICAL_TEX.read_text(encoding="utf-8")

        # Pandoc silently drops the contents of url.sty's \path{...} command.
        # Replace those commands only in the disposable Markdown input; the
        # canonical TeX retains \path so long filenames remain line-breakable.
        def markdown_path(match: re.Match[str]) -> str:
            value = match.group(1)
            escaped = re.sub(r"([_#%&])", r"\\\1", value)
            return rf"\texttt{{{escaped}}}"

        pandoc_source.write_text(
            re.sub(r"\\path\{([^{}]*)\}", markdown_path, latex),
            encoding="utf-8",
            newline="\n",
        )
        run(
            [
                "pandoc",
                str(pandoc_source),
                "--from=latex",
                "--to=gfm+tex_math_dollars",
                "--wrap=none",
                "--citeproc",
                f"--bibliography={CANONICAL_BIB}",
                "--metadata=link-citations:true",
                "--output",
                str(raw),
            ],
            cwd=ROOT,
        )
        body = raw.read_text(encoding="utf-8")
        for expected_path in (
            "scripts/verify_descendant_families.py",
            "supplement/extended_2026-07-23/logs/descendant_family_output.txt",
            "SHA256SUMS",
        ):
            if expected_path not in body:
                raise RuntimeError(
                    f"generated Markdown dropped required path: {expected_path}"
                )

    header = """# Exact Counterexamples and Spectral Mechanisms for WOW-284

**Samuil Petkov**<br>
Department of Physics, École normale supérieure, Université PSL, Paris, France<br>
<samuil.petkov@phys.ens.psl.eu><br>
> Reading copy generated from `main.tex`. The TeX source is authoritative if
> this rendering differs in notation, citations, or layout.

"""
    CANONICAL_MD.write_text(header + body.lstrip(), encoding="utf-8", newline="\n")


def copy_mirrors() -> None:
    ARXIV_DIR.mkdir(parents=True, exist_ok=True)
    for source, destination in ARXIV_MIRRORS.items():
        shutil.copy2(source, destination)


def make_arxiv_archive() -> None:
    """Create a deterministic arXiv ZIP containing source files only."""

    members = [
        ("main.tex", CANONICAL_TEX),
        ("references.bib", CANONICAL_BIB),
        ("main.bbl", CANONICAL_BBL),
    ]
    ARXIV_DIR.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(ARXIV_ZIP, "w") as archive:
        for name, source in members:
            info = zipfile.ZipInfo(name, date_time=(2026, 7, 24, 12, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, arxiv_member_bytes(source))


def validate_arxiv_archive() -> None:
    expected = ["main.tex", "references.bib", "main.bbl"]
    with zipfile.ZipFile(ARXIV_ZIP) as archive:
        if archive.namelist() != expected:
            raise RuntimeError(f"unexpected arXiv archive members: {archive.namelist()}")
        for name, source in zip(expected, [CANONICAL_TEX, CANONICAL_BIB, CANONICAL_BBL], strict=True):
            if archive.read(name) != arxiv_member_bytes(source):
                raise RuntimeError(f"arXiv archive member differs from canonical source: {name}")


def validate_release_text() -> None:
    text = CANONICAL_TEX.read_text(encoding="utf-8")
    required = [
        r"\title[Exact counterexamples to WOW-284]",
        r"\author{Samuil Petkov}",
        r"\date{}",
        r"\usepackage[margin=1in]{geometry}",
        "Howlader and Panigrahi",
        "No claim is made",
        "OpenAI ChatGPT assisted",
        "A graph6 string in this fixed",
        r"V(-\infty)=26",
        r"vertices at distance two from \(P_{0,0}\)",
        r"\texttt{v2.0.2-arxiv}",
        r"\delta^*(H_v)",
        r"\mathbb R^{V(X)}",
        r"2K-7-\sqrt{4K-3}",
        r"m_2+m_{-3}=35",
        r"V(M)=U\sqcup S",
        "permitting byte-for-byte integrity",
        "python scripts/explore_generalizations.py",
        "The explicit 50-vertex counterexample is fully formalized and verified",
        "Lean 4.31 also kernel-checks finite spectral certificates",
        "The scope of these non-50 results is deliberately finite and spectral",
        r"\section{A 40-vertex induced counterexample}",
        r"\Spec(D(R))=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}",
        r"\section{Smaller induced counterexamples}",
        r"\partial_{38}(H)=-3-\sqrt7",
        r"The scalar \(k\le3\) threshold",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise RuntimeError(f"canonical TeX is missing required release wording: {missing}")
    forbidden = [
        r"\today",
        "first counterexample",
        "smallest counterexample",
        "new distance spectrum",
        "Samuil Petkov and Codex",
        "Samuil Petkov & Codex",
        "20 July 2026",
        "21 July 2026",
        "canonical graph6 string",
        "OpenAI ChatGPT-5.6",
        "Exact rational factorization",
        "authenticates it and every other archived",
        "runs every extended exact certificate",
        "remains under verification",
        "formalization is in preparation",
    ]
    present = [item for item in forbidden if item in text]
    if present:
        raise RuntimeError(f"canonical TeX contains forbidden release wording: {present}")


def list_release_files() -> list[str]:
    # Use Git's release-visible inventory so ignored local build products
    # (for example ``*.log``) can never leak into MANIFEST.txt.  Include
    # untracked, non-ignored files so newly generated release artifacts are
    # still detected before their first commit.
    result = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    candidates = result.stdout.decode("utf-8").split("\0")
    files: list[str] = []
    for item in candidates:
        if not item:
            continue
        relative = Path(item)
        if any(part in EXCLUDED_DIRECTORIES for part in relative.parts):
            continue
        path = ROOT / relative
        if path.is_file() and relative.as_posix() not in {"MANIFEST.txt", "SHA256SUMS"}:
            files.append(relative.as_posix())
    return sorted(set(files))


def update_manifest_and_hashes() -> None:
    release_files = list_release_files()
    manifest_entries = sorted([*release_files, "MANIFEST.txt", "SHA256SUMS"])
    (ROOT / "MANIFEST.txt").write_text(
        "\n".join(manifest_entries) + "\n", encoding="utf-8", newline="\n"
    )
    hash_paths = sorted([*release_files, "MANIFEST.txt"])
    lines = [f"{sha256(ROOT / relative)}  {relative}" for relative in hash_paths]
    (ROOT / "SHA256SUMS").write_text(
        "\n".join(lines) + "\n", encoding="utf-8", newline="\n"
    )


def check_manifest_and_hashes() -> None:
    actual = sorted([*list_release_files(), "MANIFEST.txt", "SHA256SUMS"])
    recorded = (ROOT / "MANIFEST.txt").read_text(encoding="utf-8").splitlines()
    if recorded != actual:
        missing = sorted(set(actual) - set(recorded))
        stale = sorted(set(recorded) - set(actual))
        raise RuntimeError(
            "MANIFEST.txt is not synchronized"
            f"; missing entries={missing}; stale entries={stale}"
        )
    for line in (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        if sha256(ROOT / relative) != digest:
            raise RuntimeError(f"SHA-256 mismatch: {relative}")


def synchronize() -> None:
    validate_release_text()
    compile_manuscript()
    generate_markdown()
    copy_mirrors()
    make_arxiv_archive()
    validate_arxiv_archive()
    update_manifest_and_hashes()


def check() -> None:
    validate_release_text()
    for source, destination in ARXIV_MIRRORS.items():
        if source.read_bytes() != destination.read_bytes():
            raise RuntimeError(f"arXiv mirror is stale: {destination.relative_to(ROOT)}")
    validate_arxiv_archive()
    check_manifest_and_hashes()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate without modifying files")
    args = parser.parse_args()
    if args.check:
        check()
        print("manuscript synchronization check: PASS")
    else:
        synchronize()
        print("manuscript build and synchronization: PASS")


if __name__ == "__main__":
    main()
