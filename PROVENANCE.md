# Provenance and AI-assistance record

**Author:** Samuil Petkov<br>
**Manuscript date:** 19 July 2026<br>
**Audit and package preparation:** 21--22 July 2026

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

## AI assistance

OpenAI ChatGPT-5.6 Sol Pro assisted with adversarial proof checking and finding
the exact graph construction. No AI system is named as
an author. Samuil Petkov accepts full responsibility for all mathematical,
bibliographic, legal, and submission claims.

## Limits

The exact scripts and audit documents are reproducibility aids, not external
peer review. The source search is targeted and cannot establish absolute
priority or absence from unpublished communications. The repository therefore
avoids a first-discovery claim and makes no minimality claim.

The Lean 4.31 development is recorded separately from the analytic and exact
Python proofs. Until the spectral theorem passes the strict audit and CI, the
manuscript claims full Lean verification only for the explicit 50-vertex
counterexample and separately records the formalized scalar degree threshold.
