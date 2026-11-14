import Mathlib
import Wow284.DiameterThreeScalar

/-!
# Graph-level distance-matrix identity in diameter three

This module formalizes, at the level of an arbitrary finite simple graph, the
matrix identity behind the paper's Theorem `thm:diameter-three-score`:

  for a connected `k`-regular graph `G` of girth at least five and diameter
  three, with adjacency matrix `A` and distance matrix `D`,

    `D = 3J + (k - 3)I - 2A - A^2`   and   `D + kI = 3J + (2k - 2)I - (A + I)^2`.

Hypotheses are stated with Mathlib's own notions: `SimpleGraph.Connected`,
`SimpleGraph.IsRegularOfDegree`, `SimpleGraph.egirth` (girth in `ℕ∞`, `⊤` for
forests) and `SimpleGraph.diam`.  The distance matrix uses
`SimpleGraph.dist`.  The identities hold over every commutative ring.

As spectral consequences we prove the eigenvector transfer used in the paper:
a zero-sum adjacency eigenvector with eigenvalue `θ` is a distance eigenvector
with eigenvalue `k - 2 - (θ + 1)^2` (`Wow284.diameterThreeDistanceValue`), and
the constant vector is a distance eigenvector with eigenvalue
`3n - k^2 - k - 3`.

Without regularity, for connected graphs of girth at least five and diameter
at most three, we prove `D = 3J - 3I - 2A - A^2 + Δ` with `Δ` the diagonal
degree matrix, and hence `D + tI = 3J + Δ + (t - 2)I - (A + I)^2` for every
scalar `t` (`distMatrix_eq_of_diam_le_three`,
`distMatrix_add_smul_one_eq_of_diam_le_three`).

We also prove the necessary direction of the spectral window: if `D + kI` is
positive definite, every adjacency eigenvalue `θ` with a nonzero zero-sum
eigenvector satisfies `|θ + 1| < √(2k - 2)` (`abs_add_one_lt_of_posDef`).
The converse direction and the exact formula
`Φ(G) = 2k - 2 - max (θ + 1)^2` additionally need a simultaneous
diagonalization of `A` and `D` (spectral theorem plus simplicity of the
eigenvalue `k`) and are not formalized here.
-/

namespace Wow284.DiameterThreeMatrix

open Matrix SimpleGraph Finset

variable {V : Type*}

/-- The distance matrix `D(G)`, with entries `SimpleGraph.dist` cast into `R`. -/
noncomputable def distMatrix (G : SimpleGraph V) (R : Type*) [CommRing R] : Matrix V V R :=
  Matrix.of fun u v => (G.dist u v : R)

/-- The all-ones matrix `J`. -/
def allOnes (R : Type*) [CommRing R] : Matrix V V R :=
  Matrix.of fun _ _ => 1

variable {G : SimpleGraph V}

section Girth

/-- Girth at least five excludes triangles: adjacent vertices have no common
neighbour. -/
theorem not_adj_of_adj_adj (hg : 5 ≤ G.egirth) {u v x : V}
    (huv : G.Adj u v) (hux : G.Adj u x) (hxv : G.Adj x v) : False := by
  have hne_uv : u ≠ v := G.ne_of_adj huv
  have hne_ux : u ≠ x := G.ne_of_adj hux
  have hne_xv : x ≠ v := G.ne_of_adj hxv
  have hc : (Walk.cons hux (Walk.cons hxv (Walk.cons huv.symm Walk.nil))).IsCycle := by
    rw [Walk.cons_isCycle_iff]
    refine ⟨?_, ?_⟩
    · rw [Walk.isPath_def]
      simp [Walk.support_cons, hne_xv, hne_ux.symm, hne_uv.symm]
    · simp [Walk.edges_cons, hne_uv, hne_xv, hne_ux]
  have h := (le_egirth.mp hg) u _ hc
  norm_num [Walk.length_cons] at h

