# Canonical signed-component quotients at the degree-six order-50 boundary

**Status:** exact finite classification under Proof Audit 14; manuscript promotion
requires a second source review and green current-head CI.  
**Scope:** a hypothetical connected 6-regular graph of order 50, girth at least
five and diameter three satisfying the strict shifted WOW window.  
**Nonclaim:** the classification below does not eliminate either surviving
four-cell quotient and therefore does not prove nonexistence at order 50.

## 1. Correction and starting point

Let

\[
 g_6(x)=(x+2)^2((x+1)^2-10)
\]

and let

\[
 S=50J-g_6(A)-2I
\]

be the signed complement.  The audited signed-complement construction gives

\[
 S\mathbf1=2\mathbf1,
 \qquad
 S+2I\succeq0,
 \qquad
 S_{uv}\in\{-1,0,1\}\quad(u\ne v).
\]

An earlier exploratory argument used an incorrect cubic factor in
\(g_6(x)+4\).  The correct factorization is

\[
 \boxed{
 g_6(x)+4=(x+4)(x^3+2x^2-5x-8).
 }
\]

All three roots of the irreducible cubic lie in the strict shifted WOW interval,
so the cubic primary module cannot be discarded.  The unconditional order-50
exclusion based on the incorrect factorization is withdrawn.

The independent signed-root argument still proves that the underlying signed
graph of \(S\) is disconnected.  Let its connected components have vertex sets
\(V_1,\ldots,V_c\), sizes \(n_1,\ldots,n_c\), and let \(Q=(q_{ij})\) be the
adjacency quotient of the original graph \(G\) over this partition.  Because
\(A\) and \(S\) commute, the component-indicator space is \(A\)-invariant.

## 2. Five possible primary types

Write

\[
 q(x)=x^3+2x^2-5x-8.
\]

On the component-indicator space orthogonal to \(\mathbf1\), the matrix \(Q\) is
annihilated by

\[
 (x+4)q(x).
\]

Let \(a\) be the multiplicity of \(-4\) and let \(b\) be the number of cubic
primary blocks.  Then

\[
 c=1+a+3b.
\]

Since the roots of \(q\) sum to \(-2\),

\[
 \operatorname{tr}Q=6-4a-2b.
\]

The diagonal entries of an adjacency quotient are nonnegative integers, so
\(2a+b\le3\).  The only possibilities are

\[
 \boxed{
 (a,b,c)\in
 \{(1,0,2),(0,1,4),(1,1,5),(0,2,7),(0,3,10)\}.
 }
\]

This is the first major simplification: every disconnected signed-complement
case has at most ten cells.

## 3. Exact quotient constraints

Every quotient in the list above satisfies the following necessary conditions.

1. **Nonnegative integral regularity**
   \[
    Q\ge0,
    \qquad
    Q\mathbf1=6\mathbf1.
   \]
2. **Detailed balance**
   \[
    n_iq_{ij}=n_jq_{ji},
    \qquad
    \sum_i n_i=50.
   \]
3. **Simple internal cells**
   \[
    0\le q_{ii}\le n_i-1,
    \qquad
    n_iq_{ii}\equiv0\pmod2.
   \]
   If \(q_{ii}\ge2\), the induced girth-five cell obeys
   \(n_i\ge q_{ii}^2+1\).
4. **Biregular four-cycle obstruction**
   \[
    n_iq_{ij}(q_{ij}-1)\le n_j(n_j-1)
   \]
   and the symmetric inequality with \(i,j\) exchanged.
5. **Radius-two inequalities**
   \[
    (Q^2)_{ij}-6\delta_{ij}
    \le n_j-\delta_{ij}-q_{ij}.
   \]
6. **Polynomial identity**
   \[
    (Q^4+6Q^3+3Q^2-28Q-32I)_{ij}=50n_j.
   \]
   When \(a=0\), this reduces to the cubic identity
   \[
    \boxed{
    Q^3+2Q^2-5Q-8I=5\mathbf1(n_1,\ldots,n_c).
    }
   \]

