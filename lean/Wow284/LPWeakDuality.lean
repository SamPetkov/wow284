import Wow284.LPChebyshevTail
import Wow284.LPDualFinite

namespace Wow284.LP

noncomputable section

open Polynomial

/-- Evaluation of a finite nonbacktracking-basis expansion is the
corresponding finite scalar sum. -/
theorem polynomial_eval_eq_sum (k : ℕ) (c : Coefficients) (x : ℝ) :
    (polynomial k c).eval x =
      c.sum fun i a => a * (nbPoly k i).eval x := by
  classical
  change Polynomial.evalRingHom x
      (Finset.sum c.support fun i => C (c i) * nbPoly k i) =
    Finset.sum c.support fun i => c i * (nbPoly k i).eval x
  rw [map_sum]
  apply Finset.sum_congr rfl
  intro i hi
  simp

@[simp]
private theorem dual_zero (k : ℕ) :
    dual k (0 : ℝ[X]) = 0 := by
  simp [dual]

private theorem dual_add (k : ℕ) (p q : ℝ[X]) :
    dual k (p + q) = dual k p + dual k q := by
  simp [dual]
  ring

private theorem dual_C_mul (k : ℕ) (a : ℝ) (p : ℝ[X]) :
    dual k (C a * p) = a * dual k p := by
  simp [dual]
  ring

/-- The three-point dual functional commutes with the finite
nonbacktracking-basis expansion. -/
theorem dual_polynomial_eq_sum (k : ℕ) (c : Coefficients) :
    dual k (polynomial k c) =
      c.sum fun i a => a * dual k (nbPoly k i) := by
  classical
  change
    dual k (Finset.sum c.support fun i => C (c i) * nbPoly k i) =
      Finset.sum c.support fun i => c i * dual k (nbPoly k i)
  induction c.support using Finset.induction with
  | empty => simp
  | @insert i s hi ih =>
      rw [Finset.sum_insert hi, Finset.sum_insert hi, dual_add,
        dual_C_mul, ih]

/-- Adding the dual value and the principal evaluation turns each basis term
into its dual slack. -/
theorem dual_add_eval_eq_slack_sum (k : ℕ) (c : Coefficients) :
    dual k (polynomial k c) + (polynomial k c).eval (k : ℝ) =
      c.sum fun i a => a * slack k i := by
  classical
  rw [dual_polynomial_eq_sum, polynomial_eval_eq_sum]
  change
    (Finset.sum c.support fun i => c i * dual k (nbPoly k i)) +
        Finset.sum c.support (fun i => c i * (nbPoly k i).eval (k : ℝ)) =
      Finset.sum c.support fun i => c i * slack k i
  rw [← Finset.sum_add_distrib]
  apply Finset.sum_congr rfl
  intro i hi
  rw [slack]
  ring

/-- The lower dual support point belongs to the closed WOW interval. -/
theorem xiMinus_mem_wowInterval (k : ℕ) :
    xiMinus k ∈ wowInterval k := by
  have hdelta : 0 ≤ delta k := Real.sqrt_nonneg _
  constructor
  · rfl
  · simp only [xiMinus, delta] at *
    linarith

/-- The upper dual support point belongs to the closed WOW interval. -/
theorem xiPlus_mem_wowInterval (k : ℕ) :
    xiPlus k ∈ wowInterval k := by
  have hdelta : 0 ≤ delta k := Real.sqrt_nonneg _
  constructor
  · simp only [xiPlus, delta] at *
    linarith
  · rfl

/-- For `k ≥ 4`, the middle dual support point `-2` belongs to the WOW
interval. -/
theorem xiZero_mem_wowInterval (k : ℕ) (hk : 4 ≤ k) :
    xiZero ∈ wowInterval k := by
  have hdelta : 0 ≤ delta k := Real.sqrt_nonneg _
  have hdelta_sq : delta k ^ 2 = 2 * (k : ℝ) - 2 :=
    delta_sq k hk
  have hkR : (4 : ℝ) ≤ (k : ℝ) := by exact_mod_cast hk
  have hdelta_one : 1 ≤ delta k := by nlinarith
  constructor <;>
    simp only [xiZero, delta] at * <;>
      linarith

/-- A polynomial which is nonpositive on the WOW interval has nonpositive
value under the positive three-point dual functional. -/
theorem dual_nonpos_of_nonpos_on_interval
    (k : ℕ) (hk : 4 ≤ k) (p : ℝ[X])
    (hp : ∀ x ∈ wowInterval k, p.eval x ≤ 0) :
    dual k p ≤ 0 := by
  have hm :=
    mul_nonpos_of_nonneg_of_nonpos
      (weightMinus_pos k hk).le
      (hp (xiMinus k) (xiMinus_mem_wowInterval k))
  have h0 :=
    mul_nonpos_of_nonneg_of_nonpos
      (weightZero_pos k hk).le
      (hp xiZero (xiZero_mem_wowInterval k hk))
  have hp' :=
    mul_nonpos_of_nonneg_of_nonpos
      (weightPlus_pos k hk).le
      (hp (xiPlus k) (xiPlus_mem_wowInterval k))
  rw [dual]
  linarith

