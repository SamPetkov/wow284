# The exact ceiling of the two-sided nonbacktracking LP method

**Status:** exact theorem with an independent proof audit and exact Python
verification. Literature priority for the two-sided optimiser is unresolved;
no novelty claim is made.

## 1. What is being optimised

Fix an integer \(k\ge4\). Define the nonbacktracking polynomials by

\[
 F_0(x)=1,\qquad F_1(x)=x,\qquad F_2(x)=x^2-k,
\]

and, for \(i\ge3\),

\[
 F_i(x)=xF_{i-1}(x)-(k-1)F_{i-2}(x).
\]

They satisfy

\[
 F_i(k)=k(k-1)^{i-1}\qquad(i\ge1).
\]

For a \(k\)-regular graph, \(\operatorname{tr}F_i(A)\) counts closed
nonbacktracking walks of length \(i\). Therefore, if the girth is at least five,

\[
 \operatorname{tr}F_i(A)=0\quad(1\le i\le4),
\]

while

\[
 \operatorname{tr}F_i(A)\ge0\quad(i\ge5).
\]

This explains the precise coefficient cone used below: coefficients of
\(F_1,\dots,F_4\) may have either sign, but coefficients of every \(F_i\) with
\(i\ge5\) must be nonnegative.

Set

\[
 I_k=[-1-\sqrt{2k-2},\,-1+\sqrt{2k-2}].
\]

Call a finite polynomial

\[
 f(x)=\sum_{i=0}^d f_iF_i(x)
\]

**admissible** when

\[
 f_0>0,\qquad f_i\ge0\ (i\ge5),\qquad f(x)\le0\ (x\in I_k).
\]

This is the girth-five, two-sided specialization of the standard
nonbacktracking linear-programming framework. The underlying framework is due
to Nozaki; the exact two-sided certificate below is a project derivation whose
priority remains unresolved.

## 2. The LP bound for a graph

Let \(G\) be a \(k\)-regular graph of girth at least five, and suppose every
nonprincipal adjacency eigenvalue lies in \(I_k\). For an admissible \(f\),

\[
 \operatorname{tr}f(A)
 =nf_0+\sum_{i=5}^d f_i\operatorname{tr}F_i(A)
 \ge nf_0.
\]

On the other hand, the spectral decomposition gives

\[
 \operatorname{tr}f(A)
 =f(k)+\sum_{\theta\ne k}f(\theta)
 \le f(k).
\]

Hence

\[
 \boxed{n\le\frac{f(k)}{f_0}.}
\]

The problem is therefore to minimise \(f(k)/f_0\) over the admissible cone.

## 3. Main theorem: value and unique optimiser

Define

\[
 B_k=\frac{(k+2)(k^2+3)}6
\]

and

\[
 f_*(x)=
 \frac{(x+2)^2\bigl(x^2+2x-(2k-3)\bigr)}{6(k+2)}.
\]

### Theorem

For every integer \(k\ge4\) and every admissible polynomial \(f\),

\[
 \boxed{\frac{f(k)}{f_0}\ge B_k.}
\]

Equality holds if and only if \(f\) is a positive scalar multiple of \(f_*\).
Consequently, increasing the polynomial degree cannot improve this
one-variable nonbacktracking LP bound.

For a graph whose nonprincipal spectrum lies in the **open** interval
\(\operatorname{int}I_k\), equality in the graph order bound is impossible, so

\[
 \boxed{n<B_k.}
\]

At \(k=6\),

\[
 B_6=52,
\qquad
 n<52,
\qquad
 n\le51.
\]

## 4. Primal certificate

The exact expansion is

\[
\begin{aligned}
 6(k+2)f_*(x)
 ={}&6(k+2)F_0(x)+2(2k+7)F_1(x)\\
 &+(k+13)F_2(x)+6F_3(x)+F_4(x).
\end{aligned}
\]

Thus the normalized \(F_0\)-coefficient is one and all coefficients of degree
at least five vanish. Moreover,

\[
 x^2+2x-(2k-3)=(x+1)^2-(2k-2)\le0
\]

on \(I_k\), so \(f_*\le0\) there. Finally,

\[
 f_*(k)=B_k.
\]

This proves that the optimum is at most \(B_k\). The dual certificate proves
that it is no smaller.

## 5. Three-point dual certificate

Write

\[
 \Delta=\sqrt{2k-2},
 \qquad
 \xi_-=-1-\Delta,
 \qquad
 \xi_0=-2,
 \qquad
 \xi_+=-1+\Delta.
\]

Define

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

All three weights are positive. Only \(w_-\) requires work. Since both terms
being compared are positive,

\[
 (2k^2-6)^2-18(k-1)^3
 =2(k-3)(2k-3)(k^2+3)>0
\]

implies

\[
 2k^2-6>3(k-1)\Delta.
\]

Let

\[
 \mu=w_-\delta_{\xi_-}+w_0\delta_{\xi_0}+w_+\delta_{\xi_+}.
\]

Its mass is

\[
 \mu(1)=B_k-1=\frac{k(k^2+2k+3)}6.
\]

The first four moments match exactly:

\[
 \mu(F_i)=-F_i(k)\qquad(1\le i\le4).
\]

For \(i\ge5\), define the dual slack

\[
 a_i=\mu(F_i)+F_i(k).
\]

The proof needs

\[
 \boxed{a_i>0\qquad(i\ge5).}
\]

The strict inequality is important: it later forces every coefficient
\(f_i\), \(i\ge5\), to vanish in an equality case.

## 6. Finite dual slacks

For \(5\le i\le9\), exact calculation gives

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

These are positive for \(k\ge4\). For the three less immediate factors, put
\(k=m+4\). They become

\[
 3m^2+7m+5,
\]

