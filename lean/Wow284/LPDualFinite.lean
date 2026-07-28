import Wow284.LPPrimal

namespace Wow284.LP

noncomputable section

open Polynomial

/-- The defining square identity for the radical in the dual certificate. -/
theorem delta_sq (k : ℕ) (hk : 4 ≤ k) :
    delta k ^ 2 = 2 * (k : ℝ) - 2 := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  rw [delta, Real.sq_sqrt (by linarith)]

private theorem delta_pow_four (k : ℕ) (hk : 4 ≤ k) :
    delta k ^ 4 = (2 * (k : ℝ) - 2) ^ 2 := by
  calc
    delta k ^ 4 = (delta k ^ 2) ^ 2 := by ring
    _ = (2 * (k : ℝ) - 2) ^ 2 := by rw [delta_sq k hk]

private theorem delta_pow_six (k : ℕ) (hk : 4 ≤ k) :
    delta k ^ 6 = (2 * (k : ℝ) - 2) ^ 3 := by
  calc
    delta k ^ 6 = (delta k ^ 2) ^ 3 := by ring
    _ = (2 * (k : ℝ) - 2) ^ 3 := by rw [delta_sq k hk]

private theorem delta_pow_eight (k : ℕ) (hk : 4 ≤ k) :
    delta k ^ 8 = (2 * (k : ℝ) - 2) ^ 4 := by
  calc
    delta k ^ 8 = (delta k ^ 2) ^ 4 := by ring
    _ = (2 * (k : ℝ) - 2) ^ 4 := by rw [delta_sq k hk]

private theorem delta_pow_ten (k : ℕ) (hk : 4 ≤ k) :
    delta k ^ 10 = (2 * (k : ℝ) - 2) ^ 5 := by
  calc
    delta k ^ 10 = (delta k ^ 2) ^ 5 := by ring
    _ = (2 * (k : ℝ) - 2) ^ 5 := by rw [delta_sq k hk]

/-- The interior dual weight is strictly positive throughout the theorem range. -/
theorem weightZero_pos (k : ℕ) (hk : 4 ≤ k) :
    0 < weightZero k := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hk0 : 0 < (k : ℝ) := by linarith
  have hk1 : 0 < (k : ℝ) - 1 := by linarith
  have hquad : 0 < (k : ℝ) ^ 2 + 3 := by positivity
  have hdenTerm : 0 < 2 * (k : ℝ) - 3 := by linarith
  have hden : 0 < 6 * (2 * (k : ℝ) - 3) :=
    mul_pos (by norm_num) hdenTerm
  rw [weightZero]
  exact div_pos (mul_pos (mul_pos hk0 hk1) hquad) hden

/-- The upper-endpoint dual weight is strictly positive throughout the theorem range. -/
theorem weightPlus_pos (k : ℕ) (hk : 4 ≤ k) :
    0 < weightPlus k := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hk0 : 0 < (k : ℝ) := by linarith
  have hkp2 : 0 < (k : ℝ) + 2 := by linarith
  have hkm1 : 0 ≤ (k : ℝ) - 1 := by linarith
  have hdelta : 0 ≤ delta k := Real.sqrt_nonneg _
  have hbase : 0 < 2 * (k : ℝ) ^ 2 - 6 := by nlinarith
  have hterm : 0 ≤ 3 * ((k : ℝ) - 1) * delta k := by positivity
  have hinner :
      0 < 2 * (k : ℝ) ^ 2 - 6 + 3 * ((k : ℝ) - 1) * delta k :=
    add_pos_of_pos_of_nonneg hbase hterm
  have hdenTerm : 0 < 2 * (k : ℝ) - 3 := by linarith
  have hden : 0 < 24 * (2 * (k : ℝ) - 3) :=
    mul_pos (by norm_num) hdenTerm
  rw [weightPlus]
  exact div_pos (mul_pos (mul_pos hk0 hkp2) hinner) hden

