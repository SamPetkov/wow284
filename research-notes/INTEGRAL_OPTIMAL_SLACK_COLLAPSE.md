# Integral collapse of the optimal slack matrix

**Status:** exact project derivation under Proof Audit 14.
**Scope:** connected `k`-regular girth-five graphs of diameter three whose
nonprincipal adjacency spectrum lies in the open shifted WOW interval.

## 1. Integer off-diagonal squeeze

Retain the notation

\[
 g_k(x)=(x+2)^2((x+1)^2-(2k-2)),
 \qquad
 C_k=(k+2)^2(k^2+3),
\]

and put

\[
 h_k=6(k+2),
 \qquad
 M=-g_k(A)+\frac{C_k}{n}J.
\]

The optimal-slack argument gives

\[
 M\succeq0,
 \qquad
 M\mathbf1=0,
 \qquad
 M_{uu}=a:=\frac{C_k}{n}-h_k.
\]

For distinct vertices define the integer

\[
 z_{uv}=(g_k(A))_{uv}\in\mathbb Z.
\]

The `2 x 2` principal minor on `u,v` gives

\[
 \left|\frac{C_k}{n}-z_{uv}\right|\le a.
\]

The upper equality case `M_uv=a` is impossible in the strict shifted window:
it would put `e_u-e_v` in the adjacency `-2` eigenspace, contradicting the
`u`-coordinate of that eigenvalue equation. Therefore

\[
 \boxed{
 h_k+1\le z_{uv}\le \frac{2C_k}{n}-h_k
 }
 \qquad(u\ne v).
\]

## 2. The one-level case is impossible

Set

\[
 Q_{k,n}=\left\lfloor\frac{2C_k}{n}-h_k\right\rfloor.
\]

Suppose first that `Q_{k,n}=h_k+1`. Then every off-diagonal entry of `g_k(A)`
equals `h_k+1`, while its diagonal equals `h_k`. Hence

\[
 \boxed{
 g_k(A)=(h_k+1)J-I.
 }
\]

On `mathbf1` this forces `C_k+1=(h_k+1)n`. More importantly, on
`mathbf1^perp` it gives

\[
 (g_k(A)+I)|_{\mathbf1^\perp}=0.
\]

The polynomial

\[
 p_k(x)=g_k(x)+1
\]

is irreducible over the rationals for every integer `k`. Indeed, after the
translation `y=x+2`,

\[
 p_k(y-2)=y^4-2y^3+(3-2k)y^2+1.
\]

Its only possible rational roots are `1` and `-1`, but their values are
`3-2k` and `7-2k`, neither zero for integral `k`. If it factored into two monic
integer quadratics, their constant terms would be both `1` or both `-1`. In the
first case the coefficients of `y^3` and `y` would be equal; in the second they
would be negatives. They cannot be `-2` and `0`.

Thus the rational space `mathbf1^perp` is a module over the degree-four field
`Q[x]/(p_k)`. Write its dimension as `4m`. The characteristic polynomial of
`A|_{mathbf1^perp}` is then `p_k^m`. Since the sum of the four roots of `p_k` is
`-6`, the trace equation gives

\[
 0=\operatorname{tr}A=k-6m.
\]

Therefore `m=k/6` and

\[
 n-1=4m=\frac{2k}{3},
\]

contradicting the elementary bound `n>=k+1` for a simple `k`-regular graph.
Hence the one-level case never occurs.

A strict candidate must therefore have

\[
 Q_{k,n}\ge h_k+2.
\]

Equivalently,

\[
 \boxed{
 n\le
 \left\lfloor
 \frac{(k+2)^2(k^2+3)}{6(k+2)+1}
 \right\rfloor.
 }
\]

Writing

\[
 B_k=\frac{(k+2)(k^2+3)}6=\frac{C_k}{h_k},
\]

the unrounded bound is

\[
 \frac{C_k}{h_k+1}
 =B_k-\frac{B_k}{h_k+1}.
\]