/-- Girth at least five excludes four-cycles: two distinct vertices have at
most one common neighbour. -/
theorem eq_of_common_neighbours (hg : 5 ≤ G.egirth) {u v x y : V} (huv : u ≠ v)
    (hux : G.Adj u x) (hxv : G.Adj x v) (huy : G.Adj u y) (hyv : G.Adj y v) :
    x = y := by
  by_contra hxy
  have hne_ux : u ≠ x := G.ne_of_adj hux
  have hne_xv : x ≠ v := G.ne_of_adj hxv
  have hne_uy : u ≠ y := G.ne_of_adj huy
  have hne_yv : y ≠ v := G.ne_of_adj hyv
  have hc : (Walk.cons hux (Walk.cons hxv
      (Walk.cons hyv.symm (Walk.cons huy.symm Walk.nil)))).IsCycle := by
    rw [Walk.cons_isCycle_iff]
    refine ⟨?_, ?_⟩
    · rw [Walk.isPath_def]
      simp [Walk.support_cons, hne_xv, hxy, hne_ux.symm, hne_yv.symm, huv.symm,
        hne_uy.symm]
    · simp [Walk.edges_cons, huv, hxy, hne_uy, hne_ux, hne_xv]
  have h := (le_egirth.mp hg) u _ hc
  norm_num [Walk.length_cons] at h

end Girth

section Distances

variable (hconn : G.Connected)
include hconn

theorem dist_eq_two_of_common {u v : V} (huv : u ≠ v) (hnadj : ¬ G.Adj u v) {x : V}
    (hux : G.Adj u x) (hxv : G.Adj x v) : G.dist u v = 2 := by
  have hle : G.dist u v ≤ 2 := by
    simpa using SimpleGraph.dist_le (Walk.cons hux (Walk.cons hxv Walk.nil))
  have h0 : G.dist u v ≠ 0 := fun h => huv ((hconn.dist_eq_zero_iff).mp h)
  have h1 : G.dist u v ≠ 1 := fun h => hnadj (dist_eq_one_iff_adj.mp h)
  omega

theorem exists_common_of_dist_eq_two {u v : V} (h : G.dist u v = 2) :
    ∃ x, G.Adj u x ∧ G.Adj x v := by
  obtain ⟨p, hp⟩ := hconn.exists_walk_length_eq_dist u v
  rw [h] at hp
  cases p with
  | nil => simp at hp
  | cons hux q =>
    cases q with
    | nil => simp at hp
    | cons hxv r =>
      cases r with
      | nil => exact ⟨_, hux, hxv⟩
      | cons _ _ => simp [Walk.length_cons] at hp

theorem dist_eq_three_of_no_common {u v : V} (hdiam : G.diam = 3) (huv : u ≠ v)
    (hnadj : ¬ G.Adj u v) (hno : ∀ x, G.Adj u x → ¬ G.Adj x v) :
    G.dist u v = 3 := by
  have hle : G.dist u v ≤ 3 := by
    have hne : G.ediam ≠ ⊤ := ediam_ne_top_of_diam_ne_zero (by omega)
    simpa [hdiam] using (dist_le_diam (G := G) hne (u := u) (v := v))
  have h0 : G.dist u v ≠ 0 := fun h => huv ((hconn.dist_eq_zero_iff).mp h)
  have h1 : G.dist u v ≠ 1 := fun h => hnadj (dist_eq_one_iff_adj.mp h)
  have h2 : G.dist u v ≠ 2 := by
    intro h
    obtain ⟨x, hux, hxv⟩ := exists_common_of_dist_eq_two hconn h
    exact hno x hux hxv
  omega

/-- In a finite connected graph of diameter at most three every distance is at
most three. -/
theorem dist_le_three_of_diam_le [Finite V] (hdiam : G.diam ≤ 3) (u v : V) :
    G.dist u v ≤ 3 := by
  haveI : Nonempty V := hconn.nonempty
  exact le_trans (dist_le_diam (G.connected_iff_ediam_ne_top.mp hconn)) hdiam

