# Optimal-slack Gram hierarchy and near-ceiling reductions

**Status:** exact project derivation; manuscript promotion requires the usual
proof and literature audit.  
**Purpose:** unify the one-point LP ceiling, edge-local cycle bounds,
order-50 two-path constraints, and several low-degree order exclusions through
one positive-semidefinite matrix.

## 1. The optimal slack matrix

Let `G` be a connected `k`-regular graph of girth at least five and diameter
three, with adjacency matrix `A`, order `n`, and all nonprincipal adjacency
eigenvalues in the closed shifted WOW interval

\[
 I_k=[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
\]

Put

\[
 g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),
\]

\[
 C_k=g_k(k)=(k+2)^2(k^2+3),
\]

and define

\[
 \boxed{
 \mathcal M_k(G)=-g_k(A)+\frac{C_k}{n}J.
 }
\]

Then

\[
 \boxed{\mathcal M_k(G)\succeq0},
 \qquad
 \boxed{\mathcal M_k(G)\mathbf1=0}.
\]

Indeed, on the principal adjacency eigenspace, the two terms cancel.  On an
adjacency eigenvector of nonprincipal eigenvalue `theta`, the eigenvalue of
`mathcal M_k(G)` is

\[
 \bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2\ge0.
\]

The nonbacktracking expansion is

\[
 g_k=6(k+2)F_0+2(2k+7)F_1+(k+13)F_2+6F_3+F_4.
\]

Since the girth-five trace identities annihilate `F_1,...,F_4`,

\[
 \boxed{
 \operatorname{tr}\mathcal M_k(G)
 =C_k-6(k+2)n
 =6(k+2)(B_k-n),
 }
\]

where

\[
 B_k=\frac{(k+2)(k^2+3)}6.
\]

Equivalently,

\[
 \boxed{
 6(k+2)(B_k-n)
 =\sum_{\theta\ne k}
 \bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2.
 }
\]

This is the spectral-defect identity behind the exact LP ceiling.

If the nonprincipal spectrum lies in the **open** shifted interval, then

\[
 \boxed{
 \ker\mathcal M_k(G)
 =\langle\mathbf1\rangle\oplus E_{-2}(A).
 }
\]

Thus the global trace bound, the edge-local inequalities, and the order-50
three-vertex inequalities are respectively the trace, `2 x 2` principal-minor,
and `3 x 3` principal-minor levels of one optimal slack matrix.  Larger
principal minors define a canonical local semidefinite hierarchy beyond the
one-variable LP ceiling.

## 2. A universal equality exclusion for off-diagonal entries

The diagonal of `mathcal M_k(G)` is constant:

\[
 a_{k,n}=\frac{C_k}{n}-6(k+2).
\]

For distinct vertices `u,v`, positive semidefiniteness gives

\[
 |(\mathcal M_k)_{uv}|\le a_{k,n}.
\]

In the strict-window regime, equality

\[
 (\mathcal M_k)_{uv}=a_{k,n}
\]

is impossible.  It would imply

\[
 e_u-e_v\in\ker\mathcal M_k\cap\mathbf1^\perp=E_{-2}(A).
\]

But the `u`-coordinate of `A(e_u-e_v)` is `-1` when `u~v` and `0` when
`u` and `v` are nonadjacent, whereas the `u`-coordinate of
`-2(e_u-e_v)` is `-2`.

This small observation is what turns several closed interval squeezes below
into strict discrete classifications.

## 3. Entry formulas

For an edge `uv`, let `sigma_uv` denote the number of five-cycles through that
edge.  Then

\[
 (g_k(A))_{uv}=4k+14+\sigma_{uv}.
\]

For vertices `u,w` at distance two, choose their unique common neighbour and
write

\[
 r_{uw}=6\alpha_{uw}+\beta_{uw},
\]

where `alpha` and `beta` count the five- and six-cycles through the resulting
two-path.  Then

\[
 (g_k(A))_{uw}=2k+7+r_{uw}.
\]

For vertices `u,z` at distance three, put

\[
 \gamma_{uz}=(A^4)_{uz}.
\]

