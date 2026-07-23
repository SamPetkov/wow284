import Mathlib

/-! Exact scalar sign certificate for the 38-vertex counterexample. -/
namespace Wow284.Induced38

theorem sqrt_seven_lt_eight_thirds :
    Real.sqrt 7 < (8 : ℝ) / 3 := by
  have hsquare : (Real.sqrt 7) ^ 2 = (7 : ℝ) := by
    exact Real.sq_sqrt (by norm_num)
  have hnonneg : 0 ≤ Real.sqrt 7 := Real.sqrt_nonneg _
  nlinarith

theorem exact_wow_gap_positive :
    0 < (17 : ℝ) / 3 + (-3 - Real.sqrt 7) := by
  have h := sqrt_seven_lt_eight_thirds
  nlinarith

theorem least_target_above_shift :
    (-17 : ℝ) / 3 < -3 - Real.sqrt 7 := by
  have h := sqrt_seven_lt_eight_thirds
  nlinarith

end Wow284.Induced38
