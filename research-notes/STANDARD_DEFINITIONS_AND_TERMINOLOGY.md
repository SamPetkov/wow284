# Standard definitions and terminology protocol

This file fixes the graph-theoretic and spectral conventions used throughout
the post-v1 WOW-284 research stack. It distinguishes standard terminology from
project shorthand and is part of the theorem-by-theorem proof-audit protocol.

Principal reference anchors are Aouchiche--Hansen, *Distance spectra of graphs:
A survey*, Linear Algebra Appl. 458 (2014), 301--386, DOI
`10.1016/j.laa.2014.06.010`, especially Section 1 and Conjecture 7.16, and
Haemers, *Interlacing eigenvalues and graphs*, Linear Algebra Appl. 226--228
(1995), 593--616, DOI `10.1016/0024-3795(95)00199-2`, especially Theorem 2.1
and Corollary 2.3.

Moore terminology is anchored by Hoffman--Singleton, *On Moore graphs with
diameters 2 and 3*, IBM J. Res. Dev. 4 (1960), 497--504, DOI
`10.1147/rd.45.0497`. Distance-regular terminology is anchored by
Brouwer--Cohen--Neumaier, *Distance-Regular Graphs*, Springer, 1989, DOI
`10.1007/978-3-642-74341-2`.

## 1. Graph conventions

Unless a theorem explicitly says otherwise, a graph is finite, simple,
undirected, and connected.

- \(V(G)\) and \(E(G)\) are the vertex and edge sets.
- \(N(v)\) is the **open neighborhood** of \(v\); it does not contain \(v\).
- \(N[v]=N(v)\cup\{v\}\) is the **closed neighborhood**.
- \(d(v)=|N(v)|\) is the ordinary vertex degree.
- \(\delta(G)=\min_v d(v)\) and \(\Delta(G)=\max_v d(v)\) are the ordinary minimum
  and maximum degrees.
- \(\Gamma_i(v)=\{u:d_G(u,v)=i\}\) is the distance-\(i\) sphere when this notation
  is used.
- The diameter is \(\operatorname{diam}(G)=\max_{u,v}d_G(u,v)\).
- The girth \(g(G)\) is the length of a shortest cycle; a tree may be assigned
  infinite girth.
- \(G-S\) denotes the induced subgraph on \(V(G)\setminus S\).

The word **puncture** is project shorthand for vertex deletion. Formal theorem
statements should use “the induced subgraph \(G-S\)” or “delete the vertices in
\(S\)” before introducing the shorthand.

## 2. Dual degree

For a vertex of positive degree, the **dual degree** is

\[
 d^*(v)=\frac1{d(v)}\sum_{u\in N(v)}d(u).
\]

Thus dual degree is the mean degree of the neighbors of \(v\), not the ordinary
degree and not the unnormalised sum of neighbor degrees. The minimum dual
degree is

\[
 \delta^*(G)=\min_{v\in V(G)}d^*(v).
\]

Connected graphs of order at least two have no isolated vertices, so the
quantity is well-defined in the WOW-284 setting. If \(G\) is \(k\)-regular, then

\[
 d^*(v)=k
\]

for every vertex and hence \(\delta^*(G)=k\).

The symbols \(\delta(G)\) and \(\delta^*(G)\) must never be interchanged. When a
proof writes simply \(\delta\), it must state explicitly that
\(\delta=\delta(G)\) is the ordinary minimum degree.

## 3. Distance matrix and distance spectrum

For a connected graph, the distance matrix is

\[
 D(G)=\bigl(d_G(u,v)\bigr)_{u,v\in V(G)}.
\]

It is a real symmetric matrix. Its eigenvalues are the **distance eigenvalues**.
When ordered nonincreasingly they are

\[
 \partial_1(G)\ge\cdots\ge\partial_n(G).
\]

The least distance eigenvalue may be written either as

\[
 \partial_n(G)
 \quad\text{or}\quad
 \lambda_{\min}(D(G)).
\]

The manuscript should use one notation consistently within each theorem. The
characteristic polynomial convention is

\[
 \chi_M(x)=\det(xI-M).
\]

For \(D(G)\), and more generally for every real symmetric matrix \(M\) used
here, algebraic and geometric multiplicities agree. The average-row quotient
introduced below need not be symmetric, but it is diagonally similar to a real
symmetric compression and is therefore diagonalizable over \(\mathbb R\).
Characteristic-polynomial exponents always record algebraic multiplicity.

## 4. WOW-284 score

The quantity

\[
 \Phi(G)=\delta^*(G)+\lambda_{\min}(D(G))
\]

is project shorthand, not established graph-theoretic terminology. It should be
introduced before use and called the **counterexample score** or simply the
**score** only after that definition.

For a graph \(G\) satisfying the hypotheses of WOW-284 -- \(G\) connected,
\(|V(G)|\ge3\), and \(g(G)\ge5\) -- the conjecture is \(\Phi(G)\le0\), and the
logical trichotomy is

\[
 \Phi(G)>0 \;\Longleftrightarrow\; \text{strict counterexample},
\]

\[
 \Phi(G)=0 \;\Longleftrightarrow\; \text{equality case},
\]

\[
 \Phi(G)<0 \;\Longleftrightarrow\; \text{strictly satisfies the conjectured inequality}.
\]

