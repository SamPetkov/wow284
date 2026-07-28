import Wow284.LPRigidity

namespace Wow284.LP

noncomputable section

/-- Exact optimum and equality rigidity for the all-degree two-sided
nonbacktracking linear program. -/
theorem twoSidedLP_optimal_and_rigid
    (k : ℕ) (hk : 4 ≤ k) (c : Coefficients)
    (hc : Admissible k c) :
    ceiling k * c 0 ≤ (polynomial k c).eval (k : ℝ) ∧
      ((polynomial k c).eval (k : ℝ) = ceiling k * c 0 ↔
        polynomial k c = Polynomial.C (c 0) * extremal k) :=
  ⟨twoSidedLP_objective_ge k hk c hc, twoSidedLP_equality_iff k hk c hc⟩

/-- Non-vacuous exact optimality and coefficient-level rigidity.  The first
three conjuncts exhibit a normalized admissible optimizer.  The final
conjunct gives the sharp universal lower bound and identifies every equality
case with the corresponding positive scaling of that finite coefficient
family. -/
theorem twoSidedLP_exact_optimum_and_coefficient_rigidity
    (k : ℕ) (hk : 4 ≤ k) :
    Admissible k (extremalCoefficients k) ∧
      extremalCoefficients k 0 = 1 ∧
        (polynomial k (extremalCoefficients k)).eval (k : ℝ) = ceiling k ∧
          ∀ c : Coefficients, Admissible k c →
            ceiling k * c 0 ≤ (polynomial k c).eval (k : ℝ) ∧
              ((polynomial k c).eval (k : ℝ) = ceiling k * c 0 ↔
                c = c 0 • extremalCoefficients k) := by
  refine
    ⟨extremalCoefficients_admissible k (by omega), by simp, ?_, ?_⟩
  · simpa using extremalCoefficients_attains k (by omega)
  · intro c hc
    exact
      ⟨twoSidedLP_objective_ge k hk c hc,
        twoSidedLP_coefficient_equality_iff k hk c hc⟩

end

end Wow284.LP
