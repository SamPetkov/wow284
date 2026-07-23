import Mathlib

/-!
# Scalar thresholds for punctured diameter-two Moore graphs

The analytic block calculation gives:

* one-vertex puncture: `δ* = k - 1/k`, `λmin(D) = -2 - sqrt k`;
* edge-end puncture (`k ≥ 3`): `δ* = k - 2/k`, with the same least
  distance eigenvalue.

This module formalizes the resulting scalar thresholds.
-/

namespace Wow284

noncomputable section

private theorem puncture_one_margin_of_five_le (k : ℕ) (hk : 5 ≤ k) :
    2 + Real.sqrt (k : ℝ) < (k : ℝ) - 1 / (k : ℝ) := by
  let x : ℝ := k
  have hx5 : (5 : ℝ) ≤ x := by
    simpa [x] using (show (5 : ℝ) ≤ (k : ℝ) by exact_mod_cast hk)
  have hxpos : 0 < x := by nlinarith
  have hsnonneg : 0 ≤ Real.sqrt x := Real.sqrt_nonneg _
  have hsquare : (Real.sqrt x) ^ 2 = x := Real.sq_sqrt (by nlinarith)
  have hm : 0 ≤ x - 5 := by nlinarith
  have hm2 : 0 ≤ (x - 5) ^ 2 := sq_nonneg _
  have hm3 : 0 ≤ (x - 5) ^ 3 := by
    exact mul_nonneg hm2 hm
  have hm4 : 0 ≤ (x - 5) ^ 4 := by
    positivity
  have hpoly : 0 < (x ^ 2 - 2 * x - 1) ^ 2 - x ^ 3 := by
    have hid :
        (x ^ 2 - 2 * x - 1) ^ 2 - x ^ 3 =
          (x - 5) ^ 4 + 15 * (x - 5) ^ 3 + 77 * (x - 5) ^ 2 +
            149 * (x - 5) + 71 := by ring
    rw [hid]
    nlinarith
  have hnum : 0 < x ^ 2 - 2 * x - 1 := by nlinarith
  have hprod_nonneg : 0 ≤ Real.sqrt x * x := mul_nonneg hsnonneg (le_of_lt hxpos)
  have hprod_sq : (Real.sqrt x * x) ^ 2 = x ^ 3 := by
    rw [mul_pow, hsquare]
    ring
  have hmain : Real.sqrt x * x < x ^ 2 - 2 * x - 1 := by
    nlinarith
  have hrearrange :
      x - 1 / x - 2 = (x ^ 2 - 2 * x - 1) / x := by
    field_simp
    ring
  change 2 + Real.sqrt x < x - 1 / x
  rw [show 2 + Real.sqrt x < x - 1 / x ↔
      Real.sqrt x < x - 1 / x - 2 by constructor <;> intro h <;> nlinarith]
  rw [hrearrange]
  exact (lt_div_iff₀ hxpos).2 hmain

private theorem puncture_edge_margin_of_five_le (k : ℕ) (hk : 5 ≤ k) :
    2 + Real.sqrt (k : ℝ) < (k : ℝ) - 2 / (k : ℝ) := by
  let x : ℝ := k
  have hx5 : (5 : ℝ) ≤ x := by
    simpa [x] using (show (5 : ℝ) ≤ (k : ℝ) by exact_mod_cast hk)
  have hxpos : 0 < x := by nlinarith
  have hsnonneg : 0 ≤ Real.sqrt x := Real.sqrt_nonneg _
  have hsquare : (Real.sqrt x) ^ 2 = x := Real.sq_sqrt (by nlinarith)
  have hm : 0 ≤ x - 5 := by nlinarith
  have hm2 : 0 ≤ (x - 5) ^ 2 := sq_nonneg _
  have hm3 : 0 ≤ (x - 5) ^ 3 := by
    exact mul_nonneg hm2 hm
  have hm4 : 0 ≤ (x - 5) ^ 4 := by
    positivity
  have hpoly : 0 < (x ^ 2 - 2 * x - 2) ^ 2 - x ^ 3 := by
    have hid :
        (x ^ 2 - 2 * x - 2) ^ 2 - x ^ 3 =
          (x - 5) ^ 4 + 15 * (x - 5) ^ 3 + 75 * (x - 5) ^ 2 +
            133 * (x - 5) + 44 := by ring
    rw [hid]
    nlinarith
  have hnum : 0 < x ^ 2 - 2 * x - 2 := by nlinarith
  have hprod_nonneg : 0 ≤ Real.sqrt x * x := mul_nonneg hsnonneg (le_of_lt hxpos)
  have hprod_sq : (Real.sqrt x * x) ^ 2 = x ^ 3 := by
    rw [mul_pow, hsquare]
    ring
  have hmain : Real.sqrt x * x < x ^ 2 - 2 * x - 2 := by
    nlinarith
  have hrearrange :
      x - 2 / x - 2 = (x ^ 2 - 2 * x - 2) / x := by
    field_simp
    ring
  change 2 + Real.sqrt x < x - 2 / x
  rw [show 2 + Real.sqrt x < x - 2 / x ↔
      Real.sqrt x < x - 2 / x - 2 by constructor <;> intro h <;> nlinarith]
  rw [hrearrange]
  exact (lt_div_iff₀ hxpos).2 hmain

