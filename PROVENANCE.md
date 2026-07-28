# Provenance and AI-assistance record

**Author:** Samuil Petkov<br>
**Repository revision:** 29 July 2026; active PDF date suppressed<br>
**Audit and package preparation:** 21--29 July 2026

## Submitted material

Samuil Petkov submitted the explicit coordinate construction, the claimed
common-neighbor certificate, the adjacency and distance spectral derivation,
the strict WOW-284 violation, and an exact SymPy verification script as an
attached text file.

The supplied argument identified the graph as a coordinate realization of the
Hoffman-Singleton graph but deliberately proved all properties directly. The
canonical manuscript preserves that self-contained route.

The 22 July revision adds the degree-`k` Moore-graph criterion after an
adversarial review. Published minimal-cage distance-spectral formulas remain
explicitly credited; the revision does not claim those formulas as new.

On 23 July, the author supplied the extended 38/39/40/42/50 verification
package now preserved checksum-for-checksum under
`supplement/extended_2026-07-23/`. Its exact programs and graph files were
rerun in an isolated Python 3.13 environment. The canonical integration adds
verifier hardening, deterministic graph export, an integer-BFS graph6 audit,
and repairs to the Moore-subconstituent and equitable-deletion arguments.

The author subsequently supplied a generated Lean 4.31 extension. The
repository now contains kernel-checked finite spectral certificates for the
explicit constructions of orders 38, 39, 40, and 42. GitHub Actions compiled
every public endpoint with the pinned Lean/Mathlib 4.31 toolchain; the
transitive axiom reports contain only `propext`, `Classical.choice`, and
`Quot.sound`. Static source scans and deterministic generator checks reject
proof placeholders, unsafe declarations, and new axioms.

The expanded v2.3 manuscript integrates Proof Audits 01--14. Each records an
exact theorem statement, corrections or strengthening discovered during
review, a claim boundary, and an independent exact verifier. The registry at
`research-notes/PROOF_AUDIT_REGISTRY.md` maps these audits to the theorems
that appear in `main.tex`.

Proof Audit 14 introduces the integral optimal-slack and excess-matrix
hierarchy. Its polynomial identities, rounding, low-degree arithmetic, and
deletion-radius consequences were rerun exactly. Its only external theorem
input, the classification of connected regular graphs with least eigenvalue
at least `-2` beyond order 28, was checked against the original
Cameron--Goethals--Seidel--Shult source and a later journal statement.

The all-degree analytic LP optimum was formalized separately in Lean 4.31.
The formal dependency chain covers the nonbacktracking recurrence, the
explicit extremal coefficient family, admissibility and attainment, the
three-point dual moments, every positive slack including the uniform
Chebyshev tail, weak duality, complementary slackness, and uniqueness both as
a polynomial and coefficientwise. The graph trace/spectral bridge and the
punctured-Moore and deletion theorems remain analytic rather than Lean claims.

## AI assistance

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof
exploration, and Lean formalization. Samuil Petkov accepts full responsibility
for all mathematical, bibliographic, legal, and submission claims.

## Limits

The exact scripts and audit documents are reproducibility aids, not external
peer review. The manuscript's single priority statement is expressly
qualified by ``to the author's knowledge'' and is anchored to the preserved
source dated 19 July 2026; it does not assert knowledge of unpublished
communications. No minimum-order or classification claim is made.

The Lean 4.31 development is recorded separately from the analytic and exact
Python proofs. The explicit 50-vertex certificate is a complete graph-level
formalization. The non-50 public endpoints are kernel-checked finite spectral
certificates: they do not bundle every graph-theoretic hypothesis or identify
their semantic matrices with Mathlib's `SimpleGraph.dist` in one theorem.
The LP theorem is analytic and graph-independent; it does not formalize the
trace interpretation, spectral trace decomposition, or graph-order bridge.
