import Mathlib

/-!
# The scalar threshold in the Moore-graph obstruction

This module isolates the elementary real inequality governing the degree
threshold in the WOW-284 counterexample family.
-/

namespace Wow284

/-- For a natural degree `k ≥ 2`, the scalar WOW bound holds exactly for
`k ≤ 3`. -/
theorem moore_wow_bound_iff (k : ℕ) (hk : 2 ≤ k) :
    ((k : ℝ) ≤ (3 + Real.sqrt (4 * (k : ℝ) - 3)) / 2) ↔ k ≤ 3 := by
  constructor
  · intro hbound
    by_contra hnot
    have hk4 : 4 ≤ k := by omega
    have hk4_real : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk4
    have hradicand : 0 ≤ 4 * (k : ℝ) - 3 := by nlinarith
    have hsqrt_sq := Real.sq_sqrt hradicand
    have hsqrt_nonneg := Real.sqrt_nonneg (4 * (k : ℝ) - 3)
    nlinarith
  · intro hk3
    have hk_cases : k = 2 ∨ k = 3 := by omega
    rcases hk_cases with rfl | rfl
    · have hsqrt_sq : (Real.sqrt (5 : ℝ)) ^ 2 = 5 := by
        exact Real.sq_sqrt (by norm_num)
      have hsqrt_nonneg : 0 ≤ Real.sqrt (5 : ℝ) := Real.sqrt_nonneg _
      norm_num
      nlinarith
    · norm_num

/-- At degree two, the scalar WOW bound is strict. -/
theorem moore_wow_bound_strict_at_two :
    (2 : ℝ) < (3 + Real.sqrt (4 * (2 : ℝ) - 3)) / 2 := by
  have hsqrt_sq : (Real.sqrt (5 : ℝ)) ^ 2 = 5 := by
    exact Real.sq_sqrt (by norm_num)
  have hsqrt_nonneg : 0 ≤ Real.sqrt (5 : ℝ) := Real.sqrt_nonneg _
  norm_num
  nlinarith

/-- At degree three, the scalar WOW bound is attained with equality. -/
theorem moore_wow_bound_eq_at_three :
    (3 : ℝ) = (3 + Real.sqrt (4 * (3 : ℝ) - 3)) / 2 := by
  norm_num

/-- Every natural degree strictly greater than three violates the scalar WOW
bound. -/
theorem moore_wow_bound_fails_of_three_lt (k : ℕ) (hk : 3 < k) :
    ¬ ((k : ℝ) ≤ (3 + Real.sqrt (4 * (k : ℝ) - 3)) / 2) := by
  intro hbound
  have hk2 : 2 ≤ k := by omega
  have hk3 : k ≤ 3 := (moore_wow_bound_iff k hk2).mp hbound
  omega

end Wow284