theorem dist_eq_three_of_no_common_of_le {u v : V} (hle : G.dist u v ≤ 3) (huv : u ≠ v)
    (hnadj : ¬ G.Adj u v) (hno : ∀ x, G.Adj u x → ¬ G.Adj x v) :
    G.dist u v = 3 := by
  have h0 : G.dist u v ≠ 0 := fun h => huv ((hconn.dist_eq_zero_iff).mp h)
  have h1 : G.dist u v ≠ 1 := fun h => hnadj (dist_eq_one_iff_adj.mp h)
  have h2 : G.dist u v ≠ 2 := by
    intro h
    obtain ⟨x, hux, hxv⟩ := exists_common_of_dist_eq_two hconn h
    exact hno x hux hxv
  omega

end Distances

section Identity

variable [Fintype V] [DecidableEq V] [DecidableRel G.Adj] {R : Type*} [CommRing R]

/-- Entries of `A^2` for a graph of girth at least five, off the diagonal:
zero for adjacent pairs, one when there is a common neighbour, zero
otherwise. -/
theorem adjMatrix_sq_apply_of_ne (hg : 5 ≤ G.egirth) {u v : V} (huv : u ≠ v) :
    (G.adjMatrix R ^ 2) u v =
      if ∃ x, G.Adj u x ∧ G.Adj x v then 1 else 0 := by
  rw [sq, adjMatrix_mul_apply]
  simp only [adjMatrix_apply]
  by_cases h : ∃ x, G.Adj u x ∧ G.Adj x v
  · rw [if_pos h]
    obtain ⟨x, hux, hxv⟩ := h
    rw [Finset.sum_eq_single x]
    · simp [hxv]
    · intro y hy hyx
      have huy : G.Adj u y := by simpa using hy
      have : ¬ G.Adj y v := fun hyv =>
        hyx (eq_of_common_neighbours hg huv hux hxv huy hyv).symm
      simp [this]
    · intro hx
      exact absurd (by simpa using hux) hx
  · rw [if_neg h]
    refine Finset.sum_eq_zero fun y hy => ?_
    have huy : G.Adj u y := by simpa using hy
    have : ¬ G.Adj y v := fun hyv => h ⟨y, huy, hyv⟩
    simp [this]

/-- **Diameter-three distance identity** (paper, Theorem
`thm:diameter-three-score`, first display): for a connected `k`-regular graph
of girth at least five and diameter three,
`D = 3J + (k - 3)I - 2A - A^2`. -/
theorem distMatrix_eq {k : ℕ} (hconn : G.Connected) (hreg : G.IsRegularOfDegree k)
    (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3) :
    distMatrix G R =
      (3 : R) • allOnes R + ((k : R) - 3) • (1 : Matrix V V R)
        - (2 : R) • G.adjMatrix R - G.adjMatrix R ^ 2 := by
  ext u v
  simp only [distMatrix, allOnes, Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply,
    Matrix.of_apply, smul_eq_mul]
  by_cases huv : u = v
  · subst huv
    have hsq : (G.adjMatrix R ^ 2) u u = (k : R) := by
      rw [sq, adjMatrix_mul_self_apply_self, hreg u]
    rw [hsq]
    simp
  · rw [adjMatrix_sq_apply_of_ne hg huv]
    simp only [Matrix.one_apply_ne huv, adjMatrix_apply]
    by_cases hadj : G.Adj u v
    · have hno : ¬ ∃ x, G.Adj u x ∧ G.Adj x v := fun ⟨x, hux, hxv⟩ =>
        not_adj_of_adj_adj hg hadj hux hxv
      rw [dist_eq_one_iff_adj.mpr hadj]
      simp [hadj, hno]
      ring
    · by_cases hc : ∃ x, G.Adj u x ∧ G.Adj x v
      · obtain ⟨x, hux, hxv⟩ := hc
        rw [dist_eq_two_of_common hconn huv hadj hux hxv]
        simp [hadj, show ∃ x, G.Adj u x ∧ G.Adj x v from ⟨x, hux, hxv⟩]
        ring
      · have hno : ∀ x, G.Adj u x → ¬ G.Adj x v := fun x hux hxv => hc ⟨x, hux, hxv⟩
        rw [dist_eq_three_of_no_common hconn hdiam huv hadj hno]
        simp [hadj, hc]

