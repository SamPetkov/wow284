# WOW-284 extended exact-verification package

Prepared 23 July 2026 for Samuil Petkov.

## Main conclusions

The package independently verifies:

| Graph | Construction | Order | Minimum dual degree | Least distance eigenvalue | Exact score |
|---|---|---:|---:|---:|---:|
| `G50` | Hoffman-Singleton coordinate graph | 50 | `7` | `-4` | `3` |
| `G42` | second subconstituent of one `G50` vertex | 42 | `6` | `-5` | `1` |
| `G40` | delete `P_(0,*)` and `Q_(0,*)` | 40 | `6` | `-5` | `1` |
| `G39` | delete one vertex from `G40` | 39 | `35/6` | rigorously greater than `-35/6` | positive |
| `G38` | delete adjacent `P_(1,0),P_(1,1)` from `G40` | 38 | `17/3` | `-3-sqrt(7)` | `8/3-sqrt(7)>0` |

The exact finite descendant audit additionally proves:

- all 40 labelled single-vertex deletions of `G40` have the same exact distance characteristic polynomial and are counterexamples;
- all 120 labelled edge-endpoint deletions of `G40` have the same exact distance characteristic polynomial and are counterexamples;
- no isomorphism or minimality assertion is needed for those exhaustive finite statements.

## Generalizations actually checked

The report and scripts cover the following mathematical mechanisms.

1. **Regular diameter two:** girth five forces the Moore-graph situation; the existing Moore threshold applies.
2. **Regular diameter three:** for a connected `k`-regular graph of girth at least five,
   `D = 3J + (k-3)I - 2A - A^2`, and the strict counterexample criterion is
   `max_{theta != k} |theta+1| < sqrt(2k-2)`.
3. **Moore second subconstituents:** a degree-`K` diameter-two Moore graph gives a `(K-1)`-regular graph on `K(K-1)` vertices with least distance eigenvalue
   `-(5+sqrt(4K-3))/2`; it is a counterexample for integer `K >= 6`.
4. **Equitable induced-subgraph deletion:** a block-matrix framework includes the Petersen deletion that creates `G40`.
5. **Balanced layer deletions:** exact representatives for `m=0,...,4` give scores `3,1,-1,-3,0`; the natural chain stops producing strict examples after `m=1`.
6. **Negative controls:** exact checks of the Odd graph `O_4=KG(7,3)` and the Heawood graph, plus a general obstruction for regular bipartite diameter-three graphs.
7. **Three-vertex deletion screen:** all 9,880 deletions from the fixed `G40` were screened numerically; none was positive. This is exploratory only and is not a minimality proof.

No unconditional infinite family was found. The Moore-based statement is parameterized by Moore-graph existence. Covers, subdivisions and vertex replacements are not claimed to preserve the inequality.

## Files

- `report/wow284_extended_report.tex` — self-contained LaTeX working note.
- `report/wow284_extended_report.pdf` — rendered nine-page copy.
- `report/references.bib` and matching `.bbl` — bibliography.
- `scripts/verify_wow284_38_40_42.py` — principal exact verifier.
- `scripts/verify_38_graph6_independent.py` — independent graph6/Fraction-LDL pass.
- `scripts/verify_descendant_families.py` — exact exhaustive 40-singleton and 120-edge audit.
- `scripts/explore_generalizations.py` — exact broader checks plus clearly labelled numerical screen.
- `scripts/export_graphs.py` — regenerates graph6, edge-list and adjacency-list files.
- `data/graphs/` — reproducible representations of `G38`, `G39`, `G40`, `G42`, `G50`.
- `source_notes/` — the supplied handoff and the detailed Markdown audit.
- `legacy_50/` — the earlier 50-vertex submission metadata and audit note; Lean files are intentionally not duplicated.
- `logs/` — captured successful output.
- `SHA256SUMS` — integrity hashes.

## Reproduction

Use Python 3.11 or later. The audited environment used Python 3.13.5, SymPy 1.14.0, NetworkX 3.6.1 and NumPy 2.3.5.

```bash
python -m pip install -r requirements.txt
python scripts/verify_wow284_38_40_42.py
python scripts/verify_38_graph6_independent.py
python scripts/verify_descendant_families.py
python scripts/explore_generalizations.py
python scripts/export_graphs.py
```

To compile the report:

```bash
cd report
pdflatex wow284_extended_report.tex
bibtex wow284_extended_report
pdflatex wow284_extended_report.tex
pdflatex wow284_extended_report.tex
```

The existing `.bbl` can also be retained for a PDFLaTeX build without rerunning BibTeX.

## Scope

This is an exact internal verification package, not external peer review. It does not establish priority, novelty against every unpublished source, an unconditional infinite family, or minimality below order 38.
