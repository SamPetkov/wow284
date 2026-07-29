# Block intertwiners for the two surviving order-50 quotients

**Status:** exact algebraic consequence of the signed-complement construction and
the canonical quotient classification.  
**Claim boundary:** the reductions below do not classify or eliminate lifts of
the two quotient matrices.

## 1. General intertwining identity

Let the connected components of the signed complement \(S\) have vertex sets
\(V_1,\ldots,V_c\).  Write

\[
 S=\operatorname{diag}(S_1,\ldots,S_c)
\]

and write the original adjacency matrix in the same block form,

\[
 A=(A_{ij})_{1\le i,j\le c}.
\]

Since

\[
 S=(6k+14)J-2I-g_k(A),
\]

the matrices \(A\) and \(S\) commute.  Comparing the \(ij\)-blocks of
\(AS=SA\) gives

\[
 \boxed{
 A_{ij}S_j=S_iA_{ij}
 \qquad(1\le i,j\le c).
 }
\]

Thus every cross-incidence block is an intertwiner between the rational signed
modules of its endpoint components.  In particular,

\[
 P_{i,\lambda}A_{ij}P_{j,\mu}=0
 \qquad(\lambda\ne\mu),
\]

where \(P_{i,\lambda}\) denotes the spectral projection of \(S_i\).  A nonzero
cross block can carry nonprincipal variation only through signed eigenvalues
shared by the two components.

## 2. Type A: sizes \((6,8,12,24)\)

For

\[
 Q_A=
 \begin{pmatrix}
 2&0&0&4\\
 0&0&3&3\\
 0&2&0&4\\
 1&1&2&2
 \end{pmatrix},
\]

the induced graph on the six-vertex cell is 2-regular and has girth at least
five.  It is therefore a cycle \(C_6\).  The signed component on the same cell
is uniquely the positive \(C_6\) by the exact signed enumeration.

Let \(R\) be the induced adjacency matrix and \(T\) the signed-component matrix.
The diagonal intertwining identity gives

\[
 RT=TR.
\]

Fixing \(R=A(C_6)\), exact enumeration of all labelled six-cycles \(T\) commuting
with \(R\) leaves four labelled choices and two orbits under the dihedral
automorphism group of \(R\):

1. \(T=R\);
2. \(T\) shares exactly four edges with \(R\), with three dihedrally equivalent
   labelled choices.

Hence the relative pair \((G[V_1],S_1)\) has exactly two isomorphism types.

Let \(X=A_{14}\) be the \(6\times24\) incidence block.  Every row has four ones
and every column has one, so

\[
 XX^{\mathsf T}=4I_6.
\]

The relation

\[
 XS_4=S_1X
\]

therefore makes \(X^{\mathsf T}\) injective on every eigenspace of \(S_1\).
Consequently the signed 24-vertex component contains, with at least the listed
multiplicities, the complete nonprincipal signed spectrum of \(C_6\):

\[
 \boxed{
 1^{(2)},\quad(-1)^{(2)},\quad(-2)^{(1)}
 \subseteq\operatorname{Spec}(S_4).
 }
\]

At the level of columns, if a vertex of the 24-cell has parent \(a\) in the
six-cell, the signed sums of its \(S_4\)-neighbours over the six parent classes
are exactly the two neighbours of \(a\) in the signed cycle \(S_1\).

## 3. Type B: sizes \((10,10,10,20)\)

For

\[
 Q_B=
 \begin{pmatrix}
 1&0&3&2\\
 0&1&1&4\\
 3&1&0&2\\
 1&2&1&2
 \end{pmatrix},
\]

the block \(A_{23}\) between the second and third ten-cells has row and column
sum one.  It is therefore a permutation matrix \(P\).  The intertwining
identity gives

\[
 PS_3=S_2P,
\]

and hence

\[
 \boxed{
 S_2=PS_3P^{\mathsf T}.
 }
\]

Thus these two ten-vertex signed components are isomorphic, not merely
cospectral.

The \(10\times20\) blocks \(A_{14}\) and \(A_{34}\) have row sum two and column
sum one.  If they are denoted by \(X_1,X_3\), then

\[
 X_1X_1^{\mathsf T}=X_3X_3^{\mathsf T}=2I_{10}.
\]

Therefore both transposes are injective intertwiners into the 20-vertex signed
component.  Every nonprincipal signed eigenvalue of \(S_1\) and of
\(S_3\cong S_2\), with multiplicity, must occur in \(S_4\).

This is a substantial reduction for any lift search: the two ten-vertex
components share one signed isomorphism type, and the 20-vertex component must
contain the signed modules of two ten-vertex components simultaneously.

## 4. Verification

The exact verifier

```text
scripts/verify_order50_intertwining_reduction.py
```

checks the block commutation identity, both incidence-isometry identities, the
six-cycle commutant enumeration, its two dihedral orbits, and the permutation
conjugacy in Type B.
