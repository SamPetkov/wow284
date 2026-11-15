import Wow284.Induced40Z.CertificateDefinitions

/-! Generated finite certificate shard 8/8. -/
namespace Wow284.Induced40Z

set_option maxRecDepth 15000 in
lemma degree_range_row_7 : ∀ c : Fin 5, degree (coordVertex 7 c) = 5 ∨ degree (coordVertex 7 c) = 6 ∨ degree (coordVertex 7 c) = 7 := by decide
set_option maxRecDepth 15000 in
lemma dual_bound_nat_row_7 : ∀ c : Fin 5,
    39 * degree (coordVertex 7 c) ≤
      7 * neighborDegreeSum (coordVertex 7 c) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_0 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 0 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_0 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 0 d) =
      Dcert (coordVertex 7 c) (coordVertex 0 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_1 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 1 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_1 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 1 d) =
      Dcert (coordVertex 7 c) (coordVertex 1 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_2 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 2 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_2 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 2 d) =
      Dcert (coordVertex 7 c) (coordVertex 2 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_3 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 3 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_3 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 3 d) =
      Dcert (coordVertex 7 c) (coordVertex 3 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_4 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 4 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_4 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 4 d) =
      Dcert (coordVertex 7 c) (coordVertex 4 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_5 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 5 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_5 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 5 d) =
      Dcert (coordVertex 7 c) (coordVertex 5 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_6 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 6 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_6 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 6 d) =
      Dcert (coordVertex 7 c) (coordVertex 6 d) := by decide

set_option maxRecDepth 15000 in
lemma diameter_rows_7_7 : ∀ c d : Fin 5,
    HasPathAtMostThree (coordVertex 7 c) (coordVertex 7 d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_7_7 : ∀ c d : Fin 5,
    D (coordVertex 7 c) (coordVertex 7 d) =
      Dcert (coordVertex 7 c) (coordVertex 7 d) := by decide

end Wow284.Induced40Z
