# Layer-respecting perfect-matching deletions of the Hoffman--Singleton graph

**Status:** exact finite classification with symbolic characteristic polynomials,
Sturm certificates, and a dedicated line-by-line audit. No manuscript claim or
priority claim is made.

## 1. The family and classification theorem

Use the coordinate Hoffman--Singleton graph on

\[
 \{P_{i,j}:i,j\in\mathbb F_5\}\sqcup
 \{Q_{k,\ell}:k,\ell\in\mathbb F_5\}.
\]

For a permutation \(\pi\in S_5\), define

\[
 M_\pi=
 \bigl\{P_{i,j}Q_{\pi(i),\,i\pi(i)+j}:
 i,j\in\mathbb F_5\bigr\},
\]

and put

\[
 G_\pi=G_{HS}-M_\pi.
\]

### Theorem

The 120 labelled graphs \(G_\pi\) form exactly two isomorphism classes.

- The 20 affine permutations \(\pi(i)=ai+b\), \(a\ne0\), give graphs with
  \[
  \lambda_{\min}(D)=-13,
  \qquad
  \Phi=-7.
  \]
- The 100 nonaffine permutations give graphs with
  \[
  \lambda_{\min}(D)=-6-\sqrt{61},
  \qquad
  \Phi=-\sqrt{61}.
  \]

Every member is connected, simple, 6-regular, of order 50, girth five, and
diameter four.

## 2. Why \(M_\pi\) is a perfect matching

Each \(P_{i,j}\) occurs once by definition. Conversely, fix \(Q_{k,\ell}\).
There is a unique \(i=\pi^{-1}(k)\), and then the equation

\[
 i\pi(i)+j=\ell
\]

has the unique solution \(j=\ell-ik\). Thus every \(Q\)-vertex occurs exactly
once, and \(M_\pi\) is a perfect matching of 25 Hoffman--Singleton edges.

Each \(G_\pi\) is therefore simple and 6-regular. Deleting edges cannot create a
triangle or 4-cycle, while all same-layer pentagons remain. Hence every member
has girth exactly five. Exact breadth-first search on all 120 labelled members
gives diameter four and, in particular, connectedness.

## 3. Explicit coordinate automorphisms

Two finite families of automorphisms generate two orbits on the 120 matchings.
The algebra preserving the cross edges is included explicitly.

### 3.1 Type preserving

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 s\in\{1,-1\},\quad c=s/a.
\]

Define

\[
 P_{i,j}\longmapsto
 P_{ai+b,\,sj-ad i-bd},
\]

\[
 Q_{k,\ell}\longmapsto
 Q_{ck+d,\,s\ell+bc k}.
\]

The first map preserves the step-one \(P\)-cycles, and the second preserves the
step-two \(Q\)-cycles. For a cross edge \(P_{i,j}Q_{k,ik+j}\), put

\[
 i'=ai+b,\qquad k'=ck+d,\qquad j'=sj-ad i-bd.
\]

Since \(ac=s\),

\[
 i'k'+j'
 =s(ik+j)+bc k,
\]

which is exactly the second coordinate of the image of \(Q_{k,ik+j}\).
Therefore all cross edges are preserved as well.

The map sends \(M_\pi\) to \(M_{\pi'}\), where

\[
 \pi'(ai+b)=c\pi(i)+d.
\]

### 3.2 Type swapping

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 t\in\{2,-2\},\quad c=-t/a.
\]

Define

\[
 P_{i,j}\longmapsto
 Q_{ai+b,\,tj+da i+db},
\]

\[
 Q_{k,\ell}\longmapsto
 P_{ck+d,\,t\ell-cb k}.
\]

A step of size one becomes a step of size \(t=\pm2\), and a step of size two
becomes a step of size \(2t=\pm4=\mp1\). Thus the two same-layer cycle systems
are interchanged.

For a cross edge \(P_{i,j}Q_{k,ik+j}\), put

\[
 i'=ck+d,\qquad k'=ai+b,\qquad j'=t(ik+j)-cbk.
\]

Because \(ca=-t\),

\[
 i'k'+j'=tj+dai+db,
\]

which is the second coordinate of the image of \(P_{i,j}\). Hence the map is a
graph automorphism. Its action on matchings is

\[
 \pi'(c\pi(i)+d)=ai+b.
\]

## 4. Orbit exhaustion and exact isomorphism classification

The verifier checks all 400 displayed coordinate maps on every one of the 175
Hoffman--Singleton edges and on every one of the 120 matchings. The generated
action has exactly two disjoint orbits:

\[
 20+100=120.
\]

The first orbit consists precisely of the affine permutations
\(i\mapsto ai+b\); the second consists of all nonaffine permutations. Every
orbit is contained in a graph-isomorphism class because the coordinate maps are
graph automorphisms carrying deleted matching to deleted matching.

The adjacency characteristic polynomials of an affine and a nonaffine
representative differ. Therefore the two representatives are not isomorphic,
and the two coordinate orbits are exactly the two graph-isomorphism classes in
this explicit family.

## 5. Affine class

Take \(\pi(i)=i\). Exact computation gives

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

The factor \((x+13)^4\) supplies the eigenvalue \(-13\). Remove this factor and
take the square-free part of the remaining polynomial. Its exact Sturm
variation count is the same at \(-\infty\) and at \(-13\), and the remaining
polynomial is nonzero at \(-13\). Hence it has no root below or at \(-13\), so

\[
 \lambda_{\min}(D)=-13.
\]

Since the graph is 6-regular,

\[
 \Phi=6-13=-7.
\]

## 6. Nonaffine class

Take \(\pi=(0,1,2,4,3)\). Its exact adjacency polynomial differs from the
affine polynomial. The exact distance polynomial is

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

Since

\[
 61>\left(\frac{39}{5}\right)^2,
\]

this root lies below \(-69/5\). The square-free part of \(\chi_D\) is nonzero
at \(-69/5\), and its exact Sturm count gives one root in
\(( -\infty,-69/5)\). Thus

\[
 \lambda_{\min}(D)=-6-\sqrt{61}.
\]

Consequently

\[
 \Phi=6-6-\sqrt{61}=-\sqrt{61}<0.
\]

Because \(\sqrt{61}>7\), this least eigenvalue is strictly below \(-13\).

## 7. Conclusion and search value

The exact score distribution in this family is

\[
 20\text{ labelled graphs with score }-7,
 \qquad
 100\text{ labelled graphs with score }-\sqrt{61}.
\]

Thus all 120 layer-respecting perfect-matching deletions are negative controls.
This eliminates a natural order-50 construction while retaining every vertex.
It does **not** classify arbitrary perfect matchings, arbitrary 6-regular
spanning subgraphs, or all order-50 candidates.

The rejected distance-matrix shortcut remains excluded: a proposed bilinear
formula fails on the nonaffine representative. The final proof uses only the
coordinate automorphisms, exact breadth-first distances, exact characteristic
polynomials, and exact Sturm comparisons.

## 8. Verification

Run

```text
python scripts/verify_layer_matching_deletions.py
python scripts/verify_proof_audit_07_layer_matchings.py
```

The second script is independent of the first and verifies all 120 matchings,
all 400 coordinate maps, all graph hypotheses, the orbit exhaustion, the two
characteristic-polynomial pairs, and both least-root certificates without
floating-point arithmetic.