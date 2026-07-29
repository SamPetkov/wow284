#!/usr/bin/env python3
"""Assemble the WOW-284 GitHub Pages tree from Paperforge output.

The root LaTeX/PDF remain canonical.  This script copies the generated PreTeXt
HTML under ``paper/`` and combines it with the hand-authored project pages.  It
never edits the manuscript or the generated Paperforge source tree.
"""
from __future__ import annotations

import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import shutil
import subprocess

INSTANCE = Path(__file__).resolve().parents[1]
REPOSITORY = INSTANCE.parent
WEB_OUTPUT = INSTANCE / "output" / "web"
SITE_SOURCE = INSTANCE / "web-assets" / "site"
SITE_OUTPUT = INSTANCE / "output" / "site"
EXPECTED_TITLE = "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def git_value(*args: str, default: str) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=REPOSITORY,
            check=True,
            text=True,
            capture_output=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return default
    return result.stdout.strip() or default


def manuscript_version() -> str:
    citation = REPOSITORY / "CITATION.cff"
    if citation.is_file():
        match = re.search(
            r"(?m)^version:\s*[\"']?([^\s\"']+)",
            citation.read_text(encoding="utf-8"),
        )
        if match:
            return match.group(1)
    tex = REPOSITORY / "main.tex"
    if tex.is_file():
        match = re.search(r"\\newcommand\{\\RepoTag\}\{([^}]+)\}", tex.read_text(encoding="utf-8"))
        if match:
            return match.group(1)
    return "unversioned"


def copy_file(name: str, destination: str | None = None, *, required: bool = True) -> None:
    source = REPOSITORY / name
    if not source.is_file():
        if required:
            raise FileNotFoundError(f"required publication artifact is missing: {source}")
        return
    target = SITE_OUTPUT / (destination or source.name)
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def ensure_paper_index(paper_dir: Path) -> str:
    index = paper_dir / "index.html"
    if index.is_file():
        return "index.html"

    preferred = paper_dir / "paper.html"
    if preferred.is_file():
        entry = preferred.name
    else:
        candidates = sorted(
            path for path in paper_dir.glob("*.html")
            if path.name not in {"404.html", "search.html"}
        )
        if not candidates:
            raise FileNotFoundError(f"Paperforge generated no top-level HTML in {paper_dir}")
        entry = candidates[0].name

    index.write_text(
        "<!doctype html>\n"
        "<html lang=\"en\"><head><meta charset=\"utf-8\">\n"
        f"<meta http-equiv=\"refresh\" content=\"0; url={entry}\">\n"
        f"<link rel=\"canonical\" href=\"{entry}\">\n"
        "<title>WOW-284 interactive paper</title></head>\n"
        f"<body><p><a href=\"{entry}\">Open the interactive paper</a>.</p></body></html>\n",
        encoding="utf-8",
    )
    return entry


def repository_link(path: str, tag: str) -> str:
    clean = path.strip().replace("\\_", "_")
    kind = "tree" if clean.endswith("/") else "blob"
    clean = clean.rstrip("/")
    href = f"https://github.com/SamPetkov/wow284/{kind}/{tag}/{clean}"
    return (
        f'<a class="paperforge-source-link" href="{escape(href, quote=True)}">'
        f"<code>{escape(path.strip())}</code></a>"
    )


def patch_generated_paper(version: str) -> None:
    """Adapt repository-path macros that Paperforge keeps verbatim in prose."""
    paper = SITE_OUTPUT / "paper"
    tag = version if version.startswith("v") else f"v{version}"
    macro_patterns = [
        r"\\newcommand\{\\RepoTag\}\{[^}]*\}\s*",
        r"\\newcommand\{\\codefile\}\[1\]\{\s*"
        r"\\href\{[^{}]*\}\{\\path\{#1\}\}\}\s*",
        r"\\newcommand\{\\datafile\}\[1\]\{\s*"
        r"\\href\{[^{}]*\}\{\\path\{#1\}\}\}\s*",
    ]
    path_pattern = re.compile(r"\\(?:codefile|datafile|path)\{([^{}\n]+)\}")

    for html in paper.rglob("*.html"):
        text = html.read_text(encoding="utf-8")
        for pattern in macro_patterns:
            text = re.sub(pattern, "", text, flags=re.DOTALL)
        text = path_pattern.sub(lambda match: repository_link(match.group(1), tag), text)
        html.write_text(text, encoding="utf-8", newline="\n")

    stylesheet = paper / "paper-style.css"
    if stylesheet.is_file():
        css = stylesheet.read_text(encoding="utf-8")
        addition = (
            "\n/* WOW-284 repository paths inserted after Paperforge conversion. */\n"
            ".paperforge-source-link code { overflow-wrap: anywhere; }\n"
            ".paperforge-source-link { text-decoration-thickness: .08em; "
            "text-underline-offset: .16em; }\n"
        )
        if "paperforge-source-link" not in css:
            stylesheet.write_text(css + addition, encoding="utf-8", newline="\n")


