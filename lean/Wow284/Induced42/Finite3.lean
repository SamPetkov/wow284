import Wow284.Induced42.CertificateDefinitions

/-! Generated finite certificate shard 4/7. -/
namespace Wow284.Induced42

set_option maxRecDepth 15000 in
lemma degree_range_row_3 : ∀ c : Fin 6, degree (coordVertex 3 c) = 6 := by decide
set_option maxRecDepth 15000 in
lemma dual_bound_nat_row_3 : ∀ c : Fin 6,
    6 * degree (coordVertex 3 c) ≤
      1 * neighborDegreeSum (coordVertex 3 c) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_0 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 0 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_0 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 0 d) =
      Dcert (coordVertex 3 c) (coordVertex 0 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_1 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 1 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_1 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 1 d) =
      Dcert (coordVertex 3 c) (coordVertex 1 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_2 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 2 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_2 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 2 d) =
      Dcert (coordVertex 3 c) (coordVertex 2 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_3 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 3 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_3 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 3 d) =
      Dcert (coordVertex 3 c) (coordVertex 3 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_4 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 4 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_4 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 4 d) =
      Dcert (coordVertex 3 c) (coordVertex 4 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_5 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 5 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_5 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 5 d) =
      Dcert (coordVertex 3 c) (coordVertex 5 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_3_6 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 6 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_3_6 : ∀ c d : Fin 6,
    D (coordVertex 3 c) (coordVertex 6 d) =
      Dcert (coordVertex 3 c) (coordVertex 6 d) := by decide

end Wow284.Induced42
