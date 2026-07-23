# Exact Counterexamples and Spectral Mechanisms for WOW-284

**Author:** Samuil Petkov<br>
**Affiliation:** Department of Physics, École normale supérieure, Université PSL, Paris, France<br>
**Email:** <samuil.petkov@phys.ens.psl.eu><br>
**Manuscript version:** 19 July 2026 (`2026-07-19`)<br>
**Repository status:** Public research note; ready for arXiv source upload after the author's final account-level review

This repository studies WOW-284, the minimum-dual-degree conjecture recorded
as Conjecture 7.16 in Aouchiche and Hansen's *Distance Spectra of Graphs: A
Survey*. For every degree-`k` Moore graph of diameter two,

\[
\delta^*(G)=k,\qquad
\partial_{k^2+1}(G)=-\frac{3+\sqrt{4k-3}}2.
\]

Consequently WOW-284 holds for `k = 2`, is an equality for `k = 3`, and
fails for every realizable degree `k > 3`.

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

## A 40-vertex induced counterexample

Deleting the induced Petersen graph
`{P_(0,j), Q_(0,j) : j in F_5}` leaves the classical 40-vertex `(6,5)`-cage.
It is 6-regular, has girth five and diameter three, and has exact spectra

\[
\operatorname{Spec}A=
\{6^{(1)},2^{(18)},1^{(4)},(-2)^{(5)},(-3)^{(12)}\},
\]

\[
\operatorname{Spec}D=
\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}.
\]

Therefore `delta*=6>5=-lambda_min(D)`, a strict gap of one. The manuscript
gives a self-contained block-matrix proof, and `scripts/verify_40.py` checks
the construction, BFS distances, block identities, characteristic
polynomials, and a positive rational `LDL^T` certificate exactly.

## Further exact counterexamples

Reproducible exact Python programs verify strict counterexamples of orders 38,
39, 40, 42, and 50. The explicit 38-vertex example has

\[
\delta^*=\frac{17}{3},\qquad
\lambda_{\min}(D)=-3-\sqrt7,
\qquad
\delta^*+\lambda_{\min}(D)=\frac83-\sqrt7>0.
\]

Exact exhaustive computation proves that all 40 labelled single-vertex
deletions of the 40-vertex graph and all 120 labelled edge-endpoint deletions
are strict counterexamples. The repository also proves a regular
diameter-three spectral criterion and a parameterized construction from Moore
second subconstituents. It does not claim that order 38 is minimal or that the
construction gives an unconditional infinite family.

The degree-7 graph is the Hoffman-Singleton graph. The proof does not rely on
that identification: it verifies directly from coordinates over
\(\mathbb F_5\) that every adjacent pair has no common neighbor and every
nonadjacent pair has exactly one. That certificate gives connectedness,
diameter two, girth five, and the matrix identity
\(A^2=6I-A+J\), from which the full spectrum follows.

## Prior work and scope

Aouchiche and Hansen record WOW-284 and attribute it to Siemion Fajtlowicz's
1998 *Written on the Wall* report. Their 2014 survey states that the conjecture
was open there and notes equality for the Petersen graph.

The distance-spectral input is not claimed as new. Howlader and Panigrahi
published a distance-polynomial treatment of minimal `(k,5)`-cages and
explicitly listed the Petersen, Hoffman-Singleton, and hypothetical degree-57
Moore cases in 2022. Combining their `k = 7` calculation with regularity and
girth already gives the counterexample. This note isolates the sharp `k > 3`
criterion, records the WOW-284 connection, and supplies an independent,
self-contained coordinate proof.

The targeted source search documented in [`SOURCE_LEDGER.md`](SOURCE_LEDGER.md)
did not locate an earlier source explicitly connecting the Hoffman-Singleton
graph to WOW-284. That search is not a proof of priority. The manuscript makes
no claim that the observation is first, that any displayed distance spectrum
is new, or that 38 is the smallest counterexample order.

Primary links:

