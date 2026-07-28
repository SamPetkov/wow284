# The four-to-one integral excess theorem

**Status:** exact project derivation under Proof Audit 14.  Promotion still
requires independent proof and literature review.

## 1. Statement

Let \(G\) be a connected \(k\)-regular graph of girth at least five and diameter
three, where \(k\ge6\), and suppose that all nonprincipal adjacency eigenvalues
lie in the open shifted WOW interval.  Put

\[
 g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),
 \qquad
 C_k=(k+2)^2(k^2+3),
 \qquad
 h_k=6(k+2),
\]

and define the integral excess matrix

\[
 E=g_k(A)-(h_k+1)J+I.
\]

Then \(E\) is symmetric, entrywise nonnegative and integral, has zero diagonal,
and has constant row sum

\[
 \varepsilon=C_k-(h_k+1)n+1.
\]

On \(\mathbf1^\perp\), the optimal slack matrix is \(I-E\), so every
nonprincipal eigenvalue of \(E\) is at most one.  Define

\[
 \boxed{
 r=2arepsilon-n-2
  =2C_k-(12k+27)n.
 }
\]

Then

\[
 \boxed{r>0}
 \qquad\text{and}\qquad
 \boxed{n\le4r}.
\]

Consequently every such graph satisfies

\[
 \boxed{
 n\le
 \left\lfloor
 \frac{8(k+2)^2(k^2+3)}{48k+109}
 \right\rfloor.
 }
\]

The unrounded improvement over the exact one-variable LP ceiling is

\[
 \frac{C_k}{h_k}-rac{8C_k}{8h_k+13}
 =rac{13(k+2)(k^2+3)}{6(48k+109)}
 \sim\frac{13}{288}k^2.
\]

## 2. A divisibility identity

Since

\[
 n=\frac{2C_k-r}{12k+27}
\]

is integral, \(4k+9\) divides \(2C_k-r\).  The polynomial identity

\[
 128(2C_k-r)
 =(4k+9)(64k^3+112k^2+196k+327)+(129-128r)
\]

and the oddness of \(4k+9\) give

\[
 \boxed{4k+9\mid129-128r}.
\]

This finite divisibility condition is used repeatedly below.

## 3. Positivity of the excess parameter

Assume \(r\le0\).  Write

\[
 \rho=\frac{arepsilon-1}{n}=\frac12+rac{r}{2n},
 \qquad
 \mathcal M=I-E+ho J\succeq0.
\]

The \(2\times2\) principal minors give \(E_{uv}\le2+r/n\).  Thus \(E\) is a
simple graph when \(r<0\).  If \(r=0\) and \(E_{uv}=2\), then
\((e_u+e_v)^{\mathsf T}\mathcal M(e_u+e_v)=0\), so positivity puts
\(e_u+e_v\) in the kernel.  Subtracting its projection onto \(\mathbf1\) gives
an adjacency \(-2\)-eigenvector.  Its \(u\)-coordinate would force

\[
 A_{uv}=-2+rac{2k+4}{n},
\]

which is impossible because \(n\ge k^2+2\) and \(A_{uv}\in\{0,1\}\).  Hence
\(E\) is simple also at \(r=0\).

Let \(X=\overline E\).  Then \(X\) is regular of degree

\[
 d=n-1-arepsilon=rac{n-r-4}{2},
\]

and \(\lambda_{\min}(A(X))\ge-2\).  Since \(d+1\ge(n-2)/2\), \(X\) has at most
two connected components.

We use the classical regular least-eigenvalue-\(-2\) classification: a connected
regular graph of order greater than \(28\) and least eigenvalue at least \(-2\)
is a line graph or a cocktail-party graph.

### 3.1 Connected complement

If \(X\) is complete, then \(E=0\).  This is the one-level case
\(g_k(A)=(h_k+1)J-I\), already excluded by irreducibility of \(g_k(x)+1\) and
the adjacency trace.

If \(X\) is cocktail-party, then \(arepsilon=1\) and \(r=-n\).  The exact
condition \(n=C_k/(h_k+1)\), together with

\[
 1296C_k
 =(6k+13)(216k^3+396k^2+654k+1175)+277,
\]

forces \(6k+13\mid277\), hence \(k=44\) and \(n=14812\).  The excess graph is a
perfect matching.  Its \(-1\)-eigenspace has dimension \(7406\), but on that
space the adjacency matrix is annihilated by the quartic \(g_{44}(x)+2\), which
is irreducible modulo \(11\).  An irreducible quartic primary component has
dimension divisible by four, a contradiction.

A regular line-graph root is impossible: its degree would be at least \(n/4\),
while its number of vertices would be at most eight, contradicting simplicity
for \(n\ge38\).

For a semiregular bipartite root with part sizes \(a\ge b\ge2\),

\[
 \frac1a+rac1b=rac{n-r}{2n}\ge\frac12.
\]

All cases with \(b\ge3\) have \(ab<38\).  The remaining case \(b=2\) must be the
complete bipartite root \(K_{a,2}\), and forces \(r=-4\).  The divisibility
condition leaves only \(k=158\), \(n=664748\).  Here the \(-1\)-eigenspace of
\(E\) has dimension \(332373\), whereas \(g_{158}(x)+2\) is irreducible modulo
\(23\); again the dimension is not divisible by four.

### 3.2 Two components

Write the component orders as \(d+1+a_1\) and \(d+1+a_2\).  Then

\[
 a_1+a_2=r+2,
\]

