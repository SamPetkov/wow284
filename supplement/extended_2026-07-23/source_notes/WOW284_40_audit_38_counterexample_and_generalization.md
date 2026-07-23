# Audit of the 40-vertex construction and further WOW-284 counterexamples

**Date:** 22 July 2026  
**Status:** exact independent audit; no minimality or priority claim

## Executive conclusion

The proposed 40-vertex graph is correct. It is a simple connected 6-regular
graph of girth five and diameter three, with

\[
\operatorname{Spec}(D)=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}.
\]

Hence \(\delta^*=6\), \(\lambda_{\min}(D)=-5\), and its exact WOW-284 gap is
\(1\).

A strictly smaller exact counterexample is obtained by deleting the adjacent
vertices \(P_{1,0}\) and \(P_{1,1}\) from that 40-vertex graph. The resulting
38-vertex graph has

\[
\delta^*=\frac{17}{3},\qquad
\lambda_{\min}(D)=-3-\sqrt 7,
\]

and therefore

\[
\Phi=\frac{17}{3}-3-\sqrt7
     =\frac83-\sqrt7>0,
\]

because \(64>63\). Numerically the margin is approximately
\(0.0209153556\), but the proof of its sign is exact.

No claim is made that order 38 is minimal.

---

## 1. Common ambient coordinate graph

Work over \(\mathbb F_5\). The Hoffman--Singleton coordinate graph has
vertices

\[
\{P_{i,j}:i,j\in\mathbb F_5\}\sqcup
\{Q_{k,\ell}:k,\ell\in\mathbb F_5\}
\]

and adjacency rules

\[
P_{i,j}\sim P_{i,j+1},\qquad
Q_{k,\ell}\sim Q_{k,\ell+2},\qquad
P_{i,j}\sim Q_{k,ik+j}.
\]

All subscripts are modulo five.

For numerical labels use

\[
P_{i,j}\leftrightarrow 5i+j,
\qquad
Q_{k,\ell}\leftrightarrow 25+5k+\ell.
\]

The ambient graph has 50 vertices, 175 edges, degree seven, diameter two, and
the exact common-neighbor identity

\[
A_{HS}^2=6I-A_{HS}+J.
\]

---

## 2. Exact audit of the proposed 40-vertex graph

Delete

\[
S=\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}.
\]

The set \(S\) induces the Petersen graph: the five \(P\)-vertices form a
5-cycle, the five \(Q\)-vertices form the step-two 5-cycle, and
\(P_{0,j}\sim Q_{0,j}\) is a perfect matching.

Let \(R=G_{HS}-S\).

### 2.1 Order, regularity, and girth

Every remaining \(P_{i,j}\), where \(i\ne0\), loses exactly the cross-neighbor
\(Q_{0,j}\). Every remaining \(Q_{k,\ell}\), where \(k\ne0\), loses exactly
the cross-neighbor \(P_{0,\ell}\). Thus every remaining vertex has degree six.
Consequently

\[
|V(R)|=40,\qquad |E(R)|=\frac{40\cdot6}{2}=120.
\]

As an induced subgraph of a girth-five graph, \(R\) has no triangle or
4-cycle. It contains, for example,

\[
P_{1,0}P_{1,1}P_{1,2}P_{1,3}P_{1,4}P_{1,0},
\]

so its girth is exactly five.

### 2.2 Block-matrix proof of the adjacency spectrum

Order the ambient adjacency matrix as

\[
A_{HS}=\begin{pmatrix}B&C\\C^{\mathsf T}&P\end{pmatrix},
\]

where \(B\) is the adjacency matrix of \(R\) and \(P\) is the Petersen
adjacency matrix.

Each deleted vertex has four neighbors outside \(S\), and distinct deleted
vertices have no common outside neighbor. Hence

\[
C^{\mathsf T}C=4I_{10}.
\]

Every remaining vertex has exactly one deleted neighbor, so \(C\mathbf1=\mathbf1\).
Taking the top-right block of
\(A_{HS}^2=6I-A_{HS}+J\) gives

\[
BC=C(J-I-P).
\]

The Petersen spectrum is

\[
\{3^{(1)},1^{(5)},(-2)^{(4)}\}.
\]

Since \(C^{\mathsf T}C=4I\), the columns of \(C\) are independent. On
\(\operatorname{col}(C)\), the matrix \(B\) is similar to \(J-I-P\), which
has spectrum

\[
\{6^{(1)},(-2)^{(5)},1^{(4)}\}.
\]

On \(\ker(C^{\mathsf T})\), the top-left block identity gives

\[
B^2+B-6I=0.
\]

This 30-dimensional subspace therefore has only eigenvalues \(2\) and \(-3\).
The trace equation forces multiplicities 18 and 12. Thus

