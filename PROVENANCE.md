# Provenance and AI-assistance record

**Author:** Samuil Petkov<br>
**Repository revision:** 24 July 2026; active PDF date suppressed<br>
**Audit and package preparation:** 21--24 July 2026

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

## AI assistance

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking, proof
exploration, and Lean formalization. No AI system is named as an author.
Samuil Petkov accepts full responsibility for all mathematical,
bibliographic, legal, and submission claims.

## Limits

The exact scripts and audit documents are reproducibility aids, not external
peer review. The source search is targeted and cannot establish absolute
priority or absence from unpublished communications. The repository therefore
avoids a first-discovery claim and makes no minimality claim.

The Lean 4.31 development is recorded separately from the analytic and exact
Python proofs. The explicit 50-vertex certificate and scalar degree threshold
are fully formalized. The non-50 public endpoints are kernel-checked finite
spectral certificates: they do not bundle every graph-theoretic hypothesis or
identify their semantic matrices with Mathlib's `SimpleGraph.dist` in one
theorem. AxiomMath AXLE could not complete the expanded modular closure because
its remote worker exhausted memory; the incomplete fallback was rejected and
no AXLE claim is made for those endpoints.
