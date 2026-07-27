# Regular WOW-284 counterexamples have degree at least six

**Status:** proved analytically and checked by
`scripts/verify_regular_low_degree.py`. The final degree-five cage case uses
Meringer's exhaustive theorem that exactly four `(5,5)`-cages exist and four
fixed graph records whose structure and spectra are recomputed locally.

## Theorem

Let `G` be a connected regular graph on at least three vertices with girth at
least five. If

\[
 \delta^*(G)>-\lambda_{\min}(D(G)),
\]

then the degree of `G` is at least six.

## 1. Diameter obstruction

For any two vertices `u,v`, the vector `e_u-e_v` gives

\[
 \frac{(e_u-e_v)^{\mathsf T}D(e_u-e_v)}
 {\lVert e_u-e_v\rVert^2}
 =-d(u,v).
\]

Hence

\[
 \lambda_{\min}(D)\le-\operatorname{diam}(G).
\]

If `G` is `k`-regular, then `\delta^*(G)=k`. A strict counterexample must
therefore satisfy

\[
 \operatorname{diam}(G)<k.
\]

Connected regular graphs of degree zero or one have fewer than three vertices,
so only `k=2,3,4,5` remain.

## 2. Degrees two and three

A connected 2-regular graph is a cycle. Under the girth hypothesis its diameter
is at least two, contradicting the strict diameter obstruction.

Suppose `k=3`. Then the diameter is at most two. Girth at least five makes the
radius-two breadth-first layers around any vertex have sizes

\[
 1,\qquad3,\qquad3\cdot2,
\]

so the graph has at least ten vertices. The degree-diameter Moore bound for
diameter two gives at most ten vertices. Thus `G` is a degree-three Moore
graph. The Moore calculation gives

\[
 \lambda_{\min}(D)=-3,
 \qquad
 \delta^*=3,
\]

so equality holds rather than strict violation.

## 3. Degree four

The diameter is at most three.

### 3.1 Diameter two

A degree-four diameter-two graph of girth at least five would be a Moore graph
on 17 vertices. Its two nonprincipal adjacency eigenvalues would be

\[
 \frac{-1\pm\sqrt{13}}2.
\]

The corresponding multiplicities include

\[
 \frac12\left(16+\frac8{\sqrt{13}}\right),
\]

which is not an integer. Hence no such graph exists.

### 3.2 Diameter three

Write

\[
 n=4^2+1+c=17+c.
\]

The radius-two ball is proper, so `c\ge1`. The fourth-moment bound from
`VERIFIED_RESEARCH_EXTENSIONS.md` gives

\[
 n<\frac{(4+1)^2(4^2+3)}{5\cdot4+3}
 =\frac{475}{23}<21.
\]

Thus `c\in\{1,2,3\}`.

#### Excess one

If `c=1`, every vertex has exactly one vertex at distance three. The
distance-three matrix `A_3` is therefore a perfect matching on 18 vertices.
Its `-1` eigenspace has dimension nine and lies in `\mathbf1^\perp`.

For a 4-regular girth-five diameter-three graph,

\[
 A_3=J+3I-A-A^2.
\]

On the `-1` eigenspace of `A_3`, this gives

\[
 A^2+A-4I=0.
\]

The polynomial `x^2+x-4` is irreducible over `\mathbb Q`, since its
discriminant is 17. A rational invariant space on which this polynomial
annihilates the operator must have even dimension. The dimension here is nine,
a contradiction.

#### Excess two or three

For a fixed vertex, compress the adjacency matrix to its four distance layers.
At the smallest feasible internal degree of the distance-two layer, the
nonprincipal characteristic factor is a positive scalar multiple of

\[
 p_{4,c}(x)=3x^3+(c+3)x^2-9x-4c.
\]

The compression increases in the positive-semidefinite order as that internal
degree increases. Therefore its second eigenvalue is bounded below by the
largest root of `p_{4,c}`. Exact substitution gives

\[
 p_{4,2}(3/2)=-\frac18,
 \qquad
 p_{4,3}(3/2)=-\frac{15}{8}.
\]

Thus the largest root is greater than `3/2`. Interlacing yields

\[
 \lambda_2(A)>\frac32.
\]

