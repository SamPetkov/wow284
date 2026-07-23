import Wow284.Induced38.LDLLeft0
import Wow284.Induced38.LDLLeft1
import Wow284.Induced38.LDLLeft2
import Wow284.Induced38.LDLLeft3
import Wow284.Induced38.LDLLeft4
import Wow284.Induced38.LDLLeft5
import Wow284.Induced38.LDLLeft6
import Wow284.Induced38.LDLLeft7

namespace Wow284.Induced38

private lemma lpad_left_inverse_coord (r s : Fin 8) (c d : Fin 5) :
    (LpadInv * Lpad) (coordPad r c) (coordPad s d) =
      ((1 : Matrix PadVertex PadVertex ℚ)) (coordPad r c) (coordPad s d) := by
  fin_cases r
  · exact lpad_left_inverse_row_0 s c d
  · exact lpad_left_inverse_row_1 s c d
  · exact lpad_left_inverse_row_2 s c d
  · exact lpad_left_inverse_row_3 s c d
  · exact lpad_left_inverse_row_4 s c d
  · exact lpad_left_inverse_row_5 s c d
  · exact lpad_left_inverse_row_6 s c d
  · exact lpad_left_inverse_row_7 s c d

theorem lpad_left_inverse : LpadInv * Lpad = (1 : Matrix PadVertex PadVertex ℚ) := by
  ext i j
  rw [← coordPad_surj i, ← coordPad_surj j]
  exact lpad_left_inverse_coord _ _ _ _

end Wow284.Induced38