/-- The lower-endpoint dual weight is strictly positive throughout the theorem range. -/
theorem weightMinus_pos (k : ℕ) (hk : 4 ≤ k) :
    0 < weightMinus k := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hk0 : 0 < (k : ℝ) := by linarith
  have hkp2 : 0 < (k : ℝ) + 2 := by linarith
  have hkm1 : 0 ≤ (k : ℝ) - 1 := by linarith
  have hdelta_nonneg : 0 ≤ delta k := Real.sqrt_nonneg _
  have hdelta_sq : delta k ^ 2 = 2 * (k : ℝ) - 2 :=
    delta_sq k hk
  have hbase : 0 < 2 * (k : ℝ) ^ 2 - 6 := by nlinarith
  have hterm : 0 ≤ 3 * ((k : ℝ) - 1) * delta k := by positivity
  have hfactor :
      0 <
        2 * ((k : ℝ) - 3) * (2 * (k : ℝ) - 3) *
          ((k : ℝ) ^ 2 + 3) := by
    have hk3 : 0 < (k : ℝ) - 3 := by linarith
    have h2k3 : 0 < 2 * (k : ℝ) - 3 := by linarith
    have hkquad : 0 < (k : ℝ) ^ 2 + 3 := by positivity
    exact mul_pos (mul_pos (mul_pos (by norm_num) hk3) h2k3) hkquad
  have hid :
      (2 * (k : ℝ) ^ 2 - 6) ^ 2 -
          (3 * ((k : ℝ) - 1) * delta k) ^ 2 =
        2 * ((k : ℝ) - 3) * (2 * (k : ℝ) - 3) *
          ((k : ℝ) ^ 2 + 3) := by
    rw [show
      (3 * ((k : ℝ) - 1) * delta k) ^ 2 =
        9 * ((k : ℝ) - 1) ^ 2 * delta k ^ 2 by ring,
      hdelta_sq]
    ring
  have hsquare :
      (3 * ((k : ℝ) - 1) * delta k) ^ 2 <
        (2 * (k : ℝ) ^ 2 - 6) ^ 2 := by
    nlinarith
  have hinner :
      0 < 2 * (k : ℝ) ^ 2 - 6 -
        3 * ((k : ℝ) - 1) * delta k := by
    nlinarith
  have hdenTerm : 0 < 2 * (k : ℝ) - 3 := by linarith
  have hden : 0 < 24 * (2 * (k : ℝ) - 3) :=
    mul_pos (by norm_num) hdenTerm
  rw [weightMinus]
  exact div_pos (mul_pos (mul_pos hk0 hkp2) hinner) hden

/-- Exact total mass of the three-point dual functional. -/
theorem dual_mass (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 0) =
      (k : ℝ) * ((k : ℝ) ^ 2 + 2 * (k : ℝ) + 3) / 6 := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  calc
    dual k (nbPoly k 0) =
        (k : ℝ) * (2 * (k : ℝ) ^ 3 + (k : ℝ) ^ 2 - 9) /
          (6 * (2 * (k : ℝ) - 3)) := by
      simp [dual, weightMinus, weightZero, weightPlus]
      field_simp [hden, hden6, hden24]
      ring
    _ = (k : ℝ) * ((k : ℝ) ^ 2 + 2 * (k : ℝ) + 3) / 6 := by
      apply (div_eq_iff (mul_ne_zero (by norm_num) hden)).2
      ring

/-- The dual mass is exactly one less than the sharp LP ceiling. -/
theorem dual_mass_eq_ceiling_sub_one (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 0) = ceiling k - 1 := by
  rw [dual_mass k hk]
  simp [ceiling]
  ring

