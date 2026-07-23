import Wow284.Induced38.CertificateDefinitions

/-! Generated bounded finite certificate shard. -/

namespace Wow284.Induced38


set_option maxRecDepth 10000 in
lemma degree_range_row_3 : ∀ c : Fin 2,
    degree (coordVertex 3 c) = 5 ∨ degree (coordVertex 3 c) = 6 := by
  intro c
  fin_cases c <;> decide

set_option maxRecDepth 10000 in
lemma dual_cross_bound_row_3 : ∀ c : Fin 2,
    17 * degree (coordVertex 3 c) ≤
      3 * neighborDegreeSum (coordVertex 3 c) := by
  intro c
  fin_cases c <;> decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_0 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_0 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 0 d) =
      Dcert (coordVertex 3 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_1 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_1 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 1 d) =
      Dcert (coordVertex 3 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_2 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_2 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 2 d) =
      Dcert (coordVertex 3 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_3 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_3 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 3 d) =
      Dcert (coordVertex 3 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_4 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_4 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 4 d) =
      Dcert (coordVertex 3 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_5 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_5 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 5 d) =
      Dcert (coordVertex 3 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_6 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_6 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 6 d) =
      Dcert (coordVertex 3 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_7 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_7 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 7 d) =
      Dcert (coordVertex 3 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_8 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_8 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 8 d) =
      Dcert (coordVertex 3 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_9 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 9 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_9 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 9 d) =
      Dcert (coordVertex 3 c) (coordVertex 9 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_10 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 10 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_10 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 10 d) =
      Dcert (coordVertex 3 c) (coordVertex 10 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_11 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 11 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_11 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 11 d) =
      Dcert (coordVertex 3 c) (coordVertex 11 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_12 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 12 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_12 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 12 d) =
      Dcert (coordVertex 3 c) (coordVertex 12 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_13 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 13 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_13 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 13 d) =
      Dcert (coordVertex 3 c) (coordVertex 13 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_14 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 14 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_14 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 14 d) =
      Dcert (coordVertex 3 c) (coordVertex 14 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_15 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 15 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_15 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 15 d) =
      Dcert (coordVertex 3 c) (coordVertex 15 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_16 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 16 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_16 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 16 d) =
      Dcert (coordVertex 3 c) (coordVertex 16 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_17 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 17 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_17 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 17 d) =
      Dcert (coordVertex 3 c) (coordVertex 17 d) := by
  decide

set_option maxRecDepth 10000 in
lemma diameter_rows_3_18 : ∀ c d : Fin 2,
    HasPathAtMostThree (coordVertex 3 c) (coordVertex 18 d) := by
  decide

set_option maxRecDepth 10000 in
lemma semantic_distance_rows_3_18 : ∀ c d : Fin 2,
    D (coordVertex 3 c) (coordVertex 18 d) =
      Dcert (coordVertex 3 c) (coordVertex 18 d) := by
  decide


end Wow284.Induced38