\[
\operatorname{Spec}(B)=
\{6^{(1)},2^{(18)},1^{(4)},(-2)^{(5)},(-3)^{(12)}\}.
\]

No eigenspace is omitted because

\[
\mathbb R^{40}=\operatorname{col}(C)\oplus\ker(C^{\mathsf T}).
\]

### 2.3 Connectivity and diameter

The eigenvalue six of the 6-regular matrix \(B\) is simple, so \(R\) is
connected.

Pairs whose unique ambient common neighbor remains in \(R\) are at distance
at most two. If two remaining vertices have the same deleted common neighbor,
the block identities imply that the corresponding entry of \(B^3\) is six,
so they have a length-three path in \(R\). Hence the diameter is at most three.
It cannot be two, because a 6-regular diameter-two graph has at most
\(1+6+6\cdot5=37\) vertices. Therefore

\[
\operatorname{diam}(R)=3.
\]

### 2.4 Distance spectrum and violation

For every connected \(k\)-regular graph of girth at least five and diameter
three,

\[
D=3J+(k-3)I-2A-A^2.
\]

For \(R\), \(k=6\), so

\[
D=3J+3I-2B-B^2.
\]

On the all-ones vector the distance eigenvalue is 75. On a nonprincipal
adjacency eigenspace with eigenvalue \(\theta\), the distance eigenvalue is

\[
3-2\theta-\theta^2=4-(\theta+1)^2.
\]

Substitution gives

\[
\operatorname{Spec}(D(R))
=\{75^{(1)},3^{(5)},0^{(16)},(-5)^{(18)}\}.
\]

Since \(R\) is 6-regular, every dual degree is six. Therefore

\[
\delta^*(R)=6>5=-\lambda_{\min}(D(R)),
\qquad
\Phi(R)=1.
\]

---

## 3. A smaller 38-vertex counterexample

Starting from \(R\), delete the adjacent vertices

\[
a=P_{1,0},\qquad b=P_{1,1}.
\]

Call the resulting graph \(H\). Equivalently, start with the 50-vertex
coordinate graph and delete

\[
\{P_{0,j},Q_{0,j}:j\in\mathbb F_5\}
\cup\{P_{1,0},P_{1,1}\}.
\]

This is a complete reproducible construction.

For a graph6 representation, relabel the surviving original numerical labels
in increasing order by \(0,1,\ldots,37\). The graph6 string is

```text
egCGGc??G?_@?H????G?@??C?@HCP?AG_OAIaG@qGaBH?Q?HGA??c@@?HG?s_H?E_SA?@OGC?@OI??OGD??WA_O?E@@@??CCE???GKC??AKCC??EAAA??B?
```

### 3.1 Simplicity, connectivity, and girth

The graph is induced, so it remains simple and has no triangle or 4-cycle.
The 5-cycle on \(P_{2,0},\ldots,P_{2,4}\) remains. Exact breadth-first search
from every vertex gives connectedness and diameter three. Hence

\[
|V(H)|=38,\\quad |E(H)|=109,
\qquad g(H)=5,
\qquad \operatorname{diam}(H)=3.
\]

### 3.2 Exact minimum dual degree

Let

\[
A=N_R(a)\setminus\{b\},
\qquad
B=N_R(b)\setminus\{a\}.
\]

The sets \(A\) and \(B\) each have five vertices. Because \(R\) has no
triangles and no 4-cycles, they are disjoint, and no vertex of \(A\cup B\)
has a remaining neighbor in \(A\cup B\). Thus the ten vertices in
\(A\cup B\) have degree five and all their remaining neighbors have degree
six. The other 28 vertices have degree six.

A degree-six vertex has at most one neighbor in \(A\) and at most one in
\(B\), again by the absence of 4-cycles. If it has \(t\in\{0,1,2\}\) such
neighbors, its dual degree is

\[
\frac{5t+6(6-t)}6=6-\frac{t}{6}.
\]

There are \(10\cdot5=50\) incidences between \(A\cup B\) and the 28
degree-six vertices. If every degree-six vertex had at most one such neighbor,
there would be at most 28 incidences. Hence at least one has \(t=2\). It
follows exactly that

\[
\boxed{\delta^*(H)=\frac{17}{3}}.
\]

### 3.3 Exact distance characteristic polynomial

Exact integer breadth-first search constructs the 38 by 38 distance matrix.
Its characteristic polynomial is

\[
\begin{aligned}
\chi_D(x)={}&x^4(x-2)(x+5)^8(x^2+6x+2)^2\\
&\cdot(x^3+3x^2-15x-3)\\
&\cdot(x^4+5x^3-7x^2-23x-6)\\
&\cdot(x^5+9x^4+7x^3-77x^2-54x-4)\\
&\cdot(x^9-67x^8-404x^7+1772x^6+7205x^5\\
&\hspace{1.8cm}-18489x^4-17018x^3+20288x^2+16824x+1680).
\end{aligned}
\]

