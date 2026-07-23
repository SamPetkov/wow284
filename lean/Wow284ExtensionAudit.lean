import Wow284Extended

/-!
Trust-surface report for the induced-graph counterexample certificates.

This file intentionally contains no declarations.  Compiling it prints the
transitive axioms used by representative public structural, spectral, and
positive-definiteness certificates.  It remains outside the library roots so
that it is an audit command rather than a mathematical dependency.
-/

-- Induced 40-vertex certificate.
#print axioms Wow284.Induced40.degree_six
#print axioms Wow284.Induced40.semantic_distance_eq_Dcert
#print axioms Wow284.Induced40.eigenbasis_left_inverse
#print axioms Wow284.Induced40.eigenbasis_right_inverse
#print axioms Wow284.Induced40.distance_diagonalization
#print axioms Wow284.Induced40.distance_diagonal_counts
#print axioms Wow284.Induced40.distance_diagonal_entry_cases
#print axioms Wow284.Induced40.distance_diagonal_minimum_certificate
#print axioms Wow284.Induced40.dual_degree_six
#print axioms Wow284.Induced40.semantic_distance_exact_diagonal_form
#print axioms Wow284.Induced40.exact_counterexample_certificate

-- Induced 38-vertex certificate.
#print axioms Wow284.Induced38.degree_profile
#print axioms Wow284.Induced38.dual_degree_lower_bound
#print axioms Wow284.Induced38.dual_degree_attained
#print axioms Wow284.Induced38.semantic_distance_eq_Dcert
#print axioms Wow284.Induced38.ldl_identity
#print axioms Wow284.Induced38.lpad_left_inverse
#print axioms Wow284.Induced38.lpad_right_inverse
#print axioms Wow284.Induced38.pivotPad_positive
#print axioms Wow284.Induced38.shifted_distance_posDef
#print axioms Wow284.Induced38.shifted_distance_real_posDef
#print axioms Wow284.Induced38.real_eigenpair_above_neg_seventeen_thirds
#print axioms Wow284.Induced38.minimum_dual_degree_certificate
#print axioms Wow284.Induced38.exact_counterexample_certificate
#print axioms Wow284.Induced38.counterexample_endpoint
