# Edge-local spectral obstruction at degree six

**Status:** exact analytic theorem with independent symbolic verifiers and a
separate proof audit.  
**Scope:** connected 6-regular graphs of girth at least five.

## Theorem

Every connected 6-regular strict counterexample to WOW-284 has order at most

\[
  \boxed{50}.
\]

This improves the previous exact bound \(n\le 51\).

## 0. Reduction to diameter three

The spectral-window argument below assumes diameter three.  We first show that
this is automatic for a degree-six regular strict counterexample.

Suppose \(u,v\) have distance \(d\ge4\).  Define \(x\) by assigning weight \(3\)
to \(u\), weight \(1\) to each of its six neighbors, weight \(-3\) to \(v\),
weight \(-1\) to each of its six neighbors, and zero elsewhere.  The two closed
neighborhoods are disjoint and

\[
 \lVert x\rVert^2=30.
\]

The absence of triangles makes the distance between two distinct neighbors of
one center exactly two.  Across the two closed neighborhoods, triangle
inequality gives the lower bounds \(d,d-1,d-1,d-2\) for the four types of
pairs.  Since the cross-coordinate products are negative,

\[
 \frac{x^{\mathsf T}D(G)x}{\lVert x\rVert^2}
 \le \frac{204-81d}{15}\le-8.
\]

Hence \(\lambda_{\min}(D(G))\le-8\), contradicting strict violation because
\(\delta^*(G)=6\).

Diameter two is also impossible.  The girth and regularity hypotheses would
force \(n=37\) and

\[
 A^2=5I-A+J.
\]

On \(\mathbf1^\perp\), the adjacency eigenvalues would be roots of the
irreducible polynomial \(x^2+x-5\).  Therefore the characteristic polynomial
would be

\[
 (x-6)(x^2+x-5)^{18},
\]

whose trace is \(6-18=-12\), contrary to \(\operatorname{tr}A=0\).  Diameter
one is excluded by the girth hypothesis.  Thus every degree-six regular strict
counterexample has diameter three.

A complete audit of this reduction is recorded in
`DEGREE_SIX_DIAMETER_REDUCTION.md` and
`PROOF_AUDIT_01_EDGE_LOCAL_ORDER51.md`.

## 1. A centered positive-semidefinite polynomial

For a connected \(k\)-regular graph of girth at least five and diameter three,
strict violation is equivalent to

\[
  -1-\sqrt{2k-2}<\theta<-1+\sqrt{2k-2}
\]

for every nonprincipal adjacency eigenvalue \(\theta\).

Set

\[
  f_k(x)=(x+2)^2\bigl(x^2+2x-(2k-3)\bigr).
\]

On the closed WOW window, \(f_k(x)\le0\). Moreover,

\[
  f_k(k)=(k+2)^2(k^2+3)=:C_k.
\]

Hence

\[
  M=-f_k(A)+\frac{C_k}{n}J
\]

is positive semidefinite: its principal eigenvalue is zero and its
nonprincipal eigenvalues are \(-f_k(\theta)\ge0\).

## 2. Diagonal and edge entries

Because the graph is \(k\)-regular and has no triangle or 4-cycle,

\[
  (A^2)_{vv}=k,
  \qquad
  (A^4)_{vv}=k(2k-1).
\]

Consequently,

\[
  M_{vv}=\frac{C_k}{n}-6(k+2).
\]

Let \(uv\in E(G)\), and let \(\sigma_{uv}\) be the number of 5-cycles
containing the edge \(uv\). Then

\[
  (A^3)_{uv}=2k-1,
  \qquad
  (A^4)_{uv}=\sigma_{uv},
\]

so

\[
  M_{uv}=\frac{C_k}{n}-(4k+14)-\sigma_{uv}.
\]

The principal \(2\times2\) submatrix on \(u,v\) has equal diagonal entries.
Positive semidefiniteness therefore gives

\[
  -M_{vv}\le M_{uv}\le M_{vv}.
\]

Equivalently,

\[
  \boxed{\sigma_{uv}\ge2k-2}
\]

and

\[
  \boxed{
  \sigma_{uv}
  \le
  \frac{2(k+2)^2(k^2+3)}{n}-10k-26.
  }
\]

## 3. The independent combinatorial lower bound

For an edge \(uv\), both radius-two balls have size \(k^2+1\). Their
intersection consists of

- \(u,v\);
- the \(k-1\) other neighbors of \(u\);
- the \(k-1\) other neighbors of \(v\);
- one vertex for each 5-cycle containing \(uv\).

Thus

\[
  |B_2(u)\cap B_2(v)|=2k+\sigma_{uv}.
\]

Writing

\[
  n=k^2+1+c,
\]

and using \(B_2(u)\cup B_2(v)\subseteq V(G)\), we obtain

\[
  \boxed{
  \sigma_{uv}\ge(k-1)^2-c.
  }
\]

This uses Backelin's radius-two identity as the underlying ball count.

## 4. Excluding order 51

Now take \(k=6\) and \(n=51\), so \(c=14\). The combinatorial lower bound is

\[
  \sigma_{uv}\ge25-14=11.
\]

The spectral upper bound is

\[
  \sigma_{uv}
  \le
  \frac{4992}{51}-86
  =\frac{202}{17}
  <12.
\]

Since \(\sigma_{uv}\) is integral,

\[
  \sigma_{uv}=11
\]

for every edge.

The graph has

\[
  |E(G)|=\frac{6\cdot51}{2}=153
\]

edges. Counting edge--5-cycle incidences gives

\[
  5N_5=153\cdot11=1683,
\]

where \(N_5\) is the number of 5-cycles. This is impossible because 1683 is
not divisible by 5.

Therefore \(n\ne51\), and the previous bound \(n\le51\) improves to

\[
  \boxed{n\le50}.
\]

## 5. Exact structure at order 50

If \(n=50\), then \(c=13\). The same two bounds give

\[
  12\le\sigma_{uv}\le\frac{346}{25}<14,
\]

so every edge lies in either 12 or 13 five-cycles.

Let \(H\) be the spanning subgraph whose edges are those with
\(\sigma_{uv}=13\). If \(\tau(v)\) denotes the number of 5-cycles through
\(v\), then

\[
  \sum_{e\ni v}\sigma_e=2\tau(v).
\]

Hence

\[
  72+d_H(v)=2\tau(v),
\]

so every degree in \(H\) is even. If \(m=|E(H)|\), then

\[
  5N_5=12\cdot150+m=1800+m,
\]

and therefore

\[
  m\equiv0\pmod5.
\]

Thus any surviving order-50 graph must carry a highly constrained even
subgraph of high-5-cycle edges.

## 6. Exact controls

The verifier reconstructs the known order-40 and order-42 counterexamples and
checks that every edge lies respectively in 22 and 20 five-cycles. It also
recovers 528 and 504 total 5-cycles, and 66 and 60 five-cycles through every
vertex.

## Literature boundary

The radius-two ball identity is published in Backelin, arXiv:1511.08128,
Lemma 2.1. The centered polynomial uses the standard nonbacktracking/LP
framework. No priority claim is made for the edge-local combination, the
diameter reduction, or the order-51 exclusion pending a dedicated literature
search.