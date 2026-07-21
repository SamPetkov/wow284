# The Hoffman-Singleton Graph Refutes WOW-284

**Author:** Samuil Petkov<br>
**Affiliation:** Ecole normale superieure, Universite PSL, Paris, France<br>
**Manuscript version:** 19 July 2026 (`2026-07-19`)<br>
**Repository status:** Public research note; ready for arXiv source upload after the author's final account-level review

This repository gives a self-contained 50-vertex counterexample to WOW-284,
the minimum-dual-degree conjecture recorded as Conjecture 7.16 in Aouchiche
and Hansen's *Distance Spectra of Graphs: A Survey*.

For the explicitly constructed graph (G),

\[
g(G)=5,\qquad \delta^*(G)=7,\qquad
\operatorname{Spec}D(G)=\{91^{(1)},1^{(21)},(-4)^{(28)}\}.
\]

Thus

\[
\delta^*(G)=7>4=-\partial_{50}(G),
\]

and the conjectured inequality fails by the strict gap (3).

The graph is the Hoffman-Singleton graph. The proof does not rely on that
identification: it verifies directly from coordinates over
(mathbb F_5) that every adjacent pair has no common neighbor and every
nonadjacent pair has exactly one. That certificate gives connectedness,
diameter two, girth five, and the matrix identity
(A^2=6I-A+J), from which the full spectrum follows.

## Prior work and scope

Aouchiche and Hansen record WOW-284 and attribute it to Siemion Fajtlowicz's
1998 *Written on the Wall* report. Their 2014 survey states that the conjecture
was open there and notes equality for the Petersen graph.

The distance spectrum used here is not claimed as new. Howlader and
Panigrahi explicitly published the Hoffman-Singleton distance spectrum
({91,(-4)^{28},1^{21}}) in 2022. Combining their calculation with
7-regularity already gives the counterexample. This note records that
connection and supplies an independent, self-contained coordinate proof.

The targeted source search documented in [`SOURCE_LEDGER.md`](SOURCE_LEDGER.md)
did not locate an earlier source explicitly connecting the Hoffman-Singleton
graph to WOW-284. That search is not a proof of priority. The manuscript makes
no claim that the observation is first, that the distance spectrum is new, or
that 50 is the smallest counterexample order.

Primary links:

- [Aouchiche-Hansen survey](https://doi.org/10.1016/j.laa.2014.06.010)
- [Written on the Wall II catalogue](http://cms.dt.uh.edu/faculty/delavinae/research/wowII/list.htm)
- [Hoffman-Singleton paper](https://doi.org/10.1147/rd.45.0497)
- [Howlader-Panigrahi distance-spectrum paper](https://doi.org/10.1016/j.laa.2021.11.014)
- [Howlader-Panigrahi arXiv source](https://arxiv.org/abs/2109.05274)

## Repository map

- `main.tex` - authoritative manuscript source, A4 `amsart`, exact one-inch margins.
- `main.pdf`, `main.bbl` - compiled publication artifacts.
- `manuscript.md` - generated noncanonical reading copy.
- `references.bib` - bibliography maintenance file.
- `src/wow284_graph.py` - standard-library coordinate construction, BFS, girth, and dual-degree routines.
- `scripts/verify_exact.py` - exact SymPy characteristic-polynomial and rational (LDL^{\mathsf T}) certificate.
- `scripts/export_graph_data.py` - deterministic edge, adjacency, and distance CSV exporter.
- `tests/` - exhaustive structural and exact spectral regression tests.
- `results/verification.json` - machine-readable exact verification record.
- `results/edges.csv`, `results/adjacency_matrix.csv`, `results/distance_matrix.csv` - complete graph data.
- `arxiv/wow284_arxiv_source.zip` - minimal arXiv source archive containing `main.tex`, `references.bib`, and `main.bbl` only.
- `SOURCE_LEDGER.md`, `REVIEW.md`, `PROVENANCE.md` - attribution, novelty, proof-audit, and provenance records.
- `CITATION.cff`, `LICENSE`, `LICENSE_SCOPE.md` - citation and CC BY 4.0 metadata.
- `BUILD_VERIFICATION.txt`, `MANIFEST.txt`, `SHA256SUMS` - release preflight and integrity records.

## Reproduce the exact certificate

Python 3.11 or later is supported. Create an isolated environment and install
the pinned dependencies:

```bash
python -m venv .venv
python -m pip install -r requirements.txt -r requirements-dev.txt
```

On Windows, activate with `.venv\Scripts\Activate.ps1`; on POSIX systems, use
`source .venv/bin/activate`. Then run:

```bash
python -m pytest -q
python scripts/verify_exact.py --output results/verification.json
python scripts/export_graph_data.py --output-dir results
```

The symbolic verification is exact. It does not use floating-point
eigenvalues. The distance matrix is constructed by 50 independent integer BFS
runs rather than by the manuscript's formula (D=2J-2I-A).

## Build and synchronize the manuscript

A current TeX distribution with `latexmk` and BibTeX, plus Pandoc, is required.

```bash
python scripts/sync_manuscript_artifacts.py
```

This compiles in a short temporary directory, regenerates the Markdown copy,
mirrors the arXiv files, creates the deterministic source ZIP, and refreshes
the manifest and checksum ledger. Validate a frozen release without modifying
it with:

```bash
python scripts/sync_manuscript_artifacts.py --check
python scripts/validate_repository.py
```

On Windows, `./build.ps1` performs the full verification and synchronization
sequence. `make check` and `./build.sh` provide equivalent POSIX entry points.

## arXiv package

The upload archive is [`arxiv/wow284_arxiv_source.zip`](arxiv/wow284_arxiv_source.zip).
It excludes PDFs, logs, caches, repository administration, proof audits, and
code because arXiv asks authors not to include files that are unnecessary for
TeX processing. The archive includes the matching `.bbl` and `.bib`; the main
file uses a fixed date rather than `\today`.

Suggested arXiv primary category: `math.CO`. See
[`SUBMISSION_NOTES.md`](SUBMISSION_NOTES.md) for title, abstract, comments,
license, and final account-level checks. This repository prepares the upload
package but does not represent an arXiv submission or endorsement decision.

## License and responsibility

Except for cited third-party material and dependencies, the original
repository material is licensed by Samuil Petkov under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See
[`LICENSE_SCOPE.md`](LICENSE_SCOPE.md) for the exact scope.

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking and finding
the exact coordinate construction used for the graph. Samuil Petkov is the sole
author and accepts full responsibility for the mathematics, citations,
attribution, and conclusions. Reproducible checks are not peer review or
journal acceptance.
