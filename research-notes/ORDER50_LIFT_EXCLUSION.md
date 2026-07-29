# Excluding both canonical order-50 quotient lifts

**Status:** project derivation under Proof Audit 14C.  The theorem is not ready for
manuscript promotion until the primary and independent exhaustive audits pass at
the same commit.  
**Scope:** a hypothetical connected 6-regular graph of order 50, girth at least
five and diameter three satisfying the strict shifted WOW window.

## 1. Starting point

The canonical signed-component quotient classification leaves exactly two
four-cell quotients.  Relative to the connected components of the signed
complement

\[
 S=50J-g_6(A)-2I,
 \qquad
 g_6(x)=(x+2)^2((x+1)^2-10),
\]

they are

\[
 Q_A=
 \begin{pmatrix}
 2&0&0&4\\
 0&0&3&3\\
 0&2&0&4\\
 1&1&2&2
 \end{pmatrix},
 \qquad
 (n_1,n_2,n_3,n_4)=(6,8,12,24),
\]

and

\[
 Q_B=
 \begin{pmatrix}
 1&0&3&2\\
 0&1&1&4\\
 3&1&0&2\\
 1&2&1&2
 \end{pmatrix},
 \qquad
 (n_1,n_2,n_3,n_4)=(10,10,10,20).
\]

Write

\[
 S=\operatorname{diag}(S_1,S_2,S_3,S_4),
 \qquad
 A=(A_{ij}).
\]

Because \(A\) commutes with \(S\), every block satisfies

\[
 \boxed{A_{ij}S_j=S_iA_{ij}.}
\]

Each \(S_i\) is symmetric, has zero diagonal and entries in
\(\{-1,0,1\}\), has signed row sum two, satisfies \(S_i+2I\succeq0\),
and has connected support.

## 2. Elimination of Type A

The block \(C=A_{23}\) is an \(8\times12\) zero-one matrix with row sum
three and column sum two.  The absence of 4-cycles implies that its columns
are the edges of a simple cubic graph \(H\) on eight vertices.  Thus \(C\)
is the unoriented vertex-edge incidence matrix of \(H\).

The intertwining relation gives

\[
 CS_3=S_2C.
\]

Since

\[
 CC^{\mathsf T}=3I+A(H),
\]

one also has

\[
 S_2A(H)=A(H)S_2.
\]

There are exactly six simple cubic graphs on eight vertices, including the
disconnected graph \(K_4\sqcup K_4\).  An exact canonical enumeration was
performed for every one of them.  It imposes

\[
 \begin{aligned}
 &S_2=S_2^{\mathsf T},\quad
 (S_2)_{ii}=0,\quad
 (S_2)_{ij}\in\{-1,0,1\},\quad
 S_2\mathbf1=2\mathbf1,\quad
 S_2+2I\succeq0,\\
 &S_3=S_3^{\mathsf T},\quad
 (S_3)_{ii}=0,\quad
 (S_3)_{ij}\in\{-1,0,1\},\quad
 S_3\mathbf1=2\mathbf1,\quad
 S_3+2I\succeq0,
 \end{aligned}
\]

connected support, and \(CS_3=S_2C\).  Before the \(S_3\) equation, the
numbers of canonical \(S_2\)-orbits for the six cubic graphs are

\[
 18,\ 15,\ 2,\ 0,\ 31,\ 15.
\]

After the \(S_3\) equation, only twelve labelled relative candidates remain:
four over \(K_4\sqcup K_4\) and eight over the cube \(Q_3\).

Now put

\[
 M=A_{14}A_{34}^{\mathsf T}.
\]

The quotient degrees give row sum eight and column sum four.  If two vertices
of the 24-cell joined the same vertices of the 6- and 12-cells, they would
form a 4-cycle with those endpoints; hence \(M\) is a zero-one matrix.  The
block intertwiners imply

\[
 S_1M=MS_3.
\]

The six-cell is an induced \(C_6\), and the signed component \(S_1\) is the
unique positive \(C_6\).  For each of the twelve relative candidates, the
complete rational solution space of

