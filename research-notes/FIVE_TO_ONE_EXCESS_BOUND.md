# The five-to-one integral excess bound

**Status:** exact project derivation under Proof Audit 14; promotion requires the
same independent proof and literature checks as the preceding optimal-slack
results.

## 1. Statement

Let \(G\) be a connected \(k\)-regular graph of girth at least five and diameter
three, where \(k\ge6\), and suppose that every nonprincipal adjacency
eigenvalue lies in the open shifted WOW interval

\[
 I_k=(-1-\sqrt{2k-2},-1+\sqrt{2k-2}).
\]

Write

\[
 g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),
 \qquad
 C_k=(k+2)^2(k^2+3),
 \qquad
 h_k=6(k+2).
\]

The integral excess matrix is

\[
 E=g_k(A)-(h_k+1)J+I.
\]

It is symmetric, entrywise nonnegative, integral, has zero diagonal, and has
constant row sum

\[
 \varepsilon=C_k-(h_k+1)n+1.
\]

On \(\mathbf1^\perp\), the optimal slack matrix is \(I-E\), so every
nonprincipal eigenvalue of \(E\) is at most one.

Define

\[
 \boxed{
 r=2\varepsilon-n-2
   =2C_k-(2h_k+3)n.
 }
\]

Then every strict candidate satisfies

\[
 \boxed{n\le5r}.
\]

Consequently

\[
 \boxed{
 n\le
 \left\lfloor
 \frac{5C_k}{5h_k+8}
 \right\rfloor
 =
 \left\lfloor
 \frac{5(k+2)^2(k^2+3)}{30k+68}
 \right\rfloor.
 }
\]

Compared with the exact one-variable LP ceiling \(B_k=C_k/h_k\), the unrounded
improvement is

\[
 B_k-\frac{5C_k}{5h_k+8}
 =\frac{8C_k}{h_k(5h_k+8)}
 =\frac{2(k+2)(k^2+3)}{3(15k+34)},
\]

which is asymptotic to \(2k^2/45\).

## 2. Quantization of a doubled excess edge

Assume for contradiction that \(n>5r\).  The relation

\[
 \varepsilon=\frac{n+r+2}{2}
\]

shows that \(r>0\).  Put

\[
 \rho=\frac{\varepsilon-1}{n}=\frac12+\frac{r}{2n}.
\]

The optimal slack matrix has the exact form

\[
 \mathcal M=I-E+\rho J,
 \qquad
 \mathcal M\succeq0,
 \qquad
 \mathcal M\mathbf1=0.
\]

For distinct vertices, the centered two-vertex cut inequality gives

\[
 E_{uv}\le1+\frac{2(\varepsilon-1)}n
          =2+\frac rn<3.
\]

Thus every off-diagonal entry of \(E\) belongs to \(\{0,1,2\}\).

Suppose \(E_{uv}=2\).  The vector \(e_u+e_v\) has squared
\(\mathcal M\)-norm

\[
 \delta=4\rho-2=\frac{2r}{n}.
\]

For a third vertex \(w\), put \(s_w=E_{uw}+E_{vw}\in\mathbb Z\).  Its inner
product with the pair vector is

\[
 2\rho-s_w=1+\frac rn-s_w.
\]

Since \(\mathcal M_{ww}=1+\rho=3/2+r/(2n)\), Cauchy--Schwarz gives

\[
 \left(1+\frac rn-s_w\right)^2
 \le
 \frac{2r}{n}\left(\frac32+\frac{r}{2n}\right)
 =\frac{3r}{n}+\frac{r^2}{n^2}.
\]

If \(s_w\ne1\), the smallest possible absolute value of the left-hand base is
\(1-r/n\).  The inequality

\[
 \frac{3r}{n}+\frac{r^2}{n^2}
 <\left(1-\frac rn\right)^2
\]

is equivalent to \(n>5r\).  Hence \(s_w=1\) for every
\(w\notin\{u,v\}\).  Summing over those vertices gives

\[
 n-2
 =\sum_{w\notin\{u,v\}}(E_{uw}+E_{vw})
 =2(\varepsilon-2)
 =n+r-2,
\]

contradicting \(r>0\).  Therefore \(E\) is a simple graph.

## 3. The complementary least-eigenvalue graph

Let

\[
 X=\overline E.
\]

Then \(X\) is regular of degree

\[
 d=n-1-\varepsilon=\frac{n-r-4}{2},
\]

and, on \(\mathbf1^\perp\),

\[
 A(X)=-I-E.
\]

Thus

\[
 \lambda_{\min}(A(X))\ge-2.
\]

Every connected component of \(X\) is \(d\)-regular.  Moreover,

\[
 d+1=\frac{n-r-2}{2}.
\]

Since \(n>5r\) and \(n\ge k^2+2\ge38\), three components would require

