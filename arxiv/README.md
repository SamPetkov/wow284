# WOW-284: revised replacement manuscript

This directory contains the current manuscript and its source package, prepared on 14 November 2026 from the author's revised sources of 13 November 2026. The manuscript is dated 29 July 2026, the date of the first arXiv posting.

## Files

- [main.pdf](main.pdf): the 44-page paper.
- [main.tex](main.tex), [main.bbl](main.bbl), [references.bib](references.bib), [petkov-preprint.sty](petkov-preprint.sty): the matching editable sources.
- [anc/scripts/](anc/scripts/): the arXiv ancillary files.
  - `verify_round3_high_edge_filter.py`, `verify_round5_joint_pairs.py` and `verify_round6_layer_vector.py` reproduce the order-50 profile calculations of Appendix F.
  - `WOW_JOINT_PILOT.json` is the data file read by `verify_round5_joint_pairs.py`.
- [wow284_arxiv_source.zip](wow284_arxiv_source.zip): the four source files and `anc/scripts/`, ready for arXiv.
- [arxiv-abstract.txt](arxiv-abstract.txt) and [arxiv-comments.txt](arxiv-comments.txt): submission text.
- [MANIFEST.txt](MANIFEST.txt) and [SHA256SUMS](SHA256SUMS): directory inventory and digests; the digest list excludes itself.

## Changes in this revision

The paper is reorganized so that the main text follows its lines of argument. Long case analyses, exact spectra and finite certificates are in Appendices A–I, ordered by their first citation in the main text; Appendix J describes the computations and the Lean verification, and the references now precede the appendices. The reorganization changes no statement, constant, hypothesis or conclusion.

The small-order results are new. Section 9 contains:

- **Theorem 9.2.** Every strict counterexample has at least 15 vertices (written proof).
- **Proposition 9.3.** No strict counterexample has at most 19 vertices (exhaustive generation with nauty's `geng`; computer-assisted).
- **Proposition 9.4.** The strict induced subgraphs of the Hoffman–Singleton graph of orders 36 to 50, up to automorphism (computer-assisted). None has order 36 or 37.
- **Proposition 9.5.** Three irregular strict counterexamples of order 40 (computer-assisted; Lean certificates `Wow284.Induced40X`, `Induced40Y`, `Induced40Z`).

Appendix H contains the methods behind these computations and:

- **Theorem H.1.** For a connected graph of girth at least five and diameter at most three, `D = 3J − 3I − 2A − A² + Δ`, with `Δ` the diagonal degree matrix; hence `Φ(G) > 0` exactly when `3J + Δ + (δ*(G) − 2)I − (A + I)²` is positive definite. Proved; the two identities and the positive-definiteness equivalence are checked in Lean (`Wow284.DiameterThreeMatrix`), and the final step to `Φ` is written. Corollary H.2 is the corresponding form for deletions from a Moore graph.
- **Proposition H.3.** An irregular graph of order 43 with `Φ = 0` (computer-assisted; direct certificate in `scripts/verify_order43_equality.py`).
- **Proposition H.4** and **Conjecture H.5.** For `R` and `X42`, deleting two vertices leaves a strict counterexample exactly when they are adjacent (computer-assisted); the conjecture extends this to every 6-regular strict counterexample of girth five and diameter three.

The new results in Appendix F are:

- **Proposition F.4.** Let `G` be a 6-regular graph of order 50, girth at least five and diameter three, and let `τ(v)` count the five-cycles through `v`. Then `Φ(G) ≤ (795 − 21τ(v))/377` for every vertex `v`.
- **Corollary F.6.** Under the hypotheses of Theorem F.5, the high-edge graph is a disjoint union of cycles of length at least five, covering `5j` vertices for some `j = 0, …, 10`, and `50 − 5j` isolated vertices.

The abstract is rewritten, several sections are edited for clarity, and inline references to individual scripts are replaced by one section on code and data (Section J.1).

## Formalization boundary

Appendix J distinguishes the Lean-checked finite certificates, the graph-level diameter-three identities and the graph-independent LP optimum from the written graph-level arguments. Among the small-order results (Section 9 and Appendix H), only the identities and the positive-definiteness equivalence of Theorem H.1 and the certificates of Proposition 9.5 are checked in Lean. The order-50 results above are written results supported by exact computation, not Lean theorems. See the [Lean README](../lean/README.md).

## Build

Use a TeX distribution with pdfLaTeX, BibTeX, `latexmk`, and the packages
loaded by `main.tex` and `petkov-preprint.sty`. For a minimal installation,
include `newtx`, its `kastrup` (`binhex.tex`) support, and the `tex-gyre` fonts.
Keep all four source files together and run from this directory:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The ZIP contains `main.tex`, `main.bbl`, `references.bib`, and `petkov-preprint.sty` at its root, and the ancillary files under `anc/scripts/`. arXiv lists the files under `anc/` separately as ancillary files. Its replacement destination is arXiv:2607.27452.
