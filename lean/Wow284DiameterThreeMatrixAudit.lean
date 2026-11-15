import Wow284.DiameterThreeMatrix

/-!
Trust report for the graph-level diameter-three distance identity
(`Wow284.DiameterThreeMatrix`, paper Theorem `thm:diameter-three-score`).

Compiling this file prints the transitive axioms of the public endpoints, and
the `example`s restate the two matrix identities with Mathlib notions only, so
that the hypotheses can be read off without unfolding project definitions
other than `distMatrix` and `allOnes` (both one-line `Matrix.of` definitions).
-/

#print axioms Wow284.DiameterThreeMatrix.not_adj_of_adj_adj
#print axioms Wow284.DiameterThreeMatrix.eq_of_common_neighbours
#print axioms Wow284.DiameterThreeMatrix.distMatrix_eq
#print axioms Wow284.DiameterThreeMatrix.distMatrix_add_smul_one_eq
#print axioms Wow284.DiameterThreeMatrix.distMatrix_mulVec_of_adj_eigen
#print axioms Wow284.DiameterThreeMatrix.distMatrix_mulVec_real
#print axioms Wow284.DiameterThreeMatrix.distMatrix_mulVec_const
#print axioms Wow284.DiameterThreeMatrix.abs_add_one_lt_of_posDef
#print axioms Wow284.DiameterThreeMatrix.distMatrix_eq_of_diam_le_three
#print axioms Wow284.DiameterThreeMatrix.distMatrix_add_smul_one_eq_of_diam_le_three
#print axioms Wow284.DiameterThreeMatrix.posDef_shift_iff_of_diam_le_three

open Matrix SimpleGraph in
/-- Literal restatement: for a connected `k`-regular graph of girth at least
five and diameter three, `D = 3J + (k-3)I - 2A - A^2` over `ℤ`, where `D` has
entries `G.dist u v`. -/
example {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (k : ℕ) (hconn : G.Connected) (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth)
    (hdiam : G.diam = 3) :
    (Matrix.of fun u v => (G.dist u v : ℤ)) =
      (3 : ℤ) • (Matrix.of fun (_ : V) (_ : V) => (1 : ℤ)) + ((k : ℤ) - 3) • (1 : Matrix V V ℤ)
        - (2 : ℤ) • G.adjMatrix ℤ - G.adjMatrix ℤ ^ 2 :=
  Wow284.DiameterThreeMatrix.distMatrix_eq hconn hreg hg hdiam

open Matrix SimpleGraph in
/-- Literal restatement of the second form `D + kI = 3J + (2k-2)I - (A+I)^2`. -/
example {V : Type} [Fintype V] [DecidableEq V] (G : SimpleGraph V) [DecidableRel G.Adj]
    (k : ℕ) (hconn : G.Connected) (hreg : G.IsRegularOfDegree k) (hg : 5 ≤ G.egirth)
    (hdiam : G.diam = 3) :
    (Matrix.of fun u v => (G.dist u v : ℤ)) + (k : ℤ) • (1 : Matrix V V ℤ) =
      (3 : ℤ) • (Matrix.of fun (_ : V) (_ : V) => (1 : ℤ))
        + (2 * (k : ℤ) - 2) • (1 : Matrix V V ℤ) - (G.adjMatrix ℤ + 1) ^ 2 :=
  Wow284.DiameterThreeMatrix.distMatrix_add_smul_one_eq hconn hreg hg hdiam
