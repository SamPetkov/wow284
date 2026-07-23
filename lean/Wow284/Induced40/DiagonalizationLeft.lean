import Wow284.Induced40.DiagonalizationLeft0
import Wow284.Induced40.DiagonalizationLeft1
import Wow284.Induced40.DiagonalizationLeft2
import Wow284.Induced40.DiagonalizationLeft3
import Wow284.Induced40.DiagonalizationLeft4
import Wow284.Induced40.DiagonalizationLeft5
import Wow284.Induced40.DiagonalizationLeft6
import Wow284.Induced40.DiagonalizationLeft7

namespace Wow284.Induced40

open Matrix

private lemma eigenbasis_left_inverse_scaled_coord (r s : Fin 8) (c d : Fin 5) :
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex r c) (coordVertex s d) =
      (scaledIdentityInt) (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact eigenbasis_left_inverse_scaled_row_0 s c d
  · exact eigenbasis_left_inverse_scaled_row_1 s c d
  · exact eigenbasis_left_inverse_scaled_row_2 s c d
  · exact eigenbasis_left_inverse_scaled_row_3 s c d
  · exact eigenbasis_left_inverse_scaled_row_4 s c d
  · exact eigenbasis_left_inverse_scaled_row_5 s c d
  · exact eigenbasis_left_inverse_scaled_row_6 s c d
  · exact eigenbasis_left_inverse_scaled_row_7 s c d

theorem eigenbasis_left_inverse_scaled : eigenbasisInvNumerator * eigenbasisInt = scaledIdentityInt := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact eigenbasis_left_inverse_scaled_coord _ _ _ _

theorem eigenbasis_left_inverse :
    eigenbasisInv * eigenbasis = (1 : Matrix Vertex Vertex ℚ) := by
  change (((1 : ℚ) / 600) • castMatrix eigenbasisInvNumerator) *
    castMatrix eigenbasisInt = 1
  rw [Matrix.smul_mul, ← castMatrix_mul, eigenbasis_left_inverse_scaled]
  ext i j
  by_cases h : i = j
  · subst j
    simp [castMatrix, scaledIdentityInt]
  · simp [castMatrix, scaledIdentityInt, h]

theorem eigenbasis_right_inverse :
    eigenbasis * eigenbasisInv = (1 : Matrix Vertex Vertex ℚ) := by
  exact mul_eq_one_comm.mp eigenbasis_left_inverse

end Wow284.Induced40