/-- Second form of the identity: `D + kI = 3J + (2k - 2)I - (A + I)^2`. -/
theorem distMatrix_add_smul_one_eq {k : ℕ} (hconn : G.Connected)
    (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3) :
    distMatrix G R + (k : R) • (1 : Matrix V V R) =
      (3 : R) • allOnes R + (2 * (k : R) - 2) • (1 : Matrix V V R)
        - (G.adjMatrix R + 1) ^ 2 := by
  rw [distMatrix_eq hconn hreg hg hdiam]
  ext u v
  simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul, sq,
    add_mul, mul_add, Matrix.mul_one, Matrix.one_mul]
  ring

/-- **Irregular diameter-three distance identity.**  For a connected graph of
girth at least five and diameter at most three, with no regularity assumption,
`D = 3J - 3I - 2A - A^2 + Δ`, where `Δ` is the diagonal degree matrix. -/
theorem distMatrix_eq_of_diam_le_three (hconn : G.Connected) (hg : 5 ≤ G.egirth)
    (hdiam : G.diam ≤ 3) :
    distMatrix G R =
      (3 : R) • allOnes R - (3 : R) • (1 : Matrix V V R) - (2 : R) • G.adjMatrix R
        - G.adjMatrix R ^ 2 + Matrix.diagonal (fun v => (G.degree v : R)) := by
  ext u v
  simp only [distMatrix, allOnes, Matrix.sub_apply, Matrix.add_apply, Matrix.smul_apply,
    Matrix.of_apply, smul_eq_mul]
  by_cases huv : u = v
  · subst huv
    have hsq : (G.adjMatrix R ^ 2) u u = (G.degree u : R) := by
      rw [sq, adjMatrix_mul_self_apply_self]
    rw [hsq, Matrix.diagonal_apply_eq, Matrix.one_apply_eq, adjMatrix_apply,
      if_neg (G.irrefl (v := u)), SimpleGraph.dist_self, Nat.cast_zero]
    ring
  · rw [adjMatrix_sq_apply_of_ne hg huv, Matrix.diagonal_apply_ne _ huv,
      Matrix.one_apply_ne huv, adjMatrix_apply]
    by_cases hadj : G.Adj u v
    · have hno : ¬ ∃ x, G.Adj u x ∧ G.Adj x v := fun ⟨x, hux, hxv⟩ =>
        not_adj_of_adj_adj hg hadj hux hxv
      rw [dist_eq_one_iff_adj.mpr hadj, if_pos hadj, if_neg hno, Nat.cast_one]
      ring
    · by_cases hc : ∃ x, G.Adj u x ∧ G.Adj x v
      · obtain ⟨x, hux, hxv⟩ := hc
        rw [dist_eq_two_of_common hconn huv hadj hux hxv, if_neg hadj,
          if_pos (⟨x, hux, hxv⟩ : ∃ x, G.Adj u x ∧ G.Adj x v)]
        push_cast
        ring
      · have hno : ∀ x, G.Adj u x → ¬ G.Adj x v := fun x hux hxv => hc ⟨x, hux, hxv⟩
        rw [dist_eq_three_of_no_common_of_le hconn
          (dist_le_three_of_diam_le hconn hdiam u v) huv hadj hno, if_neg hadj, if_neg hc]
        push_cast
        ring

/-- Shifted irregular form: for every scalar `t`,
`D + tI = 3J + Δ + (t - 2)I - (A + I)^2`.  With `t = δ*(G)` this is the
matrix whose positive definiteness is `Φ(G) > 0`. -/
theorem distMatrix_add_smul_one_eq_of_diam_le_three (hconn : G.Connected)
    (hg : 5 ≤ G.egirth) (hdiam : G.diam ≤ 3) (t : R) :
    distMatrix G R + t • (1 : Matrix V V R) =
      (3 : R) • allOnes R + Matrix.diagonal (fun v => (G.degree v : R))
        + (t - 2) • (1 : Matrix V V R) - (G.adjMatrix R + 1) ^ 2 := by
  rw [distMatrix_eq_of_diam_le_three hconn hg hdiam]
  ext u v
  simp only [Matrix.add_apply, Matrix.sub_apply, Matrix.smul_apply, smul_eq_mul, sq,
    add_mul, mul_add, Matrix.mul_one, Matrix.one_mul]
  ring

