import Wow284.Induced42.SpectralBridge

/-!
# Lean spectral certificate for the order-42 construction

It packages the exact minimum dual degree `6/1`, positive definiteness of
`1D+6I`, and the resulting strict WOW gap for every nonzero real eigenpair
of the formal matrix. Separate imported modules contain finite structural
lemmas; they are not bundled into the public endpoint below. No floating-point
eigenvalue is used.
-/
namespace Wow284.Induced42
open Matrix
theorem minimum_dual_degree_certificate :
    (∀ v : Vertex, (6 : ℚ) / 1 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (6 : ℚ) / 1 :=
  ⟨dual_degree_lower_bound, dual_degree_attained⟩
theorem real_eigenpair_wow_gap_positive {mu : ℝ} {x : Vertex → ℝ}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : 0 < (6 : ℝ) / 1 + mu := by
  have h := real_eigenpair_above_shift hx heig; nlinarith

theorem counterexample_endpoint :
    ((∀ v : Vertex, (6 : ℚ) / 1 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (6 : ℚ) / 1) ∧
    ((1 : ℚ) • Dq + (6 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef ∧
    (∀ {mu : ℝ} {x : Vertex → ℝ}, x ≠ 0 → Dr *ᵥ x = mu • x →
      0 < (6 : ℝ) / 1 + mu) := by
  refine ⟨minimum_dual_degree_certificate, shifted_distance_posDef, ?_⟩
  intro mu x hx heig; exact real_eigenpair_wow_gap_positive hx heig
end Wow284.Induced42
