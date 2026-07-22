import Wow284.DiagonalizationDistance0
import Wow284.DiagonalizationDistance1
import Wow284.DiagonalizationDistance2
import Wow284.DiagonalizationDistance3
import Wow284.DiagonalizationDistance4
import Wow284.DiagonalizationDistance5
import Wow284.DiagonalizationDistance6
import Wow284.DiagonalizationDistance7
import Wow284.DiagonalizationDistance8
import Wow284.DiagonalizationDistance9

/-!
Generated assembly of the bounded distance-diagonalization certificate.
-/

namespace Wow284

open Matrix

private lemma distance_diagonalization_int_coord (r s : Fin 10) (c d : Fin 5) :
    (D * eigenbasisInt) (coordVertex r c) (coordVertex s d) =
      (eigenbasisInt * distanceDiagonalInt) (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact distance_diagonalization_int_row_0 s c d
  · exact distance_diagonalization_int_row_1 s c d
  · exact distance_diagonalization_int_row_2 s c d
  · exact distance_diagonalization_int_row_3 s c d
  · exact distance_diagonalization_int_row_4 s c d
  · exact distance_diagonalization_int_row_5 s c d
  · exact distance_diagonalization_int_row_6 s c d
  · exact distance_diagonalization_int_row_7 s c d
  · exact distance_diagonalization_int_row_8 s c d
  · exact distance_diagonalization_int_row_9 s c d

theorem distance_diagonalization_int :
    D * eigenbasisInt = eigenbasisInt * distanceDiagonalInt := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact distance_diagonalization_int_coord _ _ _ _


theorem distance_diagonalization :
    Dq * eigenbasis = eigenbasis * distanceDiagonal := by
  change castMatrix D * castMatrix eigenbasisInt =
    castMatrix eigenbasisInt * castMatrix distanceDiagonalInt
  simpa only [← castMatrix_mul] using congrArg castMatrix distance_diagonalization_int

end Wow284
