# WOW-284 v2.3.0

Substantive extension of the expanded manuscript.

- Introduces the positive-semidefinite optimal-slack matrix whose trace is the
  exact one-variable LP defect.
- Proves that its associated integral excess matrix is nonzero, yielding the
  stronger universal diameter-three bound
  \[
  n\le
  \left\lfloor
  \frac{(k+2)^2(k^2+3)}{6(k+2)+1}
  \right\rfloor.
  \]
- Identifies the simple-excess level with a regular auxiliary graph of least
  adjacency eigenvalue at least `-2`, and sharpens the degree-seven,
  degree-eight, and degree-nine order windows to `74`, `108`, and `150`.
- Recasts the degree-six order-50 boundary as an integral signed-root Gram
  problem.
- Adds the explicit uniform Moore-deletion radius following from the
  incidence-Gram perturbation bound.
- Adds exact symbolic verifiers and corrected primary-source attribution for
  the least-eigenvalue-`-2` classification input.

The new optimal-slack, relation-graph, and deletion-radius results are analytic
theorems supported by exact executable audits. They are outside the stated Lean
formalization boundary. The explicit counterexamples and existing Lean
certificates are unchanged.
