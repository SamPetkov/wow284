# Layer-respecting perfect-matching deletions of the Hoffman--Singleton graph

**Status:** exact finite classification with symbolic characteristic polynomials and
Sturm/root-isolation certificates.  No manuscript claim or priority claim is made.

## 1. The family

Use the coordinate Hoffman--Singleton graph on

\[
 \{P_{i,j}:i,j\in\mathbb F_5\}\sqcup
 \{Q_{k,\ell}:k,\ell\in\mathbb F_5\}.
\]

For a permutation \(\pi\in S_5\), define

\[
 M_\pi=
 \bigl\{P_{i,j}Q_{\pi(i),\,i\pi(i)+j}:
 i,j\in\mathbb F_5\bigr\}.
\]

Every vertex occurs exactly once, so \(M_\pi\) is a perfect matching.  Put

\[
 G_\pi=G_{HS}-M_\pi.
\]

Each \(G_\pi\) is simple and 6-regular.  Deleting edges cannot create a triangle
or 4-cycle, and all same-layer pentagons remain; hence every member has girth
five.  Exact breadth-first search on the two orbit representatives below gives
diameter four, which then holds throughout their coordinate-automorphism
orbits.

## 2. Explicit coordinate automorphisms

Two finite families of automorphisms are sufficient to classify all 120
matchings.

### Type preserving

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 s\in\{1,-1\},\quad c=s/a.
\]

Then

\[
 P_{i,j}\longmapsto
 P_{ai+b,\,sj-ad i-bd},
\]

\[
 Q_{k,\ell}\longmapsto
 Q_{ck+d,\,s\ell+bc k}
\]

preserves all three edge types.  It sends \(M_\pi\) to
\(M_{\pi'}\), where

\[
 \pi'(ai+b)=c\pi(i)+d.
\]

### Type swapping

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 t\in\{2,-2\},\quad c=-t/a.
\]

Then

\[
 P_{i,j}\longmapsto
 Q_{ai+b,\,tj+da i+db},
\]

\[
 Q_{k,\ell}\longmapsto
 P_{ck+d,\,t\ell-cb k}
\]

is an automorphism and sends \(M_\pi\) to \(M_{\pi'}\), where

\[
 \pi'(c\pi(i)+d)=ai+b.
\]

The verifier checks each displayed map on every one of the 175
Hoffman--Singleton edges and checks its action on every one of the 120
matchings.

The generated action has exactly two orbits:

\[
 20+100=120.
\]

The first orbit consists precisely of the affine permutations
\(i\mapsto ai+b\); the second consists of all nonaffine permutations.  Since the
coordinate maps are graph automorphisms carrying the deleted matching to the
deleted matching, all graphs in one orbit are isomorphic.

## 3. Affine orbit

Take \(\pi(i)=i\).  Exact computation gives

\[
\begin{aligned}
\chi_A(x)={}&(x-6)(x-3)^4(x-1)^4(x+2)\\
&\cdot(x^4+2x^3-13x^2-14x+29)^2\\
&\cdot(x^4+2x^3-8x^2-9x+19)^8,
\end{aligned}
\]

and

\[
\begin{aligned}
\chi_D(x)={}&(x-106)(x-2)(x-1)^4(x+13)^4\\
&\cdot(x^2+x-1)^8(x^2+3x-9)^8\\
&\cdot(x^4+14x^3+13x^2-92x-16)^2.
\end{aligned}
\]

The factor \((x+13)^4\) shows that \(-13\) is a distance eigenvalue.  An exact
Sturm count proves that the product of all remaining factors has no root below
\(-13\), and direct substitution shows that none of those factors vanishes at
\(-13\).  Therefore

\[
 \lambda_{\min}(D)=-13.
\]

Since the graph is 6-regular,

\[
 \Phi=6-13=-7.
\]

## 4. Nonaffine orbit

Take \(\pi=(0,1,2,4,3)\).  The exact distance polynomial is

\[
\begin{aligned}
\chi_D(x)={}&(x-1)^3(x+13)^3(x^2-108x+191)\\
&\cdot(x^2+x-1)^2(x^2+3x-9)^2(x^2+12x-25)\\
&\cdot(x^8+8x^7-18x^6-80x^5+111x^4+200x^3\\
&\hspace{4em}-162x^2-136x-19)^2\\
&\cdot(x^8+18x^7+81x^6-21x^5-504x^4-225x^3\\
&\hspace{4em}+759x^2+265x-5)^2.
\end{aligned}
\]

The quadratic factor gives the root

\[
 -6-\sqrt{61}.
\]

Because \(61>(39/5)^2\),

\[
 -6-\sqrt{61}<-69/5.
\]

The square-free part of \(\chi_D\) is nonzero at \(-69/5\), and an exact Sturm
count gives exactly one distinct root in
\(( -\infty,-69/5)\).  Hence

\[
 \lambda_{\min}(D)=-6-\sqrt{61}.
\]

Thus

\[
 \Phi=6-6-\sqrt{61}=-\sqrt{61}<0.
\]

The adjacency polynomial for this representative is also recomputed exactly by
the verifier and differs from the affine polynomial.  The two orbit classes are
therefore spectrally distinct as well as disjoint under the displayed action.

## 5. Conclusion and search value

All 120 explicit layer-respecting perfect-matching deletions are exact negative
controls:

\[
 \delta^*=6,\qquad \lambda_{\min}(D)\le-13.
\]

This eliminates a natural attempt to obtain order-50 regular counterexamples by
puncturing the Hoffman--Singleton edge set while retaining every vertex.  It
does **not** classify arbitrary perfect matchings, arbitrary 6-regular induced
or spanning subgraphs, or all order-50 candidates.

The rejected distance-matrix shortcut is intentionally absent: a simple
bilinear formula proposed during exploration fails on the nonaffine
representative.  The final proof uses only coordinate automorphisms, exact BFS
distances, exact characteristic polynomials, and exact Sturm/root comparisons.