Outside this hypothesis class, the sign of \(\Phi\) is only a numerical score
and does not confer counterexample or equality-case status.

“Negative control” and “equality control” are computational-research shorthand,
not standard graph classes. They must not be used as though they were
classification terms.

## 5. Rayleigh--Ritz and matrix positivity

For a real symmetric matrix \(M\),

\[
 \lambda_{\min}(M)=\min_{x\ne0}\frac{x^{\mathsf T}Mx}{x^{\mathsf T}x}.
\]

Accordingly, every test vector gives an **upper bound** on
\(\lambda_{\min}(M)\). The sign direction must be checked whenever bounds on
matrix entries are inserted into a quadratic form.

- \(M\succeq0\) means \(x^{\mathsf T}Mx\ge0\) for every \(x\).
- \(M\succ0\) means \(x^{\mathsf T}Mx>0\) for every nonzero \(x\).

For a rational symmetric matrix, exact positive definiteness may be certified by
an exact \(LDL^{\mathsf T}\) decomposition with all diagonal pivots positive.
Positive semidefiniteness cannot in general be certified by the same no-pivoting
criterion unless zero pivots and the associated kernel are handled correctly.

## 6. Partitions, quotients, compressions, and interlacing

Let \(M\) be a real symmetric matrix and let
\(\mathcal P=(C_1,\ldots,C_r)\) be a partition into nonempty cells. Let \(Z\)
be the matrix whose \(i\)-th column is \(\mathbf1_{C_i}\), and put
\[
 R=\operatorname{diag}(|C_1|,\ldots,|C_r|).
\]

The matrix of average row sums

\[
 B_{ij}=\frac1{|C_i|}
 \sum_{u\in C_i}\sum_{v\in C_j}M_{uv}
\]

is the quotient matrix
\[
 B=R^{-1}Z^{\mathsf T}MZ
\]
associated with the partition. The partition is
**equitable for \(M\)** only when, for each \(i,j\), the row sum

\[
 \sum_{v\in C_j}M_{uv}
\]

is independent of the choice of \(u\in C_i\). Equitability is equivalent to
invariance of \(\operatorname{im}Z\). In that case \(B\) represents the
restriction of \(M\) to the cell-constant subspace, so every eigenvalue of \(B\)
lifts to an eigenvalue of \(M\).

For an arbitrary partition, put
\[
 S=ZR^{-1/2}.
\]
Its columns are the normalized cell indicators. Then

\[
 Q=S^{\mathsf T}MS
   =R^{1/2}BR^{-1/2}
\]

is the symmetric **compression to normalized cell indicators**. Its eigenvalues
interlace those of \(M\) by Poincaré separation, equivalently the
Rayleigh--Ritz/min--max principle. Cauchy interlacing is the principal-submatrix
special case. The displayed identity gives the exact diagonal similarity
between \(Q\) and the average-row quotient \(B\), but \(Q\) should not be called
an equitable quotient unless equitability has been proved.

The term “normalized quotient” is acceptable only when the matrix is displayed
or explicitly defined as the symmetric compression.

## 7. Moore terminology

For maximum degree \(k\) and diameter two, the Moore bound is

\[
 |V(G)|\le1+k+k(k-1)=k^2+1.
\]

A graph attaining this bound is a **Moore graph** and, in the nontrivial
diameter-two case, is necessarily \(k\)-regular. If a finite graph has diameter
two and girth exactly five, then it is regular and hence is a Moore graph; its
radius-two count attains \(k^2+1\). The weaker convention \(g(G)\ge5\) also
allows acyclic graphs: a diameter-two star has infinite girth but does not
attain \(k^2+1\).

“Moore-type” is informal and should be avoided in theorem statements unless a
specific relaxation is defined. “Moore puncture” is project shorthand; the
standard description is “a vertex-deleted induced subgraph of a Moore graph.”

## 8. Strongly regular and distance-regular graphs

The labels **strongly regular** and **distance-regular** must be used only after
their defining intersection parameters or equivalent standard conditions have
been verified. A graph with few distinct adjacency eigenvalues or a
low-dimensional adjacency algebra is not automatically distance-regular.
Similarly, a graph of diameter two is not automatically strongly regular.

## 9. Project-specific terminology

The following expressions are allowed only after local definitions and should
not be presented as standard literature terms:

- counterexample score;
- punctured Moore graph or Moore puncture;
- layer-respecting matching deletion;
- high-edge subgraph;
- two-sided nonbacktracking LP cone;
- endpoint-neighborhood obstruction;
- deletion robustness radius;
- negative or equality control.

Each such term should be accompanied by the exact construction, matrix, cone,
or parameter it denotes.

## 10. Audit checklist

Every theorem audit must check:

1. whether \(N(v)\) is open or closed in every formula;
2. whether \(d(v)\), \(\delta(G)\), and \(\delta^*(G)\) are distinguished;
3. whether the distance-matrix and characteristic-polynomial conventions are
   fixed;
4. whether “equitable,” “quotient,” “compression,” and “interlacing” are used
   with their standard meanings;
5. whether a project shorthand has been defined before use;
6. whether strict and non-strict inequalities are preserved;
7. whether eigenvalue multiplicities and omitted invariant subspaces are fully
   accounted for;
8. whether any claimed graph class, such as strongly regular or
   distance-regular, has actually been proved.
