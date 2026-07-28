# Two Gram hierarchies for WOW-284

**Status:** exact synthesis of audited results, with one new deletion corollary.

The structural results in the manuscript can be organized around two related
Gram constructions.

## 1. The obstruction Gram matrix

For a regular diameter-three strict candidate, the optimal LP polynomial gives

\[
 M_k=-g_k(A)+\frac{C_k}{n}J\succeq0.
\]

Its trace gives the one-variable LP defect, its integral excess matrix gives the
stronger graph-order bound, and its principal minors give edge, path, and
neighbourhood constraints.

This is the hierarchy

\[
 \text{trace}
 \longrightarrow
 \text{integral excess}
 \longrightarrow
 2\times2\text{ minors}
 \longrightarrow
 3\times3\text{ minors}
 \longrightarrow
 \text{larger local minors}.
\]

## 2. The deletion Gram correction

Let `M` now be a degree-`k` Moore graph, let `S` have size `s<=k-1`, and put
`H=M-S`. Let `B` be the surviving-vertex by deleted-vertex incidence matrix,
so

\[
 B_{xz}=1
 \quad\Longleftrightarrow\quad
 x\sim_M z.
\]

The audited small-puncture normal form is

\[
 D(H)=D(M)[V(H)]+E_S,
\]

where

\[
 \boxed{
 E_S=BB^{\mathsf T}-\operatorname{diag}(BB^{\mathsf T}).
 }
\]

Put

\[
 t_x=|N_M(x)\cap S|,
 \qquad
 \tau(S)=\max_{x\in V(H)}t_x.
\]

Since `BB^T` is positive semidefinite and
`diag(BB^T)=diag(t_x)`, one has

\[
 \boxed{
 \lambda_{\min}(E_S)\ge-\tau(S).
 }
\]

The exact dual-degree formula is

\[
 \delta^*(H)=k-\frac{s}{k}.
\]

Combining these facts with the deletion-stability inequality gives the
configuration-sensitive bound

\[
 \boxed{
 \Phi(H)
 \ge
 k-\frac{3+\sqrt{4k-3}}2
 -\frac{s}{k}
 -\tau(S).
 }
\]

Because `tau(S)<=s`, every deletion set of size `s<=k-1` is guaranteed to
remain strict whenever

\[
 s\left(1+\frac1k\right)
 <
 k-\frac{3+\sqrt{4k-3}}2.
\]

Equivalently, define

\[
 r_k=\min\left\{
 k-1,
 \left\lceil
 \frac{k}{k+1}
 \left(k-\frac{3+\sqrt{4k-3}}2\right)
 \right\rceil-1
 \right\}.
\]

Then every deletion of at most `r_k` vertices is a strict counterexample.

For the Hoffman--Singleton graph, `k=7`, the uniform theorem gives `r_7=2`.
The exact orbitwise positive-definiteness calculation improves this to the
sharp universal radius five. Thus the finite orbit theorem is not merely a
large computation: it measures the gain over the general Gram perturbation
bound.

For a hypothetical degree-57 Moore graph, the parent score is 48 and the same
uniform estimate gives `r_57=47`.

## 3. Common mechanism

Both hierarchies begin with a Gram matrix and then subtract or remove a highly
structured low-dimensional component:

- the obstruction matrix centers a polynomial in the adjacency matrix by its
  principal `J` component;
- the deletion correction is the incidence Gram matrix `BB^T` with its diagonal
  removed.

The first hierarchy converts a global spectral window into integral and local
combinatorial restrictions. The second converts deleted-neighbour incidence
into quantitative stability. This gives a single conceptual narrative for the
paper's obstruction and deletion halves.
