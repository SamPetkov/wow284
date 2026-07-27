import Wow284.Induced42.LDLDefinitions
/-! Generated bounded denominator-cleared integer shard 9/9. -/
namespace Wow284.Induced42
set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_0 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 0 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 0 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_1 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 1 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 1 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_2 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 2 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 2 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_3 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 3 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 3 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_4 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 4 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 4 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_5 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 5 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 5 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_6 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 6 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 6 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_7 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 7 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 7 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

set_option maxRecDepth 25000 in
lemma lpad_left_inverse_scaled_int_rows_8_8 : ∀ c d : Fin 5,
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad 8 d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad 8 d) := by
  intro c d
  fin_cases c <;> fin_cases d <;> decide

lemma lpad_left_inverse_scaled_int_row_8 (s : Fin 9) (c d : Fin 5) :
    (BpadInvNumeratorInt * BpadInt) (coordPad 8 c) (coordPad s d) =
      (scaledIdentityInt) (coordPad 8 c) (coordPad s d) := by
  fin_cases s
  · exact lpad_left_inverse_scaled_int_rows_8_0 c d
  · exact lpad_left_inverse_scaled_int_rows_8_1 c d
  · exact lpad_left_inverse_scaled_int_rows_8_2 c d
  · exact lpad_left_inverse_scaled_int_rows_8_3 c d
  · exact lpad_left_inverse_scaled_int_rows_8_4 c d
  · exact lpad_left_inverse_scaled_int_rows_8_5 c d
  · exact lpad_left_inverse_scaled_int_rows_8_6 c d
  · exact lpad_left_inverse_scaled_int_rows_8_7 c d
  · exact lpad_left_inverse_scaled_int_rows_8_8 c d

end Wow284.Induced42
