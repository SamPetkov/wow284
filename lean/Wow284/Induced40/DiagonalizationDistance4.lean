import Wow284.Induced40.DiagonalizationDefinitions

/-! Generated bounded 5x5 certificate shard. -/
namespace Wow284.Induced40

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_0 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 0 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_1 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 1 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_2 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 2 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_3 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 3 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_4 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 4 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_5 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 5 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_6 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 6 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma distance_diagonalization_int_rows_4_7 : ∀ c d : Fin 5,
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex 7 d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex 7 d) := by
  decide

lemma distance_diagonalization_int_row_4 (s : Fin 8) (c d : Fin 5) :
    (Dcert * eigenbasisInt) (coordVertex 4 c) (coordVertex s d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_diagonalization_int_rows_4_0 c d
  · exact distance_diagonalization_int_rows_4_1 c d
  · exact distance_diagonalization_int_rows_4_2 c d
  · exact distance_diagonalization_int_rows_4_3 c d
  · exact distance_diagonalization_int_rows_4_4 c d
  · exact distance_diagonalization_int_rows_4_5 c d
  · exact distance_diagonalization_int_rows_4_6 c d
  · exact distance_diagonalization_int_rows_4_7 c d

end Wow284.Induced40
