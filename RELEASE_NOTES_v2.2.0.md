# WOW-284 v2.2.0

This release replaces the focused counterexample note with the expanded
manuscript *Counterexamples, Spectral Obstructions, and Deletion Stability for
WOW-284*.

## Mathematical additions

- Exact regular diameter-three score calculus:
  \[
  \delta^*(G)+\lambda_{\min}(D(G))
  =2k-2-\max_{\theta\ne k}(\theta+1)^2.
  \]
- Degree and diameter obstructions: every regular strict counterexample has
  degree at least six and diameter at most four; a diameter-four example must
  have degree at least ten.
- The exact all-degree one-variable nonbacktracking LP optimum
  \[
  B_k=\frac{(k+2)(k^2+3)}6
  \]
  and its unique optimizer up to positive scale.
- An edge-local five-cycle certificate excluding degree-six order 51, so a
  degree-six regular strict counterexample has order at most 50.
- Complete distance spectra for one-vertex, adjacent-pair, and nonadjacent-pair
  punctures of Moore graphs.
- A general deletion-stability inequality and a metric normal form for every
  puncture of size at most \(k-1\).
- Exact Hoffman--Singleton robustness: every deletion of at most five vertices
  remains a strict counterexample, while one explicit six-vertex deletion does
  not.
- Equality cases, finite-field and matching-deletion obstructions, and local
  constraints on a hypothetical degree-six order-50 example.

## Formal and computational verification

- Lean 4.31 retains the complete graph-level certificate for the explicit
  50-vertex counterexample.
- Lean 4.31 retains finite spectral certificates for orders 38, 39, 40, and
  42.
- A separate Lean 4.31 development formalizes the exact analytic LP optimum,
  its explicit admissible attaining coefficient family, and optimizer
  uniqueness both polynomially and coefficientwise.
- The LP formalization is deliberately graph-independent. The trace/spectral
  graph bridge, graph-order corollaries, punctured-Moore theorems, and deletion
  theory remain analytic proofs with exact Python audits.
- Proof Audits 01--13 and their independent exact verifiers are integrated
  into the manuscript and release inventory.

## Publication package

- Expanded canonical TeX, regenerated bibliography, PDF, Markdown reading
  copy, and minimal deterministic arXiv source ZIP.
- A4 paper, explicit one-inch margins, suppressed manuscript date, three
  focused keywords, and references beginning on a new page.
- Updated `CITATION.cff`, submission metadata, provenance, review, licensing,
  manifest, and strict one-entry-per-file SHA-256 ledger.
- The 19 July 2026 source snapshot remains unchanged at
  `archive/main_2026-07-19.tex`.

The immutable `v2.2.0` tag and GitHub release must be created only from the
exact tree that passes the final warning-fatal Lean 4.31 replay, repository
validation, clean TeX build, isolated arXiv ZIP build, and checksum audit.
