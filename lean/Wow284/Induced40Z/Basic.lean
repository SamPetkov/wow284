import Wow284.Basic

/-!
# The explicit 40-vertex WOW-284 counterexample

The graph is an induced subgraph of a previously verified coordinate graph.
Simplicity and exclusion of triangles and 4-cycles are inherited. Generated
finite certificates prove the degree data, diameter three, and semantic BFS
distance matrix; denominator-cleared integer LDL data prove the strict spectral
inequality.
-/
namespace Wow284.Induced40Z
open scoped BigOperators
abbrev Vertex := Fin 40

/-- Hoffman--Singleton labels retained after deleting P_(0,0), P_(0,1), P_(0,2), P_(0,3), P_(0,4), P_(1,0), Q_(0,0), Q_(0,2), Q_(1,1), Q_(1,4). -/
def embed : Vertex → Wow284.Vertex :=
  ![6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 29, 30, 32, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]

set_option maxRecDepth 10000 in
lemma embed_injective : Function.Injective embed := by
  decide

lemma embed_ne {u v : Vertex} (h : u ≠ v) : embed u ≠ embed v :=
  fun huv => h (embed_injective huv)

def Adjacent (u v : Vertex) : Prop := Wow284.Adjacent (embed u) (embed v)
instance (u v : Vertex) : Decidable (Adjacent u v) := by unfold Adjacent; infer_instance
lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using Wow284.adjacent_symm (embed u) (embed v)
lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using Wow284.adjacent_irrefl (embed v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card
def neighborDegreeSum (v : Vertex) : Nat := ∑ u ∈ neighbors v, degree u
def dualDegree (v : Vertex) : ℚ :=
  (neighborDegreeSum v : ℚ) / (degree v : ℚ)

def coordVertex (r : Fin 8) (c : Fin 5) : Vertex :=
  ⟨5 * r.val + c.val, by omega⟩
lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / 5, by omega⟩
      ⟨v.val % 5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext; simp [coordVertex]; omega

theorem no_triangle : ∀ a b c : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro u v w h
  rcases h with ⟨huv, huw, hvw, euv, evw, ewu⟩
  apply Wow284.no_triangle (embed u) (embed v) (embed w)
  exact ⟨embed_ne huv, embed_ne huw, embed_ne hvw, euv, evw, ewu⟩

theorem no_four_cycle : ∀ a b c d : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro u v w z h
  rcases h with ⟨huv, huw, huz, hvw, hvz, hwz, euv, evw, ewz, ezu⟩
  apply Wow284.no_four_cycle (embed u) (embed v) (embed w) (embed z)
  exact ⟨embed_ne huv, embed_ne huw, embed_ne huz, embed_ne hvw, embed_ne hvz, embed_ne hwz,
    euv, evw, ewz, ezu⟩

theorem explicit_five_cycle :
    Adjacent (0 : Vertex) 1 ∧ Adjacent (1 : Vertex) 2 ∧
    Adjacent (2 : Vertex) 20 ∧ Adjacent (20 : Vertex) 19 ∧
    Adjacent (19 : Vertex) 0 := by decide

def HasPathAtMostTwo (u v : Vertex) : Prop :=
  u = v ∨ Adjacent u v ∨ ∃ w, Adjacent u w ∧ Adjacent w v
def HasPathAtMostThree (u v : Vertex) : Prop :=
  HasPathAtMostTwo u v ∨ ∃ w z, Adjacent u w ∧ Adjacent w z ∧ Adjacent z v
instance (u v : Vertex) : Decidable (HasPathAtMostTwo u v) := by unfold HasPathAtMostTwo; infer_instance
instance (u v : Vertex) : Decidable (HasPathAtMostThree u v) := by unfold HasPathAtMostThree; infer_instance

open Matrix
def D : Matrix Vertex Vertex ℤ := fun u v =>
  if u = v then 0 else if Adjacent u v then 1
  else if ∃ w, Adjacent u w ∧ Adjacent w v then 2 else 3
end Wow284.Induced40Z
