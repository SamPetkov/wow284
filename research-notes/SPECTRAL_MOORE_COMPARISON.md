# Exact comparison with the published spectral-Moore bound

The upper side of the regular diameter-three WOW window is a one-sided
spectral-Moore constraint. This note compares the project bound with the
published theorem without treating the one-sided theorem as sufficient for
WOW-284.

Cioabă, Koolen, Nozaki, and Vermette, Theorem 2.3 in
*Maximizing the Order of a Regular Graph of Given Valency and Second
Eigenvalue* (SIAM J. Discrete Math. 30 (2016), 1509--1525,
DOI `10.1137/15M1030935`, arXiv:1503.06286), use the tridiagonal matrix
\(T(k,t,c)\). If \(\theta\) is its second eigenvalue, their theorem gives
\[
v(k,\theta)
\le
1+\sum_{i=0}^{t-3}k(k-1)^i+\frac{k(k-1)^{t-2}}c.
\]

For
\[
k=6,\qquad t=4,\qquad \theta=-1+\sqrt{10},
\qquad c=\frac{16+2\sqrt{10}}3,
\]
the exact characteristic polynomial is
\[
(x-6)(x+1-\sqrt{10})
\left(
x^2+\frac{13+5\sqrt{10}}3x
+\frac{20+10\sqrt{10}}3
\right).
\]
The two roots of the final quadratic are both below \(\theta\), so \(\theta\)
is the second eigenvalue of \(T(6,4,c)\). The published bound becomes
\[
v(6,-1+\sqrt{10})
\le
\frac{211}{3}-\frac{25\sqrt{10}}6.
\]
Exact squaring gives
\[
57<
\frac{211}{3}-\frac{25\sqrt{10}}6
<58,
\]
hence
\[
v(6,-1+\sqrt{10})\le57.
\]

The project-specific two-sided WOW argument gives \(n\le51\), which is
strictly stronger in this parameter case. This comparison does not claim a
new spectral-Moore theorem.

Run
```text
python scripts/verify_spectral_moore_comparison.py
```
for the exact symbolic certificate.
