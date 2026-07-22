import Wow284.DiagonalizationDefinitions

/-! Generated bounded certificate shard; do not edit by hand. -/

namespace Wow284

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_0 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 0 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_1 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 1 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_2 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 2 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_3 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 3 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_4 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 4 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_5 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 5 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_6 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 6 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_7 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 7 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_8 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 8 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_7_9 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex 9 d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex 9 d) := by
  decide

lemma eigenbasis_left_inverse_scaled_row_7 (s : Fin 10) (c d : Fin 5) :
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 7 c) (coordVertex s d) =
      (scaledIdentityInt) (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact eigenbasis_left_inverse_scaled_rows_7_0 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_1 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_2 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_3 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_4 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_5 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_6 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_7 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_8 c d
  · exact eigenbasis_left_inverse_scaled_rows_7_9 c d

end Wow284
