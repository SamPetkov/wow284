# Proof Audit 07: layer-respecting perfect-matching deletions

**Audited result:** `research-notes/LAYER_MATCHING_DELETIONS.md`.  
**Verdict:** `pass_after_correction`.  
**Scope:** the explicitly defined 120 matchings \(M_\pi\), \(\pi\in S_5\), in
the coordinate Hoffman--Singleton graph. No statement is made about all perfect
matchings of the Hoffman--Singleton graph.

## 1. Normalized theorem

For each permutation \(\pi\in S_5\), let

\[
 M_\pi=\{P_{i,j}Q_{\pi(i),\,i\pi(i)+j}:i,j\in\mathbb F_5\},
 \qquad
 G_\pi=G_{HS}-M_\pi.
\]

Then the 120 labelled graphs \(G_\pi\) form exactly two isomorphism classes.

1. If \(\pi\) is affine, \(\pi(i)=ai+b\) with \(a\ne0\), then there are 20
   labelled members in the class and
   \[
   \lambda_{\min}(D(G_\pi))=-13,
   \qquad
   \Phi(G_\pi)=-7.
   \]
2. If \(\pi\) is nonaffine, then there are 100 labelled members in the class and
   \[
   \lambda_{\min}(D(G_\pi))=-6-\sqrt{61},
   \qquad
   \Phi(G_\pi)=-\sqrt{61}.
   \]

Every member is connected, simple, 6-regular, of order 50, girth five, and
diameter four. In particular, every member is a strict negative control for
WOW-284.

## 2. Corrections found

The numerical and spectral conclusions are correct. Three proof steps were too
compressed in the original note.

1. “Every vertex occurs exactly once” did not explain the \(Q\)-vertices. For
   \(Q_{k,\ell}\), the unique incident matching edge is obtained from
   \[
   i=\pi^{-1}(k),\qquad j=\ell-ik.
   \]
2. The two coordinate maps were asserted to preserve all three edge types
   without displaying the cross-edge identities. Those identities are written
   out below.
3. Two coordinate-automorphism orbits do not by themselves exclude an
   isomorphism between the two orbits. The exact adjacency characteristic
   polynomials of the two representatives differ, so such an isomorphism is
   impossible.

These are logically relevant expository corrections. They do not change either
orbit, characteristic polynomial, least root, or score.

## 3. Hypothesis ledger

| Input | Use |
| --- | --- |
| \(\pi\in S_5\) | gives a unique inverse image \(\pi^{-1}(k)\), hence a perfect matching |
| arithmetic in \(\mathbb F_5\) | defines the coordinate graph and both automorphism families |
| \(a\ne0\) | makes the coordinate maps and transformed permutations bijective |
| \(s=\pm1\) | preserves the step-one \(P\)-cycles and step-two \(Q\)-cycles |
| \(t=\pm2\) | swaps step-one and step-two cycles |
| Hoffman--Singleton girth five | deleting edges cannot create a shorter cycle |
| retained same-layer pentagons | gives girth at most five, hence exactly five |
| exact characteristic polynomials | separate the two coordinate orbits as graph-isomorphism classes |
| exact Sturm counts | identify the least distance root without numerical ordering |

## 4. The matching is perfect

Each \(P_{i,j}\) occurs in the defining set exactly once. Conversely, fix
\(Q_{k,\ell}\). Since \(\pi\) is a permutation, there is a unique
\(i=\pi^{-1}(k)\). The equation

\[
 i\pi(i)+j=\ell
\]

then has the unique solution \(j=\ell-ik\). Thus every \(Q\)-vertex also occurs
exactly once. The 25 edges are distinct and form a perfect matching.

Deleting them lowers every degree from seven to six. The same-layer pentagons
are untouched. Since edge deletion cannot create a triangle or a 4-cycle,
\(g(G_\pi)=5\). The independent verifier performs exact breadth-first search on
all 120 labelled graphs and obtains diameter four in every case; connectedness
is included in this check.

## 5. Type-preserving coordinate maps

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 s\in\{1,-1\},\quad c=s/a.
\]

Set

\[
 P_{i,j}\mapsto P_{ai+b,\,sj-ad i-bd},
\]

\[
 Q_{k,\ell}\mapsto Q_{ck+d,\,s\ell+bc k}.
\]

The first map sends a step \(j\mapsto j\pm1\) to a step
\(sj\mapsto sj\pm s\), hence preserves each \(P\)-cycle. The second sends a
step \(\ell\mapsto\ell\pm2\) to \(s\ell\mapsto s\ell\pm2s\), hence preserves
each \(Q\)-cycle.

For a cross edge \(P_{i,j}Q_{k,ik+j}\), write

