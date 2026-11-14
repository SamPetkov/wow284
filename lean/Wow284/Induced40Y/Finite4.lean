import Wow284.Induced40Y.CertificateDefinitions

/-! Generated finite certificate shard 5/8. -/
namespace Wow284.Induced40Y

set_option maxRecDepth 15000 in
lemma degree_range_row_4 : ∀ c : Fin 5, degree (coordVertex 4 c) = 5 ∨ degree (coordVertex 4 c) = 6 ∨ degree (coordVertex 4 c) = 7 := by decide
set_option maxRecDepth 15000 in
lemma dual_bound_nat_row_4 : ∀ c : Fin 5,
    39 * degree (coordVertex 4 c) ≤
      7 * neighborDegreeSum (coordVertex 4 c) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_0 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 0 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_0 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 0 d) =
      Dcert (coordVertex 4 c) (coordVertex 0 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_1 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 1 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_1 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 1 d) =
      Dcert (coordVertex 4 c) (coordVertex 1 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_2 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 2 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_2 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 2 d) =
      Dcert (coordVertex 4 c) (coordVertex 2 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_3 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 3 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_3 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 3 d) =
      Dcert (coordVertex 4 c) (coordVertex 3 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_4 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 4 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_4 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 4 d) =
      Dcert (coordVertex 4 c) (coordVertex 4 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_5 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 5 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_5 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 5 d) =
      Dcert (coordVertex 4 c) (coordVertex 5 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_6 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 6 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_6 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 6 d) =
      Dcert (coordVertex 4 c) (coordVertex 6 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_4_7 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 4 c) (coordVertex 7 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_4_7 : ∀ c d : Fin 5,
    D (coordVertex 4 c) (coordVertex 7 d) =
      Dcert (coordVertex 4 c) (coordVertex 7 d) := by decide

end Wow284.Induced40Y
