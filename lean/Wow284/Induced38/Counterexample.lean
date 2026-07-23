import Wow284.Induced38.FiniteCertificates
import Wow284.Induced38.SpectralBridge

/-!
# End-to-end counterexample certificate for the 38-vertex graph

The original task permits a strict violation to be certified by positive
definiteness of `qD + pI`, where the exact minimum dual degree is `p/q`.
Here `p = 17` and `q = 3`.  This avoids formalizing the stronger Sturm
calculation for the exact least eigenvalue before the counterexample itself is
kernel-checked.
-/

namespace Wow284.Induced38

open Matrix

/-- The minimum dual degree is exactly `17/3`: it is a lower bound at every
vertex and is attained by an explicit vertex. -/
theorem minimum_dual_degree_certificate :
    (∀ v : Vertex, (17 : ℚ) / 3 ≤ dualDegree v) ∧
      ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3 :=
  ⟨dual_degree_lower_bound, dual_degree_attained⟩

/-- Exact rational positive-definiteness certificate for the strict WOW-284
violation.  This is the task's `qD + pI` criterion with `q = 3`, `p = 17`. -/
theorem exact_counterexample_certificate :
    ((∀ v : Vertex, (17 : ℚ) / 3 ≤ dualDegree v) ∧
      ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3) ∧
    ((3 : ℚ) • Dq + (17 : ℚ) •
      (1 : Matrix Vertex Vertex ℚ)).PosDef := by
  exact ⟨minimum_dual_degree_certificate, shifted_distance_posDef⟩

/-- Every real distance eigenpair has a strictly positive WOW gap against the
exact minimum dual degree `17/3`. -/
theorem real_eigenpair_wow_gap_positive
    {mu : ℝ} {x : Vertex → ℝ} (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) :
    0 < (17 : ℝ) / 3 + mu := by
  have h := real_eigenpair_above_neg_seventeen_thirds hx heig
  linarith

/-- Public end-to-end endpoint: exact minimum dual degree, exact shifted
positive-definiteness, and the induced strict inequality for every real
eigenpair. -/
theorem counterexample_endpoint :
    ((∀ v : Vertex, (17 : ℚ) / 3 ≤ dualDegree v) ∧
      ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3) ∧
    ((3 : ℚ) • Dq + (17 : ℚ) •
      (1 : Matrix Vertex Vertex ℚ)).PosDef ∧
    (∀ {mu : ℝ} {x : Vertex → ℝ}, x ≠ 0 → Dr *ᵥ x = mu • x →
      0 < (17 : ℝ) / 3 + mu) := by
  refine ⟨minimum_dual_degree_certificate, shifted_distance_posDef, ?_⟩
  intro mu x hx heig
  exact real_eigenpair_wow_gap_positive hx heig

end Wow284.Induced38