\[
 i'=ai+b,\qquad k'=ck+d,\qquad j'=sj-ad i-bd.
\]

Because \(ac=s\),

\[
 i'k'+j'
 =sik+bc k+sj
 =s(ik+j)+bc k,
\]

which is exactly the second coordinate of the image of \(Q_{k,ik+j}\). Thus
cross edges are preserved.

The matching image is \(M_{\pi'}\), where

\[
 \pi'(ai+b)=c\pi(i)+d.
\]

The displayed cross-edge identity proves the second-coordinate equality as
well; there is no additional condition hidden in this formula.

## 6. Type-swapping coordinate maps

Choose

\[
 a\in\mathbb F_5^\times,\quad b,d\in\mathbb F_5,\quad
 t\in\{2,-2\},\quad c=-t/a.
\]

Set

\[
 P_{i,j}\mapsto Q_{ai+b,\,tj+da i+db},
\]

\[
 Q_{k,\ell}\mapsto P_{ck+d,\,t\ell-cb k}.
\]

A step of size one in a \(P\)-cycle becomes a step of size \(t=\pm2\) in a
\(Q\)-cycle. A step of size two in a \(Q\)-cycle becomes a step of size
\(2t=\pm4=\mp1\) in a \(P\)-cycle.

For the image of the cross edge \(P_{i,j}Q_{k,ik+j}\), put

\[
 i'=ck+d,\qquad k'=ai+b,\qquad j'=t(ik+j)-cb k.
\]

Since \(ca=-t\),

\[
 i'k'+j'
 =(ck+d)(ai+b)+t(ik+j)-cbk
 =tj+dai+db,
\]

which is the second coordinate of the image of \(P_{i,j}\). Therefore the map
is a graph automorphism. Its action on matchings is

\[
 \pi'(c\pi(i)+d)=ai+b.
\]

## 7. Orbit exhaustion and isomorphism classes

There are 400 displayed coordinate maps. The independent finite audit checks
that all are distinct bijections of the 50 vertices, preserve all 175
Hoffman--Singleton edges, and send every one of the 120 matchings to the
predicted matching.

The generated action on \(S_5\) has two disjoint orbits of sizes

\[
 20\quad\text{and}\quad100.
\]

The first is exactly the set of affine permutations; the second is its
complement. Each orbit is contained in a graph-isomorphism class because the
coordinate maps are graph automorphisms.

To exclude an isomorphism between the two orbits, compute the adjacency
characteristic polynomial of one representative from each orbit. They differ.
Since adjacency characteristic polynomials are graph-isomorphism invariants,
the two coordinate orbits are exactly the two graph-isomorphism classes in this
120-member family.

## 8. Exact least-root certificates

For the affine representative, the distance polynomial contains
\((x+13)^4\). Remove that factor, take the square-free part of the remaining
polynomial, and form its exact Sturm sequence. The sign-variation count is the
same at \(-\infty\) and at \(-13\), while the remaining polynomial is nonzero at
\(-13\). Hence it has no root below or at \(-13\), and

\[
 \lambda_{\min}(D)=-13.
\]

For the nonaffine representative, the factor \(x^2+12x-25\) gives the root
\(-6-\sqrt{61}\). Since

\[
 61>\left(\frac{39}{5}\right)^2,
\]

this root lies below \(-69/5\). The square-free distance polynomial is nonzero
at \(-69/5\), and its Sturm sequence has exactly one root in
\(( -\infty,-69/5)\). Therefore that algebraic root is the least one.

Finally, \(\sqrt{61}>7\), so the nonaffine least root is strictly below
\(-13\). The exact score distribution is therefore

\[
 20\text{ graphs with score }-7,
 \qquad
 100\text{ graphs with score }-\sqrt{61}.
\]

## 9. Independent verification

Run

```text
python scripts/verify_proof_audit_07_layer_matchings.py
```

The script does not import the original matching-deletion verifier. It checks:

- all 120 perfect matchings and all 120 resulting graph hypotheses;
- all 400 coordinate automorphisms and all 48,000 matching images;
- the exact 20/100 orbit exhaustion and affine characterization;
- both complete adjacency and distance characteristic polynomials;
- exact spectral separation of the two orbits;
- both Sturm/root-isolation certificates;
- the exact score distribution.

No floating-point arithmetic or numerical eigensolver is used.

## 10. Claim boundary

The theorem classifies only the displayed family \(\{M_\pi:\pi\in S_5\}\).
It does not classify all perfect matchings of the Hoffman--Singleton graph, all
6-regular spanning subgraphs, or all order-50 candidates. Literature priority
for the two distance spectra remains unresolved.