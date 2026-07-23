import Mathlib

/-!
# Scalar part of the diameter-three criterion

For a regular girth-five diameter-three graph, an adjacency eigenvalue `theta`
produces the distance eigenvalue `k - 2 - (theta+1)^2`.  This file isolates the
exact scalar equivalence used by the analytic argument.
-/

namespace Wow284

def diameterThreeDistanceValue (k theta : ℝ) : ℝ :=
  k - 2 - (theta + 1) ^ 2

theorem diameter_three_gap_identity (k theta : ℝ) :
    k + diameterThreeDistanceValue k theta =
      2 * k - 2 - (theta + 1) ^ 2 := by
  unfold diameterThreeDistanceValue
  ring

theorem diameter_three_scalar_criterion (k theta : ℝ) (hk : 1 ≤ k) :
    0 < k + diameterThreeDistanceValue k theta ↔
      |theta + 1| < Real.sqrt (2 * k - 2) := by
  have hrad : 0 ≤ 2 * k - 2 := by nlinarith
  have hsquare : (Real.sqrt (2 * k - 2)) ^ 2 = 2 * k - 2 :=
    Real.sq_sqrt hrad
  have hsnonneg : 0 ≤ Real.sqrt (2 * k - 2) := Real.sqrt_nonneg _
  rw [diameter_three_gap_identity]
  constructor
  · intro h
    rw [abs_lt]
    constructor
    · by_contra hnot
      push_neg at hnot
      nlinarith [sq_nonneg ((theta + 1) + Real.sqrt (2 * k - 2))]
    · by_contra hnot
      push_neg at hnot
      nlinarith [sq_nonneg ((theta + 1) - Real.sqrt (2 * k - 2))]
  · intro h
    rw [abs_lt] at h
    nlinarith [sq_nonneg ((theta + 1) + Real.sqrt (2 * k - 2)),
      sq_nonneg ((theta + 1) - Real.sqrt (2 * k - 2))]

end Wow284
