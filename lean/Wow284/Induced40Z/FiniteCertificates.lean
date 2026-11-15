import Wow284.Induced40Z.Finite0
import Wow284.Induced40Z.Finite1
import Wow284.Induced40Z.Finite2
import Wow284.Induced40Z.Finite3
import Wow284.Induced40Z.Finite4
import Wow284.Induced40Z.Finite5
import Wow284.Induced40Z.Finite6
import Wow284.Induced40Z.Finite7
/-! Assembly of exact degree, dual-degree, diameter, and distance certificates. -/
namespace Wow284.Induced40Z
private lemma degree_range_coord (r : Fin 8) (c : Fin 5) : degree (coordVertex r c) = 5 ∨ degree (coordVertex r c) = 6 ∨ degree (coordVertex r c) = 7 := by
  fin_cases r
  · exact degree_range_row_0 c
  · exact degree_range_row_1 c
  · exact degree_range_row_2 c
  · exact degree_range_row_3 c
  · exact degree_range_row_4 c
  · exact degree_range_row_5 c
  · exact degree_range_row_6 c
  · exact degree_range_row_7 c
theorem degree_range (v : Vertex) : degree v = 5 ∨ degree v = 6 ∨ degree v = 7 := by
  rw [← coordVertex_surj v]; exact degree_range_coord _ _
theorem degree_positive (v : Vertex) : 0 < degree v := by
  rcases degree_range v with h | h <;> omega

theorem degree_profile : (Finset.univ.filter fun v : Vertex => degree v = 5).card = 10 ∧
    (Finset.univ.filter fun v : Vertex => degree v = 6).card = 24 ∧
    (Finset.univ.filter fun v : Vertex => degree v = 7).card = 6 := by decide
private lemma dual_bound_nat_coord (r : Fin 8) (c : Fin 5) :
    39 * degree (coordVertex r c) ≤
      7 * neighborDegreeSum (coordVertex r c) := by
  fin_cases r
  · exact dual_bound_nat_row_0 c
  · exact dual_bound_nat_row_1 c
  · exact dual_bound_nat_row_2 c
  · exact dual_bound_nat_row_3 c
  · exact dual_bound_nat_row_4 c
  · exact dual_bound_nat_row_5 c
  · exact dual_bound_nat_row_6 c
  · exact dual_bound_nat_row_7 c
private theorem dual_bound_nat (v : Vertex) :
    39 * degree v ≤ 7 * neighborDegreeSum v := by
  rw [← coordVertex_surj v]
  exact dual_bound_nat_coord _ _
theorem dual_degree_lower_bound (v : Vertex) : (39 : ℚ) / 7 ≤ dualDegree v := by
  unfold dualDegree
  have hdegree : (0 : ℚ) < (degree v : ℚ) := by
    exact_mod_cast degree_positive v
  apply (div_le_div_iff₀ (by norm_num : (0 : ℚ) < 7) hdegree).2
  have hbound := dual_bound_nat v
  have hbound' :
      39 * degree v ≤ neighborDegreeSum v * 7 := by
    simpa [mul_comm] using hbound
  exact_mod_cast hbound'
private lemma dual_degree_attained_data :
    degree (5 : Vertex) = 7 ∧
      neighborDegreeSum (5 : Vertex) = 39 := by decide
