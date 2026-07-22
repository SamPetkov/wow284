import Wow284.DiagonalizationDefinitions

/-! Generated bounded certificate shard; do not edit by hand. -/

namespace Wow284

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_0 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 0 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_1 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 1 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_2 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 2 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_3 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 3 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_4 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 4 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_5 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 5 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_6 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 6 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_7 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 7 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_8 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 8 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_8_9 : ∀ c d : Fin 5,
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex 9 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex 9 d) := by
  decide

lemma distance_diagonalization_int_row_8 (s : Fin 10) (c d : Fin 5) :
    (D * eigenbasisInt) (coordVertex 8 c) (coordVertex s d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 8 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_diagonalization_int_rows_8_0 c d
  · exact distance_diagonalization_int_rows_8_1 c d
  · exact distance_diagonalization_int_rows_8_2 c d
  · exact distance_diagonalization_int_rows_8_3 c d
  · exact distance_diagonalization_int_rows_8_4 c d
  · exact distance_diagonalization_int_rows_8_5 c d
  · exact distance_diagonalization_int_rows_8_6 c d
  · exact distance_diagonalization_int_rows_8_7 c d
  · exact distance_diagonalization_int_rows_8_8 c d
  · exact distance_diagonalization_int_rows_8_9 c d

end Wow284
