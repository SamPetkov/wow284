# Provenance and AI-assistance record

**Author:** Samuil Petkov<br>
**Manuscript date:** 19 July 2026<br>
**Audit and package preparation:** 21--23 July 2026

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
repository preserves its induced-40 structural/diagonalization certificates
and induced-38 finite/LDL data as the opt-in `Wow284Extension` target. Static
source scans and deterministic generator checks pass. The extension is not
recorded as a completed formal proof: the 40-vertex endpoint theorem and the
38-vertex positive-definiteness/spectral bridge remain open, and the earlier
AXLE report does not cover these new modules.

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
Python proofs. The explicit 50-vertex certificate and scalar degree threshold
have passed the strict audit and CI. Staged Lean source now covers substantial
finite and matrix certificates for orders 40 and 38, but no expanded
end-to-end formalization is claimed pending the missing wrappers, kernel build,
axiom review, and AXLE strict audit.
