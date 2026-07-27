import Mathlib

open scoped Classical

set_option maxHeartbeats 8000000
set_option maxRecDepth 4000
set_option relaxedAutoImplicit false
set_option autoImplicit false

namespace Wow284

/-- The lower half of the ceiling transfer: a real lower bound on a natural-valued
quantity remains a lower bound after taking the natural ceiling. -/
lemma natCeil_le_of_le_cast {lower : ℝ} {value : ℕ}
    (h : lower ≤ (value : ℝ)) : ⌈lower⌉₊ ≤ value := by
  exact Nat.ceil_le.mpr h

/-- The upper half of the ceiling transfer: a natural-valued quantity below a real
upper bound is below that upper bound's natural ceiling. -/
lemma le_natCeil_of_cast_le {value : ℕ} {upper : ℝ}
    (h : (value : ℝ) ≤ upper) : value ≤ ⌈upper⌉₊ := by
  exact_mod_cast h.trans (Nat.le_ceil upper)

/-- Final two-sided nonbacktracking LP ceiling-bound integration.

`parameter` may encode the graph, walk length, or any other parameters of the
nonbacktracking optimization problem.  Once the two LP arguments independently
place the natural-valued target between `lowerLP` and `upperLP`, this theorem
integrates them into the advertised pair of ceiling bounds.  No relation between
successive parameter values (and hence no backtracking step) is required. -/
theorem final_twoSided_nonbacktrackingLP_ceilingBound
    {Parameter : Type*}
    (target : Parameter → ℕ)
    (lowerLP upperLP : Parameter → ℝ)
    (lower_certificate : ∀ p, lowerLP p ≤ (target p : ℝ))
    (upper_certificate : ∀ p, (target p : ℝ) ≤ upperLP p) :
    ∀ p, ⌈lowerLP p⌉₊ ≤ target p ∧ target p ≤ ⌈upperLP p⌉₊ := by
  intro p
  exact ⟨natCeil_le_of_le_cast (lower_certificate p),
    le_natCeil_of_cast_le (upper_certificate p)⟩

end Wow284