/-- The degree-one dual moment cancels the principal evaluation. -/
theorem dual_nbPoly_one (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 1) = -(nbPoly k 1).eval (k : ℝ) := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
    nbPoly]
  field_simp [hden, hden', hden6, hden24]
  nlinarith

/-- The degree-two dual moment cancels the principal evaluation. -/
theorem dual_nbPoly_two (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 2) = -(nbPoly k 2).eval (k : ℝ) := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
    nbPoly]
  field_simp [hden, hden', hden6, hden24]
  ring_nf
  rw [hd2]
  ring

/-- The degree-three dual moment cancels the principal evaluation. -/
theorem dual_nbPoly_three (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 3) = -(nbPoly k 3).eval (k : ℝ) := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  have hd4 := delta_pow_four k hk
  simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
    nbPoly, Nat.cast_sub hk1]
  field_simp [hden, hden', hden6, hden24]
  ring_nf
  rw [hd4, hd2]
  ring

/-- The degree-four dual moment cancels the principal evaluation. -/
theorem dual_nbPoly_four (k : ℕ) (hk : 4 ≤ k) :
    dual k (nbPoly k 4) = -(nbPoly k 4).eval (k : ℝ) := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  have hd4 := delta_pow_four k hk
  simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
    nbPoly, Nat.cast_sub hk1]
  field_simp [hden, hden', hden6, hden24]
  ring_nf
  rw [hd4, hd2]
  ring

/-- Simultaneous statement of the four exact cancelling dual moments. -/
theorem dual_nbPoly_eq_neg_eval_of_one_le_of_le_four
    (k i : ℕ) (hk : 4 ≤ k) (hi1 : 1 ≤ i) (hi4 : i ≤ 4) :
    dual k (nbPoly k i) = -(nbPoly k i).eval (k : ℝ) := by
  interval_cases i <;>
    simp_all only [dual_nbPoly_one, dual_nbPoly_two, dual_nbPoly_three,
      dual_nbPoly_four]

/-- Exact degree-five dual slack. -/
theorem slack_five_formula (k : ℕ) (hk : 4 ≤ k) :
    slack k 5 =
      (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
        ((k : ℝ) ^ 2 + 3) / 3 := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  have hd4 := delta_pow_four k hk
  have hd6 := delta_pow_six k hk
  rw [slack]
  simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
    nbPoly, Nat.cast_sub hk1]
  field_simp [hden, hden', hden6, hden24]
  ring_nf
  rw [hd6, hd4, hd2]
  ring

/-- Exact dual slacks in degrees six through nine. -/
theorem slack_six_to_nine_formulas (k : ℕ) (hk : 4 ≤ k) :
    slack k 6 =
        (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
          (5 * (k : ℝ) - 13) * ((k : ℝ) ^ 2 + 3) / 6 ∧
      slack k 7 =
        (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
          ((k : ℝ) ^ 2 + 3) *
            (3 * (k : ℝ) ^ 2 - 17 * (k : ℝ) + 25) / 3 ∧
      slack k 8 =
        (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
          ((k : ℝ) ^ 2 + 3) *
            (6 * (k : ℝ) ^ 3 - 47 * (k : ℝ) ^ 2 +
              139 * (k : ℝ) - 150) / 6 ∧
      slack k 9 =
        (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
          ((k : ℝ) ^ 2 + 3) *
            (3 * (k : ℝ) ^ 4 - 27 * (k : ℝ) ^ 3 +
              106 * (k : ℝ) ^ 2 - 219 * (k : ℝ) + 194) / 3 := by
  have hk1 : 1 ≤ k := by omega
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hden : 2 * (k : ℝ) - 3 ≠ 0 := by linarith
  have hden' : (k : ℝ) * 2 - 3 ≠ 0 := by linarith
  have hden6 : 6 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hden24 : 24 * (2 * (k : ℝ) - 3) ≠ 0 :=
    mul_ne_zero (by norm_num) hden
  have hd2 := delta_sq k hk
  have hd4 := delta_pow_four k hk
  have hd6 := delta_pow_six k hk
  have hd8 := delta_pow_eight k hk
  have hd10 := delta_pow_ten k hk
  constructor
  · rw [slack]
    simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
      nbPoly, Nat.cast_sub hk1]
    field_simp [hden, hden', hden6, hden24]
    ring_nf
    rw [hd6, hd4, hd2]
    ring
  constructor
  · rw [slack]
    simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
      nbPoly, Nat.cast_sub hk1]
    field_simp [hden, hden', hden6, hden24]
    ring_nf
    rw [hd8, hd6, hd4, hd2]
    ring
  constructor
  · rw [slack]
    simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
      nbPoly, Nat.cast_sub hk1]
    field_simp [hden, hden', hden6, hden24]
    ring_nf
    rw [hd8, hd6, hd4, hd2]
    ring
  · rw [slack]
    simp [dual, weightMinus, weightZero, weightPlus, xiMinus, xiZero, xiPlus,
      nbPoly, Nat.cast_sub hk1]
    field_simp [hden, hden', hden6, hden24]
    ring_nf
    rw [hd10, hd8, hd6, hd4, hd2]
    ring

/-- Exact degree-six dual slack. -/
theorem slack_six_formula (k : ℕ) (hk : 4 ≤ k) :
    slack k 6 =
      (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
        (5 * (k : ℝ) - 13) * ((k : ℝ) ^ 2 + 3) / 6 :=
  (slack_six_to_nine_formulas k hk).1

/-- Exact degree-seven dual slack. -/
theorem slack_seven_formula (k : ℕ) (hk : 4 ≤ k) :
    slack k 7 =
      (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
        ((k : ℝ) ^ 2 + 3) *
          (3 * (k : ℝ) ^ 2 - 17 * (k : ℝ) + 25) / 3 :=
  (slack_six_to_nine_formulas k hk).2.1

/-- Exact degree-eight dual slack. -/
theorem slack_eight_formula (k : ℕ) (hk : 4 ≤ k) :
    slack k 8 =
      (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
        ((k : ℝ) ^ 2 + 3) *
          (6 * (k : ℝ) ^ 3 - 47 * (k : ℝ) ^ 2 +
            139 * (k : ℝ) - 150) / 6 :=
  (slack_six_to_nine_formulas k hk).2.2.1

/-- Exact degree-nine dual slack. -/
theorem slack_nine_formula (k : ℕ) (hk : 4 ≤ k) :
    slack k 9 =
      (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) + 2) *
        ((k : ℝ) ^ 2 + 3) *
          (3 * (k : ℝ) ^ 4 - 27 * (k : ℝ) ^ 3 +
            106 * (k : ℝ) ^ 2 - 219 * (k : ℝ) + 194) / 3 :=
  (slack_six_to_nine_formulas k hk).2.2.2

/-- All five finite dual slacks are strictly positive. -/
theorem finite_slacks_positive (k : ℕ) (hk : 4 ≤ k) :
    0 < slack k 5 ∧ 0 < slack k 6 ∧ 0 < slack k 7 ∧
      0 < slack k 8 ∧ 0 < slack k 9 := by
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hm : 0 ≤ (k : ℝ) - 4 := by linarith
  have hkpos : 0 < (k : ℝ) := by linarith
  have hk1pos : 0 < (k : ℝ) - 1 := by linarith
  have hk2pos : 0 < (k : ℝ) + 2 := by linarith
  have hsqpos : 0 < (k : ℝ) ^ 2 + 3 := by
    nlinarith [sq_nonneg (k : ℝ)]
  have h6 : 0 < 5 * (k : ℝ) - 13 := by linarith
  have h7 :
      0 < 3 * (k : ℝ) ^ 2 - 17 * (k : ℝ) + 25 := by
    rw [show
      3 * (k : ℝ) ^ 2 - 17 * (k : ℝ) + 25 =
        3 * ((k : ℝ) - 4) ^ 2 + 7 * ((k : ℝ) - 4) + 5 by ring]
    positivity
  have h8 :
      0 < 6 * (k : ℝ) ^ 3 - 47 * (k : ℝ) ^ 2 +
        139 * (k : ℝ) - 150 := by
    rw [show
      6 * (k : ℝ) ^ 3 - 47 * (k : ℝ) ^ 2 + 139 * (k : ℝ) - 150 =
        6 * ((k : ℝ) - 4) ^ 3 + 25 * ((k : ℝ) - 4) ^ 2 +
          51 * ((k : ℝ) - 4) + 38 by ring]
    positivity
  have h9 :
      0 < 3 * (k : ℝ) ^ 4 - 27 * (k : ℝ) ^ 3 +
        106 * (k : ℝ) ^ 2 - 219 * (k : ℝ) + 194 := by
    rw [show
      3 * (k : ℝ) ^ 4 - 27 * (k : ℝ) ^ 3 +
          106 * (k : ℝ) ^ 2 - 219 * (k : ℝ) + 194 =
        3 * ((k : ℝ) - 4) ^ 4 + 21 * ((k : ℝ) - 4) ^ 3 +
          70 * ((k : ℝ) - 4) ^ 2 + 101 * ((k : ℝ) - 4) + 54 by ring]
    positivity
  constructor
  · rw [slack_five_formula k hk]
    positivity
  constructor
  · rw [slack_six_formula k hk]
    positivity
  constructor
  · rw [slack_seven_formula k hk]
    positivity
  constructor
  · rw [slack_eight_formula k hk]
    positivity
  · rw [slack_nine_formula k hk]
    positivity

/-- Strict positivity for every finite-slack degree `5 ≤ i ≤ 9`. -/
theorem slack_pos_of_five_le_of_le_nine
    (k i : ℕ) (hk : 4 ≤ k) (hi5 : 5 ≤ i) (hi9 : i ≤ 9) :
    0 < slack k i := by
  have hs := finite_slacks_positive k hk
  interval_cases i <;> simp_all

end

end Wow284.LP