theorem dual_degree_attained : ∃ v : Vertex, dualDegree v = (39 : ℚ) / 7 := by
  refine ⟨5, ?_⟩
  rcases dual_degree_attained_data with ⟨hdegree, hsum⟩
  norm_num [dualDegree, hdegree, hsum]

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
    D (coordVertex 0 c) (coordVertex s d) = Dcert (coordVertex 0 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_0_0 c d
  · exact semantic_distance_rows_0_1 c d
  · exact semantic_distance_rows_0_2 c d
  · exact semantic_distance_rows_0_3 c d
  · exact semantic_distance_rows_0_4 c d
  · exact semantic_distance_rows_0_5 c d
  · exact semantic_distance_rows_0_6 c d
  · exact semantic_distance_rows_0_7 c d
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
    D (coordVertex 1 c) (coordVertex s d) = Dcert (coordVertex 1 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_1_0 c d
  · exact semantic_distance_rows_1_1 c d
  · exact semantic_distance_rows_1_2 c d
  · exact semantic_distance_rows_1_3 c d
  · exact semantic_distance_rows_1_4 c d
  · exact semantic_distance_rows_1_5 c d
  · exact semantic_distance_rows_1_6 c d
  · exact semantic_distance_rows_1_7 c d
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
    D (coordVertex 2 c) (coordVertex s d) = Dcert (coordVertex 2 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_2_0 c d
  · exact semantic_distance_rows_2_1 c d
  · exact semantic_distance_rows_2_2 c d
  · exact semantic_distance_rows_2_3 c d
  · exact semantic_distance_rows_2_4 c d
  · exact semantic_distance_rows_2_5 c d
  · exact semantic_distance_rows_2_6 c d
  · exact semantic_distance_rows_2_7 c d
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
    D (coordVertex 3 c) (coordVertex s d) = Dcert (coordVertex 3 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_3_0 c d
  · exact semantic_distance_rows_3_1 c d
  · exact semantic_distance_rows_3_2 c d
  · exact semantic_distance_rows_3_3 c d
  · exact semantic_distance_rows_3_4 c d
  · exact semantic_distance_rows_3_5 c d
  · exact semantic_distance_rows_3_6 c d
  · exact semantic_distance_rows_3_7 c d
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
    D (coordVertex 4 c) (coordVertex s d) = Dcert (coordVertex 4 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_4_0 c d
  · exact semantic_distance_rows_4_1 c d
  · exact semantic_distance_rows_4_2 c d
  · exact semantic_distance_rows_4_3 c d
  · exact semantic_distance_rows_4_4 c d
  · exact semantic_distance_rows_4_5 c d
  · exact semantic_distance_rows_4_6 c d
  · exact semantic_distance_rows_4_7 c d
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
    D (coordVertex 5 c) (coordVertex s d) = Dcert (coordVertex 5 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_5_0 c d
  · exact semantic_distance_rows_5_1 c d
  · exact semantic_distance_rows_5_2 c d
  · exact semantic_distance_rows_5_3 c d
  · exact semantic_distance_rows_5_4 c d
  · exact semantic_distance_rows_5_5 c d
  · exact semantic_distance_rows_5_6 c d
  · exact semantic_distance_rows_5_7 c d
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
    D (coordVertex 6 c) (coordVertex s d) = Dcert (coordVertex 6 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_6_0 c d
  · exact semantic_distance_rows_6_1 c d
  · exact semantic_distance_rows_6_2 c d
  · exact semantic_distance_rows_6_3 c d
  · exact semantic_distance_rows_6_4 c d
  · exact semantic_distance_rows_6_5 c d
  · exact semantic_distance_rows_6_6 c d
  · exact semantic_distance_rows_6_7 c d
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
    D (coordVertex 7 c) (coordVertex s d) = Dcert (coordVertex 7 c) (coordVertex s d) := by
  fin_cases s
  · exact semantic_distance_rows_7_0 c d
  · exact semantic_distance_rows_7_1 c d
  · exact semantic_distance_rows_7_2 c d
  · exact semantic_distance_rows_7_3 c d
  · exact semantic_distance_rows_7_4 c d
  · exact semantic_distance_rows_7_5 c d
  · exact semantic_distance_rows_7_6 c d
  · exact semantic_distance_rows_7_7 c d
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
  intro u v; rw [← coordVertex_surj u, ← coordVertex_surj v]; exact diameter_coord _ _ _ _
set_option maxRecDepth 15000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo (0 : Vertex) 3 ∧ HasPathAtMostThree (0 : Vertex) 3 := by decide
private lemma semantic_distance_coord (r s : Fin 8) (c d : Fin 5) :
    D (coordVertex r c) (coordVertex s d) = Dcert (coordVertex r c) (coordVertex s d) := by
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
  ext i j; rw [← coordVertex_surj i, ← coordVertex_surj j]; exact semantic_distance_coord _ _ _ _
end Wow284.Induced40Z