But the diameter-three WOW criterion requires every nonprincipal adjacency
eigenvalue to lie below

\[
 -1+\sqrt{2\cdot4-2}=-1+\sqrt6<\frac32.
\]

This contradiction excludes degree four.

## 4. Degree five

The diameter is at most four.

### 4.1 Diameter two

A degree-five Moore graph would have nonprincipal adjacency eigenvalues

\[
 \frac{-1\pm\sqrt{17}}2
\]

and a multiplicity containing

\[
 \frac12\left(25+\frac{15}{\sqrt{17}}\right),
\]

which is not an integer. Hence diameter two is impossible.

### 4.2 Diameter four

Choose a diametral geodesic with five vertices. The corresponding principal
submatrix of the graph distance matrix is the distance matrix of `P_5`, whose
characteristic polynomial is

\[
 (x^2+6x+4)(x^3-6x^2-18x-8).
\]

It has the eigenvalue

\[
 -3-\sqrt5<-5.
\]

Cauchy interlacing gives `\lambda_{\min}(D(G))<-5`, so `G` cannot be a
strict counterexample.

### 4.3 Diameter three

Write

\[
 n=5^2+1+c=26+c.
\]

Meringer's exhaustive cage generation proves that a 5-regular graph of girth
five has at least 30 vertices, so `c\ge4`, and that exactly four graphs attain
order 30. The fourth-moment bound gives the strict inequality

\[
 n<\frac{(5+1)^2(5^2+3)}{5\cdot5+3}=36,
\]

so `c\le9`.

#### Excess at least six

The distance-layer polynomial is

\[
 p_{5,c}(x)=4x^3+(c+4)x^2-16x-5c.
\]

At `x=11/6`,

\[
 p_{5,c}(11/6)=-\frac{177c-946}{108}<0
 \qquad(c\ge6).
\]

The largest root is therefore greater than `11/6`, and interlacing gives

\[
 \lambda_2(A)>\frac{11}{6}.
\]

On the other hand,

\[
 \frac{11}{6}>-1+\sqrt8,
\]

whereas strict WOW violation requires
`\lambda_2(A)<-1+\sqrt8`. Thus `c=6,7,8,9` are impossible.

#### Excess five

Let `a` be the average number of neighbors that a vertex in the 20-vertex
distance-two layer has within that layer. Feasibility gives

\[
 a\ge4-\frac54=\frac{11}{4}.
\]

Since `a=2e/20=e/10` for an integer edge count `e`, in fact

\[
 a\ge\frac{14}{5}.
\]

At `a=14/5`, the normalized four-layer compression has characteristic
polynomial

\[
 \frac15(x-5)(x+1)(5x^2+5x-26).
\]

Its positive nonprincipal root is

\[
 \frac{-5+\sqrt{545}}{10}>-1+\sqrt8.
\]

The compression is nondecreasing in the positive-semidefinite order as `a`
increases. Interlacing therefore excludes `c=5`.

#### Excess four: the four `(5,5)`-cages

Here `n=30`. Meringer proved that exactly four nonisomorphic `(5,5)`-cages
exist. The records in `data/cages55/` reconstruct those four labelled graphs
and are checked independently by `scripts/verify_regular_low_degree.py`.

For the Meringer and Robertson–Wegner graphs, the exact distance
characteristic polynomial contains `(x+6)`, so `-6` is a distance
eigenvalue. For the Foster and Wong graphs it contains

\[
 x^2+6x-11,
\]

whose smaller root is `-3-2\sqrt5<-5`. In every case

\[
 \lambda_{\min}(D)\le-5,
\]

so no order-30 cage is a strict counterexample.

This completes the degree-five case and the proof of the theorem.

## 5. Exact verification

Run

```text
python scripts/verify_regular_low_degree.py
```

The script checks:

- the symbolic reductions used above;
- the first ten public House of Graphs adjacency rows for each cage;
- order, size, degree, connectedness, girth, and diameter;
- full exact adjacency and distance characteristic polynomials;
- exact automorphism-group orders 30, 96, 20, and 120;
- pairwise nonisomorphism;
- an explicit distance eigenvalue at most `-5` for every cage.

No numerical eigensolver is used for a theorem.
