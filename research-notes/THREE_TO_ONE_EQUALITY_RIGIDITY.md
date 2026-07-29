# Equality rigidity in the three-to-one integral excess bound

**Status:** exact arithmetic corollary of the three-to-one theorem.  
**Claim boundary:** this classifies the parameter set at which equality could
occur; it does not prove that a graph with those parameters exists.

Let

\[
 C_k=(k+2)^2(k^2+3),
 \qquad
 r=2C_k-(12k+27)n.
\]

The three-to-one theorem gives

\[
 n\le3r.
\]

Suppose equality holds.  Substituting \(n=3r\) into the definition of \(r\)
gives

\[
 \boxed{
 (18k+41)r=C_k.
 }
\]

Thus \(18k+41\) divides \(C_k\).  Since
\(\gcd(18k+41,18)=1\), the exact Euclidean division

\[
\begin{aligned}
 18^4C_k={}&(18k+41)
 (5832k^3+10044k^2+17946k+29107)\\
 &+66325
\end{aligned}
\]

shows that

\[
 18k+41\mid66325.
\]

Now

\[
 66325=5^2\cdot7\cdot379.
\]

For \(k\ge6\), the divisor \(18k+41\) is at least \(149\) and is congruent to
\(5\pmod{18}\).  Among the divisors of \(66325\), the unique divisor with these
properties is

\[
 1895=18\cdot103+41.
\]

Hence equality in the three-to-one theorem can occur only at

\[
 \boxed{k=103.}
\]

The corresponding parameters are forced:

\[
 C_{103}=116997300,
 \qquad
 r=\frac{C_{103}}{1895}=61740,
 \qquad
 n=3r=185220.
\]

Therefore

\[
 \boxed{
 n=3r
 \quad\Longrightarrow\quad
 (k,n,r)=(103,185220,61740).
 }
\]

The handshake product is even, so parity does not exclude this unique arithmetic
case.  No existence claim is made.

The exact verifier is

```text
scripts/verify_three_to_one_equality_rigidity.py
```

and checks the polynomial remainder, divisor classification, parameter values,
and the defining equality.