\[
 n\ge3(d+1)=\frac{3(n-r-2)}2,
\]

or \(n\le3r+6\), which is impossible.  Hence \(X\) is connected or has
exactly two components.

We use the classical Cameron--Goethals--Seidel--Shult classification in its
regular form: a connected regular graph with least eigenvalue at least \(-2\)
and more than \(28\) vertices is a line graph or a cocktail-party graph.  The
root graph of a connected regular line graph is regular or semiregular
bipartite.

### 3.1 Connected case

Assume first that \(X\) is connected.  It is not cocktail-party because that
would give degree \(n-2\).

If \(X=L(Y)\) with \(Y\) regular, then the degree of \(Y\) is

\[
 q=\frac{d+2}{2}=\frac{n-r}{4}.
\]

The number of vertices of \(Y\) is \(2n/q=8n/(n-r)<10\).  Simplicity of
\(Y\) requires \(q\le |V(Y)|-1\).  Since \(n\ge38\) and \(n>5r\), this would
force \(q=8\), \(|V(Y)|=9\), and \(n=36\), a contradiction.

If \(Y\) is semiregular bipartite of degrees \(p,q\), let

\[
 a=\frac np,
 \qquad
 b=\frac nq
\]

be the two part sizes, with \(a\ge b\ge2\).  Then

\[
 \frac1a+\frac1b
 =\frac{p+q}{n}
 =\frac{n-r}{2n}
 \in\left(\frac25,\frac12\right).
\]

The only integer possibilities with product at least \(n\) and \(n\ge38\)
are

\[
 (a,b,n,r)=(13,3,39,7)
 \quad\text{or}\quad
 (14,3,42,8).
\]

The radius-two lower bound \(n\ge k^2+2\) then forces \(k=6\), but the exact
formula \(r=2C_k-(2h_k+3)n\) gives neither \(7\) nor \(8\).  Thus the
connected case is impossible.

### 3.2 Two-component case

Suppose now that \(X=X_1\sqcup X_2\).  Write

\[
 |V(X_i)|=d+1+a_i,
 \qquad a_i\ge0.
\]

Then

\[
 a_1+a_2=r+2.
\]

For \(k\ge9\), the inequality \(n>5r\) makes both component orders larger
than \(28\).  For \(k=6,7,8\), direct substitution into
\(r=2C_k-(2h_k+3)n\), together with the radius-two and parity conditions,
shows that no order satisfies \(r>0\) and \(n>5r\).  Hence the regular
least-eigenvalue classification applies to both components.

A cocktail-party component has \(a_i=1\), and a complete component has
\(a_i=0\).  A regular line-graph root is impossible by the same root-size
argument as in the connected case.  For a noncomplete semiregular bipartite
root, if \(A\ge B\ge2\) are its part sizes, then

\[
 \frac1A+\frac1B
 =\frac{d+2}{|V(X_i)|}
 >\frac35.
\]

Thus \(B=2\) with \(2\le A\le9\), or \((A,B)=(3,3)\).  In every case
\(AB\le18\), contradicting simplicity because the component has more than
\(28\) edges.  Therefore each component is complete or cocktail-party, so

\[
 a_1+a_2\le2,
\]

contrary to \(a_1+a_2=r+2>2\).

This completes the proof of \(n\le5r\).

## 4. Consequences

The closed-form order bound gives

\[
\begin{array}{c|ccccc}
 k&6&7&8&9&10\\
 \hline
 n\text{ (before parity)}&50&75&108&150&201.
\end{array}
\]

Parity improves the degree-seven value to \(74\).  Continuing,

\[
\begin{array}{c|cccccc}
 k&11&12&13&14&15&16\\
 \hline
 n\text{ (before parity)}&263&336&422&521&636&765.
\end{array}
\]

Thus odd degree improves the \(k=11\) value to \(262\).  The theorem also
removes the residual order \(1259\) at degree \(19\), giving \(n\le1258\).

The accompanying exact verifier checks every algebraic identity, the
Cauchy--Schwarz threshold, the reciprocal-part-size enumeration, the low-degree
vacuity checks, and the stated order table.

## 5. Literature boundary

The optimal-slack matrix, integral excess matrix, doubled-edge quantization,
and five-to-one bound are project-derived.  The sole external structural input
is the classical classification of connected regular graphs with least
eigenvalue at least \(-2\): line graph, cocktail-party graph, or order at most
\(28\).  The original root-system classification is due to Cameron, Goethals,
Seidel and Shult, *Journal of Algebra* 43 (1976), 305--327,
DOI `10.1016/0021-8693(76)90162-9`; the regular formulation is recorded in
Cvetkovi\'c, Rowlinson and Simi\'c, *Spectral Generalizations of Line Graphs*,
Cambridge University Press, 2004, Theorem 3.12.2.