/-- Irregular window criterion (over `ℝ`): `D + tI` is positive definite iff
`3J + Δ + (t - 2)I - (A + I)^2` is. -/
theorem posDef_shift_iff_of_diam_le_three (hconn : G.Connected) (hg : 5 ≤ G.egirth)
    (hdiam : G.diam ≤ 3) (t : ℝ) :
    (distMatrix G ℝ + t • (1 : Matrix V V ℝ)).PosDef ↔
      ((3 : ℝ) • allOnes ℝ + Matrix.diagonal (fun v => (G.degree v : ℝ))
        + (t - 2) • (1 : Matrix V V ℝ) - (G.adjMatrix ℝ + 1) ^ 2).PosDef := by
  rw [distMatrix_add_smul_one_eq_of_diam_le_three hconn hg hdiam]

end Identity

section Spectral

theorem allOnes_mulVec_of_sum_eq_zero [Fintype V] {R : Type*} [CommRing R] {x : V → R}
    (hx : ∑ i, x i = 0) :
    allOnes (V := V) R *ᵥ x = 0 := by
  ext u
  simp [allOnes, mulVec, dotProduct, hx]

variable [Fintype V] [DecidableEq V] [DecidableRel G.Adj] {R : Type*} [CommRing R]

/-- **Eigenvector transfer.**  A zero-sum adjacency eigenvector with eigenvalue
`θ` is a distance eigenvector with eigenvalue `k - 2 - (θ + 1)^2`. -/
theorem distMatrix_mulVec_of_adj_eigen {k : ℕ} (hconn : G.Connected)
    (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3)
    {x : V → R} (hx : ∑ i, x i = 0) {θ : R} (hA : G.adjMatrix R *ᵥ x = θ • x) :
    distMatrix G R *ᵥ x = ((k : R) - 2 - (θ + 1) ^ 2) • x := by
  rw [distMatrix_eq hconn hreg hg hdiam]
  have hA2 : (G.adjMatrix R ^ 2) *ᵥ x = (θ ^ 2) • x := by
    rw [sq, ← Matrix.mulVec_mulVec, hA, Matrix.mulVec_smul, hA, smul_smul, sq]
  simp only [Matrix.sub_mulVec, Matrix.add_mulVec, Matrix.smul_mulVec,
    allOnes_mulVec_of_sum_eq_zero hx, Matrix.one_mulVec, hA, hA2]
  ext u
  simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul, Pi.zero_apply]
  ring

/-- Real form of the transfer, phrased with the existing scalar
`Wow284.diameterThreeDistanceValue k θ = k - 2 - (θ + 1)^2`. -/
theorem distMatrix_mulVec_real {k : ℕ} (hconn : G.Connected)
    (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3)
    {x : V → ℝ} (hx : ∑ i, x i = 0) {θ : ℝ} (hA : G.adjMatrix ℝ *ᵥ x = θ • x) :
    distMatrix G ℝ *ᵥ x = Wow284.diameterThreeDistanceValue (k : ℝ) θ • x := by
  rw [distMatrix_mulVec_of_adj_eigen hconn hreg hg hdiam hx hA]
  rfl

/-- **Necessary direction of the spectral window.**  If `D + kI` is positive
definite, then every adjacency eigenvalue `θ` admitting a nonzero zero-sum
eigenvector satisfies `|θ + 1| < √(2k - 2)`.

