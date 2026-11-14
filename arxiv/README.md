# WOW-284: revised replacement manuscript

This directory contains the current manuscript and its source package, prepared on 14 November 2026 from the author's revised sources of 13 November 2026. The manuscript is dated 29 July 2026, the date of the first arXiv posting.

## Files

- [main.pdf](main.pdf): the 41-page paper.
- [main.tex](main.tex), [main.bbl](main.bbl), [references.bib](references.bib), [petkov-preprint.sty](petkov-preprint.sty): the matching editable sources.
- [anc/scripts/](anc/scripts/): the arXiv ancillary files.
  - `verify_round3_high_edge_filter.py`, `verify_round5_joint_pairs.py` and `verify_round6_layer_vector.py` reproduce the order-50 profile calculations of Appendix A.
  - `WOW_JOINT_PILOT.json` is the data file read by `verify_round5_joint_pairs.py`.
- [wow284_arxiv_source.zip](wow284_arxiv_source.zip): the four source files and `anc/scripts/`, ready for arXiv.
- [arxiv-abstract.txt](arxiv-abstract.txt) and [arxiv-comments.txt](arxiv-comments.txt): submission text.
- [MANIFEST.txt](MANIFEST.txt) and [SHA256SUMS](SHA256SUMS): directory inventory and digests; the digest list excludes itself.

## Changes in this revision

Both new results are in Appendix A:

- **Proposition A.2.** Let `G` be a 6-regular graph of order 50, girth at least five and diameter three, and let `τ(v)` count the five-cycles through `v`. Then `Φ(G) ≤ (795 − 21τ(v))/377` for every vertex `v`.
- **Corollary A.4.** Under the hypotheses of Theorem A.3, the high-edge graph is a disjoint union of cycles of length at least five and isolated vertices. Its necessary degree profiles are `(n_0, n_2, n_4) = (50 − 5j, 5j, 0)` for `j = 0, …, 10`.

The abstract is rewritten, several sections are edited for clarity, and inline references to individual scripts are replaced by one section on code and data (Section I.1).

## Formalization boundary

Appendix I distinguishes the Lean-checked finite certificates and the graph-independent LP optimum from the written graph-level arguments. The order-50 results above are written results supported by exact computation, not Lean theorems. See the [Lean README](../lean/README.md).

## Build

Use a TeX distribution with pdfLaTeX, BibTeX, `latexmk`, and the packages
loaded by `main.tex` and `petkov-preprint.sty`. For a minimal installation,
include `newtx`, its `kastrup` (`binhex.tex`) support, and the `tex-gyre` fonts.
Keep all four source files together and run from this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The ZIP contains `main.tex`, `main.bbl`, `references.bib`, and `petkov-preprint.sty` at its root, and the ancillary files under `anc/scripts/`. arXiv lists the files under `anc/` separately as ancillary files. Its replacement destination is arXiv:2607.27452.