Then

\[
 (g_k(A))_{uz}=6+\gamma_{uz}.
\]

The `2 x 2` minors therefore give the exact interval bounds

\[
 2k-2\le\sigma_{uv}
 \le \frac{2C_k}{n}-10k-26,
\]

\[
 4k+5\le r_{uw}
 \le \frac{2C_k}{n}-8k-19,
\]

\[
 6k+6\le\gamma_{uz}
 \le \frac{2C_k}{n}-6k-18.
\]

The lower endpoint in each interval is excluded by the preceding kernel
argument.

## 4. The order-50 signed-root reduction

Assume now that `k=6`, `n=50`, and the shifted window is strict.  Put

\[
 g_6(x)=(x+2)^2((x+1)^2-10)
\]

and

\[
 \boxed{
 T=50J-g_6(A)-2I.
 }
\]

Then

\[
 \boxed{T\mathbf1=2\mathbf1},
 \qquad
 \boxed{T+2I\succeq0}.
\]

Moreover, `T` has zero diagonal and every off-diagonal entry lies in
`{-1,0,1}`.  More precisely:

- on an edge, `T_uv=12-sigma_uv`, so the values are `0,-1`;
- at distance two, `T_uw=31-r_uw`, so the values are `1,0,-1`;
- at distance three, `T_uz=44-gamma_uz`, so the values are `1,0,-1`.

The possible equality value `2` at distance two or three is excluded by the
kernel argument above.  Thus `T+2I` is a positive-semidefinite integral Gram
matrix with diagonal two and off-diagonal entries in `{-1,0,1}`.  Equivalently,
a hypothetical order-50 candidate produces fifty norm-`sqrt(2)` vectors with
pairwise inner products in `{-1,0,1}` and constant signed row sum two.

The centered optimal slack is recovered from

\[
 \boxed{
 25\mathcal M_6=25(T+2I)-2J.
 }
\]

This is a root-type reformulation of the unresolved order-50 problem.

### A new neighbourhood inequality

Let `H` be the high-edge subgraph, so an edge is in `H` when it lies in
thirteen five-cycles.  For a vertex `v`, put

\[
 d=d_H(v)\in\{0,2,4\}
\]

and

\[
 R_v=\sum_{\{u,w\}\subseteq N(v)}r_{uvw}.
\]

For a real parameter `a`, apply `T+2I\succeq0` to

\[
 x=a e_v+\sum_{u\in N(v)}e_u.
\]

Since `T_vu=-1` on a high edge and zero on a low edge, while
`T_uw=31-r_uvw` for two neighbours of `v`,

\[
 x^{\mathsf T}(T+2I)x
 =2a^2-2da+942-2R_v\ge0.
\]

Minimizing at `a=d/2` gives

\[
 R_v\le471-\frac{d^2}{4}.
\]

Equality would put `x` in the kernel of `T+2I`, which is orthogonal to
`mathbf1`, but `x` has positive coordinate sum `6+d/2`.  Therefore

\[
 \boxed{
 R_v\le470-\frac{d_H(v)^2}{4}.
 }
\]

In particular the three local upper bounds are

\[
 d_H(v)=0,2,4
 \quad\Longrightarrow\quad
 R_v\le470,469,466.
\]

Summing over all vertices and using

\[
 \sum_vR_v=30N_5+6N_6,
 \qquad
 N_5=360+\frac m5,
 \qquad
 S_2=\sum_vd_H(v)^2,
\]

gives the exact consequence

\[
 \boxed{
 N_6\le \frac{6350}{3}-m-\frac{S_2}{24}.
 }
\]

The existing shifted-moment upper bound is numerically stronger after coarse
profile aggregation, so this does not reduce the current count of 266 coarse
profiles.  Its value is structural: it is a genuine seven-vertex neighbourhood
constraint that is invisible to the separate `3 x 3` two-path minors.

## 5. Near-ceiling collapse at degrees seven, eight, and nine

The same slack matrix improves the low-degree order windows.

### Degree seven: order 76 is impossible

