import Wow284.DiagonalizationDefinitions

/-! Generated bounded certificate shard; do not edit by hand. -/

namespace Wow284

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_0 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 0 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 0 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_1 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 1 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 1 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_2 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 2 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 2 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_3 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 3 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 3 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_4 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 4 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 4 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_5 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 5 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 5 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_6 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 6 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 6 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_7 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 7 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 7 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_8 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 8 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 8 d) := by
  decide

set_option maxRecDepth 10000 in
lemma eigenbasis_left_inverse_scaled_rows_5_9 : ∀ c d : Fin 5,
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex 9 d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex 9 d) := by
  decide

lemma eigenbasis_left_inverse_scaled_row_5 (s : Fin 10) (c d : Fin 5) :
    (eigenbasisInvNumerator * eigenbasisInt) (coordVertex 5 c) (coordVertex s d) =
      (scaledIdentityInt) (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact eigenbasis_left_inverse_scaled_rows_5_0 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_1 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_2 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_3 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_4 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_5 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_6 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_7 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_8 c d
  · exact eigenbasis_left_inverse_scaled_rows_5_9 c d

end Wow284
