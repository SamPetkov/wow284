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

-- Generated order-40 certificate: X42 minus the endpoints of an edge.
#print axioms Wow284.Induced40X.degree_profile
#print axioms Wow284.Induced40X.no_triangle
#print axioms Wow284.Induced40X.no_four_cycle
#print axioms Wow284.Induced40X.diameter_at_most_three
#print axioms Wow284.Induced40X.semantic_distance_eq_Dcert
#print axioms Wow284.Induced40X.ldl_identity
#print axioms Wow284.Induced40X.shifted_distance_real_posDef
#print axioms Wow284.Induced40X.counterexample_endpoint

-- Generated order-40 certificate: HS - {P_(0,*), P_(1,0), Q_(0,0), Q_(0,2), Q_(2,2), Q_(4,4)}.
#print axioms Wow284.Induced40Y.degree_profile
#print axioms Wow284.Induced40Y.no_triangle
#print axioms Wow284.Induced40Y.no_four_cycle
#print axioms Wow284.Induced40Y.diameter_at_most_three
#print axioms Wow284.Induced40Y.semantic_distance_eq_Dcert
#print axioms Wow284.Induced40Y.ldl_identity
#print axioms Wow284.Induced40Y.shifted_distance_real_posDef
#print axioms Wow284.Induced40Y.counterexample_endpoint

-- Generated order-40 certificate: HS - {P_(0,*), P_(1,0), Q_(0,0), Q_(0,2), Q_(1,1), Q_(1,4)}.
#print axioms Wow284.Induced40Z.degree_profile
#print axioms Wow284.Induced40Z.no_triangle
#print axioms Wow284.Induced40Z.no_four_cycle
#print axioms Wow284.Induced40Z.diameter_at_most_three
#print axioms Wow284.Induced40Z.semantic_distance_eq_Dcert
#print axioms Wow284.Induced40Z.ldl_identity
#print axioms Wow284.Induced40Z.shifted_distance_real_posDef
#print axioms Wow284.Induced40Z.counterexample_endpoint
-- Graph-level diameter-three distance identities.
#print axioms Wow284.DiameterThreeMatrix.distMatrix_eq
#print axioms Wow284.DiameterThreeMatrix.distMatrix_add_smul_one_eq
#print axioms Wow284.DiameterThreeMatrix.distMatrix_mulVec_of_adj_eigen
#print axioms Wow284.DiameterThreeMatrix.distMatrix_mulVec_const
#print axioms Wow284.DiameterThreeMatrix.abs_add_one_lt_of_posDef
#print axioms Wow284.DiameterThreeMatrix.distMatrix_eq_of_diam_le_three
#print axioms Wow284.DiameterThreeMatrix.distMatrix_add_smul_one_eq_of_diam_le_three
#print axioms Wow284.DiameterThreeMatrix.posDef_shift_iff_of_diam_le_three
