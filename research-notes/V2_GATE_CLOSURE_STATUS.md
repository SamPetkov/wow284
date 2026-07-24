# Candidate closure status for the four mandatory v2 gates

This branch is stacked on PR #12 and does not modify the submitted manuscript
or arXiv package. A gate is not approved merely because its files exist: it
still requires independent mathematical review and green CI.

| Gate | Candidate artifact | Independent route | Status |
| --- | --- | --- | --- |
| Jørgensen order-96 provenance | source snapshot, normalized rows, graph6, provenance JSON, exact verifier | legacy row parser plus new three-way reconstruction | candidate closed |
| No floating spectral decisions | exact extension entrypoint and AST workflow audit | exact characteristic polynomials, Sturm, LDL, quotient arguments | candidate closed |
| Degree-six \(c\ge15\) | exact layer-compression proof | independent fourth-moment proof | candidate closed |
| Nonadjacent puncture direct sum | generic orthogonal decomposition and multiplicity proof | explicit 48-dimensional \(k=7\) basis audit | candidate closed |

Promotion to a manuscript PR requires:

1. all exact gate workflows green;
2. independent review of the written proofs;
3. no unresolved review thread affecting a gate;
4. refreshed literature wording;
5. a separate PR for any `main.tex` change.
