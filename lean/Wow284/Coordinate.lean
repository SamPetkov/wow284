import Mathlib

/-!
# Symbolic coordinate model over `ZMod 5`

This is the proof-oriented form of the construction. It avoids large finite
enumerations: all common-neighbor arguments reduce to field arithmetic in
`ZMod 5`.
-/

namespace Wow284.Coordinate

abbrev F := ZMod 5
abbrev Vertex := Sum (F × F) (F × F)

def P (i j : F) : Vertex := Sum.inl (i, j)
def Q (k l : F) : Vertex := Sum.inr (k, l)

@[simp] theorem card_vertex : Fintype.card Vertex = 50 := by
  norm_num [Vertex, F]

def Adjacent : Vertex → Vertex → Prop
  | Sum.inl (i, j), Sum.inl (i', j') =>
      i = i' ∧ (j' = j + 1 ∨ j = j' + 1)
  | Sum.inr (k, l), Sum.inr (k', l') =>
      k = k' ∧ (l' = l + 2 ∨ l = l' + 2)
  | Sum.inl (i, j), Sum.inr (k, l) => l = i * k + j
  | Sum.inr (k, l), Sum.inl (i, j) => l = i * k + j

instance (u v : Vertex) : Decidable (Adjacent u v) := by
  cases u <;> cases v <;> simp only [Adjacent]
  all_goals infer_instance

theorem adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  cases u with
  | inl p =>
      rcases p with ⟨i, j⟩
      cases v with
      | inl p' =>
          rcases p' with ⟨i', j'⟩
          simp only [Adjacent]
          constructor <;> rintro ⟨h, hstep⟩
          · exact ⟨h.symm, hstep.symm⟩
          · exact ⟨h.symm, hstep.symm⟩
      | inr q => rfl
  | inr q =>
      rcases q with ⟨k, l⟩
      cases v with
      | inl p => rfl
      | inr q' =>
          rcases q' with ⟨k', l'⟩
          simp only [Adjacent]
          constructor <;> rintro ⟨h, hstep⟩
          · exact ⟨h.symm, hstep.symm⟩
          · exact ⟨h.symm, hstep.symm⟩

theorem adjacent_irrefl (v : Vertex) : ¬Adjacent v v := by
  cases v with
  | inl p =>
      rcases p with ⟨i, j⟩
      simp only [Adjacent, true_and]
      intro h
      rcases h with h | h
      all_goals
        have hone : (1 : F) = 0 := by
          apply add_left_cancel (a := j)
          simpa using h.symm
        exact (by decide : (1 : F) ≠ 0) hone
  | inr q =>
      rcases q with ⟨k, l⟩
      simp only [Adjacent, true_and]
      intro h
      rcases h with h | h
      all_goals
        have htwo : (2 : F) = 0 := by
          apply add_left_cancel (a := l)
          simpa using h.symm
        exact (by decide : (2 : F) ≠ 0) htwo

/-- Every field element is one of the five signed representatives used in
the mixed common-neighbor argument. -/
theorem zmod5_partition (x : F) :
    x = 0 ∨ x = 1 ∨ x = -1 ∨ x = 2 ∨ x = -2 := by
  letI : Fact (Nat.Prime 5) := ⟨by norm_num⟩
  have hp : x ^ 5 = x := by simpa using ZMod.pow_card x
  have hz : x * (x - 1) * (x + 1) * (x - 2) * (x + 2) = 0 := by
    calc
      _ = x ^ 5 - x := by
        ring_nf
        have h5 : (5 : F) = 0 := by decide
        have h4 : (4 : F) = -1 := by decide
        rw [h5, h4]
        ring
      _ = 0 := sub_eq_zero.mpr hp
  rcases mul_eq_zero.mp hz with h | h
  · rcases mul_eq_zero.mp h with h | h
    · rcases mul_eq_zero.mp h with h | h
      · rcases mul_eq_zero.mp h with h | h
        · exact Or.inl h
        · exact Or.inr (Or.inl (sub_eq_zero.mp h))
      · exact Or.inr (Or.inr (Or.inl (eq_neg_of_add_eq_zero_left h)))
    · exact Or.inr (Or.inr (Or.inr (Or.inl (sub_eq_zero.mp h))))
  · exact Or.inr (Or.inr (Or.inr (Or.inr (eq_neg_of_add_eq_zero_left h))))

