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
BUILD_REPORT = ROOT / "BUILD_VERIFICATION.txt"
SUBMISSION_NOTES = ROOT / "SUBMISSION_NOTES.md"
V22_DIR = ROOT / "v22"

RELEASE_TITLE = (
    "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284"
)
RELEASE_TAG = "v2.2.3"

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


def pdf_page_count(path: Path) -> int:
    """Read the actual PDF page count from Poppler's machine-readable output."""

    result = subprocess.run(
        ["pdfinfo", str(path)],
        cwd=ROOT,
        check=True,
        text=True,
        capture_output=True,
    )
    match = re.search(r"^Pages:\s+(\d+)\s*$", result.stdout, flags=re.MULTILINE)
    if match is None:
        raise RuntimeError(f"pdfinfo did not report a page count for {path}")
    return int(match.group(1))


def replace_counted(text: str, pattern: str, replacement: str, *, label: str) -> str:
    updated, count = re.subn(pattern, replacement, text)
    if count != 1:
        raise RuntimeError(f"{label}: expected one metadata marker, found {count}")
    return updated


def update_page_count_metadata(page_count: int) -> None:
    """Synchronize release prose with the page count of the compiled PDF."""

    submission = SUBMISSION_NOTES.read_text(encoding="utf-8")
    submission = replace_counted(
        submission,
        r"\*\*Comments:\*\* \d+ pages\.",
        f"**Comments:** {page_count} pages.",
        label="submission page count",
    )
    SUBMISSION_NOTES.write_text(submission, encoding="utf-8", newline="\n")

    report = BUILD_REPORT.read_text(encoding="utf-8")
    report = replace_counted(
        report,
        r"PASS  PDF page count: \d+\.",
        f"PASS  PDF page count: {page_count}.",
        label="build-report page count",
    )
    BUILD_REPORT.write_text(report, encoding="utf-8", newline="\n")


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
        # Pandoc numbers theorem-like environments even when their printed
        # titles already carry the intended public labels.
        body = body.replace(
            "**Conjecture (WOW-284) 1**.",
            "**Conjecture (WOW-284)**.",
        )
        body = body.replace("**Theorem A 1**.", "**Theorem A**.")
        for expected_path in (
            "scripts/verify_extended.py",
            "scripts/verify_proof_audit_02_two_sided_lp.py",
            "scripts/verify_proof_audit_11_diameter_four.py",
            "scripts/verify_proof_audit_12_small_puncture.py",
            "scripts/verify_proof_audit_13_hs_robustness.py",
            "data/graphs/",
        ):
            if expected_path not in body:
                raise RuntimeError(
                    f"generated Markdown dropped required path: {expected_path}"
                )

    header = """# Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284

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
    V22_DIR.mkdir(parents=True, exist_ok=True)
    for source in (CANONICAL_TEX, CANONICAL_BIB, CANONICAL_BBL):
        shutil.copy2(source, V22_DIR / source.name)


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
        r"\title[Counterexamples and obstructions for WOW-284]",
        RELEASE_TITLE,
        r"\author{Samuil Petkov}",
        r"\email{samuil.petkov@phys.ens.psl.eu}",
        r"\date{}",
        r"\usepackage[margin=1in]{geometry}",
        r"\keywords{distance spectrum, dual degree, Moore graph}",
        "pdfkeywords={distance spectrum, dual degree, Moore graph}",
        rf"\newcommand{{\RepoTag}}{{{RELEASE_TAG}}}",
        "WOW-284 asserts",
        "OpenAI ChatGPT-5.6 Sol Pro assisted",
        r"\section{Moment bounds and the exact LP ceiling}",
        r"\begin{theorem}[Exact LP ceiling and rigidity]",
        "the analytic LP\noptimum and rigidity for every integer \\(k\\ge4\\)",
        "proves that it is admissible and attains equality",
        "polynomial and at coefficient level",
        "This LP formalization is deliberately graph-independent",
        r"the trace interpretation of the \(F_i(A)\)",
        r"\section{Distance spectra of punctured Moore graphs}",
        r"\section{Small punctures and exact Hoffman--Singleton robustness}",
        r"\label{cor:edge-cycle-sieve}",
        r"\label{cor:uniform-deletion}",
        "first proof that WOW-284 is false",
        r"\clearpage",
        r"correspond to release \texttt{v2.2.3}",
    ]
    missing = [item for item in required if item not in text]
    if missing:
        raise RuntimeError(f"canonical TeX is missing required release wording: {missing}")
    if text.count("first proof that WOW-284 is false") != 1:
        raise RuntimeError("the qualified priority statement must appear exactly once")
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
        "Exact rational factorization",
        "authenticates it and every other archived",
        "runs every extended exact certificate",
        "remains under verification",
        "formalization is in preparation",
        r"\texttt{v2.0.5-arxiv}",
        r"\texttt{v2.1.0}",
        "Exact Counterexamples and Spectral Mechanisms for WOW-284",
        "The earlier arXiv submission was withdrawn",
        "they are not included in the Lean claim above",
    ]
    present = [item for item in forbidden if item in text]
    if present:
        raise RuntimeError(f"canonical TeX contains forbidden release wording: {present}")

    report = BUILD_REPORT.read_text(encoding="utf-8")
    authoritative = (
        "The authoritative SHA-256 digests for main.pdf and\n"
        "      arxiv/wow284_arxiv_source.zip are recorded in SHA256SUMS."
    )
    if authoritative not in report:
        raise RuntimeError("build report does not delegate artifact digests to SHA256SUMS")
    stale_digest_patterns = [
        r"[0-9a-f]{64}\s+main\.pdf",
        r"[0-9a-f]{64}\s+arxiv/wow284_arxiv_source\.zip",
    ]
    if any(re.search(pattern, report) for pattern in stale_digest_patterns):
        raise RuntimeError("build report embeds duplicated PDF or arXiv ZIP digests")


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
    expected_hash_paths = sorted(item for item in actual if item != "SHA256SUMS")
    lines = (ROOT / "SHA256SUMS").read_text(encoding="utf-8").splitlines()
    parsed: list[tuple[str, str]] = []
    for line in lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\r\n]+)", line)
        if match is None:
            raise RuntimeError(f"malformed SHA256SUMS line: {line!r}")
        parsed.append((match.group(1), match.group(2)))
    recorded_hash_paths = [relative for _, relative in parsed]
    if recorded_hash_paths != expected_hash_paths:
        missing = sorted(set(expected_hash_paths) - set(recorded_hash_paths))
        stale = sorted(set(recorded_hash_paths) - set(expected_hash_paths))
        duplicates = sorted(
            relative
            for relative in set(recorded_hash_paths)
            if recorded_hash_paths.count(relative) != 1
        )
        raise RuntimeError(
            "SHA256SUMS is not a complete one-entry-per-file ledger"
            f"; missing entries={missing}; stale entries={stale}; duplicates={duplicates}"
        )
    for digest, relative in parsed:
        if not (ROOT / relative).is_file():
            raise RuntimeError(f"SHA256SUMS references a missing file: {relative}")
        if sha256(ROOT / relative) != digest:
            raise RuntimeError(f"SHA-256 mismatch: {relative}")


def synchronize() -> None:
    validate_release_text()
    compile_manuscript()
    update_page_count_metadata(pdf_page_count(CANONICAL_PDF))
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
    for source in (CANONICAL_TEX, CANONICAL_BIB, CANONICAL_BBL):
        destination = V22_DIR / source.name
        if source.read_bytes() != destination.read_bytes():
            raise RuntimeError(f"v22/{source.name} is not synchronized")
    page_count = pdf_page_count(CANONICAL_PDF)
    submission = SUBMISSION_NOTES.read_text(encoding="utf-8")
    if f"**Comments:** {page_count} pages." not in submission:
        raise RuntimeError("submission page count does not match main.pdf")
    report = BUILD_REPORT.read_text(encoding="utf-8")
    if f"PASS  PDF page count: {page_count}." not in report:
        raise RuntimeError("build-report page count does not match main.pdf")
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
