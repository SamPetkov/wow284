import Wow284.Induced42.LDLDefinitions
/-! Generated bounded denominator-cleared integer shard 7/9. -/
namespace Wow284.Induced42
set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_0 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 0 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 0 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_1 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 1 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 1 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_2 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 2 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 2 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_3 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 3 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 3 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_4 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 4 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 4 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_5 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 5 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 5 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_6 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 6 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 6 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_7 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 7 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 7 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma ldl_scaled_identity_int_rows_6_8 : ∀ c d : Fin 5,
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad 8 d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad 8 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

lemma ldl_scaled_identity_int_row_6 (s : Fin 9) (c d : Fin 5) :
    (BpadInt * WpadInt * BpadInt.transpose) (coordPad 6 c) (coordPad s d) =
      (MscaledPadInt) (coordPad 6 c) (coordPad s d) := by
  fin_cases s
  · exact ldl_scaled_identity_int_rows_6_0 c d
  · exact ldl_scaled_identity_int_rows_6_1 c d
  · exact ldl_scaled_identity_int_rows_6_2 c d
  · exact ldl_scaled_identity_int_rows_6_3 c d
  · exact ldl_scaled_identity_int_rows_6_4 c d
  · exact ldl_scaled_identity_int_rows_6_5 c d
  · exact ldl_scaled_identity_int_rows_6_6 c d
  · exact ldl_scaled_identity_int_rows_6_7 c d
  · exact ldl_scaled_identity_int_rows_6_8 c d

end Wow284.Induced42