theorem common_neighbors_PQ (i j k l : F)
    (hne : ¬Adjacent (P i j) (Q k l)) :
    ∃! w : Vertex, Adjacent (P i j) w ∧ Adjacent (Q k l) w := by
  let d : F := l - i * k - j
  have hd0 : d ≠ 0 := by
    intro hd
    apply hne
    simp only [P, Q, Adjacent]
    dsimp [d] at hd
    linear_combination hd
  rcases zmod5_partition d with hd | hd | hd | hd | hd
  · exact (hd0 hd).elim
  · refine ⟨P i (j + 1), ?_, ?_⟩
    · constructor
      · simp [P, Adjacent]
      · simp only [P, Q, Adjacent]
        dsimp [d] at hd
        linear_combination hd
    · intro y hy
      cases y with
      | inl p =>
          rcases p with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.1 with ⟨ha, hb | hb⟩
          · subst a
            simp only [Sum.inl.injEq, Prod.mk.injEq, true_and]
            exact hb
          · subst a
            have hbad : (-2 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 + hb
            exact ((by decide : (-2 : F) ≠ 0) hbad).elim
      | inr q =>
          rcases q with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.2 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (-3 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 + hb
            exact ((by decide : (-3 : F) ≠ 0) hbad).elim
          · subst a
            have hbad : (1 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 - hb
            exact ((by decide : (1 : F) ≠ 0) hbad).elim
  · refine ⟨P i (j - 1), ?_, ?_⟩
    · constructor
      · simp only [P, Adjacent, true_and]
        right
        ring
      · simp only [P, Q, Adjacent]
        dsimp [d] at hd
        linear_combination hd
    · intro y hy
      cases y with
      | inl p =>
          rcases p with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.1 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (2 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 - hb
            exact ((by decide : (2 : F) ≠ 0) hbad).elim
          · subst a
            simp only [Sum.inl.injEq, Prod.mk.injEq, true_and]
            rw [hb]
            ring
      | inr q =>
          rcases q with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.2 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (-1 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 + hb
            exact ((by decide : (-1 : F) ≠ 0) hbad).elim
          · subst a
            have hbad : (3 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 - hb
            exact ((by decide : (3 : F) ≠ 0) hbad).elim
  · refine ⟨Q k (l - 2), ?_, ?_⟩
    · constructor
      · simp only [P, Q, Adjacent]
        dsimp [d] at hd
        linear_combination hd
      · simp only [Q, Adjacent, true_and]
        right
        ring
    · intro y hy
      cases y with
      | inl p =>
          rcases p with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.1 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (-1 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 - hb
            exact ((by decide : (-1 : F) ≠ 0) hbad).elim
          · subst a
            have hbad : (-3 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 + hb
            exact ((by decide : (-3 : F) ≠ 0) hbad).elim
      | inr q =>
          rcases q with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.2 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (-4 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 + hb
            exact ((by decide : (-4 : F) ≠ 0) hbad).elim
          · subst a
            simp only [Sum.inr.injEq, Prod.mk.injEq, true_and]
            rw [hb]
            ring
  · refine ⟨Q k (l + 2), ?_, ?_⟩
    · constructor
      · simp only [P, Q, Adjacent]
        dsimp [d] at hd
        linear_combination hd
      · simp [Q, Adjacent]
    · intro y hy
      cases y with
      | inl p =>
          rcases p with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.1 with ⟨ha, hb | hb⟩
          · subst a
            have hbad : (3 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 - hb
            exact ((by decide : (3 : F) ≠ 0) hbad).elim
          · subst a
            have hbad : (1 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.2 + hb
            exact ((by decide : (1 : F) ≠ 0) hbad).elim
      | inr q =>
          rcases q with ⟨a, b⟩
          simp only [P, Q, Adjacent] at hy ⊢
          rcases hy.2 with ⟨ha, hb | hb⟩
          · subst a
            simp only [Sum.inr.injEq, Prod.mk.injEq, true_and]
            exact hb
          · subst a
            have hbad : (4 : F) = 0 := by
              dsimp [d] at hd
              linear_combination hd - hy.1 - hb
            exact ((by decide : (4 : F) ≠ 0) hbad).elim

end Wow284.Coordinate