For a `k`-regular graph the minimum dual degree is `k`, so positive
definiteness of `D + kI` is the paper's strictness condition `Φ(G) > 0`
(`λ_min(D) > -k`); that reformulation is the spectral theorem for the
symmetric matrix `D` and is not restated here. -/
theorem abs_add_one_lt_of_posDef {k : ℕ} (hconn : G.Connected)
    (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3)
    (hpd : (distMatrix G ℝ + (k : ℝ) • (1 : Matrix V V ℝ)).PosDef)
    {x : V → ℝ} (hx0 : x ≠ 0) (hx : ∑ i, x i = 0) {θ : ℝ}
    (hA : G.adjMatrix ℝ *ᵥ x = θ • x) :
    |θ + 1| < Real.sqrt (2 * (k : ℝ) - 2) := by
  have hpos := (Matrix.posDef_iff_dotProduct_mulVec.mp hpd).2 hx0
  have hmul : (distMatrix G ℝ + (k : ℝ) • (1 : Matrix V V ℝ)) *ᵥ x =
      ((k : ℝ) + Wow284.diameterThreeDistanceValue (k : ℝ) θ) • x := by
    rw [Matrix.add_mulVec, distMatrix_mulVec_real hconn hreg hg hdiam hx hA,
      Matrix.smul_mulVec, Matrix.one_mulVec]
    ext i
    simp only [Pi.add_apply, Pi.smul_apply, smul_eq_mul]
    ring
  rw [hmul, dotProduct_smul, smul_eq_mul] at hpos
  have hs : 0 ≤ star x ⬝ᵥ x := by
    simp only [star_trivial, dotProduct]
    exact Finset.sum_nonneg fun i _ => mul_self_nonneg (x i)
  have hc : 0 < (k : ℝ) + Wow284.diameterThreeDistanceValue (k : ℝ) θ := by
    rcases le_or_gt ((k : ℝ) + Wow284.diameterThreeDistanceValue (k : ℝ) θ) 0 with h | h
    · exact absurd hpos (not_lt.mpr (mul_nonpos_of_nonpos_of_nonneg h hs))
    · exact h
  have hk : (1 : ℝ) ≤ k := by
    unfold Wow284.diameterThreeDistanceValue at hc
    nlinarith [sq_nonneg (θ + 1)]
  exact (Wow284.diameter_three_scalar_criterion (k : ℝ) θ hk).mp hc

/-- The constant vector is a distance eigenvector with eigenvalue
`3n - k^2 - k - 3`, where `n = |V|`. -/
theorem distMatrix_mulVec_const {k : ℕ} (hconn : G.Connected)
    (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth) (hdiam : G.diam = 3) :
    distMatrix G R *ᵥ (fun _ => (1 : R)) =
      (3 * (Fintype.card V : R) - (k : R) ^ 2 - k - 3) • (fun _ => (1 : R)) := by
  rw [distMatrix_eq hconn hreg hg hdiam]
  have hA : G.adjMatrix R *ᵥ (fun _ => (1 : R)) = (k : R) • (fun _ => (1 : R)) := by
    ext v
    have := adjMatrix_mulVec_const_apply_of_regular (α := R) (a := (1 : R)) hreg (v := v)
    simpa [Function.const] using this
  have hA2 : (G.adjMatrix R ^ 2) *ᵥ (fun _ => (1 : R)) =
      ((k : R) ^ 2) • (fun _ => (1 : R)) := by
    rw [sq, ← Matrix.mulVec_mulVec, hA, Matrix.mulVec_smul, hA, smul_smul, sq]
  have hJ : allOnes (V := V) R *ᵥ (fun _ => (1 : R)) =
      (Fintype.card V : R) • (fun _ => (1 : R)) := by
    ext u
    simp [allOnes, mulVec, dotProduct]
  simp only [Matrix.sub_mulVec, Matrix.add_mulVec, Matrix.smul_mulVec, hJ,
    Matrix.one_mulVec, hA, hA2]
  ext u
  simp only [Pi.sub_apply, Pi.add_apply, Pi.smul_apply, smul_eq_mul]
  ring

end Spectral

end Wow284.DiameterThreeMatrix
