import Wow284.Induced40.Structural0
import Wow284.Induced40.Structural1
import Wow284.Induced40.Structural2
import Wow284.Induced40.Structural3
import Wow284.Induced40.Structural4
import Wow284.Induced40.Structural5
import Wow284.Induced40.Structural6
import Wow284.Induced40.Structural7

/-!
Assembly of the finite structural certificates for the induced 40-vertex graph.
-/

namespace Wow284.Induced40

open Matrix

private lemma degree_coord (r : Fin 8) (c : Fin 5) :
    degree (coordVertex r c) = 6 := by
  fin_cases r
  · exact degree_row_0 c
  · exact degree_row_1 c
  · exact degree_row_2 c
  · exact degree_row_3 c
  · exact degree_row_4 c
  · exact degree_row_5 c
  · exact degree_row_6 c
  · exact degree_row_7 c

theorem degree_six : ∀ v : Vertex, degree v = 6 := by
  intro v
  rw [← coordVertex_surj v]
  exact degree_coord _ _

private lemma diameter_row_0 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_0_0 c d
  · exact diameter_rows_0_1 c d
  · exact diameter_rows_0_2 c d
  · exact diameter_rows_0_3 c d
  · exact diameter_rows_0_4 c d
  · exact diameter_rows_0_5 c d
  · exact diameter_rows_0_6 c d
  · exact diameter_rows_0_7 c d