The quadratic factor has roots \(-3\pm\sqrt7\). An exact Sturm calculation
shows that \(\chi_D\) has exactly one distinct real root below \(-28/5\).
Since

\[
-3-\sqrt7<-\frac{28}{5}
\quad\text{because}\quad
7>\left(\frac{13}{5}\right)^2,
\]

that root is necessarily the least distance eigenvalue. Therefore

\[
\boxed{\lambda_{\min}(D(H))=-3-\sqrt7}.
\]

As a logically independent sign certificate, exact rational LDL-transpose
factorization shows that

\[
3D(H)+17I
\]

has 38 strictly positive pivots. The smallest pivot in the fixed coordinate
ordering used by the verifier is

\[
\frac{12434320241260060}{51172748480408387}>0.
\]

### 3.4 Strict violation

Finally,

\[
\Phi(H)=\frac{17}{3}-3-\sqrt7=\frac83-\sqrt7.
\]

Both sides in \(8/3>\sqrt7\) are positive, and

\[
\left(\frac83\right)^2-7=\frac{64}{9}-\frac{63}{9}=\frac19>0.
\]

Thus

\[
\boxed{\delta^*(H)>-\lambda_{\min}(D(H))}.
\]

---

## 4. Two further exact examples

### 4.1 Order 39

Delete only \(P_{1,0}\) from \(R\). The resulting graph has degree multiset

\[
6^{(33)},5^{(6)},
\]

and

\[
\delta^*=\frac{35}{6}.
\]

Exact rational LDL-transpose decomposition proves that

\[
6D+35I\succ0.
\]

The smallest pivot in the verifier's fixed ordering is

\[
\frac{128650413252103}{36129805596929}>0.
\]

Thus this order-39 graph is also an exact counterexample.

### 4.2 Order 42

Fix \(P_{0,0}\) in the 50-vertex Moore graph and delete it together with its
seven neighbors. The 42 vertices at distance two induce a 6-regular graph of
girth at least five and diameter three. Its spectra are

\[
\operatorname{Spec}(A)=
\{6^{(1)},2^{(21)},(-1)^{(6)},(-3)^{(14)}\},
\]

and

\[
\operatorname{Spec}(D)=
\{81^{(1)},4^{(6)},0^{(14)},(-5)^{(21)}\}.
\]

Therefore \(\delta^*=6\) and the exact gap is again one.

---

## 5. General diameter-three spectral criterion

Let \(G\) be any connected \(k\)-regular graph of girth at least five and
diameter three. Let its adjacency eigenvalues be

\[
k=\theta_0>\theta_1\ge\cdots\ge\theta_{n-1}.
\]

The absence of triangles and 4-cycles gives

\[
A_2=A^2-kI,
\]

where \(A_2\) is the distance-two matrix. Since the diameter is three,

\[
A_3=J-I-A-A_2.
\]

Consequently

\[
\boxed{D=3J+(k-3)I-2A-A^2}.
\]

The principal distance eigenvalue is

\[
3n-k^2-k-3>0,
\]

and every nonprincipal adjacency eigenvalue \(\theta\) gives the distance
eigenvalue

\[
\boxed{\mu(\theta)=k-2-(\theta+1)^2}.
\]

Because \(\delta^*(G)=k\), this yields the exact equivalence

\[
\boxed{
G\text{ refutes WOW-284}
\iff
\max_{\theta\ne k}|\theta+1|<\sqrt{2k-2}.
}
\]

This is a general mechanism, not merely a calculation for one graph. It also
explains why girth-five cages do not automatically work: their nonprincipal
adjacency spectrum must satisfy this additional sharp inequality.

For the 40-vertex graph, the largest value of \(|\theta+1|\) is three, while
\(\sqrt{2k-2}=\sqrt{10}>3\).

---

## 6. A parameterized Moore-subconstituent construction

Let \(M\) be a Moore graph of diameter two and degree \(K\ge3\). Fix a vertex
\(v\), and let \(X\) be the subgraph induced by the vertices at distance two
from \(v\).

Then

\[
|V(X)|=K(K-1),
\qquad
X\text{ is }(K-1)\text{-regular},
\qquad
g(X)\ge5,
\qquad
\operatorname{diam}(X)=3.
\]

Put

\[
q=\sqrt{4K-3},
\qquad
r=\frac{-1+q}{2},
\qquad
s=\frac{-1-q}{2}.
\]

A block decomposition relative to
\(\{v\}\sqcup N(v)\sqcup V(X)\) gives the adjacency eigenvalues

\[
K-1,
\qquad
-1\text{ with multiplicity }K-1,
\qquad
r,s
\]

