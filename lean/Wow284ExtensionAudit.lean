import Wow284Extended

/-!
Opt-in trust-surface report for the staged induced-graph extension.

This file intentionally contains no declarations.  Compiling it prints the
transitive axioms used by representative public structural, spectral, and
scalar certificates for the 40- and 38-vertex developments.  It is kept
outside the library roots so that it remains an audit command rather than a
mathematical dependency.
-/

-- Induced 40-vertex certificate.
#print axioms Wow284.Induced40.degree_six
#print axioms Wow284.Induced40.semantic_distance_eq_Dcert
#print axioms Wow284.Induced40.distance_polynomial
#print axioms Wow284.Induced40.eigenbasis_left_inverse
#print axioms Wow284.Induced40.distance_diagonalization
#print axioms Wow284.Induced40.distance_diagonal_counts
#print axioms Wow284.Induced40.exact_wow_gap_positive
#print axioms Wow284.Induced40.dual_degree_six
#print axioms Wow284.Induced40.semantic_distance_exact_diagonal_form
#print axioms Wow284.Induced40.counterexample_spectral_endpoint

-- Induced 38-vertex certificate and its staged LDL data.
#print axioms Wow284.Induced38.degree_profile
#print axioms Wow284.Induced38.dual_degree_lower_bound
#print axioms Wow284.Induced38.semantic_distance_eq_Dcert
#print axioms Wow284.Induced38.ldl_identity
#print axioms Wow284.Induced38.lpad_left_inverse
#print axioms Wow284.Induced38.lpad_right_inverse
#print axioms Wow284.Induced38.pivotPad_positive
#print axioms Wow284.Induced38.shifted_distance_real_posDef
#print axioms Wow284.Induced38.real_eigenpair_above_neg_seventeen_thirds
#print axioms Wow284.Induced38.exact_wow_gap_positive
