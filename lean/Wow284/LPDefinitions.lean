import Mathlib

open scoped BigOperators

namespace Wow284.LP

noncomputable section

open Polynomial

/-- The nonbacktracking polynomial sequence for degree `k`.

The exceptional definition of `F₂` is the one appropriate to regular graphs:
`F₂ = X² - k`.  From `F₃` onward the recurrence has parameter `k - 1`.
-/
def nbPoly (k : ℕ) : ℕ → ℝ[X]
  | 0 => 1
  | 1 => X
  | 2 => X ^ 2 - C (k : ℝ)
  | n + 3 => X * nbPoly k (n + 2) - C ((k - 1 : ℕ) : ℝ) * nbPoly k (n + 1)

@[simp]
theorem nbPoly_zero (k : ℕ) : nbPoly k 0 = 1 := rfl

@[simp]
theorem nbPoly_one (k : ℕ) : nbPoly k 1 = X := rfl

@[simp]
theorem nbPoly_two (k : ℕ) : nbPoly k 2 = X ^ 2 - C (k : ℝ) := rfl

theorem nbPoly_add_three (k n : ℕ) :
    nbPoly k (n + 3) =
      X * nbPoly k (n + 2) - C ((k - 1 : ℕ) : ℝ) * nbPoly k (n + 1) := rfl

/-- A finite coefficient family in the nonbacktracking basis. -/
abbrev Coefficients := ℕ →₀ ℝ

/-- The polynomial represented by a finite nonbacktracking-basis expansion. -/
def polynomial (k : ℕ) (c : Coefficients) : ℝ[X] :=
  c.sum fun i a => C a * nbPoly k i

/-- The closed shifted WOW interval. -/
def wowInterval (k : ℕ) : Set ℝ :=
  Set.Icc (-1 - Real.sqrt (2 * (k : ℝ) - 2))
    (-1 + Real.sqrt (2 * (k : ℝ) - 2))

/-- The exact admissible cone used by the one-variable nonbacktracking LP. -/
def Admissible (k : ℕ) (c : Coefficients) : Prop :=
  0 < c 0 ∧
    (∀ i, 5 ≤ i → 0 ≤ c i) ∧
      ∀ x ∈ wowInterval k, (polynomial k c).eval x ≤ 0

/-- The claimed optimum of the one-variable LP. -/
def ceiling (k : ℕ) : ℝ :=
  ((k : ℝ) + 2) * ((k : ℝ) ^ 2 + 3) / 6

/-- The normalized extremal polynomial. -/
def extremal (k : ℕ) : ℝ[X] :=
  C (1 / (6 * ((k : ℝ) + 2))) *
    (X + C 2) ^ 2 *
      (X ^ 2 + C 2 * X - C (2 * (k : ℝ) - 3))

/-- The square-root parameter in the dual certificate. -/
def delta (k : ℕ) : ℝ := Real.sqrt (2 * (k : ℝ) - 2)

/-- The lower endpoint of the shifted WOW interval. -/
def xiMinus (k : ℕ) : ℝ := -1 - delta k

/-- The interior support point of the three-point dual certificate. -/
def xiZero : ℝ := -2

/-- The upper endpoint of the shifted WOW interval. -/
def xiPlus (k : ℕ) : ℝ := -1 + delta k

/-- The weight at the lower endpoint of the dual certificate. -/
def weightMinus (k : ℕ) : ℝ :=
  (k : ℝ) * ((k : ℝ) + 2) *
      (2 * (k : ℝ) ^ 2 - 6 - 3 * ((k : ℝ) - 1) * delta k) /
    (24 * (2 * (k : ℝ) - 3))

/-- The weight at the interior point of the dual certificate. -/
def weightZero (k : ℕ) : ℝ :=
  (k : ℝ) * ((k : ℝ) - 1) * ((k : ℝ) ^ 2 + 3) /
    (6 * (2 * (k : ℝ) - 3))

/-- The weight at the upper endpoint of the dual certificate. -/
def weightPlus (k : ℕ) : ℝ :=
  (k : ℝ) * ((k : ℝ) + 2) *
      (2 * (k : ℝ) ^ 2 - 6 + 3 * ((k : ℝ) - 1) * delta k) /
    (24 * (2 * (k : ℝ) - 3))

/-- The three-point dual functional, written as a finite sum rather than as
a measure-theoretic integral. -/
def dual (k : ℕ) (p : ℝ[X]) : ℝ :=
  weightMinus k * p.eval (xiMinus k) +
    weightZero k * p.eval xiZero +
      weightPlus k * p.eval (xiPlus k)

/-- The dual slack in nonbacktracking degree `i`. -/
def slack (k i : ℕ) : ℝ :=
  dual k (nbPoly k i) + (nbPoly k i).eval (k : ℝ)

end

end Wow284.LP
