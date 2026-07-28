import Wow284.LPRecurrence

namespace Wow284.LP

noncomputable section

open Polynomial

/-- The exact nonbacktracking-basis expansion of the unnormalized optimizer. -/
theorem extremal_numerator_expansion (k : ℕ) (hk : 1 ≤ k) :
    (X + C 2) ^ 2 * (X ^ 2 + C 2 * X - C (2 * (k : ℝ) - 3)) =
      C (6 * ((k : ℝ) + 2)) * nbPoly k 0 +
        C (2 * (2 * (k : ℝ) + 7)) * nbPoly k 1 +
          C ((k : ℝ) + 13) * nbPoly k 2 +
            C 6 * nbPoly k 3 + nbPoly k 4 := by
  apply Polynomial.funext
  intro x
  simp [nbPoly, Nat.cast_sub hk]
  ring

/-- The optimizer takes the claimed objective value at the principal point. -/
theorem extremal_eval_at_degree (k : ℕ) :
    (extremal k).eval (k : ℝ) = ceiling k := by
  simp [extremal, ceiling]
  field_simp
  ring

/-- The explicit optimizer is nonpositive on the full shifted WOW interval. -/
theorem extremal_nonpos_on_interval (k : ℕ) (hk : 1 ≤ k) (x : ℝ)
    (hx : x ∈ wowInterval k) :
    (extremal k).eval x ≤ 0 := by
  have hrad : 0 ≤ 2 * (k : ℝ) - 2 := by
    have hk_real : (1 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
    linarith
  have hdelta : 0 ≤ delta k := by
    exact Real.sqrt_nonneg _
  have hdelta_sq : (delta k) ^ 2 = 2 * (k : ℝ) - 2 := by
    simp [delta, Real.sq_sqrt hrad]
  have hlower_raw : -1 - delta k ≤ x := by
    simpa [wowInterval, delta] using hx.1
  have hupper_raw : x ≤ -1 + delta k := by
    simpa [wowInterval, delta] using hx.2
  have hlower : -(delta k) ≤ x + 1 := by linarith
  have hupper : x + 1 ≤ delta k := by linarith
  have hleft : 0 ≤ delta k - (x + 1) := by linarith
  have hright : 0 ≤ delta k + (x + 1) := by linarith
  have hproduct : 0 ≤ (delta k - (x + 1)) * (delta k + (x + 1)) :=
    mul_nonneg hleft hright
  have hboundary : x ^ 2 + 2 * x - (2 * (k : ℝ) - 3) ≤ 0 := by
    nlinarith
  have hsquare : 0 ≤ (x + 2) ^ 2 := sq_nonneg _
  have hnumerator :
      (x + 2) ^ 2 * (x ^ 2 + 2 * x - (2 * (k : ℝ) - 3)) ≤ 0 :=
    mul_nonpos_of_nonneg_of_nonpos hsquare hboundary
  have hscale : 0 ≤ 1 / (6 * ((k : ℝ) + 2)) := by positivity
  simpa [extremal, mul_assoc] using
    mul_nonpos_of_nonneg_of_nonpos hscale hnumerator

/-- The normalized finitely supported coefficient family representing the
explicit extremal polynomial. -/
def extremalCoefficients (k : ℕ) : Coefficients :=
  Finsupp.single 0 1 +
    Finsupp.single 1 ((2 * (k : ℝ) + 7) / (3 * ((k : ℝ) + 2))) +
      Finsupp.single 2 (((k : ℝ) + 13) / (6 * ((k : ℝ) + 2))) +
        Finsupp.single 3 (1 / ((k : ℝ) + 2)) +
          Finsupp.single 4 (1 / (6 * ((k : ℝ) + 2)))

@[simp]
theorem extremalCoefficients_zero (k : ℕ) :
    extremalCoefficients k 0 = 1 := by
  simp [extremalCoefficients]

@[simp]
theorem extremalCoefficients_one (k : ℕ) :
    extremalCoefficients k 1 =
      (2 * (k : ℝ) + 7) / (3 * ((k : ℝ) + 2)) := by
  simp [extremalCoefficients]

@[simp]
theorem extremalCoefficients_two (k : ℕ) :
    extremalCoefficients k 2 =
      ((k : ℝ) + 13) / (6 * ((k : ℝ) + 2)) := by
  simp [extremalCoefficients]

@[simp]
theorem extremalCoefficients_three (k : ℕ) :
    extremalCoefficients k 3 = 1 / ((k : ℝ) + 2) := by
  simp [extremalCoefficients]

@[simp]
theorem extremalCoefficients_four (k : ℕ) :
    extremalCoefficients k 4 = 1 / (6 * ((k : ℝ) + 2)) := by
  simp [extremalCoefficients]

theorem extremalCoefficients_eq_zero_of_five_le
    (k i : ℕ) (hi : 5 ≤ i) :
    extremalCoefficients k i = 0 := by
  simp [extremalCoefficients, show i ≠ 0 by omega,
    show i ≠ 1 by omega, show i ≠ 2 by omega, show i ≠ 3 by omega,
    show i ≠ 4 by omega]

/-- The explicit finite coefficient family represents the normalized
extremal quartic exactly. -/
theorem polynomial_extremalCoefficients
    (k : ℕ) (hk : 1 ≤ k) :
    polynomial k (extremalCoefficients k) = extremal k := by
  classical
  rw [polynomial]
  unfold extremalCoefficients
  repeat'
    rw [Finsupp.sum_add_index' (by simp)
      (by intros; simp [add_mul])]
  repeat'
    rw [Finsupp.sum_single_index (by simp)]
  apply Polynomial.funext
  intro x
  simp [extremal, nbPoly, Nat.cast_sub hk]
  field_simp
  ring

/-- The normalized explicit coefficient family is feasible for the exact
two-sided nonbacktracking linear program. -/
theorem extremalCoefficients_admissible
    (k : ℕ) (hk : 1 ≤ k) :
    Admissible k (extremalCoefficients k) := by
  refine ⟨by simp, ?_, ?_⟩
  · intro i hi
    rw [extremalCoefficients_eq_zero_of_five_le k i hi]
  · intro x hx
    rw [polynomial_extremalCoefficients k hk]
    exact extremal_nonpos_on_interval k hk x hx

/-- The explicit normalized coefficient family attains the sharp objective
value. -/
theorem extremalCoefficients_attains
    (k : ℕ) (hk : 1 ≤ k) :
    (polynomial k (extremalCoefficients k)).eval (k : ℝ) =
      ceiling k * extremalCoefficients k 0 := by
  rw [polynomial_extremalCoefficients k hk, extremal_eval_at_degree]
  simp

end

end Wow284.LP
