import Wow284.Induced39.LDLDefinitions
/-! Generated bounded denominator-cleared integer shard 4/8. -/
namespace Wow284.Induced39
set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_0 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 0 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 0 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_1 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 1 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 1 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_2 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 2 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 2 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_3 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 3 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 3 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_4 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 4 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 4 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_5 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 5 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 5 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_6 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 6 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 6 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_3_7 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad 7 d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad 7 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

lemma ldl_scaled_identity_int_row_3 (s : Fin 8) (c d : Fin 5) :
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 3 c) (coordPad s d) =
      (MscaledPadInt) (coordPad 3 c) (coordPad s d) := by
  fin_cases s
  · exact ldl_scaled_identity_int_rows_3_0 c d
  · exact ldl_scaled_identity_int_rows_3_1 c d
  · exact ldl_scaled_identity_int_rows_3_2 c d
  · exact ldl_scaled_identity_int_rows_3_3 c d
  · exact ldl_scaled_identity_int_rows_3_4 c d
  · exact ldl_scaled_identity_int_rows_3_5 c d
  · exact ldl_scaled_identity_int_rows_3_6 c d
  · exact ldl_scaled_identity_int_rows_3_7 c d

end Wow284.Induced39
