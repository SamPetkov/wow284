import Wow284.Induced40X.LDLIdentity0
import Wow284.Induced40X.LDLIdentity1
import Wow284.Induced40X.LDLIdentity2
import Wow284.Induced40X.LDLIdentity3
import Wow284.Induced40X.LDLIdentity4
import Wow284.Induced40X.LDLIdentity5
import Wow284.Induced40X.LDLIdentity6
import Wow284.Induced40X.LDLIdentity7
namespace Wow284.Induced40X
private lemma ldl_scaled_identity_int_coord (r s : Fin 8) (c d : Fin 5) :
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad r c) (coordPad s d) = (MscaledPadInt) (coordPad r c) (coordPad s d) := by
  fin_cases r
  · exact ldl_scaled_identity_int_row_0 s c d
  · exact ldl_scaled_identity_int_row_1 s c d
  · exact ldl_scaled_identity_int_row_2 s c d
  · exact ldl_scaled_identity_int_row_3 s c d
  · exact ldl_scaled_identity_int_row_4 s c d
  · exact ldl_scaled_identity_int_row_5 s c d
  · exact ldl_scaled_identity_int_row_6 s c d
  · exact ldl_scaled_identity_int_row_7 s c d
theorem ldl_scaled_identity_int : BpadInt * WpadInt * BpadInt.transpose = MscaledPadInt := by
  ext i j
  rw [← coordPad_surj i, ← coordPad_surj j]
  exact ldl_scaled_identity_int_coord _ _ _ _

end Wow284.Induced40X
