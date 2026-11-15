import Wow284.Induced40X.SpectralBridge

/-!
# Lean spectral certificate for the order-40 construction

It packages the exact minimum dual degree `17/3`, positive definiteness of
`3D+17I`, and the resulting strict WOW gap for every nonzero real eigenpair
of the formal matrix. Separate imported modules contain finite structural
lemmas; they are not bundled into the public endpoint below. No floating-point
eigenvalue is used.
-/
namespace Wow284.Induced40X
open Matrix
theorem minimum_dual_degree_certificate :
    (∀ v : Vertex, (17 : ℚ) / 3 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3 :=
  ⟨dual_degree_lower_bound, dual_degree_attained⟩
theorem real_eigenpair_wow_gap_positive {mu : ℝ} {x : Vertex → ℝ}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : 0 < (17 : ℝ) / 3 + mu := by
  have h := real_eigenpair_above_shift hx heig; nlinarith

theorem counterexample_endpoint :
    ((∀ v : Vertex, (17 : ℚ) / 3 ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = (17 : ℚ) / 3) ∧
    ((3 : ℚ) • Dq + (17 : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef ∧
    (∀ {mu : ℝ} {x : Vertex → ℝ}, x ≠ 0 → Dr *ᵥ x = mu • x →
      0 < (17 : ℝ) / 3 + mu) := by
  refine ⟨minimum_dual_degree_certificate, shifted_distance_posDef, ?_⟩
  intro mu x hx heig; exact real_eigenpair_wow_gap_positive hx heig
end Wow284.Induced40X
