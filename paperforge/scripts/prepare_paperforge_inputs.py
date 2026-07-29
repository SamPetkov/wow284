#!/usr/bin/env python3
"""Prepare generated Paperforge inputs from the canonical manuscript artifacts.

Paperforge currently converts an authored ``thebibliography`` environment, while
WOW-284 keeps BibTeX as its canonical bibliography.  We therefore create a
throw-away staging draft containing an empty references anchor and generate
``references/extra-biblio.xml`` from the canonical ``references.bib`` in the
citation order recorded by the canonical BBL.  Neither canonical source is
modified.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import re

from pybtex.backends.plaintext import Backend
from pybtex.database import parse_file
from pybtex.style.formatting.unsrt import Style

INSTANCE = Path(__file__).resolve().parents[1]
REPOSITORY = INSTANCE.parent
DRAFT_SOURCE = REPOSITORY / "main.tex"
BIB_SOURCE = REPOSITORY / "references.bib"
BBL_SOURCE = REPOSITORY / "main.bbl"
DRAFT_TARGET = INSTANCE / "inputs" / "draft" / "main.tex"
BIB_TARGET = INSTANCE / "references" / "extra-biblio.xml"

EXPECTED_TITLE = "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284"

TITLE_COMMAND = re.compile(
    r"\\title(?:\[[^\]]*\])?\s*\{([^{}]+)\}",
    re.DOTALL,
)
BIBLIOGRAPHY_BLOCK = re.compile(
    r"\\clearpage\s*"
    r"\\begingroup\s*"
    r"\\footnotesize\s*"
    r"\\setlength\{\\bibsep\}\{0pt\}\s*"
    r"\\renewcommand\{\\bibsection\}\{\\section\*\{References\}\}\s*"
    r"\\bibliographystyle\{[^}]+\}\s*"
    r"\\bibliography\{[^}]+\}\s*"
    r"\\endgroup",
    re.DOTALL,
)
BIBITEM = re.compile(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", re.DOTALL)


def stage_draft() -> None:
    text = DRAFT_SOURCE.read_text(encoding="utf-8")

    # Paperforge's current title extractor does not accept the amsart optional
    # running title split over two lines.  Normalize only the generated staging
    # copy to the ordinary one-argument form.
    title_matches = TITLE_COMMAND.findall(text)
    if len(title_matches) != 1:
        raise AssertionError(f"expected one LaTeX title command, found {len(title_matches)}")
    normalized_title = " ".join(title_matches[0].split())
    if normalized_title != EXPECTED_TITLE:
        raise AssertionError(f"unexpected canonical title: {normalized_title!r}")
    text = TITLE_COMMAND.sub(lambda _match: f"\\title{{{EXPECTED_TITLE}}}", text, count=1)

    replacement = (
        "\\clearpage\n"
        "\\begin{thebibliography}{99}\n"
        "\\end{thebibliography}\n"
    )
    # A callable replacement prevents the regular-expression engine from
    # interpreting LaTeX backslashes (for example ``\clearpage``) as escapes.
    text, count = BIBLIOGRAPHY_BLOCK.subn(lambda _match: replacement, text)
    if count != 1:
        raise AssertionError(
            f"expected one canonical bibliography block in {DRAFT_SOURCE}, found {count}"
        )
    DRAFT_TARGET.parent.mkdir(parents=True, exist_ok=True)
    DRAFT_TARGET.write_text(text, encoding="utf-8", newline="\n")


def canonical_citation_order() -> list[str]:
    keys = BIBITEM.findall(BBL_SOURCE.read_text(encoding="utf-8"))
    if not keys or len(keys) != len(set(keys)):
        raise AssertionError("canonical BBL has no entries or duplicate citation keys")
    return keys


def render_bibliography() -> int:
    database = parse_file(str(BIB_SOURCE), bib_format="bibtex")
    keys = canonical_citation_order()
    unknown = [key for key in keys if key not in database.entries]
    if unknown:
        raise AssertionError(f"BBL keys absent from references.bib: {unknown}")

    style = Style()
    backend = Backend()
    formatted = list(style.format_bibliography(database, citations=keys))
    if [entry.key for entry in formatted] != keys:
        raise AssertionError("Pybtex changed the canonical BBL citation order")

    lines = [
        '<?xml version="1.0" encoding="utf-8"?>',
        "<!-- GENERATED from ../../references.bib and ../../main.bbl. -->",
        "<references-extra>",
    ]
    for label, entry in enumerate(formatted, start=1):
        rendered = " ".join(entry.text.render(backend).split())
        lines.append(
            f'  <biblio type="raw" label="{label}" '
            f'xml:id="bib-{escape(entry.key, quote=True)}">'
            f"{escape(rendered)}"
            "</biblio>"
        )
    lines.append("</references-extra>")
    BIB_TARGET.parent.mkdir(parents=True, exist_ok=True)
    BIB_TARGET.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(formatted)


def main() -> None:
    for path in (DRAFT_SOURCE, BIB_SOURCE, BBL_SOURCE):
        if not path.is_file():
            raise FileNotFoundError(path)
    stage_draft()
    count = render_bibliography()
    print(f"Paperforge staging draft: {DRAFT_TARGET}")
    print(f"Paperforge bibliography entries: {count}")


if __name__ == "__main__":
    main()