so \(r\in\{-2,-1,0\}\).  The divisibility condition, parity and the radius-two
lower bound leave only

\[
 (r,k,n)=(-1,62,40875).
\]

Both components have order greater than \(28\).  Since their total excess is
one, the classification forces one complete component and one cocktail-party
component, of orders \(20437\) and \(20438\).  The excess spectrum then contains
\(-1\) with multiplicity \(10219\).  But \(g_{62}(x)+2\) is irreducible modulo
\(23\), contradicting divisibility of the corresponding rational primary
component by four.

Thus \(r>0\).

## 4. Quantization of a doubled excess edge

Assume for contradiction that \(n>4r\), and put \(x=r/n\in(0,1/4)\).  Then

\[
 \rho=\frac{1+x}{2},
 \qquad
 \mathcal M=I-E+ho J.
\]

Suppose \(E_{uv}=2\).  For \(w\notin\{u,v\}\), put
\(s_w=E_{uw}+E_{vw}\).  The pair vector \(e_u+e_v\) satisfies

\[
 (e_u+e_v)^{\mathsf T}\mathcal M(e_u+e_v)=2x,
\]

and

\[
 (e_u+e_v)^{\mathsf T}\mathcal M e_w=1+x-s_w.
\]

Cauchy--Schwarz gives

\[
 (1+x-s_w)^2\le x(3+x).
\]

Since \(x<1/4\), this forces \(s_w\in\{1,2\}\).  Summing over \(w\) shows that
exactly \(r\) vertices have \(s_w=2\).

The \(3\times3\) determinant for a vertex of type \((2,0)\) or \((0,2)\) is

\[
 \frac{11x-3}{2}<0.
\]

Therefore every one of the \(r\) exceptional vertices has type \((1,1)\).
If two such vertices \(w,z\) existed, put \(c=E_{wz}\in\{0,1,2\}\).  The
corresponding \(4\times4\) determinants are

\[
 3(4x-1),
 \qquad
 6(3x-1),
 \qquad
 9(2x-1),
\]

for \(c=0,1,2\), respectively.  All are negative.  Hence \(r\le1\).  Since
\(r>0\), one has \(r=1\), but the divisibility identity would require
\(4k+9\mid1\), impossible.  Thus \(E\) is simple.

## 5. Classification of the simple excess graph

Again put \(X=\overline E\).  It is regular of degree

\[
 d=rac{n-r-4}{2}
\]

and has least eigenvalue at least \(-2\).  The inequality \(n>4r\), together
with \(n\ge38\), shows that \(X\) has at most two components.

### 5.1 Connected case

The complete and cocktail-party cases are excluded by \(r>0\).  Suppose
\(X=L(Y)\).

If \(Y\) is regular of degree \(q\), then

\[
 q=rac{n-r}{4}>rac{3n}{16},
 \qquad
 |V(Y)|=rac{2n}{q}<rac{32}{3}.
\]

Simplicity leaves only the finite possibilities
\((q,|V(Y)|)=(8,10)\) or \((9,10)\), giving \((n,r)=(40,8)\) or \((45,9)\).
The radius-two bound forces \(k=6\), and the exact formula for \(r\) rules out
both.

If \(Y\) is semiregular bipartite with part sizes \(a\ge b\ge2\), then

\[
 \frac1a+rac1b=rac{n-r}{2n}\in\left(\frac38,\frac12\right).
\]

Simplicity and \(n\ge38\) leave only \(b=3\), \(13\le a\le23\), with the
finite edge counts allowed by divisibility of the two part degrees.  Direct
substitution into \(r=2C_k-(12k+27)n\), with \(n\ge k^2+2\) and \(kn\) even,
rules out every case.

### 5.2 Two-component case

For \(k=6,7,8\), direct substitution shows that no admissible order has
\(r>0\) and \(n>4r\).  Hence \(k\ge9\).  Each component then has order greater
than \(28\).

A regular line-graph root is impossible: its root degree exceeds \(3n/16\),
while its root order is less than seven.  For a semiregular bipartite root,
component size and \(n>4r\) give

\[
 \frac1a+rac1b>rac7{12}.
\]

The possible part sizes have product at most \(22\), smaller than the component
order.  Thus every component is complete or cocktail-party.  Their excesses
over \(d+1\) are \(0\) and \(1\), so \(a_1+a_2\le2\), contradicting
\(a_1+a_2=r+2>2\).

This proves \(n\le4r\).

## 6. Resulting order windows

The closed-form bound gives, before parity,

\[
\begin{array}{c|rrrrrrrrrrrrrrr}
 k&6&7&8&9&10&11&12&13&14&15&16&17&18&19&20\\
 \hline
 n&50&75&108&150&201&263&336&422&521&635&765&911&1075&1257&1459.
\end{array}
\]

Parity improves the odd-degree entries, for example

\[
 k=7:n\le74,
 \quad
 k=11:n\le262,
 \quad
 k=15:n\le634,
 \quad
 k=19:n\le1256.
\]

The accompanying verifier checks all polynomial identities, modular
irreducibility certificates, finite line-root cases, Gram determinants and the
order table exactly.

## 7. Literature boundary

The optimal slack matrix, excess parameter, doubled-edge quantization and
four-to-one theorem are project-derived.  The sole external structural input is
the classical classification of connected regular graphs with least eigenvalue
at least \(-2\), due to Cameron, Goethals, Seidel and Shult, together with its
standard regular line-graph formulation.
