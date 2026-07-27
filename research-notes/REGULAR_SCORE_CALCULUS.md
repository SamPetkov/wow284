# A two-regime score calculus for regular WOW-284 graphs

## Purpose

This note compresses the regular diameter-two and diameter-three arguments into
one theorem.  It is a mathematical reorganisation of proved material, not a
priority claim.  Its value is expository: every regular example in the present
paper can be checked from one scalar adjacency-spectrum statistic.

For a connected graph \(G\), write

\[
  \Phi(G):=\delta^*(G)+\lambda_{\min}(D(G)).
\]

Thus \(G\) is a strict WOW-284 counterexample exactly when \(\Phi(G)>0\).

## The master theorem

### Theorem

Let \(G\) be a connected \(k\)-regular graph of girth at least five.

1. If \(G\) has diameter two, then \(G\) is a Moore graph of order
   \(k^2+1\),
   
   \[
     D=2J-2I-A,
   \]
   
   and
   
   \[
     \Phi(G)=k-2-\lambda_2(A),
   \]
   
   where \(\lambda_2(A)\) is the largest nonprincipal adjacency eigenvalue.
   In this regime
   
   \[
     \lambda_2(A)=\frac{-1+\sqrt{4k-3}}2,
   \]
   
   so
   
   \[
     \Phi(G)=k-\frac{3+\sqrt{4k-3}}2.
   \]
   
   Hence the graph is a strict counterexample exactly when \(k>3\), and lies
   on equality when \(k=3\).

2. If \(G\) has diameter three, define the shifted adjacency radius
   
   \[
     \rho_{-1}(G):=
     \max_{\theta\in\operatorname{Spec}(A),\ \theta\ne k}|\theta+1|.
   \]
   
   Then
   
   \[
     D=3J+(k-3)I-2A-A^2
   \]
   
   and
   
   \[
     \boxed{\Phi(G)=2k-2-\rho_{-1}(G)^2.}
   \]
   
   Consequently \(G\) is a strict counterexample, equality graph, or negative
   control according as
   
   \[
     \rho_{-1}(G)
     <,=,>
     \sqrt{2k-2}.
   \]

### Proof

Fix a vertex \(v\).  Girth at least five makes the vertices reached by
nonbacktracking walks of lengths zero, one, and two from \(v\) distinct.  If the
diameter is two, these \(1+k+k(k-1)=k^2+1\) vertices exhaust the graph.  Thus
\(G\) attains the Moore bound.  Adjacent vertices have no common neighbour and
nonadjacent vertices have exactly one, so

\[
  A^2=(k-1)I-A+J.
\]

Every nonedge has distance two, whence

\[
  D=2J-2I-A.
\]

On the all-ones line, \(D\) has the positive transmission eigenvalue
\(2(k^2)-k\).  On \(\mathbf 1^\perp\), an adjacency eigenvalue \(\theta\)
therefore maps to \(-2-\theta\).  The least distance eigenvalue is obtained from
the largest nonprincipal adjacency eigenvalue, giving

\[
  \Phi(G)=k-2-\lambda_2(A).
\]

Restricting the Moore identity to \(\mathbf 1^\perp\) gives

\[
  A^2+A-(k-1)I=0,
\]

so the largest nonprincipal root is
\(( -1+\sqrt{4k-3})/2\).  For \(k\ge2\), the sign comparison reduces to

\[
  (2k-3)^2-(4k-3)=4(k-1)(k-3).
\]

The degree-two score is negative, the degree-three score is zero, and every
realisable degree \(k>3\) gives a strict violation.

Now suppose the diameter is three.  Since the graph contains no triangle or
4-cycle, its distance-two matrix is

\[
  A_2=A^2-kI.
\]

Using \(A_3=J-I-A-A_2\),

\[
  D=A+2A_2+3A_3
   =3J+(k-3)I-2A-A^2.
\]

The all-ones vector has distance eigenvalue

\[
  3|V(G)|-k^2-k-3.
\]

Because every off-diagonal entry of \(D\) is positive and every row sum is the
same, this is the Perron eigenvalue and hence the largest distance eigenvalue.
On \(\mathbf 1^\perp\), an adjacency eigenvalue \(\theta\) maps to

\[
  k-3-2\theta-\theta^2
  =k-2-(\theta+1)^2.
\]

The least distance eigenvalue is therefore

\[
  k-2-\rho_{-1}(G)^2.
\]

Regularity gives \(\delta^*(G)=k\), proving the displayed score formula.
\(\square\)

## Exact examples through one table

| graph | \(k\) | diameter | controlling statistic | \(\lambda_{\min}(D)\) | \(\Phi\) |
|---|---:|---:|---:|---:|---:|
| Petersen | 3 | 2 | \(\lambda_2=1\) | \(-3\) | \(0\) |
| Hoffman--Singleton | 7 | 2 | \(\lambda_2=2\) | \(-4\) | \(3\) |
| O'Keefe--Wong 40-vertex graph | 6 | 3 | \(\rho_{-1}^2=9\) | \(-5\) | \(1\) |
| Hoffman--Singleton second subconstituent | 6 | 3 | \(\rho_{-1}^2=9\) | \(-5\) | \(1\) |

The order-96 Jørgensen graph is an exact diameter-three equality control:
\(\delta^*=9\) and \(\lambda_{\min}(D)=-9\).  Its provenance and complete exact
spectrum remain certified separately by
`scripts/verify_jorgensen96_provenance.py`.

## Manuscript use

The theorem can replace several repeated calculations in a selective Version 2
manuscript.

- The Moore section proves the diameter-two line once.
- The regular 40- and 42-vertex examples need only display their adjacency
  spectra and evaluate \(\rho_{-1}\).
- Equality and negative controls can be discussed in the same scalar language.
- Later degree and diameter obstructions can be introduced as restrictions on
  the two remaining regular regimes.

A compact transition is:

> For regular girth-five graphs of diameter at most three, WOW-284 is governed
> by one adjacency statistic: the largest nonprincipal eigenvalue in diameter
> two and the spectral radius about \(-1\) in diameter three.

## Exact executable audit

`scripts/verify_regular_score_calculus.py` independently checks:

- the adjacency-to-distance spectral transfer for the Petersen,
  Hoffman--Singleton, 40-vertex, and 42-vertex graphs;
- the exact distance spectra and WOW scores in the table;
- the diameter-two scalar identity
  \(\Phi=k-2-\lambda_2(A)\);
- the diameter-three scalar identity
  \(\Phi=2k-2-\rho_{-1}^2\);
- the Moore threshold through degree \(10\,000\) using only the exact identity
  \(4(k-1)(k-3)\).

The script does not replace the graph-level structural and provenance
certificates already present in the repository.
