# Proof Audit 04: regular strict counterexamples have degree at least six

**Audited result:** `REGULAR_LOW_DEGREE_OBSTRUCTION.md`.

**Audit mode:** theorem-by-theorem and line-by-line, with every degree and
diameter case separated.  The independent verifier does not import
`scripts/verify_regular_low_degree.py`.

**Provisional verdict:** `pass`.

No false statement or reversed interlacing inequality was found.  The audit
produces a shorter proof by using the already audited all-degree LP ceiling:
for degree four it leaves only order 18, and for degree five it leaves only
orders 30, 31, and 32.  This removes several redundant layer-polynomial cases
from the logical core.

## 1. Normalised theorem

Let \(G\) be a connected \(k\)-regular graph on at least three vertices with
girth at least five.  If

\[
 k+\lambda_{\min}(D(G))>0,
\]

then

\[
 \boxed{k\ge6}.
\]

Since \(G\) is regular, \(\delta^*(G)=k\), so this is exactly the regular case
of strict violation of WOW-284.

## 2. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| connected | finite graph distance and the degree--diameter argument |
| \(k\)-regular | \(\delta^*=k\), fixed breadth-first layer sizes |
| girth at least five | no overlap in the first two breadth-first layers |
| at least three vertices | excludes the connected regular graphs of degree zero or one |
| strict violation | forces \(\operatorname{diam}(G)<k\) |

## 3. Critical lemma A: diameter obstruction

For vertices \(u,v\), the vector \(e_u-e_v\) has norm squared two and

\[
 (e_u-e_v)^{\mathsf T}D(e_u-e_v)=-2d(u,v).
\]

Hence

\[
 \lambda_{\min}(D)\le-d(u,v).
\]

Taking a diametral pair gives

\[
 \boxed{\lambda_{\min}(D)\le-\operatorname{diam}(G).}
\]

A regular strict counterexample therefore satisfies

\[
 \boxed{\operatorname{diam}(G)<k.}
\]

This inequality is strict; replacing it by \(\le k\) would not exclude the
cycle and Petersen boundary cases.

## 4. Degrees zero, one, and two

A connected 0-regular graph is \(K_1\), and a connected 1-regular graph is
\(K_2\), so neither has at least three vertices.

A connected 2-regular graph is a cycle.  Under the girth-five hypothesis its
order is at least five and its diameter is at least two, contradicting
\(\operatorname{diam}(G)<2\).

## 5. Degree three

The diameter obstruction gives \(\operatorname{diam}(G)\le2\).  Around any
vertex, girth at least five forces disjoint breadth-first layers of sizes

\[
 1,\quad3,\quad6.
\]

Thus \(n\ge10\).  The Moore bound for degree three and diameter two gives
\(n\le10\), so equality holds and \(G\) is a degree-three Moore graph.  Its
least distance eigenvalue is \(-3\), while \(\delta^*=3\).  This is equality in
WOW-284, not strict violation.

## 6. Degree four

The diameter is at most three.

### 6.1 Diameter two

The girth condition forces the Moore identity and order 17.  The two
nonprincipal adjacency roots are

\[
 \frac{-1\pm\sqrt{13}}2.
\]

The multiplicity

\[
 \frac12\left(16+\frac8{\sqrt{13}}\right)
\]

is not integral, so this graph cannot exist.

### 6.2 Diameter three

The audited LP ceiling gives

\[
 n<\frac{(4+2)(4^2+3)}6=19.
\]

The radius-two ball has 17 vertices and diameter three requires at least one
vertex outside it.  Therefore

\[
 \boxed{n=18}.
\]

Every vertex has exactly one vertex at distance three, so the distance-three
matrix \(A_3\) is a perfect matching.  Its \(-1\)-eigenspace has dimension nine
and is contained in \(\mathbf1^\perp\).  The diameter-three identity

\[
 A_3=J+3I-A-A^2
\]

shows on this rational invariant space that

\[
 A^2+A-4I=0.
\]

The polynomial \(x^2+x-4\) is irreducible over \(\mathbb Q\), since its
discriminant is 17.  A rational vector space annihilated by this irreducible
quadratic has even dimension.  The dimension is nine, a contradiction.

Thus degree four is impossible.

## 7. Degree five

The diameter is at most four.

### 7.1 Diameter two

The Moore roots are

\[
 \frac{-1\pm\sqrt{17}}2,
\]

and the corresponding multiplicity

\[
 \frac12\left(25+\frac{15}{\sqrt{17}}\right)
\]

is not integral.  Diameter two is impossible.

### 7.2 Diameter four

A diametral geodesic has five vertices.  Every distance between two vertices
of that geodesic equals their path distance; otherwise the endpoint path could
be shortened.  The corresponding principal submatrix of \(D(G)\) is therefore
\(D(P_5)\), whose characteristic polynomial is

