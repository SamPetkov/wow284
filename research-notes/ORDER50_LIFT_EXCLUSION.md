# Excluding both canonical order-50 quotient lifts

**Status:** project derivation under Proof Audit 14C. Manuscript promotion requires
both exact implementations and all current-head regressions to pass at the same
commit.  
**Scope:** a hypothetical connected 6-regular graph of order 50, girth at least
five and diameter three satisfying the strict shifted WOW window.

## 1. Starting point

The audited signed-component quotient classification leaves exactly two
four-cell quotients. Relative to the connected components of the signed
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
three and column sum two. The absence of 4-cycles implies that its columns are
the edges of a simple cubic graph \(H\) on eight vertices. Thus \(C\) is the
unoriented vertex-edge incidence matrix of \(H\). The intertwining relation
gives

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

There are exactly six isomorphism classes of simple cubic graphs on eight
vertices, including \(K_4\sqcup K_4\). For each class the primary verifier
canonically enumerates every signed matrix \(S_2\) satisfying

\[
 S_2=S_2^{\mathsf T},\qquad
 (S_2)_{ii}=0,\qquad
 (S_2)_{ij}\in\{-1,0,1\},
\]

\[
 S_2\mathbf1=2\mathbf1,\qquad
 S_2+2I\succeq0,
\]

connected support, and \(S_2A(H)=A(H)S_2\). The exact canonical orbit counts
for the six cubic classes are

\[
 \boxed{18,\ 15,\ 2,\ 0,\ 31,\ 7.}
\]

For each orbit the equation \(CS_3=S_2C\), signed row sum, entry set,
connected support and exact positive semidefiniteness are imposed on \(S_3\).
After canonical reduction, exactly one signed-pair orbit survives. It occurs
for

\[
 \boxed{H=K_4\sqcup K_4.}
\]

Now put

\[
 M=A_{14}A_{34}^{\mathsf T}.
\]

The quotient degrees give row sum eight and column sum four. If two vertices of
the 24-cell joined the same vertices of the 6- and 12-cells, they would form a
4-cycle with those endpoints. Hence \(M\) is zero-one. The block intertwiners
give

\[
 S_1M=MS_3.
\]

The six-cell is an induced \(C_6\), and the signed component \(S_1\) is the
unique positive \(C_6\). For the sole signed-pair orbit, the complete rational
affine solution space of

\[
 A(C_6)M=MS_3,
 \qquad
 M\mathbf1=8\mathbf1,
 \qquad
 M^{\mathsf T}\mathbf1=4\mathbf1
\]

has dimension six. Exact enumeration of its binary points gives

\[
 \boxed{0\text{ zero-one solutions}.}
\]

Therefore Type A has no lift.

## 3. Signed ten-vertex components in Type B

In Type B, the first and second ten-cells induce perfect matchings, while the
third is independent. The block \(A_{23}\) is a permutation matrix. After
relabelling it to the identity,

\[
 S_2=S_3.
\]

The diagonal intertwining relations show that \(S_1\) and \(S_2\) commute with
fixed-point-free matching involutions.

An exact enumeration of symmetric signed \(10\times10\) matrices with zero
diagonal, entries in \(\{-1,0,1\}\), signed row sum two, connected support,
least eigenvalue at least \(-2\), and commuting with a fixed perfect matching
gives:

\[
 \begin{array}{c|r}
 \text{quantity}&\text{exact count}\\
 \hline
 \text{positive degree-two supports}&57{,}464\\
 \text{positive supports passing exact PSD}&632\\
 \text{negative-edge assignments tested}&3{,}647{,}592\\
 \text{signed labelled matrices}&1{,}152\\
 \text{matching-centralizer orbits}&2
 \end{array}
\]

In both orbits the signed matrix is the ordinary positive cycle \(C_{10}\).
The two orbits record the two relative positions of the fixed perfect matching
inside that cycle. Consequently

\[
 \boxed{S_1\cong S_2\cong S_3\cong C_{10}.}
\]

## 4. The final twenty-vertex component

Let

\[
 X_1=A_{14},\qquad
 X_3=A_{34},\qquad
 L=X_1X_3^{\mathsf T}.
\]

Every column of \(X_1\) and \(X_3\) contains one entry equal to one, and every
row contains two. The absence of 4-cycles makes \(L\) zero-one. Thus

\[
 L\mathbf1=2\mathbf1,
 \qquad
 L^{\mathsf T}\mathbf1=2\mathbf1.
\]

The intertwining identities give

\[
 A(C_{10})L=LA(C_{10}).
\]

There are exactly 140 labelled zero-one solutions and six orbits under the
independent dihedral actions on the two cycles. Their bipartite supports have
one, two or five connected components, with two orbits of each type.

For a fixed \(L\), label the twenty edges of its bipartite support and let
\(X_1,X_3\) be the corresponding endpoint-incidence matrices. The verifier
solves exactly for every symmetric matrix \(T\) satisfying

\[
 X_1T=A(C_{10})X_1,
 \qquad
 X_3T=A(C_{10})X_3,
\]

\[
 T\mathbf1=2\mathbf1,
 \qquad
 T_{ii}=0,
 \qquad
 T_{ij}\in\{-1,0,1\},
 \qquad
 T+2I\succeq0.
\]

For the six dihedral orbits, respectively, the exact data

\[
 \begin{array}{c|rrrrrr}
 \text{support components}&5&1&2&1&2&5\\
 \text{affine dimension}&10&0&1&0&1&10\\
 \text{entry-admissible points}&11664&1&2&1&2&7776\\
 \text{exact PSD completions}&1&1&1&1&1&1
 \end{array}
\]

are obtained. In every case the unique exact positive-semidefinite completion
is the ordinary unsigned graph

\[
 \boxed{T\cong C_{10}\sqcup C_{10}.}
\]

Its support is disconnected. But \(V_4\) is one connected component of the
signed complement by construction. This contradiction eliminates Type B.

## 5. Consequence

Both canonical order-50 quotient types are impossible. Therefore

\[
 \boxed{
 \text{no connected 6-regular strict WOW counterexample has order }50.
 }
\]

Combining this with the audited integral-excess order bound gives

\[
 \boxed{k=6\quad\Longrightarrow\quad n\le49.}
\]

This theorem does not assert that order 49 is attainable, does not classify
irregular counterexamples, and does not affect the explicit regular order-40
construction.

## 6. Independent verification

The primary exact verifier is run in two memory-isolated modes:

```text
python scripts/verify_order50_lift_exclusion.py --type-a
python scripts/verify_order50_lift_exclusion.py --type-b
```

It uses exact integer and rational linear algebra. Floating-point arithmetic is
used only to nominate a principal minor for rejection; every rejection is
confirmed by an exact Bareiss determinant, and every surviving candidate is
checked by exact rational positive semidefiniteness.

The independent replay is

```text
python scripts/verify_proof_audit_14c_order50_lifts.py
```

It does not import the primary verifier. It regenerates the cubic classes,
repeats the Type-A affine enumeration, and uses separately compiled C++
backends for the signed ten-vertex census and the exact twenty-vertex completion
filter:

```text
scripts/order50_lift_independent.cpp
scripts/order50_completion_filter.cpp
```

The two implementations reproduce the same Type-A orbit vector, the same
unique signed-pair orbit, the same zero binary lifts, all 140 Type-B
intertwiners, the same six dihedral orbits, and the same six disconnected exact
completions.