Suppose `k=7`, `n=76`.  Then the diagonal of `mathcal M_7` is `27/19`.
The integer interval bounds and the strict exclusion of their lower endpoints
show that every off-diagonal entry is either `8/19` or `-11/19`.

Let `X` be the graph joining pairs with slack entry `8/19`.  Then

\[
 19\mathcal M_7=38I-11J+19A(X).
\]

The zero row sum gives

\[
 X\text{ is }42\text{-regular},
\]

and on `mathbf1^perp`, positive semidefiniteness gives

\[
 \lambda_{\min}(A(X))\ge-2.
\]

Since `42>76/2`, the graph `X` is connected.  The classical classification of
connected regular graphs with least eigenvalue at least `-2` and more than 28
vertices says that `X` is a line graph or a cocktail-party graph.  It is not a
cocktail-party graph, whose degree would be 74.

If `X=L(Y)`, regularity of the line graph forces `Y` to be regular or
semiregular bipartite.  In the regular case, the degree of `Y` would be 22 and

\[
 |V(Y)|=\frac{2\cdot76}{22}=\frac{76}{11},
\]

impossible.  In the semiregular bipartite case, the two degrees `r,s` divide 76
and satisfy `r+s=44`; no pair of divisors of 76 has this sum.  Hence order 76 is
impossible.

Therefore a degree-seven diameter-three strict counterexample has

\[
 \boxed{n\le74}.
\]

### Degree eight: orders 110 and 109 are impossible

For `k=8`, `n=110`, the diagonal is `10/11`.  The interval bounds and kernel
exclusion force every off-diagonal entry to be `-1/11`, contradicting the zero
row sum.

For `k=8`, `n=109`, every off-diagonal entry is `51/109` or `-58/109`.  Let `X`
join the pairs of the first type.  Then

\[
 109\mathcal M_8=218I-58J+109A(X).
\]

The graph `X` is 56-regular, connected, and has least eigenvalue at least
`-2`.  It is neither a cocktail-party graph nor a line graph: a regular root
graph would have degree 29 and `218/29` vertices, while a semiregular bipartite
root graph would require two divisors of the prime 109 summing to 58.

Thus

\[
 \boxed{n\le108}
\]

for degree-eight regular strict counterexamples.

### Degree nine: order 152 is impossible

For `k=9`, `n=152`, the diagonal is `33/38`.  The integer interval bounds and
kernel exclusion force every off-diagonal entry to be `-5/38`, again
contradicting the zero row sum.  Since the handshake lemma forces even order,

\[
 \boxed{n\le150}
\]

for degree-nine regular strict counterexamples.

The improved low-degree windows are therefore

\[
 \boxed{
 \begin{array}{rcl}
 k=6&:&n\le50,\\
 k=7&:&n=50\text{ in diameter two, or }n\le74\text{ in diameter three},\\
 k=8&:&n\le108,\\
 k=9&:&n\le150.
 \end{array}
 }
\]

## 6. Literature boundary

The optimal slack matrix and its specialization to the shifted WOW window are
project-derived.  The classification input used only for the degree-seven and
degree-eight near-ceiling exclusions is classical: connected regular graphs
with least eigenvalue at least `-2` are line graphs, cocktail-party graphs, or
exceptional graphs represented in `E_8`; the exceptional regular graphs have at
most 28 vertices.  A suitable reference is Cvetkovic--Rowlinson--Simic,
*Spectral Generalizations of Line Graphs*, Cambridge University Press, 2004,
Chapter 4.

No claim is made here that the root-system classification itself is new.

## 7. Promotion recommendation

The general slack-matrix proposition and spectral-defect identity should be
promoted: they unify three existing proof levels without lengthening the paper
substantially.  The improved degree-seven through degree-nine windows are also
clean theorem-level gains.  The order-50 signed-root reduction is valuable as a
short structural reformulation and a guide to the next local semidefinite step.

The neighbourhood `N_6` inequality is exact but does not shrink the current
coarse-profile count; it is best presented as a structural corollary rather
than advertised as a numerical breakthrough.