with the remaining multiplicities determined by dimension and trace. Applying
the diameter-three distance polynomial gives

\[
\boxed{
\lambda_{\min}(D(X))=-\frac{5+\sqrt{4K-3}}{2}.
}
\]

Since \(X\) is \((K-1)\)-regular,

\[
\boxed{
\Phi(X)=K-1-\frac{5+\sqrt{4K-3}}2.
}
\]

This is positive exactly for integer \(K\ge6\). Therefore:

> The second subconstituent of every degree-\(K\) diameter-two Moore graph with
> \(K\ge6\) is a WOW-284 counterexample.

For the known degree-seven Hoffman--Singleton graph, this is precisely the
42-vertex counterexample above. If the unresolved degree-57 Moore graph exists,
this mechanism would produce a 56-regular counterexample on 3192 vertices.

This is a parameterized theorem. It is not currently an unconditional infinite
family, because diameter-two Moore graphs are known only in very restricted
degrees and the degree-57 case remains unresolved.

---

## 7. How the 40-vertex construction fits the general mechanism

The 40-vertex graph comes from a second, nested Moore-graph operation. The
degree-seven Moore graph contains the deleted induced degree-three Moore graph,
namely the Petersen graph, and every outside vertex has exactly one neighbor in
that Petersen graph.

More generally, suppose a degree-\(K\) Moore graph contains an induced
degree-\(r\) Moore graph and every outside vertex has exactly one neighbor in
the induced subgraph. Counting cross edges forces

\[
K=r^2-r+1.
\]

The outside induced graph is \((K-1)\)-regular, has girth at least five and,
for \(r\ge3\), diameter three. The same block argument gives the ambient Moore
roots on the orthogonal complement of the incidence columns, and the least
distance eigenvalue is again

\[
-\frac{5+\sqrt{4K-3}}2.
\]

For \((r,K)=(3,7)\), this yields the 40-vertex graph and the exact gap one.
No infinite chain of such nested Moore graphs is currently known.

---

## 8. Scope of the generalization

The work above establishes three distinct mechanisms:

1. diameter-two Moore graphs of degree greater than three;
2. second subconstituents of degree-\(K\) Moore graphs for \(K\ge6\);
3. the exact spectral criterion for every regular girth-at-least-five,
   diameter-three graph.

It also supplies explicit counterexamples of orders 50, 42, 40, 39, and 38.

What has **not** been established is an unconditional infinite family of
pairwise nonisomorphic counterexamples. The Moore-based parameterized families
are conditional on the existence of the corresponding Moore graphs. The
regular diameter-three criterion gives a precise target for future algebraic
constructions, but existence must still be proved separately.

No minimality claim is made for the 38-vertex graph. A numerical search over
induced deletions of the 40-vertex graph found no positive three-vertex deletion,
but that is not an exhaustive search over all graphs of smaller order.

---

## 9. Reproducibility

Run

```bash
python verify_wow284_38_40_42.py
```

with Python 3.11 or later and SymPy 1.14. The verifier independently constructs
all graph distances by integer breadth-first search, checks exact characteristic
polynomials, runs exact Sturm root counting, and computes exact rational
LDL-transpose certificates.

SHA-256 of the verifier used for this report:

```text
cd16128f9370b70ccaf9a71ac5a4845ddb1a80027b88c1c7774342f32f9f8e74
```

## References for the classical graph constructions

- M. O'Keefe and P.-K. Wong, *A smallest graph of girth 5 and valency 6*,
  Journal of Combinatorial Theory, Series B 26 (1979), 145--149,
  DOI: `10.1016/0095-8956(79)90052-2`.
- P.-K. Wong, *On the uniqueness of the smallest graph of girth 5 and valency
  6*, Journal of Graph Theory 3 (1979), 407--409,
  DOI: `10.1002/jgt.3190030413`.
- G. Exoo and R. Jajcay, *Dynamic Cage Survey*, Electronic Journal of
  Combinatorics, DOI: `10.37236/37`.
- M. Klin, M. Muzychuk, and M. Ziv-Av, *Higmanian Rank-5 Association Schemes
  on 40 Points*, Michigan Mathematical Journal 58 (2009), 255--284,
  DOI: `10.1307/mmj/1242071692`.

### Independent graph6 verification pass

A second verifier starts only from the graph6 string, computes all distances
with NetworkX Floyd--Warshall rather than the coordinate BFS, computes a minimum
cycle basis, and implements exact no-pivot LDL-transpose decomposition directly
with Python `Fraction`. It reproduces the same 38 positive pivots and the same
smallest pivot.

SHA-256:

```text
2f000797ef62db1f0d3231d9ba05ef18386a9b31753c27d9f54137b86454142e
```
