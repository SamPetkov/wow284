import Wow284.Induced40X.LDLLeft0
import Wow284.Induced40X.LDLLeft1
import Wow284.Induced40X.LDLLeft2
import Wow284.Induced40X.LDLLeft3
import Wow284.Induced40X.LDLLeft4
import Wow284.Induced40X.LDLLeft5
import Wow284.Induced40X.LDLLeft6
import Wow284.Induced40X.LDLLeft7
namespace Wow284.Induced40X
private lemma lpad_left_inverse_scaled_int_coord (r s : Fin 8) (c d : Fin 5) :
    (BpadInvNumeratorInt * BpadInt) (coordPad r c) (coordPad s d) = (scaledIdentityInt) (coordPad r c) (coordPad s d) := by
  fin_cases r
  · exact lpad_left_inverse_scaled_int_row_0 s c d
  · exact lpad_left_inverse_scaled_int_row_1 s c d
  · exact lpad_left_inverse_scaled_int_row_2 s c d
  · exact lpad_left_inverse_scaled_int_row_3 s c d
  · exact lpad_left_inverse_scaled_int_row_4 s c d
  · exact lpad_left_inverse_scaled_int_row_5 s c d
  · exact lpad_left_inverse_scaled_int_row_6 s c d
  · exact lpad_left_inverse_scaled_int_row_7 s c d
theorem lpad_left_inverse_scaled_int : BpadInvNumeratorInt * BpadInt = scaledIdentityInt := by
  ext i j
  rw [← coordPad_surj i, ← coordPad_surj j]
  exact lpad_left_inverse_scaled_int_coord _ _ _ _

end Wow284.Induced40X
