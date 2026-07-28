import Wow284.LPCeiling

/-!
Trust report for the exact all-degree two-sided nonbacktracking LP theorem.

Compiling this file prints the transitive axioms used by the strict-slack,
explicit optimizer, objective, polynomial and coefficient rigidity, and
combined public endpoints.
-/

#print axioms Wow284.LP.all_slacks_positive
#print axioms Wow284.LP.extremalCoefficients_admissible
#print axioms Wow284.LP.extremalCoefficients_attains
#print axioms Wow284.LP.twoSidedLP_objective_ge
#print axioms Wow284.LP.twoSidedLP_equality_iff
#print axioms Wow284.LP.twoSidedLP_coefficient_equality_iff
#print axioms Wow284.LP.twoSidedLP_positive_ray_equality_iff
#print axioms Wow284.LP.twoSidedLP_optimal_and_rigid
#print axioms Wow284.LP.twoSidedLP_exact_optimum_and_coefficient_rigidity
