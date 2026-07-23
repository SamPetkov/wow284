# WOW-284 arXiv package

The upload artifact is `wow284_arxiv_source.zip`. It contains only
`main.tex`, `references.bib`, and the matching generated `main.bbl`.

The `main.tex`, `main.bbl`, `references.bib`, `main.pdf`, and `main.md` files
in this directory mirror the canonical root artifacts for inspection. The
mirrored PDF and Markdown are not members of the source ZIP.

Build the unpacked source with:

```text
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The manuscript uses `\date{}` so the PDF does not carry a stale internal
version date. arXiv records submission and revision dates separately.
