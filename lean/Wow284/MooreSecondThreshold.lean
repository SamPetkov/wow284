import Mathlib

/-!
# Scalar threshold for Moore second subconstituents

If a degree-`K` diameter-two Moore graph exists, its second subconstituent has
degree `K-1` and least distance eigenvalue
`-(5 + sqrt (4K-3))/2`.  This module formalizes only the scalar threshold.
-/

namespace Wow284

theorem moore_second_gap_positive_iff (K : ℕ) (hK : 2 ≤ K) :
    0 < (K : ℝ) - 1 - (5 + Real.sqrt (4 * (K : ℝ) - 3)) / 2 ↔
      6 ≤ K := by
  have hKreal : (2 : ℝ) ≤ (K : ℝ) := by exact_mod_cast hK
  have hrad : 0 ≤ 4 * (K : ℝ) - 3 := by nlinarith
  have hsquare : (Real.sqrt (4 * (K : ℝ) - 3)) ^ 2 =
      4 * (K : ℝ) - 3 := Real.sq_sqrt hrad
  have hsnonneg : 0 ≤ Real.sqrt (4 * (K : ℝ) - 3) := Real.sqrt_nonneg _
  constructor
  · intro hgap
    by_contra hnot
    have hK5 : K ≤ 5 := by omega
    have cases : K = 2 ∨ K = 3 ∨ K = 4 ∨ K = 5 := by omega
    rcases cases with rfl | rfl | rfl | rfl
    all_goals norm_num at hsquare hsnonneg
    all_goals nlinarith
  · intro hK6
    have hK6r : (6 : ℝ) ≤ (K : ℝ) := by exact_mod_cast hK6
    nlinarith [sq_nonneg ((K : ℝ) - 6)]

theorem moore_second_gap_positive_of_six_le (K : ℕ) (hK : 6 ≤ K) :
    0 < (K : ℝ) - 1 - (5 + Real.sqrt (4 * (K : ℝ) - 3)) / 2 := by
  exact (moore_second_gap_positive_iff K (by omega)).2 hK

end Wow284
