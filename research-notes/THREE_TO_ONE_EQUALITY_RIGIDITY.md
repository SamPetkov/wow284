# Equality rigidity for the three-to-one bound

**Status:** exact arithmetic corollary of the three-to-one excess theorem.

Let

\[
C_k=(k+2)^2(k^2+3),
\qquad
r=2C_k-(12k+27)n.
\]

If equality holds in the unrounded inequality \(n\le3r\), then

\[
(18k+41)r=C_k.
\]

Exact Euclidean division gives

\[
\begin{aligned}
18^4C_k={}&(18k+41)
(5832k^3+10044k^2+17946k+29107)\\
&+66325.
\end{aligned}
\]

Thus \(18k+41\mid66325\). Since

\[
66325=5^2\cdot7\cdot379,
\]

and \(18k+41\ge149\) with \(18k+41\equiv5\pmod {18}\), the only
possible divisor is \(1895=18\cdot103+41\). Consequently

\[
\boxed{(k,n,r)=(103,185220,61740).}
\]

This classifies the arithmetic parameter set at equality. It does not prove
that a graph with these parameters exists, and it does not classify saturation
of the floored integer bound.

The exact audit is
`scripts/verify_three_to_one_equality_rigidity.py`.
