#!/usr/bin/env python3
"""Shared exact graph specifications and Lean renderers for orders 39 and 42."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import sys
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))
from common_graphs import graph40, graph42, induced, distance_matrix, dual_degrees

ROOT = Path(__file__).resolve().parents[1]

@dataclass(frozen=True)
class Spec:
    order: int; namespace: str; graph: tuple[frozenset[int], ...]
    labels: tuple[tuple[str,int,int], ...]; row_count: int; col_count: int
    shift_scale: int; shift_diag: int; pad_order: int; pad_rows: int
    degree_values: tuple[int,...]; degree_profile: tuple[tuple[int,int],...]
    dual_p: int; dual_q: int; attained_vertex: int
    dist3_pair: tuple[int,int]; five_cycle: tuple[int,int,int,int,int]
    base_import: str; embed_code: str; inherited_prefix: str


def graph39():
    g40, labels40 = graph40()
    return induced(g40, labels40, {("P", 1, 0)})


def spec39() -> Spec:
    graph, labels = graph39()
    embed = '''def embed40 (v : Vertex) : Wow284.Induced40.Vertex :=
  ⟨v.val + 1, by omega⟩

lemma embed40_injective : Function.Injective embed40 := by
  intro u v h
  apply Fin.ext
  simpa [embed40] using congrArg Fin.val h

lemma embed40_ne {u v : Vertex} (h : u ≠ v) : embed40 u ≠ embed40 v :=
  fun huv => h (embed40_injective huv)
'''
    return Spec(39, "Induced39", graph, labels, 13, 3, 6, 35, 40, 8,
        (5, 6), ((5, 6), (6, 33)), 35, 6, 1, (0, 3), (4, 5, 6, 7, 8),
        "Wow284.Induced40.Basic", embed, "Wow284.Induced40")


def spec42() -> Spec:
    graph, labels = graph42()
    old = [2, 3] + list(range(5, 25)) + list(range(26, 30)) + \
        list(range(31, 35)) + list(range(36, 40)) + \
        list(range(41, 45)) + list(range(46, 50))
    assert len(old) == 42
    embed = '''/-- Old Hoffman--Singleton labels retained after deleting `P_(0,0)`
and its seven neighbours: `0, 1, 4, 25, 30, 35, 40, 45`. -/
def embed : Vertex → Wow284.Vertex :=
  ![''' + ", ".join(map(str, old)) + ''']

set_option maxRecDepth 10000 in
lemma embed_injective : Function.Injective embed := by
  decide

lemma embed_ne {u v : Vertex} (h : u ≠ v) : embed u ≠ embed v :=
  fun huv => h (embed_injective huv)
'''
    return Spec(42, "Induced42", graph, labels, 7, 6, 1, 6, 45, 9,
        (6,), ((6, 42),), 6, 1, 0, (0, 22), (2, 3, 4, 5, 6),
        "Wow284.Basic", embed, "Wow284")


def lean_rat(value: sp.Expr) -> str:
    value = sp.Rational(value)
    return str(int(value.p)) if value.q == 1 else f"(({int(value.p)} : ℚ) / {int(value.q)})"


def lean_int_matrix(name: str, matrix: sp.Matrix, typ: str = "Vertex") -> str:
    if any(sp.denom(value) != 1 for value in matrix):
        raise AssertionError(f"{name} has a non-integral entry")
    rows = [", ".join(str(int(matrix[i,j])) for j in range(matrix.cols)) for i in range(matrix.rows)]
    return f"def {name} : Matrix {typ} {typ} ℤ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def lean_rat_matrix(name: str, matrix: sp.Matrix, typ: str) -> str:
    rows = [", ".join(lean_rat(matrix[i,j]) for j in range(matrix.cols)) for i in range(matrix.rows)]
    return f"def {name} : Matrix {typ} {typ} ℚ := !![\n    " + ";\n    ".join(rows) + "\n  ]\n"


def verify_spec(spec: Spec) -> None:
    assert len(spec.graph) == spec.order
    assert min(dual_degrees(spec.graph)) == sp.Rational(spec.dual_p, spec.dual_q)
    distance = distance_matrix(spec.graph)
    assert max(distance) == 3
    shifted = spec.shift_scale * distance + spec.shift_diag * sp.eye(spec.order)
    _, delta = shifted.LDLdecomposition(hermitian=True)
    assert all(delta[i,i] > 0 for i in range(spec.order))


def basic(spec: Spec) -> str:
    ns, pre = spec.namespace, spec.inherited_prefix
    emb = "embed40" if ns == "Induced39" else "embed"
    ne = "embed40_ne" if ns == "Induced39" else "embed_ne"
    a,b,c,d,e = spec.five_cycle
    return f'''import {spec.base_import}

/-!
# The explicit {spec.order}-vertex WOW-284 counterexample

The graph is an induced subgraph of a previously verified coordinate graph.
Simplicity and exclusion of triangles and 4-cycles are inherited. Generated
finite certificates prove the degree data, diameter three, and semantic BFS
distance matrix; denominator-cleared integer LDL data prove the strict spectral
inequality.
-/
namespace Wow284.{ns}
open scoped BigOperators
abbrev Vertex := Fin {spec.order}

{spec.embed_code}
def Adjacent (u v : Vertex) : Prop := {pre}.Adjacent ({emb} u) ({emb} v)
instance (u v : Vertex) : Decidable (Adjacent u v) := by unfold Adjacent; infer_instance
lemma adjacent_symm (u v : Vertex) : Adjacent u v ↔ Adjacent v u := by
  simpa [Adjacent] using {pre}.adjacent_symm ({emb} u) ({emb} v)
lemma adjacent_irrefl (v : Vertex) : ¬ Adjacent v v := by
  simpa [Adjacent] using {pre}.adjacent_irrefl ({emb} v)

def neighbors (v : Vertex) : Finset Vertex := Finset.univ.filter (Adjacent v)
def degree (v : Vertex) : Nat := (neighbors v).card
def neighborDegreeSum (v : Vertex) : Nat := ∑ u ∈ neighbors v, degree u
def dualDegree (v : Vertex) : ℚ :=
  (neighborDegreeSum v : ℚ) / (degree v : ℚ)

def coordVertex (r : Fin {spec.row_count}) (c : Fin {spec.col_count}) : Vertex :=
  ⟨{spec.col_count} * r.val + c.val, by omega⟩
lemma coordVertex_surj (v : Vertex) :
    coordVertex ⟨v.val / {spec.col_count}, by omega⟩
      ⟨v.val % {spec.col_count}, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext; simp [coordVertex]; omega

theorem no_triangle : ∀ a b c : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ b ≠ c ∧ Adjacent a b ∧ Adjacent b c ∧ Adjacent c a) := by
  intro u v w h
  rcases h with ⟨huv, huw, hvw, euv, evw, ewu⟩
  apply {pre}.no_triangle ({emb} u) ({emb} v) ({emb} w)
  exact ⟨{ne} huv, {ne} huw, {ne} hvw, euv, evw, ewu⟩

theorem no_four_cycle : ∀ a b c d : Vertex,
    ¬(a ≠ b ∧ a ≠ c ∧ a ≠ d ∧ b ≠ c ∧ b ≠ d ∧ c ≠ d ∧
      Adjacent a b ∧ Adjacent b c ∧ Adjacent c d ∧ Adjacent d a) := by
  intro u v w z h
  rcases h with ⟨huv, huw, huz, hvw, hvz, hwz, euv, evw, ewz, ezu⟩
  apply {pre}.no_four_cycle ({emb} u) ({emb} v) ({emb} w) ({emb} z)
  exact ⟨{ne} huv, {ne} huw, {ne} huz, {ne} hvw, {ne} hvz, {ne} hwz,
    euv, evw, ewz, ezu⟩

theorem explicit_five_cycle :
    Adjacent ({a} : Vertex) {b} ∧ Adjacent ({b} : Vertex) {c} ∧
    Adjacent ({c} : Vertex) {d} ∧ Adjacent ({d} : Vertex) {e} ∧
    Adjacent ({e} : Vertex) {a} := by decide

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
end Wow284.{ns}
'''


def bridge(spec: Spec) -> str:
    n,a,b = spec.namespace,spec.shift_scale,spec.shift_diag
    return f'''import Wow284.{n}.FiniteCertificates
import Wow284.{n}.LDLData
import Mathlib.Analysis.Matrix.PosDef

/-! Exact positive-definiteness bridge for the order-{spec.order} graph. -/
namespace Wow284.{n}
open Matrix
def Dq : Matrix Vertex Vertex ℚ := D.map (Int.castRingHom ℚ)
theorem Mcore_eq_shifted_distance :
    Mcore = ({a} : ℚ) • Dq + ({b} : ℚ) • (1 : Matrix Vertex Vertex ℚ) := by
  rw [Mcore, Dq, semantic_distance_eq_Dcert]
  ext i j
  change ((({a} * Dcert i j + {b} * (if i = j then 1 else 0) : ℤ) : ℚ)) =
    ({a} : ℚ) * ((Dcert i j : ℤ) : ℚ) +
      ({b} : ℚ) * (if i = j then 1 else 0)
  by_cases h : i = j <;> simp [h, Int.cast_add, Int.cast_mul]

theorem deltaPad_posDef : DeltaPad.PosDef := Matrix.PosDef.diagonal pivotPad_positive
theorem lpad_isUnit : IsUnit Lpad := Matrix.isUnit_of_left_inverse lpad_left_inverse
theorem Mpad_posDef : Mpad.PosDef := by
  rw [← ldl_identity]
  rw [← Matrix.conjTranspose_eq_transpose_of_trivial]
  exact
    deltaPad_posDef.mul_mul_conjTranspose_same (Matrix.vecMul_injective_of_isUnit lpad_isUnit)
theorem Mcore_posDef : Mcore.PosDef := by
  rw [← Mpad_submatrix]; exact Mpad_posDef.submatrix embedPad_injective
theorem shifted_distance_posDef :
    (({a} : ℚ) • Dq + ({b} : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef := by
  rw [← Mcore_eq_shifted_distance]; exact Mcore_posDef

noncomputable def Dr : Matrix Vertex Vertex ℝ := D.map (Int.castRingHom ℝ)
private noncomputable def LpadR : Matrix PadVertex PadVertex ℝ := Lpad.map (Rat.castHom ℝ)
private noncomputable def DeltaPadR : Matrix PadVertex PadVertex ℝ := DeltaPad.map (Rat.castHom ℝ)
private noncomputable def MpadR : Matrix PadVertex PadVertex ℝ := Mpad.map (Rat.castHom ℝ)
private noncomputable def McoreR : Matrix Vertex Vertex ℝ := Mcore.map (Rat.castHom ℝ)
private noncomputable def LpadInvR : Matrix PadVertex PadVertex ℝ := LpadInv.map (Rat.castHom ℝ)
private theorem deltaPadR_eq : DeltaPadR = diagonal (fun i => (pivotPad i : ℝ)) := by
  ext i j
  change ((if i = j then pivotPad i else 0 : ℚ) : ℝ) =
    if i = j then (pivotPad i : ℝ) else 0
  by_cases h : i = j <;> simp [h]
private theorem pivotPadR_positive (i : PadVertex) : 0 < (pivotPad i : ℝ) := by
  exact_mod_cast pivotPad_positive i
private theorem deltaPadR_posDef : DeltaPadR.PosDef := by
  rw [deltaPadR_eq]; exact Matrix.PosDef.diagonal pivotPadR_positive
private theorem lpadR_left_inverse : LpadInvR * LpadR = (1 : Matrix PadVertex PadVertex ℝ) := by
  rw [LpadInvR, LpadR, ← Matrix.map_mul, lpad_left_inverse]; simp
private theorem lpadR_isUnit : IsUnit LpadR := Matrix.isUnit_of_left_inverse lpadR_left_inverse
private theorem ldl_identity_real : LpadR * DeltaPadR * LpadR.transpose = MpadR := by
  rw [LpadR, DeltaPadR, MpadR, ← Matrix.map_mul]
  change (Lpad * DeltaPad).map (Rat.castHom ℝ) *
    (Lpad.transpose.map (Rat.castHom ℝ)) = Mpad.map (Rat.castHom ℝ)
  rw [← Matrix.map_mul]
  exact congrArg (fun M : Matrix PadVertex PadVertex ℚ =>
    Matrix.map M (Rat.castHom ℝ)) ldl_identity
private theorem MpadR_posDef : MpadR.PosDef := by
  rw [← ldl_identity_real]
  rw [← Matrix.conjTranspose_eq_transpose_of_trivial]
  exact
    deltaPadR_posDef.mul_mul_conjTranspose_same (Matrix.vecMul_injective_of_isUnit lpadR_isUnit)
private theorem MpadR_submatrix : MpadR.submatrix embedPad embedPad = McoreR := by
  ext i j
  change ((Mpad (embedPad i) (embedPad j) : ℚ) : ℝ) =
    ((Mcore i j : ℚ) : ℝ)
  have h := congrArg (fun M : Matrix Vertex Vertex ℚ => M i j) Mpad_submatrix
  exact_mod_cast h
private theorem McoreR_posDef : McoreR.PosDef := by
  rw [← MpadR_submatrix]; exact MpadR_posDef.submatrix embedPad_injective
private theorem McoreR_eq_shifted_distance :
    McoreR = ({a} : ℝ) • Dr + ({b} : ℝ) • (1 : Matrix Vertex Vertex ℝ) := by
  rw [McoreR, Dr, Mcore_eq_shifted_distance]
  ext i j
  by_cases h : i = j <;> simp [Dq, h]
theorem shifted_distance_real_posDef :
    (({a} : ℝ) • Dr + ({b} : ℝ) • (1 : Matrix Vertex Vertex ℝ)).PosDef := by
  rw [← McoreR_eq_shifted_distance]; exact McoreR_posDef

theorem real_eigenpair_above_shift {{mu : ℝ}} {{x : Vertex → ℝ}}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : (-{b} : ℝ) / {a} < mu := by
  have hpos := shifted_distance_real_posDef.dotProduct_mulVec_pos hx
  rw [add_mulVec, smul_mulVec, smul_mulVec, one_mulVec, heig] at hpos
  simp only [star_trivial, dotProduct_add, dotProduct_smul, smul_eq_mul] at hpos
  have hnorm : 0 < dotProduct x x := by
    have hnonneg : 0 ≤ dotProduct x x :=
      Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
    have hne : dotProduct x x ≠ 0 := (dotProduct_self_eq_zero).not.mpr hx
    exact lt_of_le_of_ne hnonneg hne.symm
  have hprod : 0 < (({a} : ℝ) * mu + {b}) * dotProduct x x := by
    nlinarith [hpos]
  have hcoeff : 0 < ({a} : ℝ) * mu + {b} := by
    rcases (mul_pos_iff.mp hprod) with h | h
    · exact h.1
    · exact False.elim ((not_lt_of_ge hnorm.le) h.2)
  nlinarith
end Wow284.{n}
'''


def counterexample(spec: Spec) -> str:
    n,p,q,a,b = spec.namespace,spec.dual_p,spec.dual_q,spec.shift_scale,spec.shift_diag
    m=f"({p} : ℚ) / {q}"
    return f'''import Wow284.{n}.SpectralBridge

/-!
# Lean spectral certificate for the order-{spec.order} construction

It packages the exact minimum dual degree `{p}/{q}`, positive definiteness of
`{a}D+{b}I`, and the resulting strict WOW gap for every nonzero real eigenpair
of the formal matrix. Separate imported modules contain finite structural
lemmas; they are not bundled into the public endpoint below. No floating-point
eigenvalue is used.
-/
namespace Wow284.{n}
open Matrix
theorem minimum_dual_degree_certificate :
    (∀ v : Vertex, {m} ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = {m} :=
  ⟨dual_degree_lower_bound, dual_degree_attained⟩
theorem real_eigenpair_wow_gap_positive {{mu : ℝ}} {{x : Vertex → ℝ}}
    (hx : x ≠ 0) (heig : Dr *ᵥ x = mu • x) : 0 < ({p} : ℝ) / {q} + mu := by
  have h := real_eigenpair_above_shift hx heig; nlinarith

theorem counterexample_endpoint :
    ((∀ v : Vertex, {m} ≤ dualDegree v) ∧ ∃ v : Vertex, dualDegree v = {m}) ∧
    (({a} : ℚ) • Dq + ({b} : ℚ) • (1 : Matrix Vertex Vertex ℚ)).PosDef ∧
    (∀ {{mu : ℝ}} {{x : Vertex → ℝ}}, x ≠ 0 → Dr *ᵥ x = mu • x →
      0 < ({p} : ℝ) / {q} + mu) := by
  refine ⟨minimum_dual_degree_certificate, shifted_distance_posDef, ?_⟩
  intro mu x hx heig; exact real_eigenpair_wow_gap_positive hx heig
end Wow284.{n}
'''