def replace_placeholders(values: dict[str, str]) -> None:
    for path in SITE_OUTPUT.rglob("*.html"):
        text = path.read_text(encoding="utf-8")
        for key, value in values.items():
            text = text.replace("{{" + key + "}}", value)
        path.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    if not SITE_SOURCE.is_dir():
        raise FileNotFoundError(f"hand-authored site tree is missing: {SITE_SOURCE}")
    if not WEB_OUTPUT.is_dir():
        raise FileNotFoundError(
            f"Paperforge web output is missing: {WEB_OUTPUT}; run `paperforge build web` first"
        )

    if SITE_OUTPUT.exists():
        shutil.rmtree(SITE_OUTPUT)
    shutil.copytree(SITE_SOURCE, SITE_OUTPUT)
    shutil.copytree(WEB_OUTPUT, SITE_OUTPUT / "paper")
    paper_entry = ensure_paper_index(SITE_OUTPUT / "paper")

    copy_file("main.pdf", "paper.pdf")
    copy_file("CITATION.cff")
    copy_file("BUILD_VERIFICATION.txt")
    copy_file("SHA256SUMS")
    copy_file("LICENSE")

    provenance = INSTANCE / "output" / "build-provenance.json"
    if provenance.is_file():
        shutil.copy2(provenance, SITE_OUTPUT / "build-provenance.json")

    version = manuscript_version()
    patch_generated_paper(version)

    source_commit = os.environ.get("SOURCE_COMMIT") or git_value(
        "rev-parse", "HEAD", default="unknown"
    )
    source_short = source_commit[:12] if source_commit != "unknown" else source_commit
    paperforge_commit = os.environ.get("PAPERFORGE_COMMIT", "unrecorded")
    paperforge_short = paperforge_commit[:12]
    pdf_hash = sha256(REPOSITORY / "main.pdf")

    values = {
        "VERSION": version,
        "COMMIT": source_commit,
        "COMMIT_SHORT": source_short,
        "PAPERFORGE_COMMIT": paperforge_commit,
        "PAPERFORGE_SHORT": paperforge_short,
        "PDF_SHA256": pdf_hash,
        "PDF_SHA256_SHORT": pdf_hash[:16],
    }
    replace_placeholders(values)

    status = {
        "schema": 1,
        "paper": {
            "title": EXPECTED_TITLE,
            "version": version,
            "source_commit": source_commit,
            "pdf_sha256": pdf_hash,
        },
        "paperforge": {
            "commit": paperforge_commit,
            "paper_entry": f"paper/{paper_entry}",
        },
        "formalization": {
            "lean_version": "4.31",
            "mathlib_version": "4.31",
            "scope": [
                "50-vertex graph-level counterexample certificate",
                "finite spectral certificates at orders 38, 39, 40, and 42",
                "all-degree one-variable LP optimum, attainment, and rigidity",
            ],
        },
    }
    (SITE_OUTPUT / "status.json").write_text(
        json.dumps(status, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    (SITE_OUTPUT / ".nojekyll").write_text("", encoding="utf-8")

    print(f"assembled site: {SITE_OUTPUT}")
    print(f"interactive paper entry: paper/{paper_entry}")
    print(f"manuscript version: {version}")
    print(f"source commit: {source_commit}")
    print(f"PDF SHA-256: {pdf_hash}")


if __name__ == "__main__":
    main()