/-- Admissibility makes the dual functional of the represented polynomial
nonpositive. -/
theorem dual_polynomial_nonpos
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    dual k (polynomial k c) ≤ 0 :=
  dual_nonpos_of_nonpos_on_interval k hk (polynomial k c) hc.2.2

/-- The degree-zero slack is exactly the LP ceiling. -/
theorem slack_zero_eq_ceiling (k : ℕ) (hk : 4 ≤ k) :
    slack k 0 = ceiling k := by
  rw [slack, dual_mass_eq_ceiling_sub_one k hk]
  simp

/-- The four unconstrained low-degree coefficients have zero dual slack. -/
theorem slack_eq_zero_of_one_le_of_le_four
    (k i : ℕ) (hk : 4 ≤ k) (hi1 : 1 ≤ i) (hi4 : i ≤ 4) :
    slack k i = 0 := by
  rw [slack, dual_nbPoly_eq_neg_eval_of_one_le_of_le_four k i hk hi1 hi4]
  ring

/-- The elementary finite-sum core of weak duality.  The exact mass/moment
and all-degree strict-slack theorems are supplied separately by the finite
dual and Chebyshev-tail modules. -/
private theorem ceiling_mul_le_slack_sum_of_certificates
    (k : ℕ) (c : Coefficients)
    (hc0 : 0 < c 0)
    (hcoeff : ∀ i, 5 ≤ i → 0 ≤ c i)
    (hmass : slack k 0 = ceiling k)
    (hmoment : ∀ i, 1 ≤ i → i ≤ 4 → slack k i = 0)
    (hslack : ∀ i, 5 ≤ i → 0 < slack k i) :
    ceiling k * c 0 ≤ c.sum fun i a => a * slack k i := by
  classical
  have hzero_mem : 0 ∈ c.support := by
    simpa [Finsupp.mem_support_iff] using ne_of_gt hc0
  calc
    ceiling k * c 0 =
        ∑ i ∈ c.support, if i = 0 then c i * slack k i else 0 := by
          simp [hzero_mem, hmass, mul_comm]
    _ ≤ ∑ i ∈ c.support, c i * slack k i := by
          apply Finset.sum_le_sum
          intro i hi
          by_cases hi0 : i = 0
          · subst i
            simp
          · simp only [hi0, ↓reduceIte]
            by_cases hi4 : i ≤ 4
            · have hi1 : 1 ≤ i := Nat.one_le_iff_ne_zero.mpr hi0
              rw [hmoment i hi1 hi4]
              simp
            · have hi5 : 5 ≤ i := by omega
              exact mul_nonneg (hcoeff i hi5) (le_of_lt (hslack i hi5))
    _ = c.sum fun i a => a * slack k i := rfl

/-- Weak duality once the separately established mass, moment, and strict
slack certificates are supplied.  This theorem is private so the exported
objective theorem cannot acquire certificate hypotheses. -/
private theorem objective_lower_bound_of_certificates
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c)
    (hmass : slack k 0 = ceiling k)
    (hmoment : ∀ i, 1 ≤ i → i ≤ 4 → slack k i = 0)
    (hslack : ∀ i, 5 ≤ i → 0 < slack k i) :
    ceiling k * c 0 ≤ (polynomial k c).eval (k : ℝ) := by
  have hsum :=
    ceiling_mul_le_slack_sum_of_certificates
      k c hc.1 hc.2.1 hmass hmoment hslack
  rw [← dual_add_eval_eq_slack_sum] at hsum
  have hdual := dual_polynomial_nonpos k hk c hc
  linarith

/-- The exact finite-support slack inequality used by weak duality.  Unlike
the internal engine, this exported theorem discharges every mass, moment,
and all-degree slack obligation from the exact certificate modules. -/
theorem ceiling_mul_le_slack_sum
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ceiling k * c 0 ≤ c.sum fun i a => a * slack k i :=
  ceiling_mul_le_slack_sum_of_certificates
    k c hc.1 hc.2.1
      (slack_zero_eq_ceiling k hk)
      (slack_eq_zero_of_one_le_of_le_four k · hk)
      (all_slacks_positive k · hk)

/-- The sharp objective lower bound for every admissible finite
nonbacktracking-basis expansion. -/
theorem twoSidedLP_objective_ge
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ceiling k * c 0 ≤ (polynomial k c).eval (k : ℝ) :=
  objective_lower_bound_of_certificates
    k hk c hc
      (slack_zero_eq_ceiling k hk)
      (slack_eq_zero_of_one_le_of_le_four k · hk)
      (all_slacks_positive k · hk)

end

end Wow284.LP