Thus integrality improves the exact one-variable LP ceiling by an asymptotic
amount `k^2/36`, before any local cycle or graph-classification input is used.
In particular it gives immediately

\[
 (k,n)=(5,32),(6,51),(8,110),(9,152)
\]

as impossible. If `Q_{k,n}\le h_k`, no integer off-diagonal entry is available
at all; this excludes `(k,n)=(8,111)` directly.

The degree-six order-51 result therefore has a short global proof. The
edge-five-cycle contradiction remains useful as the local combinatorial
manifestation of the same optimal slack matrix.

## 3. Two-level collapse

Suppose

\[
 Q_{k,n}=h_k+2.
\]

Then every off-diagonal entry of `g_k(A)` is `h_k+1` or `h_k+2`. Let `X` be the
graph joining pairs of the first type. Since

\[
 a=\frac{C_k}{n}-h_k,
\]

one has the exact identities

\[
 \boxed{
 M=2I+(a-2)J+A(X)
 }
\]

and

\[
 \boxed{
 A(X)=(h_k+2)J-2I-g_k(A).
 }
\]

The zero row sum makes `X` regular of degree

\[
 \boxed{
 d_X=(h_k+2)n-C_k-2.
 }
\]

On the orthogonal complement of `mathbf1`,

\[
 2I+A(X)\succeq0,
\]

so

\[
 \boxed{
 \lambda_{\min}(A(X))\ge-2.
 }
\]

Moreover `A` and `A(X)` commute and are simultaneously diagonalizable. In the
strict shifted window,

\[
 E_{-2}(A(X))=E_{-2}(A).
\]

This is the general source of the auxiliary relation graphs used in the
near-ceiling degree-seven and degree-eight exclusions.

When `n>28` and `X` is connected, the classical least-eigenvalue-minus-two
classification reduces `X` to a line graph or a cocktail-party graph. The
remaining possibilities can be tested arithmetically:

- a cocktail-party graph has degree `n-2`;
- if `X=L(Y)` and `Y` is regular of degree `r`, then
  `d_X=2(r-1)` and `r` divides `2n`;
- if `Y` is semiregular bipartite of degrees `r,s`, then `r` and `s` divide
  `n` and satisfy `r+s=d_X+2`.

## 4. Consequences currently used

For `k=5`, the universal integral bound gives `n<=31`; parity gives `n<=30`.
For `k=6`, it gives `n<=50` directly.

For `k=7,n=76`, the relation graph is 42-regular on 76 vertices. It is neither
cocktail-party nor a possible regular or semiregular line graph. Hence the
largest diameter-three order at degree seven is at most 74.

For `k=8,n=109`, the relation graph is 56-regular on 109 vertices and the same
classification-and-divisibility argument excludes it. Together with the
global integral bound, this gives order at most 108.

For `k=9`, the universal bound gives `n<=151`; parity gives `n<=150`.

Thus

\[
 \boxed{
 \begin{array}{rcl}
 k=5&:&n\le30,\\
 k=6&:&n\le50,\\
 k=7&:&n=50\text{ in diameter two, or }n\le74\text{ in diameter three},\\
 k=8&:&n\le108,\\
 k=9&:&n\le150.
 \end{array}
 }
\]

## 5. Literature boundary

The integral slack-collapse theorem, irreducibility argument, order
improvement, and auxiliary relation graph are project-derived. The only
external theorem in the final classification step is the classical result
that a connected regular graph with more than 28 vertices and least
eigenvalue at least `-2` is a line graph or a cocktail-party graph. This
follows from the classification of Cameron--Goethals--Seidel--Shult,
*Journal of Algebra* 43 (1976), 305--327, DOI
`10.1016/0021-8693(76)90162-9`; the statement is also recalled explicitly in
the introduction of Koolen--Yu--Liang--Choi--Markowsky, *European Journal of
Combinatorics* 126 (2025), Article 104118, DOI
`10.1016/j.ejc.2024.104118`.
