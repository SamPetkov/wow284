import Wow284.Induced38.LDLIdentity0
import Wow284.Induced38.LDLIdentity1
import Wow284.Induced38.LDLIdentity2
import Wow284.Induced38.LDLIdentity3
import Wow284.Induced38.LDLIdentity4
import Wow284.Induced38.LDLIdentity5
import Wow284.Induced38.LDLIdentity6
import Wow284.Induced38.LDLIdentity7

namespace Wow284.Induced38

private lemma ldl_identity_coord (r s : Fin 8) (c d : Fin 5) :
    (Lpad * DeltaPad * Lpad.transpose) (coordPad r c) (coordPad s d) =
      (Mpad) (coordPad r c) (coordPad s d) := by
  fin_cases r
  · exact ldl_identity_row_0 s c d
  · exact ldl_identity_row_1 s c d
  · exact ldl_identity_row_2 s c d
  · exact ldl_identity_row_3 s c d
  · exact ldl_identity_row_4 s c d
  · exact ldl_identity_row_5 s c d
  · exact ldl_identity_row_6 s c d
  · exact ldl_identity_row_7 s c d

theorem ldl_identity : Lpad * DeltaPad * Lpad.transpose = Mpad := by
  ext i j
  rw [← coordPad_surj i, ← coordPad_surj j]
  exact ldl_identity_coord _ _ _ _

end Wow284.Induced38
