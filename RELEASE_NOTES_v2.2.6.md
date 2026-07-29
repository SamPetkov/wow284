# WOW-284 v2.2.6

Substantive extension of the expanded manuscript.

This release subsumes the unpublished v2.2.5 candidate and is the first
public release of the integrated optimal-slack and signed-complement results.

- Introduces the positive-semidefinite optimal-slack matrix whose trace is the
  exact one-variable LP defect.
- Proves that its associated integral excess matrix is nonzero, yielding a
  strengthened diameter-three bound.
- Proves the three-to-one excess theorem
  \(r>0\) and \(n\le3r\), where
  \(r=2(k+2)^2(k^2+3)-(12k+27)n\), yielding the sharper diameter-three bound
  \[
  n\le
  \left\lfloor
  \frac{3(k+2)^2(k^2+3)}{18k+41}
  \right\rfloor.
  \]
- Shows that equality in the underlying unrounded inequality \(n\le3r\)
  has the unique arithmetic parameter triple
  \((k,n,r)=(103,185220,61740)\), without asserting existence.
- Identifies the simple-excess level with a regular auxiliary graph of least
  adjacency eigenvalue at least `-2`; graph realizability and small Gram
  minors force the three-to-one quantization. This sharpens the degree-seven,
  degree-eight, and degree-nine order windows to `74`, `108`, and `150`.
- Recasts the degree-six order-50 boundary as an integral signed-root Gram
  problem, identifies its signed-complement bridge, and proves that the
  associated Gram matrix has rank at least `30`.
- Uses the connected signed-root representation and a corrected
  nonbacktracking trace-parity argument to prove that this signed complement
  is necessarily disconnected.
- Adds the explicit uniform Moore-deletion radius following from the
  incidence-Gram perturbation bound.
- Adds two independent exact three-to-one verifiers, an equality-rigidity
  audit, a signed-complement verifier, a corrected order-50 moment verifier,
  a disconnectedness verifier, and a component-invariance counterexample
  guard, together with
  corrected primary-source attribution for the least-eigenvalue-`-2`
  ordinary and signed classification inputs.

The experimental order-50 nonexistence argument is not included. Its proposed
factorization was corrected, the unconditional `n <= 49` claim was rejected,
and the remaining signed-component quotient route is documented only
conditionally: commutation with the signed complement does not by itself
prove that the component partition is equitable.

The new optimal-slack, relation-graph, and deletion-radius results are analytic
theorems supported by exact executable audits. They are outside the stated Lean
formalization boundary. The explicit counterexamples and existing Lean
certificates are unchanged.
