import Wow284.Induced39.SpectralBridge

/-!
# Lean spectral certificate for the order-39 construction

It packages the exact minimum dual degree `35/6`, positive definiteness of
`6D+35I`, and the resulting strict WOW gap for every nonzero real eigenpair
of the formal matrix. Separate imported modules contain finite structural
lemmas; they are not bundled into the public endpoint below. No floating-point
eigenvalue is used.
-/
namespace Wow284.Induced39
open Matrix
theorem minimum_dual_degree_certificate :
    (∀ v : Vertex, (35 : ℚ) / 6 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (35 : ℚ) / 6 :=
  ⟨dual_degree_lower_bound, dual_degree_attained⟩
theorem real_eigenpair_wow_gap_positive {mu : ℝ} {x : Vertex → ℝ}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : 0 < (35 : ℝ) / 6 + mu := by
  have h := real_eigenpair_above_shift hx heig; nlinarith

theorem counterexample_endpoint :
    ((∀ v : Vertex, (35 : ℚ) / 6 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (35 : ℚ) / 6) ∧
    ((6 : ℚ) • Dq + (35 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef ∧
    (∀ {mu : ℝ} {x : Vertex → ℝ}, x ≠ 0 → Dr *ᵥ x = mu • x →
      0 < (35 : ℝ) / 6 + mu) := by
  refine ⟨minimum_dual_degree_certificate, shifted_distance_posDef, ?_⟩
  intro mu x hx heig; exact real_eigenpair_wow_gap_positive hx heig
end Wow284.Induced39