- [Aouchiche-Hansen survey](https://doi.org/10.1016/j.laa.2014.06.010)
- [Hoffman-Singleton paper](https://doi.org/10.1147/rd.45.0497)
- [Howlader-Panigrahi distance-spectrum paper](https://doi.org/10.1016/j.laa.2021.11.014)
- [Howlader-Panigrahi arXiv source](https://arxiv.org/abs/2109.05274)
- [O'Keefe-Wong 40-vertex cage](https://doi.org/10.1016/0095-8956(79)90052-2)
- [Wong uniqueness theorem](https://doi.org/10.1002/jgt.3190030413)
- [Klin-Muzychuk-Ziv-Av structural study](https://doi.org/10.1307/mmj/1242071692)

## Repository map

- `main.tex` - authoritative manuscript source, A4 `amsart`, exact one-inch margins.
- `main.pdf`, `main.bbl` - compiled publication artifacts.
- `manuscript.md` - generated noncanonical reading copy.
- `references.bib` - bibliography maintenance file.
- `src/wow284_graph.py` - standard-library coordinate construction, BFS, girth, and dual-degree routines.
- `src/wow284_induced40.py` - exact induced 40-vertex construction and structural certificate.
- `scripts/verify_exact.py` - exact SymPy characteristic-polynomial and rational (LDL^{\mathsf T}) certificate.
- `scripts/verify_40.py` - exact block, spectrum, and positive-definiteness certificate for the 40-vertex graph.
- `scripts/verify_extended.py` - cross-platform runner for all extended exact certificates.
- `scripts/verify_wow284_38_40_42.py` - combined exact verifier for orders 38, 39, 40, and 42.
- `scripts/verify_38_graph6_independent.py` - graph6/integer-BFS/Fraction-LDL audit of the 38-vertex graph.
- `scripts/verify_descendant_families.py` - exhaustive exact audit of all 40 singleton and 120 edge-endpoint deletions.
- `scripts/explore_generalizations.py` - exact controls plus a separately labelled numerical screen.
- `scripts/export_graphs.py` - deterministic graph6, adjacency-list, edge-list, and summary exporter.
- `scripts/export_graph_data.py` - deterministic edge, adjacency, and distance CSV exporter.
- `scripts/generate_lean_diagonalization.py` - deterministic exact-data generator for the Lean spectral certificate.
- `scripts/generate_lean40_structural.py`, `scripts/generate_lean40_diagonalization.py` - deterministic generators for the staged 40-vertex Lean certificates.
- `scripts/generate_lean38_certificates.py`, `scripts/generate_lean38_ldl.py` - deterministic generators for the staged 38-vertex finite and LDL data.
- `tests/` - exhaustive structural and exact spectral regression tests.
- `results/verification.json` - machine-readable exact verification record.
- `results/verification_40.json` - machine-readable exact verification record for the 40-vertex graph.
- `results/edges.csv`, `results/adjacency_matrix.csv`, `results/distance_matrix.csv` - complete graph data.
- `data/graphs/` - machine-readable representations of the 38-, 39-, 40-, 42-, and 50-vertex graphs.
- `supplement/extended_2026-07-23/` - checksum-preserved original extended handoff, report, code, data, and captured outputs.
- `arxiv/wow284_arxiv_source.zip` - minimal arXiv source archive containing `main.tex`, `references.bib`, and `main.bbl` only.
- `SOURCE_LEDGER.md`, `REVIEW.md`, `PROVENANCE.md` - attribution, novelty, proof-audit, and provenance records.
- `CITATION.cff`, `LICENSE`, `LICENSE_SCOPE.md` - citation and CC BY 4.0 metadata.
- `BUILD_VERIFICATION.txt`, `MANIFEST.txt`, `SHA256SUMS` - release preflight and integrity records.
- `lean/` - Lean 4.31/Mathlib 4.31 development and pinned project configuration.

## Formal verification

The explicit 50-vertex counterexample is fully formalized and verified in
Lean 4.31/Mathlib 4.31. The development checks the graph definition,
simplicity, 7-regularity, the exhaustive common-neighbor certificate, girth
five, the adjacency-square and distance-matrix identities, and an exact
spectral diagonalization with multiplicities `91^1`, `(-4)^28`, and `1^21`.
The scalar `k <= 3` threshold is formalized separately. The generic
Moore-graph derivation in the paper remains a conventional proof, so the
completed formal-verification claim is intentionally limited to the explicit
50-vertex counterexample and the scalar threshold.

The 38-, 39-, 40-, and 42-vertex results and the extended criteria are
analytic results verified by reproducible exact Python certificates; they are
outside the completed Lean-verification claim.

The spectral computation is sharded into bounded integer certificates and
then assembled into a rational two-sided inverse and diagonalization. The
release audit rejects `sorry`, `admit`, `native_decide`, `bv_decide`, unsafe
declarations, and new axioms. Representative axiom audits report only the
standard dependencies `propext`, `Classical.choice`, and `Quot.sound`.

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
python scripts/verify_40.py --output results/verification_40.json
python scripts/export_graph_data.py --output-dir results
python scripts/verify_extended.py
```

The theorem-level verification is exact and does not use floating-point
eigenvalues. Distance matrices are reconstructed by integer BFS rather than
from the manuscript's spectral identities. To include the explicitly labelled
numerical three-vertex screen, run
`python scripts/verify_extended.py --include-exploratory`.

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
the exact graph construction. Samuil Petkov is the sole
author and accepts full responsibility for the mathematics, citations,
attribution, and conclusions. Reproducible checks are not peer review or
journal acceptance.
