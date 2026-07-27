import Wow284.Induced42.Finite0
import Wow284.Induced42.Finite1
import Wow284.Induced42.Finite2
import Wow284.Induced42.Finite3
import Wow284.Induced42.Finite4
import Wow284.Induced42.Finite5
import Wow284.Induced42.Finite6
/-! Assembly of exact degree, dual-degree, diameter, and distance certificates. -/
namespace Wow284.Induced42
private lemma degree_coord (r : Fin 7) (c : Fin 6) :
    degree (coordVertex r c) = 6 := by
  fin_cases r
  · exact degree_range_row_0 c
  · exact degree_range_row_1 c
  · exact degree_range_row_2 c
  · exact degree_range_row_3 c
  · exact degree_range_row_4 c
  · exact degree_range_row_5 c
  · exact degree_range_row_6 c
theorem degree_six (v : Vertex) : degree v = 6 := by
  rw [← coordVertex_surj v]; exact degree_coord _ _
theorem degree_positive (v : Vertex) : 0 < degree v := by
  rw [degree_six v]
  omega

theorem degree_profile : (Finset.univ.filter fun v : Vertex => degree v = 6).card = 42 := by decide
private lemma dual_bound_nat_coord (r : Fin 7) (c : Fin 6) :
    6 * degree (coordVertex r c) ≤
      1 * neighborDegreeSum (coordVertex r c) := by
  fin_cases r
  · exact dual_bound_nat_row_0 c
  · exact dual_bound_nat_row_1 c
  · exact dual_bound_nat_row_2 c
  · exact dual_bound_nat_row_3 c
  · exact dual_bound_nat_row_4 c
  · exact dual_bound_nat_row_5 c
  · exact dual_bound_nat_row_6 c
private theorem dual_bound_nat (v : Vertex) :
    6 * degree v ≤ 1 * neighborDegreeSum v := by
  rw [← coordVertex_surj v]
  exact dual_bound_nat_coord _ _
theorem dual_degree_lower_bound (v : Vertex) : (6 : ℚ) / 1 ≤ dualDegree v := by
  unfold dualDegree
  have hdegree : (0 : ℚ) < (degree v : ℚ) := by
    exact_mod_cast degree_positive v
  apply (div_le_div_iff₀ (by norm_num : (0 : ℚ) < 1) hdegree).2
  have hbound := dual_bound_nat v
  have hbound' :
      6 * degree v ≤ neighborDegreeSum v * 1 := by
    simpa [mul_comm] using hbound
  exact_mod_cast hbound'
private lemma dual_degree_attained_data :
    degree (0 : Vertex) = 6 ∧
      neighborDegreeSum (0 : Vertex) = 36 := by decide
theorem dual_degree_attained : ∃ v : Vertex, dualDegree v = (6 : ℚ) / 1 := by
  refine ⟨0, ?_⟩
  rcases dual_degree_attained_data with ⟨hdegree, hsum⟩
  norm_num [dualDegree, hdegree, hsum]

private lemma diameter_row_0 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_0_0 c d
  · exact diameter_rows_0_1 c d
  · exact diameter_rows_0_2 c d
  · exact diameter_rows_0_3 c d
  · exact diameter_rows_0_4 c d
  · exact diameter_rows_0_5 c d
  · exact diameter_rows_0_6 c d