\[
 (x^2+6x+4)(x^3-6x^2-18x-8).
\]

It has eigenvalue

\[
 -3-\sqrt5<-5.
\]

Cauchy interlacing gives

\[
 \lambda_{\min}(D(G))\le-3-\sqrt5<-5,
\]

which contradicts strict violation at degree five.

### 7.3 Diameter three: order reduction

Meringer's exhaustive theorem gives \(n\ge30\) for a 5-regular girth-five graph
(*Journal of Graph Theory* 30 (1999), 137--146,
DOI `10.1002/(SICI)1097-0118(199902)30:2<137::AID-JGT7>3.0.CO;2-G`).
The audited LP ceiling gives

\[
 n<\frac{(5+2)(5^2+3)}6=\frac{98}{3},
\]

so

\[
 \boxed{n\in\{30,31,32\}.}
\]

The handshake identity \(5n=2|E(G)|\) makes \(n\) even, so the logical core
already reduces to \(n\in\{30,32\}\). Writing \(n=26+c\), only \(c=4,6\)
remain.  The excess-five calculation below is retained as an independent
robustness check, even though parity excludes that case.

### 7.4 Excess six

At the smallest feasible internal degree of the distance-two layer, the
nonprincipal layer factor is

\[
 p_{5,6}(x)=4x^3+10x^2-16x-30.
\]

At \(x=11/6\),

\[
 p_{5,6}(11/6)=-\frac{29}{27}<0.
\]

Since the leading coefficient is positive, its largest root is greater than
\(11/6\).  The normalised layer compression increases in positive-semidefinite
order with the internal degree, so interlacing gives

\[
 \lambda_2(A)>\frac{11}{6}>-1+\sqrt8.
\]

This contradicts the strict diameter-three WOW window.

### 7.5 Excess five

Let \(a\) be the average internal degree in the 20-vertex distance-two layer.
Feasibility gives \(a\ge11/4\).  Since \(a=2e/20=e/10\) for an integer edge
count \(e\),

\[
 a\ge\frac{14}{5}.
\]

At \(a=14/5\), the normalised layer compression has characteristic polynomial

\[
 \frac15(x-5)(x+1)(5x^2+5x-26).
\]

Its positive nonprincipal root is

\[
 \frac{-5+\sqrt{545}}{10}>-1+\sqrt8.
\]

Positive-semidefinite monotonicity and interlacing exclude excess five.

### 7.6 Excess four

Here \(n=30\).  Meringer proved in the cited exhaustive-generation paper that
exactly four nonisomorphic 5-regular 30-vertex girth-five graphs exist.  The four
committed graph6 records are
independently reconstructed, checked to be pairwise nonisomorphic cages, and
have exact distance characteristic polynomials containing either

\[
 x+6
\]

or

\[
 x^2+6x-11.
\]

The corresponding witnessed distance eigenvalues are \(-6\) or
\(-3-2\sqrt5\), both at most \(-5\).  Hence none is a strict counterexample.

This completes the proof.

## 8. Positive-semidefinite monotonicity used above

For distance-layer sizes

\[
 1,\quad k,\quad k(k-1),\quad c,
\]

and average internal degree \(a\) in the distance-two layer, the symmetric
normalised compression has the bottom-right block

\[
 \begin{pmatrix}
 a&(k-1-a)\sqrt{k(k-1)/c}\\
 (k-1-a)\sqrt{k(k-1)/c}&
 k-k(k-1)(k-1-a)/c
 \end{pmatrix}.
\]

Its derivative with respect to \(a\) is

\[
 \begin{pmatrix}1&-\sqrt r\\-\sqrt r&r\end{pmatrix}
 =\begin{pmatrix}1\\-\sqrt r\end{pmatrix}
  \begin{pmatrix}1&-\sqrt r\end{pmatrix}\succeq0,
 \qquad r=\frac{k(k-1)}c.
\]

Thus every ordered eigenvalue of the compression is nondecreasing in \(a\).
This supplies the exact monotonicity used in the excess-five and excess-six
cases.

## 9. Independent verification

`scripts/verify_proof_audit_04_regular_low_degree.py` checks without importing
the original verifier:

1. every diameter and Moore-multiplicity reduction;
2. the audited LP bounds at degrees four and five;
3. the odd-dimensional irreducible-quadratic contradiction at degree four;
4. the exact \(P_5\) distance polynomial and interlacing witness;
5. both degree-five layer-compression calculations and radical comparisons;
6. the rank-one positive-semidefinite derivative;
7. all four graph6 cage records, pairwise nonisomorphism, girth, diameter, and
   exact distance-polynomial witnesses.

## 10. Verdict

The theorem passes.  The main improvement is proof compression: the audited LP
ceiling reduces the diameter-three degree-four case to \(n=18\) and the
degree-five case to \(n=30,31,32\).  No numerical eigenvalue ordering is used.
