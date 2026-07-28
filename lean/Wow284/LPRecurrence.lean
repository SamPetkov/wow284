import Wow284.LPDefinitions

namespace Wow284.LP

noncomputable section

open Polynomial

/-- Evaluation of the nonbacktracking polynomial at the principal value. -/
theorem nbPoly_eval_at_degree (k i : ℕ) (hk : 1 ≤ k) (hi : 1 ≤ i) :
    (nbPoly k i).eval (k : ℝ) =
      (k : ℝ) * (((k - 1 : ℕ) : ℝ) ^ (i - 1)) := by
  induction i using Nat.strong_induction_on with
  | h i ih =>
      rcases i with (_ | _ | i)
      · omega
      · simp [nbPoly]
      · rcases i with (_ | i)
        · simp [nbPoly, Nat.cast_sub hk]
          ring
        · rw [nbPoly_add_three]
          simp only [eval_sub, eval_mul, eval_X, eval_C]
          rw [ih (i + 2) (by omega) (by omega), ih (i + 1) (by omega) (by omega)]
          push_cast [Nat.cast_sub hk]
          simp only [pow_succ]
          ring

/-- Every nonbacktracking polynomial is monic of its indexed degree. -/
theorem nbPoly_isMonicOfDegree (k i : ℕ) :
    (nbPoly k i).IsMonicOfDegree i := by
  induction i using Nat.strong_induction_on with
  | h i ih =>
      rcases i with (_ | _ | _ | n)
      · simp [nbPoly]
      · simpa [nbPoly] using Polynomial.isMonicOfDegree_X ℝ
      · have hmain :
            (X ^ 2 : ℝ[X]).IsMonicOfDegree 2 :=
          Polynomial.isMonicOfDegree_X_pow ℝ 2
        have hlow : (C (k : ℝ)).natDegree < 2 := by
          simp
        simpa [nbPoly] using hmain.sub hlow
      · have hmain :
            (X * nbPoly k (n + 2)).IsMonicOfDegree (n + 3) := by
          have :=
            (Polynomial.isMonicOfDegree_X ℝ).mul
              (ih (n + 2) (by omega))
          simpa only [Nat.add_comm, Nat.add_left_comm, Nat.add_assoc] using this
        have hlow :
            (C (((k - 1 : ℕ) : ℝ)) * nbPoly k (n + 1)).natDegree <
              n + 3 := by
          calc
            (C (((k - 1 : ℕ) : ℝ)) * nbPoly k (n + 1)).natDegree
                ≤ (nbPoly k (n + 1)).natDegree :=
              natDegree_C_mul_le _ _
            _ = n + 1 := (ih (n + 1) (by omega)).natDegree_eq
            _ < n + 3 := by omega
        rw [nbPoly_add_three]
        exact hmain.sub hlow

/-- The nonbacktracking polynomials, indexed by their exact degrees, form a
polynomial sequence. -/
def nbSequence (k : ℕ) : Polynomial.Sequence ℝ where
  elems' := nbPoly k
  degree_eq' i :=
    (degree_eq_iff_natDegree_eq (nbPoly_isMonicOfDegree k i).ne_zero).2
      (nbPoly_isMonicOfDegree k i).natDegree_eq

/-- The full nonbacktracking polynomial family is linearly independent. -/
theorem nbPoly_linearIndependent (k : ℕ) :
    LinearIndependent ℝ (nbPoly k) :=
  (nbSequence k).linearIndependent

/-- The finite nonbacktracking expansion is the standard finitely supported
linear combination of the polynomial sequence. -/
theorem polynomial_eq_linearCombination (k : ℕ) (c : Coefficients) :
    polynomial k c = Finsupp.linearCombination ℝ (nbPoly k) c := by
  simp [polynomial, Finsupp.linearCombination_apply,
    Polynomial.smul_eq_C_mul]

/-- Coefficients in the nonbacktracking basis are unique. -/
theorem polynomial_injective (k : ℕ) :
    Function.Injective (polynomial k) := by
  intro c d h
  apply nbPoly_linearIndependent k
  simpa only [← polynomial_eq_linearCombination] using h

/-- Scaling a finite coefficient family scales its represented polynomial. -/
theorem polynomial_smul (k : ℕ) (a : ℝ) (c : Coefficients) :
    polynomial k (a • c) = C a * polynomial k c := by
  rw [polynomial_eq_linearCombination, map_smul,
    ← polynomial_eq_linearCombination]
  exact Polynomial.smul_eq_C_mul (p := polynomial k c) a

end

end Wow284.LP
