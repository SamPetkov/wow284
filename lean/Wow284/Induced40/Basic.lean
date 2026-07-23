import Wow284.Basic

/-!
# The induced 40-vertex counterexample

This module reuses the kernel-checked 50-vertex coordinate graph and defines
its induced 40-vertex subgraph by an explicit embedding.  The finite degree,
diameter, distance-matrix, and diagonalization certificates are generated in
separate sharded modules.
-/

namespace Wow284.Induced40

abbrev Vertex := Fin 40

/-- The surviving old labels are 5,...,24 and 30,...,49. -/
def embed (v : Vertex) : Wow284.Vertex :=
  if h : v.val < 20 then
    ⟨v.val + 5, by omega⟩
  else
    ⟨v.val + 10, by omega⟩

lemma embed_injective : Function.Injective embed := by
  intro u v huv
  apply Fin.ext
  simp only [embed] at huv
  split at huv <;> split at huv <;> simp_all <;> omega

lemma embed_ne {u v : Vertex} (h : u ≠ v) : embed u ≠ embed v :=
  fun huv => h (embed_injective huv)

/-- Adjacency is inherited from the 50-vertex graph. -/
def Adjacent (u v : Vertex) : Prop := Wow284.Adjacent (embed u) (embed v)

instance (u v : Vertex) : Decidable (Adjacent u v) := by
  unfold Adjacent
  infer_instance

lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using Wow284.adjacent_symm (embed u) (embed v)

lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using Wow284.adjacent_irrefl (embed v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card

def commonNeighborCount (u v : Vertex) : Nat :=
  (Finset.univ.filter fun w => Adjacent u w ∧ Adjacent v w).card

/-- Eight rows of five vertices, used by generated bounded certificates. -/
def coordVertex (r : Fin 8) (c : Fin 5) : Vertex :=
  ⟨5 * r.val + c.val, by omega⟩

lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 5, by omega⟩
      ⟨v.val % 5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext
  simp [coordVertex]
  omega

/-- Triangles cannot be created by taking an induced subgraph. -/
theorem no_triangle :
    ∀ a b c : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro a b c h
  rcases h with ⟨hab, hac, hbc, eab, ebc, eca⟩
  apply Wow284.no_triangle (embed a) (embed b) (embed c)
  exact ⟨embed_ne hab, embed_ne hac, embed_ne hbc, eab, ebc, eca⟩

/-- Four-cycles cannot be created by taking an induced subgraph. -/
theorem no_four_cycle :
    ∀ a b c d : Vertex,
      ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
        Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro a b c d h
  rcases h with ⟨hab, hac, had, hbc, hbd, hcd, eab, ebc, ecd, eda⟩
  apply Wow284.no_four_cycle (embed a) (embed b) (embed c) (embed d)
  exact ⟨embed_ne hab, embed_ne hac, embed_ne had, embed_ne hbc,
    embed_ne hbd, embed_ne hcd, eab, ebc, ecd, eda⟩

/-- Vertices 0,...,4 are the surviving `P_(1,*)` five-cycle. -/
theorem explicit_five_cycle :
    Adjacent (0 : Vertex) 1 ∧ Adjacent (1 : Vertex) 2 ∧
    Adjacent (2 : Vertex) 3 ∧ Adjacent (3 : Vertex) 4 ∧
    Adjacent (4 : Vertex) 0 := by
  decide

def HasPathAtMostTwo (u v : Vertex) : Prop :=
  u = v ∨ Adjacent u v ∨ ∃ w, Adjacent u w ∧ Adjacent w v

def HasPathAtMostThree (u v : Vertex) : Prop :=
  HasPathAtMostTwo u v ∨
    ∃ w z, Adjacent u w ∧ Adjacent w z ∧ Adjacent z v

instance (u v : Vertex) : Decidable (HasPathAtMostTwo u v) := by
  unfold HasPathAtMostTwo
  infer_instance

instance (u v : Vertex) : Decidable (HasPathAtMostThree u v) := by
  unfold HasPathAtMostThree
  infer_instance

open Matrix

def A : Matrix Vertex Vertex ℤ := fun u v => if Adjacent u v then 1 else 0

def J : Matrix Vertex Vertex ℤ := fun _ _ => 1

/-- Semantic distance matrix; the generated structural certificate proves that
all off-diagonal entries are the actual graph distances. -/
def D : Matrix Vertex Vertex ℤ := fun u v =>
  if u = v then 0
  else if Adjacent u v then 1
  else if ∃ w, Adjacent u w ∧ Adjacent w v then 2
  else 3

end Wow284.Induced40
