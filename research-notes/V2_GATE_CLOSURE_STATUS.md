# Closure status for the four mandatory v2 gates

The former public PR #12--#23 stack has been integrated, and each gate below
has an exact verifier, an independent check that does not merely call the
original verifier, and a written claim-boundary audit. The completed private
release replay also covers the generated Lean endpoints and standalone source.
Public promotion still requires the exact candidate head to retain green CI
and no unresolved review feedback.

| Gate | Primary artifact | Independent route | Status |
| --- | --- | --- | --- |
| Jørgensen order-96 provenance | source snapshot, normalized rows, graph6, provenance JSON, exact verifier | legacy row parser plus three-way reconstruction | closed |
| No floating spectral decisions | exact extension entrypoint and AST workflow audit | exact characteristic polynomials, Sturm, LDL, and quotient arguments | closed |
| Degree-six \(c\ge15\) | exact layer-compression proof | independent fourth-moment proof | closed |
| Nonadjacent puncture direct sum | generic orthogonal decomposition and multiplicity proof | explicit 48-dimensional \(k=7\) basis audit and Proof Audit 03 | closed |

The release gate is fail-closed: any change to a proof-path verifier, generated
Lean source, manuscript mirror, manifest, or recorded hash must be followed by
the corresponding freshness and replay checks before public merge.
