import Wow284.Induced42.CertificateDefinitions

/-! Generated finite certificate shard 2/7. -/
namespace Wow284.Induced42

set_option maxRecDepth 15000 in
lemma degree_range_row_1 : ∀ c : Fin 6, degree (coordVertex 1 c) = 6 := by decide
set_option maxRecDepth 15000 in
lemma dual_bound_nat_row_1 : ∀ c : Fin 6,
    6 * degree (coordVertex 1 c) ≤
      1 * neighborDegreeSum (coordVertex 1 c) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_0 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 0 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_0 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 0 d) =
      Dcert (coordVertex 1 c) (coordVertex 0 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_1 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 1 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_1 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 1 d) =
      Dcert (coordVertex 1 c) (coordVertex 1 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_2 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 2 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_2 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 2 d) =
      Dcert (coordVertex 1 c) (coordVertex 2 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_3 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 3 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_3 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 3 d) =
      Dcert (coordVertex 1 c) (coordVertex 3 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_4 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 4 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_4 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 4 d) =
      Dcert (coordVertex 1 c) (coordVertex 4 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_5 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 5 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_5 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 5 d) =
      Dcert (coordVertex 1 c) (coordVertex 5 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_1_6 : ∀ c d : Fin 6,
    HasPathAtMostThree (coordVertex 1 c) (coordVertex 6 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_1_6 : ∀ c d : Fin 6,
    D (coordVertex 1 c) (coordVertex 6 d) =
      Dcert (coordVertex 1 c) (coordVertex 6 d) := by decide

end Wow284.Induced42
