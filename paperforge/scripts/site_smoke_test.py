#!/usr/bin/env python3
"""Fail-closed checks for the assembled WOW-284 Paperforge site."""
from __future__ import annotations

from html.parser import HTMLParser
import hashlib
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

INSTANCE = Path(__file__).resolve().parents[1]
REPOSITORY = INSTANCE.parent
SITE = INSTANCE / "output" / "site"
CUSTOM_PAGES = [
    SITE / "index.html",
    SITE / "formalization" / "index.html",
    SITE / "reproducibility" / "index.html",
]


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag not in {"a", "link", "script", "img"}:
            return
        key = "href" if tag in {"a", "link"} else "src"
        for name, value in attrs:
            if name == key and value:
                self.links.append(value)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def resolve_local(page: Path, target: str) -> Path | None:
    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("mailto:", "javascript:", "#")):
        return None
    path_part = unquote(parsed.path)
    if not path_part:
        return None
    candidate = (page.parent / path_part).resolve()
    try:
        candidate.relative_to(SITE.resolve())
    except ValueError as error:
        raise AssertionError(f"local link escapes the site tree: {page} -> {target}") from error
    if path_part.endswith("/"):
        candidate /= "index.html"
    elif candidate.is_dir():
        candidate /= "index.html"
    return candidate


def check_custom_page(page: Path) -> int:
    if not page.is_file():
        raise AssertionError(f"missing custom page: {page}")
    text = page.read_text(encoding="utf-8")
    if "{{" in text or "}}" in text:
        raise AssertionError(f"unexpanded placeholder in {page}")
    parser = LinkCollector()
    parser.feed(text)
    checked = 0
    for target in parser.links:
        local = resolve_local(page, target)
        if local is None:
            continue
        if not local.exists():
            raise AssertionError(f"broken local link: {page.relative_to(SITE)} -> {target}")
        checked += 1
    return checked


def main() -> None:
    required = [
        SITE / "index.html",
        SITE / "site.css",
        SITE / "paper" / "index.html",
        SITE / "paper.pdf",
        SITE / "CITATION.cff",
        SITE / "BUILD_VERIFICATION.txt",
        SITE / "SHA256SUMS",
        SITE / "status.json",
        SITE / ".nojekyll",
    ]
    missing = [str(path) for path in required if not path.exists()]
    if missing:
        raise AssertionError(f"missing site artifacts: {missing}")

    pdf = SITE / "paper.pdf"
    if pdf.stat().st_size < 10_000 or not pdf.read_bytes().startswith(b"%PDF-"):
        raise AssertionError("paper.pdf is not a nontrivial PDF")

    paper_html = sorted((SITE / "paper").rglob("*.html"))
    if len(paper_html) < 2:
        raise AssertionError("Paperforge output does not contain an interactive HTML document")

    status = json.loads((SITE / "status.json").read_text(encoding="utf-8"))
    if status.get("schema") != 1:
        raise AssertionError("unexpected status.json schema")
    expected_hash = sha256(REPOSITORY / "main.pdf")
    if status["paper"]["pdf_sha256"] != expected_hash:
        raise AssertionError("site PDF checksum disagrees with canonical main.pdf")
    if sha256(pdf) != expected_hash:
        raise AssertionError("copied site PDF differs from canonical main.pdf")

    links = sum(check_custom_page(page) for page in CUSTOM_PAGES)

    custom_text = "\n".join(page.read_text(encoding="utf-8") for page in CUSTOM_PAGES)
    forbidden = [
        "smallest counterexample",
        "first proof",
        "fully formalized paper",
        "classifies all counterexamples",
    ]
    for phrase in forbidden:
        if phrase in custom_text.lower():
            raise AssertionError(f"unsupported site claim: {phrase}")

    print("WOW-284 Paperforge site smoke test: PASS")
    print(f"custom pages: {len(CUSTOM_PAGES)}")
    print(f"local links checked: {links}")
    print(f"generated HTML files: {len(paper_html)}")
    print(f"PDF SHA-256: {expected_hash}")


if __name__ == "__main__":
    main()
