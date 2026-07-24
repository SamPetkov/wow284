# Exact closure of the degree-six \(c\ge 15\) gate

**Status:** candidate gate closure, pending independent review and green CI.  
**Scope:** connected 6-regular graphs of girth at least five and diameter three.

Write
\[
  n=37+c.
\]
A strict WOW-284 counterexample must have every nonprincipal adjacency
eigenvalue in
\[
  \bigl(-1-\sqrt{10},-1+\sqrt{10}\bigr).
\]

## 1. Distance-layer compression

Fix a vertex. The distance layers have sizes
\[
  1,\quad 6,\quad 30,\quad c.
\]
Let \(a\) be the average number of neighbors that a distance-two vertex has
inside the distance-two layer. Edge counting and nonnegativity of the
distance-three internal degree give
\[
  a\ge a_0:=5-\frac c5.
\]

The normalized symmetric compression is
\[
S(a)=
\begin{pmatrix}
0&\sqrt6&0&0\\
\sqrt6&0&\sqrt5&0\\
0&\sqrt5&a&(5-a)\sqrt{30/c}\\
0&0&(5-a)\sqrt{30/c}&6-\frac{30(5-a)}c
\end{pmatrix}.
\]
With
\[
  z=(0,0,1,-\sqrt{30/c})^{\mathsf T},
\]
one has the exact rank-one identity
\[
  S(a)-S(a_0)=(a-a_0)zz^{\mathsf T}\succeq0.
\]
Thus each ordered eigenvalue of \(S(a)\) is at least the corresponding
eigenvalue of \(S(a_0)\). The matrix \(S(a)\) is a compression of the
adjacency matrix and has eigenvalue \(6\), with eigenvector given by the square
roots of the layer sizes. Hence \(\lambda_1(S(a))=6\). Since
\(S(a_0)\preceq S(a)\), we have \(\lambda_1(S(a_0))\le6\); the
characteristic polynomial below already has the factor \(x-6\), so
\(\lambda_1(S(a_0))=6\).

The characteristic polynomial of \(S(a_0)\) is
\[
  \det(xI-S(a_0))
  =\frac{x-6}{5}\,p_{6,c}(x),
\]
where
\[
  p_{6,c}(x)=5x^3+(c+5)x^2-25x-6c.
\]
Put
\[
  r=-1+\sqrt{10}.
\]
Direct substitution gives
\[
  \boxed{p_{6,c}(r)=-(2\sqrt{10}-5)(c-15).}
\]
Since \(2\sqrt{10}-5>0\), this is nonpositive for every \(c\ge15\).
As \(p_{6,c}\) has positive leading coefficient, its largest real root is at
least \(r\). The preceding argument shows that this root is a nonprincipal
eigenvalue of \(S(a_0)\), and therefore
\[
  \lambda_2(S(a))\ge \lambda_2(S(a_0))\ge r.
\]
Interlacing between the compression and the adjacency matrix gives
\[
  \lambda_2(A)\ge r.
\]
This contradicts the strict WOW window. Equality at \(c=15\) already excludes
strict violation. Hence
\[
  \boxed{c\le14,\qquad n\le51.}
\]

At the boundary,
\[
  p_{6,15}(x)=5(x+2)(x^2+2x-9),
\]
whose largest root is exactly \(-1+\sqrt{10}\).

## 2. Independent fourth-moment certificate

Let
\[
  k=\theta_0,\theta_1,\ldots,\theta_{n-1}
\]
be the adjacency eigenvalues and put \(y_i=\theta_i+1\) for \(i\ge1\).
For a \(k\)-regular graph with no triangle or 4-cycle,
\[
\operatorname{tr}A=0,\quad
\operatorname{tr}A^2=nk,\quad
\operatorname{tr}A^3=0,\quad
\operatorname{tr}A^4=nk(2k-1).
\]
A direct expansion yields
\[
\boxed{
\sum_{i=1}^{n-1}
(2k-2-y_i^2)(y_i+1)^2
=(k+2)\bigl((k+2)(k^2+3)-6n\bigr).
}
\]
In a strict regular diameter-three counterexample,
\[
  2k-2-y_i^2>0
\]
for every \(i\ge1\). The sum cannot vanish: vanishing would force
\(y_i+1=0\), hence \(\theta_i=-2\), for every nonprincipal eigenvalue.
The trace equation would then give
\[
  0=k-2(n-1),\qquad n=1+\frac{k}{2},
\]
whereas a simple \(k\)-regular graph has \(n\ge k+1\). Thus the sum is
strictly positive. Therefore
\[
  n<\frac{(k+2)(k^2+3)}6.
\]
At \(k=6\), this gives \(n<52\), hence again \(n\le51\).

## 3. Optimality inside the fourth-moment quadratic class

For any quadratic \(q\) nonnegative on
\([ -\sqrt{2k-2},\sqrt{2k-2}]\), the analogous fourth-moment certificate
cannot improve the preceding order bound. The exact remainder is
\[
  \frac{k(k-1)(k^2+3)}6\,q(-1)\ge0.
\]
The choice \(q(y)=(y+1)^2\) attains equality in this comparison.

## Verification

Run
```text
python scripts/verify_degree_six_gate.py
```
The script checks every displayed identity with exact SymPy arithmetic and
contains no floating-point spectral decision.
