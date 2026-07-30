# WOW-284 Paperforge site

This directory turns the canonical repository manuscript, `../main.tex`, into a
structured PreTeXt/Paperforge HTML paper and combines it with a hand-authored
project site.

The public site is intended for GitHub Pages at:

```text
https://sampetkov.github.io/wow284/
```

## Source policy

- `../main.tex`, `../references.bib`, and `../main.bbl` remain the canonical
  manuscript, bibliography, and citation-order sources.
- `scripts/prepare_paperforge_inputs.py` creates a disposable staging draft under
  `inputs/` and converts the canonical BibTeX records to Paperforge-native
  bibliography entries. This is an ingestion adapter, not a second manuscript.
- `source/`, `inputs/`, and `output/` are generated and are never hand-edited.
- website-only explanations live under `web-assets/site/`.
- the homepage reserves `#arxiv-link` for the public abstract-page URL; until
  arXiv assigns an identifier at announcement, it displays a forthcoming notice.
- the archived PDF copied to the site is `../main.pdf`; Paperforge does not
  replace the arXiv/journal PDF.
- formalization claims follow `../lean/README.md` and
  `../lean/NON50_CERTIFICATES.md` exactly.

## Local build

Prerequisites are Python 3.11 or later and Git. The script creates a local virtual
environment, pins Paperforge and PreTeXt, stages the canonical BibTeX inputs,
generates the interactive paper, assembles the project pages, and runs the smoke
tests:

```bash
bash paperforge/scripts/build-local.sh
```

The output is written to:

```text
paperforge/output/site/
```

Serve it locally with:

```bash
python3 -m http.server 8000 --directory paperforge/output/site
```

Then open `http://localhost:8000/`.

## Pinned toolchain

```text
Paperforge  726cc7d679441e28f39cfd52d3e2dd0251c79a6d
PreTeXt     2.43.2
```

The pin is repeated in the GitHub Pages workflow and embedded in the generated
`status.json`.

## Formalization links

The first site release links to the complete public Lean source and describes
its verified scope. Per-statement Paperforge Lean badges are intentionally a
second phase. Paperforge's declaration-map mining is heuristic; the candidate
map must be reviewed before badges are accepted and published.

The intended follow-up is:

1. configure `[formalizations.primary]` against `../lean`;
2. run `paperforge ingest --bootstrap`;
3. review `crosswalk/lean-decl-map.candidate.json` statement by statement;
4. accept only accurate theorem-to-declaration links;
5. add filtered doc-gen4 or Verso output under the Pages site.

This prevents helper declarations or finite matrix certificates from being
presented as stronger graph-level formalizations than they actually are.

## Deployment

`.github/workflows/paperforge-pages.yml` builds on pull requests and publishes on
pushes to `main`. In the repository settings, GitHub Pages must use **GitHub
Actions** as its source.
