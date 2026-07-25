# Diameter reduction for degree-six regular counterexamples

**Status:** exact analytic lemma introduced by Proof Audit 01.  
**Scope:** connected 6-regular graphs of girth at least five.

## Lemma

If \(G\) is a connected 6-regular strict counterexample to WOW-284 with girth at
least five, then

\[
  \operatorname{diam}(G)=3.
\]

## 1. Diameter at least four is impossible

Let \(u,v\) be vertices at distance

\[
  d=d_G(u,v)\ge4.
\]

The closed neighborhoods \(\{u\}\cup N(u)\) and \(\{v\}\cup N(v)\) are
disjoint.  Define a vector \(x\in\mathbb R^{V(G)}\) by

\[
 x_u=3,\qquad x_a=1\quad(a\in N(u)),
\]

\[
 x_v=-3,\qquad x_b=-1\quad(b\in N(v)),
\]

and \(x_z=0\) elsewhere.  Its squared norm is

\[
 \lVert x\rVert^2=2(3^2+6)=30.
\]

Because the graph has no triangles, two distinct neighbors of one vertex are
at distance exactly two.  Hence the total unordered contribution to
\(x^{\mathsf T}D(G)x/2\) from pairs lying in the same closed neighborhood is

\[
 2\left(6\cdot3+\binom62\cdot2\right)=96.
\]

For cross pairs, the triangle inequality gives

\[
 d_G(u,v)=d,
\]

\[
 d_G(u,b)\ge d-1,\qquad d_G(a,v)\ge d-1,
\]

and

\[
 d_G(a,b)\ge d-2
\]

for \(a\in N(u)\), \(b\in N(v)\).  Since all corresponding products of
coordinates have negative sign, these lower distance bounds give the upper
estimate

\[
 \frac12x^{\mathsf T}D(G)x
 \le
 96-9d-36(d-1)-36(d-2)
 =204-81d.
\]

Therefore

\[
 \frac{x^{\mathsf T}D(G)x}{\lVert x\rVert^2}
 \le
 \frac{204-81d}{15}
 \le -8.
\]

Thus

\[
 \lambda_{\min}(D(G))\le-8.
\]

Regularity gives \(\delta^*(G)=6\), so

\[
 \delta^*(G)+\lambda_{\min}(D(G))\le-2<0.
\]

Hence a degree-six strict counterexample cannot have diameter at least four.

## 2. Diameter two is impossible

Suppose instead that \(\operatorname{diam}(G)=2\).  Since \(G\) is 6-regular
and has no triangle or 4-cycle, the radius-two ball around every vertex has

\[
 1+6+6\cdot5=37
\]

vertices.  Diameter two therefore forces \(|V(G)|=37\), and the adjacency
matrix satisfies the Moore identity

\[
 A^2=5I-A+J.
\]

On \(\mathbf1^\perp\), every adjacency eigenvalue is a root of

\[
 x^2+x-5.
\]

The polynomial \(x^2+x-5\) is irreducible over \(\mathbb Q\), since its
discriminant is \(21\).  Because \(A\) has an integral characteristic
polynomial and the nonprincipal space has dimension \(36\), its characteristic
polynomial would have to be

\[
 (x-6)(x^2+x-5)^{18}.
\]

Its trace would then be

\[
 6+18(-1)=-12,
\]

contradicting \(\operatorname{tr}A=0\) for a simple graph.

Thus diameter two is impossible.  Diameter one is excluded by the girth
hypothesis.  Combined with the previous section, the only remaining diameter
is three.

## Consequence

Any theorem proved for connected 6-regular strict counterexamples under an
explicit diameter-three assumption may be promoted to all connected 6-regular
strict counterexamples only after citing this lemma.

The proof uses no classification of Moore graphs and no floating-point
spectral computation.