The quotient is symmetrizable by
\(\operatorname{diag}(\sqrt{n_1},\ldots,\sqrt{n_c})\), so the polynomial
identities account for the complete primary decomposition rather than merely a
formal annihilator.

## 4. Canonical enumeration

An exact isomorphism-reduced enumeration gives the following counts after the
internal parity and Moore-ball filters.

\[
\begin{array}{c|ccccc}
 c&2&4&5&7&10\\
\hline
 \text{canonical quotients}&1&3&0&0&0.
\end{array}
\]

The seven-cell backend explores 13,561,449 branch nodes and 5,380 complete
row-sum leaves.  The ten-cell backend explores 7,860,789 branch nodes.  In the
ten-cell case, the diagonal cubic identity forces all ten cell sizes to be even,
reducing the 16,928 nondecreasing partitions of 50 to 164 before the quotient
search begins.

### 4.1 The two-cell case

The unique quotient is

\[
 (n_1,n_2)=(20,30),
 \qquad
 Q=
 \begin{pmatrix}
 0&6\\
 4&2
 \end{pmatrix}.
\]

This is the cubic-free branch.  The previously audited incidence-design and
block-trace argument excludes it without using the incorrect cubic
factorization.

### 4.2 The four-cell case

The first canonical quotient has sizes \((2,12,12,24)\).  It is impossible
because a signed component on two vertices, with zero diagonal and entries in
\(\{-1,0,1\}\), cannot have signed row sum two.

Exactly two canonical quotient types remain.

#### Type A

\[
 (n_1,n_2,n_3,n_4)=(6,8,12,24),
\]

\[
 \boxed{
 Q_A=
 \begin{pmatrix}
 2&0&0&4\\
 0&0&3&3\\
 0&2&0&4\\
 1&1&2&2
 \end{pmatrix}.
 }
\]

#### Type B

\[
 (n_1,n_2,n_3,n_4)=(10,10,10,20),
\]

\[
 \boxed{
 Q_B=
 \begin{pmatrix}
 1&0&3&2\\
 0&1&1&4\\
 3&1&0&2\\
 1&2&1&2
 \end{pmatrix}.
 }
\]

The matrices are stated up to simultaneous permutation of rows, columns and
cell sizes.

Thus any hypothetical order-50 candidate has a disconnected signed complement
with exactly four components and one of the two quotient types above.

## 5. A local uniqueness result in Type A

The six-vertex signed component in Type A has zero diagonal, off-diagonal
entries in \(\{-1,0,1\}\), signed row sum two, connected support, and least
eigenvalue at least \(-2\).  Exhaustive exact enumeration, followed by
isomorphism reduction, leaves one type:

\[
 \boxed{
 \text{the component is the unsigned positive cycle }C_6.
 }
\]

This is uniqueness up to relabelling; no switching operation is used.

## 6. Consequences and remaining search

The corrected order-50 boundary has been reduced from an unrestricted
6-regular graph search to two explicit four-cell systems.

For Type A:

- the 6-cell is an induced \(C_6\);
- the 8- and 12-cells are independent;
- the 24-cell is 2-regular;
- every vertex of the 24-cell has a unique neighbour in the 6-cell.

For Type B:

- two 10-cells induce perfect matchings;
- one 10-cell is independent;
- the 20-cell is 2-regular;
- the cross-block degrees are fixed by \(Q_B\).

The next exact stage is therefore a block-design classification inside these two
quotient types, using the zero off-component blocks of
\(S=50J-g_6(A)-2I\), rather than a search over all order-50 regular graphs.

## 7. Verification

The primary verifier is

```text
scripts/verify_order50_component_quotients.py
```

and its exhaustive compiled backends are

```text
scripts/order50_component_quotients_c7.cpp
scripts/order50_component_quotients_c10.cpp
```

They check the complete quotient constraints, canonical reduction, the empty
5-, 7- and 10-cell cases, the two surviving four-cell quotients, and uniqueness
of the six-vertex signed component.  No floating-point eigenvalue decision is
used.