\[
 A(C_6)M=MS_3,
 \qquad
 M\mathbf1=8\mathbf1,
 \qquad
 M^{\mathsf T}\mathbf1=4\mathbf1
\]

contains no zero-one matrix.  Therefore Type A has no lift.

## 3. Signed ten-vertex components in Type B

In Type B, the first and second ten-cells induce perfect matchings, while the
third is independent.  The block \(A_{23}\) is a permutation matrix.  After
relabelling it to the identity, one has

\[
 S_2=S_3.
\]

The diagonal intertwining relation also shows that \(S_1\) and \(S_2\)
commute with fixed-point-free matching involutions.

An exact enumeration of symmetric signed \(10\times10\) matrices with zero
diagonal, entries in \(\{-1,0,1\}\), signed row sum two, connected support,
least eigenvalue at least \(-2\), and commuting with a fixed perfect matching
gives 1152 labelled matrices and exactly two orbits under the matching
centralizer.  In both orbits the signed matrix is the ordinary positive cycle
\(C_{10}\).  The two orbits record the two possible relative positions of the
matching inside the cycle.

Consequently

\[
 \boxed{S_1\cong S_2\cong S_3\cong C_{10}.}
\]

## 4. The final twenty-vertex component

Let

\[
 X_1=A_{14},
 \qquad
 X_3=A_{34},
 \qquad
 L=X_1X_3^{\mathsf T}.
\]

Every column of \(X_1\) and \(X_3\) contains one entry equal to one, while every
row contains two.  The absence of 4-cycles makes \(L\) a zero-one matrix.
Thus

\[
 L\mathbf1=2\mathbf1,
 \qquad
 L^{\mathsf T}\mathbf1=2\mathbf1.
\]

The intertwining identities give

\[
 A(C_{10})L=LA(C_{10}).
\]

There are 140 labelled zero-one solutions and exactly six orbits under the
independent dihedral actions on the two cycles.  Their bipartite support has
respectively one, two or five connected components, with two orbits of each
kind.

For a fixed \(L\), label the twenty edges of its bipartite support and let
\(X_1,X_3\) be the corresponding endpoint-incidence matrices.  We then solve
exactly for every symmetric matrix \(T\) satisfying

\[
 \begin{aligned}
 &X_1T=A(C_{10})X_1,\\
 &X_3T=A(C_{10})X_3,\\
 &T\mathbf1=2\mathbf1,\\
 &T_{ii}=0,\qquad T_{ij}\in\{-1,0,1\},\\
 &T+2I\succeq0.
 \end{aligned}
\]

The affine dimensions are \(0,1,10\) when the bipartite support of \(L\) has
one, two, five components, respectively.  For each of the six dihedral orbits
there is exactly one positive-semidefinite completion.  In every case that
completion is

\[
 \boxed{T\cong C_{10}\sqcup C_{10}.}
\]

Its support is disconnected.  But \(V_4\) is, by construction, one connected
component of the signed complement.  This contradiction eliminates Type B.

## 5. Consequence

Both canonical order-50 quotient types are impossible.  Therefore

\[
 \boxed{
 \text{no connected 6-regular strict WOW counterexample has order }50.
 }
\]

Combining this with the audited integral-excess order bound gives

\[
 \boxed{
 k=6\quad\Longrightarrow\quad n\le49.
 }
\]

This theorem does not assert that order 49 is attainable, does not classify
irregular counterexamples, and does not affect the explicit regular order-40
construction.

## 6. Verification

The primary exact verifier is

```text
scripts/verify_order50_lift_exclusion.py
```

It generates the six cubic graphs on eight vertices, classifies the signed
\(8\)- and \(12\)-vertex intertwining pairs, checks the missing Type-A incidence
block, classifies the matching-symmetric signed ten-vertex components, reduces
the \(10\times10\) two-regular intertwiners to six dihedral orbits, and checks
every twenty-vertex completion by exact rational positive semidefiniteness.
No floating-point eigenvalue decision is used.
