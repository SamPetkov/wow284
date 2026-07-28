# Integral collapse of the optimal slack matrix

**Status:** exact project derivation under Proof Audit 14.  
**Scope:** connected `k`-regular girth-five graphs of diameter three whose
nonprincipal adjacency spectrum lies in the open shifted WOW interval.

## 1. General theorem

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

In particular,

\[
 \boxed{
 n\le
 \left\lfloor
 \frac{2(k+2)^2(k^2+3)}{12(k+2)+1}
 \right\rfloor.
 }
\]

Writing

\[
 B_k=\frac{(k+2)(k^2+3)}6=\frac{C_k}{h_k},
\]

the unrounded bound is

\[
 \frac{2C_k}{2h_k+1}
 =B_k-\frac{B_k}{2h_k+1}.
\]

Thus integrality improves the exact one-variable LP ceiling by an asymptotic
amount `k^2/72`, before any local cycle or graph-classification input is used.

## 2. One-level collapse

Set

\[
 Q_{k,n}=\left\lfloor\frac{2C_k}{n}-h_k\right\rfloor.
\]

If `Q_{k,n}=h_k+1`, every off-diagonal entry of `g_k(A)` equals `h_k+1`.
The zero row sum of `M` then forces

\[
 \boxed{
 C_k+1=(h_k+1)n.
 }
\]

Hence every order in this one-level range is excluded unless this exact
divisibility identity holds.

This immediately excludes:

\[
 (k,n)=(5,32),\quad(6,51),\quad(8,110),\quad(9,152).
\]

The degree-six order-51 exclusion therefore has a second proof that is shorter
than the edge-five-cycle incidence contradiction. The latter remains useful as
the local combinatorial manifestation of the same slack matrix.

If `Q_{k,n}\le h_k`, no integer off-diagonal entry is available at all. This
excludes `(k,n)=(8,111)` directly.

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

one has the exact identity

\[
 \boxed{
 M=2I+(a-2)J+A(X).
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

This is the general source of the auxiliary relation graphs used in the
near-ceiling degree-seven and degree-eight exclusions.

When `n>28` and `X` is connected, the classical least-eigenvalue-minus-two
classification reduces `X` to a line graph or a cocktail-party graph. The
remaining possibilities can then be tested arithmetically:

- a cocktail-party graph has degree `n-2`;
- if `X=L(Y)` and `Y` is regular of degree `r`, then
  `d_X=2(r-1)` and `r` divides `2n`;
- if `Y` is semiregular bipartite of degrees `r,s`, then `r` and `s` divide
  `n` and satisfy `r+s=d_X+2`.

## 4. Consequences currently used

For `k=7,n=76`, the relation graph is 42-regular on 76 vertices. It is neither
cocktail-party nor a possible regular or semiregular line graph. Hence the
largest diameter-three order at degree seven is at most 74.

For `k=8,n=109`, the relation graph is 56-regular on 109 vertices and the same
classification-and-divisibility argument excludes it. Together with the
zero-level exclusion at 111 and the one-level exclusion at 110, this gives
order at most 108.

The one-level collapse at `k=9,n=152`, followed by parity, gives order at most
150.

## 5. Literature boundary

The integral slack-collapse theorem, the order improvement, and the auxiliary
relation graph are project-derived. The only external theorem in the final
classification step is the classical result that a connected regular graph
with more than 28 vertices and least eigenvalue at least `-2` is a line graph or
a cocktail-party graph. See Cvetkovic, Rowlinson and Simic, *Spectral
Generalizations of Line Graphs*, Cambridge University Press, 2004, Theorem
3.12.2; the same statement is recalled in the introduction of Koolen--Yu--Liang--
Choi--Markowsky, *European Journal of Combinatorics* 126 (2025), Article
104118, DOI `10.1016/j.ejc.2024.104118`.