private lemma semantic_distance_row_0 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 0 c) (coordVertex s d) = Dcert (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_0_0 c d
  · exact semantic_distance_rows_0_1 c d
  · exact semantic_distance_rows_0_2 c d
  · exact semantic_distance_rows_0_3 c d
  · exact semantic_distance_rows_0_4 c d
  · exact semantic_distance_rows_0_5 c d
  · exact semantic_distance_rows_0_6 c d
private lemma diameter_row_1 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_1_0 c d
  · exact diameter_rows_1_1 c d
  · exact diameter_rows_1_2 c d
  · exact diameter_rows_1_3 c d
  · exact diameter_rows_1_4 c d
  · exact diameter_rows_1_5 c d
  · exact diameter_rows_1_6 c d
private lemma semantic_distance_row_1 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 1 c) (coordVertex s d) = Dcert (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_1_0 c d
  · exact semantic_distance_rows_1_1 c d
  · exact semantic_distance_rows_1_2 c d
  · exact semantic_distance_rows_1_3 c d
  · exact semantic_distance_rows_1_4 c d
  · exact semantic_distance_rows_1_5 c d
  · exact semantic_distance_rows_1_6 c d
private lemma diameter_row_2 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_2_0 c d
  · exact diameter_rows_2_1 c d
  · exact diameter_rows_2_2 c d
  · exact diameter_rows_2_3 c d
  · exact diameter_rows_2_4 c d
  · exact diameter_rows_2_5 c d
  · exact diameter_rows_2_6 c d
private lemma semantic_distance_row_2 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 2 c) (coordVertex s d) = Dcert (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_2_0 c d
  · exact semantic_distance_rows_2_1 c d
  · exact semantic_distance_rows_2_2 c d
  · exact semantic_distance_rows_2_3 c d
  · exact semantic_distance_rows_2_4 c d
  · exact semantic_distance_rows_2_5 c d
  · exact semantic_distance_rows_2_6 c d
private lemma diameter_row_3 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_3_0 c d
  · exact diameter_rows_3_1 c d
  · exact diameter_rows_3_2 c d
  · exact diameter_rows_3_3 c d
  · exact diameter_rows_3_4 c d
  · exact diameter_rows_3_5 c d
  · exact diameter_rows_3_6 c d
private lemma semantic_distance_row_3 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 3 c) (coordVertex s d) = Dcert (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_3_0 c d
  · exact semantic_distance_rows_3_1 c d
  · exact semantic_distance_rows_3_2 c d
  · exact semantic_distance_rows_3_3 c d
  · exact semantic_distance_rows_3_4 c d
  · exact semantic_distance_rows_3_5 c d
  · exact semantic_distance_rows_3_6 c d
private lemma diameter_row_4 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_4_0 c d
  · exact diameter_rows_4_1 c d
  · exact diameter_rows_4_2 c d
  · exact diameter_rows_4_3 c d
  · exact diameter_rows_4_4 c d
  · exact diameter_rows_4_5 c d
  · exact diameter_rows_4_6 c d
private lemma semantic_distance_row_4 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 4 c) (coordVertex s d) = Dcert (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_4_0 c d
  · exact semantic_distance_rows_4_1 c d
  · exact semantic_distance_rows_4_2 c d
  · exact semantic_distance_rows_4_3 c d
  · exact semantic_distance_rows_4_4 c d
  · exact semantic_distance_rows_4_5 c d
  · exact semantic_distance_rows_4_6 c d
private lemma diameter_row_5 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_5_0 c d
  · exact diameter_rows_5_1 c d
  · exact diameter_rows_5_2 c d
  · exact diameter_rows_5_3 c d
  · exact diameter_rows_5_4 c d
  · exact diameter_rows_5_5 c d
  · exact diameter_rows_5_6 c d
private lemma semantic_distance_row_5 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 5 c) (coordVertex s d) = Dcert (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_5_0 c d
  · exact semantic_distance_rows_5_1 c d
  · exact semantic_distance_rows_5_2 c d
  · exact semantic_distance_rows_5_3 c d
  · exact semantic_distance_rows_5_4 c d
  · exact semantic_distance_rows_5_5 c d
  · exact semantic_distance_rows_5_6 c d
private lemma diameter_row_6 (s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact diameter_rows_6_0 c d
  · exact diameter_rows_6_1 c d
  · exact diameter_rows_6_2 c d
  · exact diameter_rows_6_3 c d
  · exact diameter_rows_6_4 c d
  · exact diameter_rows_6_5 c d
  · exact diameter_rows_6_6 c d
private lemma semantic_distance_row_6 (s : Fin 7) (c d : Fin 6) :
    D (coordVertex 6 c) (coordVertex s d) = Dcert (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_6_0 c d
  · exact semantic_distance_rows_6_1 c d
  · exact semantic_distance_rows_6_2 c d
  · exact semantic_distance_rows_6_3 c d
  · exact semantic_distance_rows_6_4 c d
  · exact semantic_distance_rows_6_5 c d
  · exact semantic_distance_rows_6_6 c d
private lemma diameter_coord (r s : Fin 7) (c d : Fin 6) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact diameter_row_0 s c d
  · exact diameter_row_1 s c d
  · exact diameter_row_2 s c d
  · exact diameter_row_3 s c d
  · exact diameter_row_4 s c d
  · exact diameter_row_5 s c d
  · exact diameter_row_6 s c d
theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v; rw [← coordVertex_surj u, ← coordVertex_surj v]; exact diameter_coord _ _ _ _
set_option maxRecDepth 15000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 22 ∧ HasPathAtMostThree (0 : Vertex) 22 := by decide
private lemma semantic_distance_coord (r s : Fin 7) (c d : Fin 6) :
    D (coordVertex r c) (coordVertex s d) = Dcert (coordVertex r c) (coordVertex s d) := by
  fin_cases r
  · exact semantic_distance_row_0 s c d
  · exact semantic_distance_row_1 s c d
  · exact semantic_distance_row_2 s c d
  · exact semantic_distance_row_3 s c d
  · exact semantic_distance_row_4 s c d
  · exact semantic_distance_row_5 s c d
  · exact semantic_distance_row_6 s c d
theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j; rw [← coordVertex_surj i, ← coordVertex_surj j]; exact semantic_distance_coord _ _ _ _
end Wow284.Induced42