/-- A one-vertex puncture is a strict scalar counterexample exactly from
integer degree five onward. -/
theorem puncture_one_positive_iff (k : ℕ) (hk : 2 ≤ k) :
    (2 + Real.sqrt (k : ℝ) < (k : ℝ) - 1 / (k : ℝ)) ↔ 5 ≤ k := by
  constructor
  · intro h
    by_contra hnot
    have hk4 : k ≤ 4 := by omega
    have cases : k = 2 ∨ k = 3 ∨ k = 4 := by omega
    rcases cases with rfl | rfl | rfl
    · have hsquare : (Real.sqrt (2 : ℝ)) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
      have hsnonneg : 0 ≤ Real.sqrt (2 : ℝ) := Real.sqrt_nonneg _
      norm_num at h
      nlinarith
    · have hsquare : (Real.sqrt (3 : ℝ)) ^ 2 = 3 := Real.sq_sqrt (by norm_num)
      have hsnonneg : 0 ≤ Real.sqrt (3 : ℝ) := Real.sqrt_nonneg _
      norm_num at h
      nlinarith
    · norm_num at h
  · exact puncture_one_margin_of_five_le k

/-- An edge-end puncture has the same degree threshold. -/
theorem puncture_edge_positive_iff (k : ℕ) (hk : 2 ≤ k) :
    (2 + Real.sqrt (k : ℝ) < (k : ℝ) - 2 / (k : ℝ)) ↔ 5 ≤ k := by
  constructor
  · intro h
    by_contra hnot
    have hk4 : k ≤ 4 := by omega
    have cases : k = 2 ∨ k = 3 ∨ k = 4 := by omega
    rcases cases with rfl | rfl | rfl
    · have hsquare : (Real.sqrt (2 : ℝ)) ^ 2 = 2 := Real.sq_sqrt (by norm_num)
      have hsnonneg : 0 ≤ Real.sqrt (2 : ℝ) := Real.sqrt_nonneg _
      norm_num at h
      nlinarith
    · have hsquare : (Real.sqrt (3 : ℝ)) ^ 2 = 3 := Real.sq_sqrt (by norm_num)
      have hsnonneg : 0 ≤ Real.sqrt (3 : ℝ) := Real.sqrt_nonneg _
      norm_num at h
      nlinarith
    · norm_num at h
  · exact puncture_edge_margin_of_five_le k

/-- The degree-seven one-vertex puncture has exact margin
`48/7-(2+sqrt 7)>0`. -/
theorem hs_puncture_one_strict :
    2 + Real.sqrt (7 : ℝ) < (48 : ℝ) / 7 := by
  have h := (puncture_one_positive_iff 7 (by norm_num)).2 (by norm_num)
  norm_num at h ⊢
  exact h

/-- The degree-seven edge puncture has exact margin
`47/7-(2+sqrt 7)>0`. -/
theorem hs_puncture_edge_strict :
    2 + Real.sqrt (7 : ℝ) < (47 : ℝ) / 7 := by
  have h := (puncture_edge_positive_iff 7 (by norm_num)).2 (by norm_num)
  norm_num at h ⊢
  exact h

end

end Wow284
