# An exact ceiling for the standard two-sided nonbacktracking LP method

**Status:** exact project derivation, pending independent mathematical review,
literature-priority clearance, and green CI. No novelty claim is made.

## 1. Setting

Fix an integer \(k\ge4\). Define the nonbacktracking polynomials by
\[
F_0(x)=1,\qquad F_1(x)=x,\qquad F_2(x)=x^2-k,
\]
and
\[
F_i(x)=xF_{i-1}(x)-(k-1)F_{i-2}(x)\qquad(i\ge3).
\]
Then
\[
F_i(k)=k(k-1)^{i-1}\qquad(i\ge1).
\]
For a \(k\)-regular graph, \(\operatorname{tr}F_i(A)\) counts closed
nonbacktracking walks of length \(i\). In a graph of girth at least five,
\[
\operatorname{tr}F_i(A)=0\qquad(1\le i\le4),
\]
while
\[
\operatorname{tr}F_i(A)\ge0\qquad(i\ge5).
\]

The regular diameter-three WOW window is
\[
I_k=
[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
\]
Consider any finite polynomial
\[
f(x)=\sum_{i=0}^d f_iF_i(x)
\]
satisfying
\[
f_0>0,\qquad f_i\ge0\ (i\ge5),\qquad f(x)\le0\ (x\in I_k).
\]
The usual nonbacktracking linear-programming argument gives
\[
|V(G)|\le\frac{f(k)}{f_0}
\]
for every \(k\)-regular graph of girth at least five whose nonprincipal
adjacency spectrum lies in \(I_k\).

The framework is standard; see H. Nozaki, *Linear Programming Bounds for
Regular Graphs*, Graphs and Combinatorics 31 (2015), 1973--1984,
DOI `10.1007/s00373-015-1613-7`, arXiv:1407.4562. The two-sided WOW
specialization and the optimal dual certificate below are project derivations
whose priority is unresolved.

## 2. Exact optimal value

### Theorem

For every integer \(k\ge4\), every polynomial satisfying the preceding LP
conditions obeys
\[
\boxed{
\frac{f(k)}{f_0}
\ge
B_k:=\frac{(k+2)(k^2+3)}6.
}
\]
Equality is attained by
\[
\boxed{
f_*(x)=
\frac{(x+2)^2\bigl(x^2+2x-(2k-3)\bigr)}{6(k+2)}.
}
\]
Consequently, no polynomial degree in this standard LP hierarchy can improve
the order bound \(n\le B_k\). For a strict WOW-window graph, equality at
\(B_k\) is impossible, so
\[
\boxed{n<B_k.}
\]
At \(k=6\), this is exactly
\[
n<52,\qquad n\le51.
\]

### Primal certificate

The exact expansion is
\[
\begin{aligned}
6(k+2)f_*(x)
={}&6(k+2)F_0(x)+2(2k+7)F_1(x)\\
&+(k+13)F_2(x)+6F_3(x)+F_4(x).
\end{aligned}
\]
Thus the \(F_0\)-coefficient is one after normalization, and all coefficients
of degree at least five vanish. On \(I_k\),
\[
x^2+2x-(2k-3)=(x+1)^2-(2k-2)\le0,
\]
so \(f_*\le0\). Finally,
\[
f_*(k)=\frac{(k+2)(k^2+3)}6=B_k.
\]

## 3. Dual measure

Put
\[
\Delta=\sqrt{2k-2},
\qquad
\xi_-=-1-\Delta,
\qquad
\xi_0=-2,
\qquad
\xi_+=-1+\Delta.
\]
Define the positive weights
\[
\begin{aligned}
w_-&=
\frac{k(k+2)\bigl(2k^2-6-3(k-1)\Delta\bigr)}{24(2k-3)},\\
w_0&=
\frac{k(k-1)(k^2+3)}{6(2k-3)},\\
w_+&=
\frac{k(k+2)\bigl(2k^2-6+3(k-1)\Delta\bigr)}{24(2k-3)}.
\end{aligned}
\]
The only nonobvious positivity is that of \(w_-\). Since \(2k^2-6>0\), it
follows from
\[
(2k^2-6)^2-18(k-1)^3
=2(k-3)(2k-3)(k^2+3)>0.
\]
Let
\[
\mu=w_-\delta_{\xi_-}+w_0\delta_{\xi_0}+w_+\delta_{\xi_+}.
\]
Its mass is
\[
\mu(1)=B_k-1=\frac{k(k^2+2k+3)}6.
\]
Direct calculation gives
\[
\mu(F_i)=-F_i(k)\qquad(1\le i\le4).
\]
For \(5\le i\le9\), the slacks
\[
a_i:=\mu(F_i)+F_i(k)
\]
are
\[
\begin{aligned}
a_5={}&\frac{k(k-1)(k+2)(k^2+3)}3,\\
a_6={}&\frac{k(k-1)(k+2)(5k-13)(k^2+3)}6,\\
a_7={}&\frac{k(k-1)(k+2)(k^2+3)(3k^2-17k+25)}3,\\
a_8={}&\frac{k(k-1)(k+2)(k^2+3)}6
       (6k^3-47k^2+139k-150),\\
a_9={}&\frac{k(k-1)(k+2)(k^2+3)}3
       (3k^4-27k^3+106k^2-219k+194).
\end{aligned}
\]
They are strictly positive for \(k\ge4\). For the last three factors, writing
\(k=m+4\) gives respectively
\[
3m^2+7m+5,
\]
\[
6m^3+25m^2+51m+38,
\]
and
\[
3m^4+21m^3+70m^2+101m+54.
\]

## 4. Uniform tail bound

All three support points lie in
\[
[-2\sqrt{k-1},2\sqrt{k-1}]
\]
when \(k\ge4\). If
\[
t=2\sqrt{k-1}\,z,\qquad |z|\le1,
\]
then for \(i\ge2\),
\[
F_i(t)
=(k-1)^{i/2}U_i(z)
-(k-1)^{(i-2)/2}U_{i-2}(z),
\]
where \(U_i\) is the Chebyshev polynomial of the second kind. Since
\(|U_j(z)|\le j+1\),
\[
|F_i(t)|
\le
(k-1)^{i/2}
\left(i+1+\frac{i-1}{k-1}\right).
\]
Writing \(r=k-1\ge3\), the ratio of the resulting measure bound to
\(F_i(k)=k(k-1)^{i-1}\) is at most
\[
R_{r,i}
=
\frac{(r^2+4r+6)((i+1)r+i-1)}{6r^{i/2}}.
\]
For \(r\ge3\),
\[
r^2+4r+6\le3r^2,
\]
and
\[
(i+1)r+i-1\le\frac{4i+2}{3}r.
\]
Therefore
\[
R_{r,i}
\le
\frac{2i+1}{3}r^{3-i/2}
\le
\frac{2i+1}{3}3^{3-i/2}.
\]
At \(i=10\), the last expression is \(7/9\), and it decreases thereafter
because
\[
(2i+3)^2<3(2i+1)^2.
\]
Hence
\[
\mu(F_i)>-F_i(k)\qquad(i\ge10).
\]
Together with the finite checks, this proves
\[
\mu(F_i)\ge-F_i(k)\qquad(i\ge5).
\]

## 5. Dual conclusion

Since \(f\le0\) on the support of \(\mu\),
\[
\int f\,d\mu\le0.
\]
On the other hand,
\[
\begin{aligned}
\int f\,d\mu
&=(B_k-1)f_0
  -\sum_{i=1}^4 f_iF_i(k)
  +\sum_{i=5}^d f_i\mu(F_i)\\
&\ge
(B_k-1)f_0-\sum_{i=1}^d f_iF_i(k)\\
&=B_kf_0-f(k).
\end{aligned}
\]
Thus \(f(k)\ge B_kf_0\), proving the ceiling.

If a graph has strict WOW window and \(n=B_k\), equality in the primal
certificate would force every nonprincipal adjacency eigenvalue to be a zero
of \(f_*\). The endpoints are excluded by strictness, so every such eigenvalue
would equal \(-2\). The trace equation would then give
\[
0=k-2(n-1),
\]
which is incompatible with \(n\ge k+1\). Hence \(n<B_k\).

## 6. Consequence for the next search

At degree six, higher-degree polynomials in the standard one-point
nonbacktracking LP hierarchy cannot reduce the candidate range below
\[
40\le n\le51.
\]
Any further reduction must use information outside that hierarchy, such as:

- additional local intersection constraints;
- cycle-count congruences or realizability constraints;
- a multi-point or semidefinite refinement;
- canonical generation.

## Verification

Run
```text
python scripts/verify_two_sided_lp_ceiling.py
```
The script checks the primal expansion, dual weights, moments, finite slacks,
and uniform tail inequalities with exact symbolic arithmetic.