\[
 6m^3+25m^2+51m+38,
\]

and

\[
 3m^4+21m^3+70m^2+101m+54,
\]

respectively.

## 7. Uniform tail for every degree \(i\ge10\)

Put \(r=k-1\ge3\). The support of \(\mu\) lies inside

\[
 [-2\sqrt r,2\sqrt r].
\]

The only nontrivial endpoint check is

\[
 1+\sqrt{2r}\le2\sqrt r.
\]

Both sides are positive, and after rearranging and squaring this follows from

\[
 (2r-1)^2-8r>0.
\]

At \(r=m+3\), the left side equals

\[
 4m^2+12m+1>0.
\]

For \(t=2\sqrt r\,z\) with \(|z|\le1\),

\[
 F_i(t)=r^{i/2}U_i(z)-r^{(i-2)/2}U_{i-2}(z),
\]

where \(U_i\) is the Chebyshev polynomial of the second kind. Since
\(|U_j(z)|\le j+1\),

\[
 |F_i(t)|
 \le
 r^{i/2}\left(i+1+\frac{i-1}{r}\right).
\]

Using the positivity of the dual weights and their total mass, one obtains

\[
 \frac{|\mu(F_i)|}{F_i(k)}
 \le
 R_{r,i}:=
 \frac{(r^2+4r+6)((i+1)r+i-1)}{6r^{i/2}}.
\]

For \(r\ge3\),

\[
 r^2+4r+6\le3r^2
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

At \(i=10\), this is \(7/9\). It decreases with \(i\), because

\[
 3(2i+1)^2-(2i+3)^2=8i^2-6>0.
\]

Hence

\[
 |\mu(F_i)|<F_i(k)
\]

and therefore

\[
 a_i=\mu(F_i)+F_i(k)>0
 \qquad(i\ge10).
\]

Together with the finite calculation, this proves strict positivity of every
dual slack \(a_i\) for \(i\ge5\).

## 8. Weak duality gives the optimum

Because \(f\le0\) on the support of \(\mu\),

\[
 \int f\,d\mu\le0.
\]

Using the exact moments for \(i\le4\), the nonnegative coefficients
\(f_i\) for \(i\ge5\), and the inequalities
\(\mu(F_i)\ge-F_i(k)\),

\[
\begin{aligned}
 \int f\,d\mu
 &=(B_k-1)f_0-
   \sum_{i=1}^4 f_iF_i(k)+
   \sum_{i=5}^d f_i\mu(F_i)\\
 &\ge
 (B_k-1)f_0-
 \sum_{i=1}^d f_iF_i(k)\\
 &=B_kf_0-f(k).
\end{aligned}
\]

Thus

\[
 0\ge B_kf_0-f(k),
\]

which is equivalent to

\[
 \frac{f(k)}{f_0}\ge B_k.
\]

## 9. Equality is rigid

Suppose now that

\[
 f(k)=B_kf_0.
\]

Every inequality in the dual chain must be an equality.

First, all dual slacks \(a_i\) are strictly positive for \(i\ge5\), while
\(f_i\ge0\). Hence

\[
 f_i=0\qquad(i\ge5).
\]

Thus \(f\) has degree at most four.

Second,

\[
 \int f\,d\mu=0.
\]

The three weights are positive and \(f\le0\) on \(I_k\), so

\[
 f(\xi_-)=f(-2)=f(\xi_+)=0.
\]

The point \(-2\) lies in the interior of \(I_k\). A real polynomial that is
nonpositive on an interval and vanishes at an interior point must have even
multiplicity there. Therefore \(-2\) is at least a double root.

The degree is at most four, so these roots exhaust it:

\[
 f(x)=c(x-\xi_-)(x+2)^2(x-\xi_+)
 =c(x+2)^2\bigl(x^2+2x-(2k-3)\bigr).
\]

Since the factor on the right is nonpositive on \(I_k\), admissibility and
\(f_0>0\) force \(c>0\). Hence \(f\) is a positive scalar multiple of
\(f_*\).

This proves uniqueness of the optimiser up to scaling.

## 10. Strict graph consequence

Suppose a graph has all nonprincipal eigenvalues in the open interval
\(\operatorname{int}I_k\) and has \(n=B_k\). Equality in the LP bound would
force the unique optimizer \(f_*\), and then every nonprincipal eigenvalue would
be a zero of \(f_*\).

The endpoint zeros are excluded by strictness, leaving only \(-2\). Hence every
nonprincipal adjacency eigenvalue would equal \(-2\), and the trace equation
would give

\[
 0=k-2(n-1).
\]

This is incompatible with \(n\ge k+1\) for a simple connected \(k\)-regular
graph. Thus

\[
 n<B_k.
\]

## 11. Scope and research consequence

The theorem is an exact ceiling for the following method only:

- one-variable polynomials in the nonbacktracking basis;
- trace positivity from girth at least five;
- pointwise nonpositivity on the full shifted WOW interval.

It does not cover multipoint semidefinite bounds, local intersection matrices,
cycle-incidence constraints, or canonical generation.

At degree six, this method cannot improve the candidate range beyond

\[
 40\le n\le51.
\]

The order-51 exclusion in the next research stage succeeds precisely because it
uses edge-local 5-cycle information absent from this LP cone.

## 12. Verification

The original exact certificate is

```text
python scripts/verify_two_sided_lp_ceiling.py
```

The independent audit is

```text
python scripts/verify_proof_audit_02_two_sided_lp.py
```

The second script does not import the first. It checks the recurrence, primal
expansion, dual weights, exact moments, finite slacks, support inclusion,
Chebyshev tail, uniqueness nullspace, and an exact concrete grid
\(4\le k\le12\), \(5\le i\le30\).