private lemma semantic_distance_row_0 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 0 c) (coordVertex s d) =
      Dcert (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_0_0 c d
  · exact semantic_distance_rows_0_1 c d
  · exact semantic_distance_rows_0_2 c d
  · exact semantic_distance_rows_0_3 c d
  · exact semantic_distance_rows_0_4 c d
  · exact semantic_distance_rows_0_5 c d
  · exact semantic_distance_rows_0_6 c d
  · exact semantic_distance_rows_0_7 c d
private lemma distance_polynomial_entry_row_0 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 0 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_0_0 c d
  · exact distance_polynomial_entry_rows_0_1 c d
  · exact distance_polynomial_entry_rows_0_2 c d
  · exact distance_polynomial_entry_rows_0_3 c d
  · exact distance_polynomial_entry_rows_0_4 c d
  · exact distance_polynomial_entry_rows_0_5 c d
  · exact distance_polynomial_entry_rows_0_6 c d
  · exact distance_polynomial_entry_rows_0_7 c d
private lemma diameter_row_1 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_1_0 c d
  · exact diameter_rows_1_1 c d
  · exact diameter_rows_1_2 c d
  · exact diameter_rows_1_3 c d
  · exact diameter_rows_1_4 c d
  · exact diameter_rows_1_5 c d
  · exact diameter_rows_1_6 c d
  · exact diameter_rows_1_7 c d
private lemma semantic_distance_row_1 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 1 c) (coordVertex s d) =
      Dcert (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_1_0 c d
  · exact semantic_distance_rows_1_1 c d
  · exact semantic_distance_rows_1_2 c d
  · exact semantic_distance_rows_1_3 c d
  · exact semantic_distance_rows_1_4 c d
  · exact semantic_distance_rows_1_5 c d
  · exact semantic_distance_rows_1_6 c d
  · exact semantic_distance_rows_1_7 c d
private lemma distance_polynomial_entry_row_1 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 1 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_1_0 c d
  · exact distance_polynomial_entry_rows_1_1 c d
  · exact distance_polynomial_entry_rows_1_2 c d
  · exact distance_polynomial_entry_rows_1_3 c d
  · exact distance_polynomial_entry_rows_1_4 c d
  · exact distance_polynomial_entry_rows_1_5 c d
  · exact distance_polynomial_entry_rows_1_6 c d
  · exact distance_polynomial_entry_rows_1_7 c d
private lemma diameter_row_2 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_2_0 c d
  · exact diameter_rows_2_1 c d
  · exact diameter_rows_2_2 c d
  · exact diameter_rows_2_3 c d
  · exact diameter_rows_2_4 c d
  · exact diameter_rows_2_5 c d
  · exact diameter_rows_2_6 c d
  · exact diameter_rows_2_7 c d
private lemma semantic_distance_row_2 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 2 c) (coordVertex s d) =
      Dcert (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_2_0 c d
  · exact semantic_distance_rows_2_1 c d
  · exact semantic_distance_rows_2_2 c d
  · exact semantic_distance_rows_2_3 c d
  · exact semantic_distance_rows_2_4 c d
  · exact semantic_distance_rows_2_5 c d
  · exact semantic_distance_rows_2_6 c d
  · exact semantic_distance_rows_2_7 c d
private lemma distance_polynomial_entry_row_2 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 2 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_2_0 c d
  · exact distance_polynomial_entry_rows_2_1 c d
  · exact distance_polynomial_entry_rows_2_2 c d
  · exact distance_polynomial_entry_rows_2_3 c d
  · exact distance_polynomial_entry_rows_2_4 c d
  · exact distance_polynomial_entry_rows_2_5 c d
  · exact distance_polynomial_entry_rows_2_6 c d
  · exact distance_polynomial_entry_rows_2_7 c d
private lemma diameter_row_3 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_3_0 c d
  · exact diameter_rows_3_1 c d
  · exact diameter_rows_3_2 c d
  · exact diameter_rows_3_3 c d
  · exact diameter_rows_3_4 c d
  · exact diameter_rows_3_5 c d
  · exact diameter_rows_3_6 c d
  · exact diameter_rows_3_7 c d
private lemma semantic_distance_row_3 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 3 c) (coordVertex s d) =
      Dcert (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_3_0 c d
  · exact semantic_distance_rows_3_1 c d
  · exact semantic_distance_rows_3_2 c d
  · exact semantic_distance_rows_3_3 c d
  · exact semantic_distance_rows_3_4 c d
  · exact semantic_distance_rows_3_5 c d
  · exact semantic_distance_rows_3_6 c d
  · exact semantic_distance_rows_3_7 c d
private lemma distance_polynomial_entry_row_3 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 3 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_3_0 c d
  · exact distance_polynomial_entry_rows_3_1 c d
  · exact distance_polynomial_entry_rows_3_2 c d
  · exact distance_polynomial_entry_rows_3_3 c d
  · exact distance_polynomial_entry_rows_3_4 c d
  · exact distance_polynomial_entry_rows_3_5 c d
  · exact distance_polynomial_entry_rows_3_6 c d
  · exact distance_polynomial_entry_rows_3_7 c d
private lemma diameter_row_4 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_4_0 c d
  · exact diameter_rows_4_1 c d
  · exact diameter_rows_4_2 c d
  · exact diameter_rows_4_3 c d
  · exact diameter_rows_4_4 c d
  · exact diameter_rows_4_5 c d
  · exact diameter_rows_4_6 c d
  · exact diameter_rows_4_7 c d
private lemma semantic_distance_row_4 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 4 c) (coordVertex s d) =
      Dcert (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_4_0 c d
  · exact semantic_distance_rows_4_1 c d
  · exact semantic_distance_rows_4_2 c d
  · exact semantic_distance_rows_4_3 c d
  · exact semantic_distance_rows_4_4 c d
  · exact semantic_distance_rows_4_5 c d
  · exact semantic_distance_rows_4_6 c d
  · exact semantic_distance_rows_4_7 c d
private lemma distance_polynomial_entry_row_4 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 4 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_4_0 c d
  · exact distance_polynomial_entry_rows_4_1 c d
  · exact distance_polynomial_entry_rows_4_2 c d
  · exact distance_polynomial_entry_rows_4_3 c d
  · exact distance_polynomial_entry_rows_4_4 c d
  · exact distance_polynomial_entry_rows_4_5 c d
  · exact distance_polynomial_entry_rows_4_6 c d
  · exact distance_polynomial_entry_rows_4_7 c d
private lemma diameter_row_5 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_5_0 c d
  · exact diameter_rows_5_1 c d
  · exact diameter_rows_5_2 c d
  · exact diameter_rows_5_3 c d
  · exact diameter_rows_5_4 c d
  · exact diameter_rows_5_5 c d
  · exact diameter_rows_5_6 c d
  · exact diameter_rows_5_7 c d
private lemma semantic_distance_row_5 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 5 c) (coordVertex s d) =
      Dcert (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_5_0 c d
  · exact semantic_distance_rows_5_1 c d
  · exact semantic_distance_rows_5_2 c d
  · exact semantic_distance_rows_5_3 c d
  · exact semantic_distance_rows_5_4 c d
  · exact semantic_distance_rows_5_5 c d
  · exact semantic_distance_rows_5_6 c d
  · exact semantic_distance_rows_5_7 c d
private lemma distance_polynomial_entry_row_5 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 5 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_5_0 c d
  · exact distance_polynomial_entry_rows_5_1 c d
  · exact distance_polynomial_entry_rows_5_2 c d
  · exact distance_polynomial_entry_rows_5_3 c d
  · exact distance_polynomial_entry_rows_5_4 c d
  · exact distance_polynomial_entry_rows_5_5 c d
  · exact distance_polynomial_entry_rows_5_6 c d
  · exact distance_polynomial_entry_rows_5_7 c d
private lemma diameter_row_6 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_6_0 c d
  · exact diameter_rows_6_1 c d
  · exact diameter_rows_6_2 c d
  · exact diameter_rows_6_3 c d
  · exact diameter_rows_6_4 c d
  · exact diameter_rows_6_5 c d
  · exact diameter_rows_6_6 c d
  · exact diameter_rows_6_7 c d
private lemma semantic_distance_row_6 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 6 c) (coordVertex s d) =
      Dcert (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_6_0 c d
  · exact semantic_distance_rows_6_1 c d
  · exact semantic_distance_rows_6_2 c d
  · exact semantic_distance_rows_6_3 c d
  · exact semantic_distance_rows_6_4 c d
  · exact semantic_distance_rows_6_5 c d
  · exact semantic_distance_rows_6_6 c d
  · exact semantic_distance_rows_6_7 c d
private lemma distance_polynomial_entry_row_6 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 6 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_6_0 c d
  · exact distance_polynomial_entry_rows_6_1 c d
  · exact distance_polynomial_entry_rows_6_2 c d
  · exact distance_polynomial_entry_rows_6_3 c d
  · exact distance_polynomial_entry_rows_6_4 c d
  · exact distance_polynomial_entry_rows_6_5 c d
  · exact distance_polynomial_entry_rows_6_6 c d
  · exact distance_polynomial_entry_rows_6_7 c d
private lemma diameter_row_7 (s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_7_0 c d
  · exact diameter_rows_7_1 c d
  · exact diameter_rows_7_2 c d
  · exact diameter_rows_7_3 c d
  · exact diameter_rows_7_4 c d
  · exact diameter_rows_7_5 c d
  · exact diameter_rows_7_6 c d
  · exact diameter_rows_7_7 c d
private lemma semantic_distance_row_7 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 7 c) (coordVertex s d) =
      Dcert (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_7_0 c d
  · exact semantic_distance_rows_7_1 c d
  · exact semantic_distance_rows_7_2 c d
  · exact semantic_distance_rows_7_3 c d
  · exact semantic_distance_rows_7_4 c d
  · exact semantic_distance_rows_7_5 c d
  · exact semantic_distance_rows_7_6 c d
  · exact semantic_distance_rows_7_7 c d
private lemma distance_polynomial_entry_row_7 (s : Fin 8) (c d : Fin 5) :
    D (coordVertex 7 c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact distance_polynomial_entry_rows_7_0 c d
  · exact distance_polynomial_entry_rows_7_1 c d
  · exact distance_polynomial_entry_rows_7_2 c d
  · exact distance_polynomial_entry_rows_7_3 c d
  · exact distance_polynomial_entry_rows_7_4 c d
  · exact distance_polynomial_entry_rows_7_5 c d
  · exact distance_polynomial_entry_rows_7_6 c d
  · exact distance_polynomial_entry_rows_7_7 c d

private lemma diameter_coord (r s : Fin 8) (c d : Fin 5) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact diameter_row_0 s c d
  · exact diameter_row_1 s c d
  · exact diameter_row_2 s c d
  · exact diameter_row_3 s c d
  · exact diameter_row_4 s c d
  · exact diameter_row_5 s c d
  · exact diameter_row_6 s c d
  · exact diameter_row_7 s c d

theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v
  rw [← coordVertex_surj u, ← coordVertex_surj v]
  exact diameter_coord _ _ _ _

set_option maxRecDepth 10000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 5 ∧ HasPathAtMostThree (0 : Vertex) 5 := by
  decide

private lemma semantic_distance_coord (r s : Fin 8) (c d : Fin 5) :
    D (coordVertex r c) (coordVertex s d) =
      Dcert (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact semantic_distance_row_0 s c d
  · exact semantic_distance_row_1 s c d
  · exact semantic_distance_row_2 s c d
  · exact semantic_distance_row_3 s c d
  · exact semantic_distance_row_4 s c d
  · exact semantic_distance_row_5 s c d
  · exact semantic_distance_row_6 s c d
  · exact semantic_distance_row_7 s c d

theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact semantic_distance_coord _ _ _ _

private lemma distance_polynomial_coord (r s : Fin 8) (c d : Fin 5) :
    D (coordVertex r c) (coordVertex s d) =
      ((3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
        - (2 : ℤ) • A - A * A) (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact distance_polynomial_entry_row_0 s c d
  · exact distance_polynomial_entry_row_1 s c d
  · exact distance_polynomial_entry_row_2 s c d
  · exact distance_polynomial_entry_row_3 s c d
  · exact distance_polynomial_entry_row_4 s c d
  · exact distance_polynomial_entry_row_5 s c d
  · exact distance_polynomial_entry_row_6 s c d
  · exact distance_polynomial_entry_row_7 s c d

theorem distance_polynomial :
    D = (3 : ℤ) • J + (3 : ℤ) • (1 : Matrix Vertex Vertex ℤ)
      - (2 : ℤ) • A - A * A := by
  ext i j
  rw [← coordVertex_surj i, ← coordVertex_surj j]
  exact distance_polynomial_coord _ _ _ _

end Wow284.Induced40
