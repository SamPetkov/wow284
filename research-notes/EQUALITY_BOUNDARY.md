# Equality in the regular diameter-three criterion

**Status:** proved for connected regular graphs of girth at least five and
diameter three. The scalar algebra is checked by
`scripts/verify_equality_boundary.py`; the exact 96-vertex boundary example is
checked independently by `scripts/verify_jorgensen_96.py`. No classification or
novelty claim is made.

## Theorem

Let `G` be a connected `k`-regular graph of girth at least five and diameter
three. Write

\[
 k=\theta_0,\theta_1,\ldots,\theta_{n-1}
\]

for its adjacency eigenvalues. Then

\[
 \delta^*(G)=-\lambda_{\min}(D(G))
\]

if and only if

\[
 \max_{i\ge1}|\theta_i+1|=\sqrt{2k-2}.
\]

Equivalently, equality holds precisely when

\[
 D+kI\succeq0
\]

and `D+kI` is singular.

If `2k-2` is not a square, the two boundary adjacency eigenvalues

\[
 -1\pm\sqrt{2k-2}
\]

occur with the same multiplicity. Hence the distance eigenvalue `-k` has even
multiplicity.

If `2k-2` is a square, then necessarily

\[
 k=2r^2+1
\]

for an integer `r\ge1`.

## Proof

The diameter-three identity gives

\[
 D+kI=3J+(2k-2)I-(A+I)^2.
\]

On `\mathbf1^\perp`, an adjacency eigenvalue `\theta` therefore gives the
shifted distance eigenvalue

\[
 2k-2-(\theta+1)^2.
\]

The principal shifted distance eigenvalue is

\[
 3n-k^2-3.
\]

Because the graph has girth at least five, its closed radius-two ball has
`k^2+1` vertices. Diameter three supplies at least one further vertex, so

\[
 n\ge k^2+2.
\]

Consequently

\[
 3n-k^2-3\ge2k^2+3>0.
\]

Thus the least eigenvalue of `D+kI` occurs on `\mathbf1^\perp`, and

\[
 \lambda_{\min}(D)+k
 =2k-2-\max_{i\ge1}(\theta_i+1)^2.
\]

Equality in WOW-284 is exactly the vanishing of this quantity, proving the
first two statements.

The two possible boundary values are the roots of

\[
 x^2+2x-(2k-3).
\]

If `2k-2` is not a square, this polynomial is irreducible over `\mathbb Q`.
The adjacency characteristic polynomial lies in `\mathbb Z[x]`, so algebraic
conjugacy forces the two roots to have the same multiplicity. Both map to the
same distance eigenvalue `-k`, whose multiplicity is therefore even.

If `2k-2=s^2`, then `s` is even because its square is even. Writing `s=2r`
gives

\[
 k=\frac{s^2+2}{2}=2r^2+1.
\]

## Exact order-96 boundary example

The repository contains the published adjacency list of Jørgensen's
9-regular graph of order 96 and girth five. Its exact adjacency characteristic
polynomial contains

\[
 (x-3)^7(x+5),
\]

and

\[
 -1\pm\sqrt{2\cdot9-2}=3,-5.
\]

Both boundary adjacency eigenvalues map to the distance eigenvalue `-9`.
Their multiplicities add to eight, matching the exact distance factor

\[
 (x+9)^8.
\]

Thus

\[
 \delta^*=9,
 \qquad
 \lambda_{\min}(D)=-9,
\]

and the graph lies exactly on the WOW-284 boundary.

Run

```text
python scripts/verify_equality_boundary.py
python scripts/verify_jorgensen_96.py
```

for the symbolic and finite exact checks.

## Scope and literature status

The graph construction and its public adjacency list are due to Leif
K. Jørgensen and are available through his girth-five graph archive. Spectral
Moore bounds, predistance-polynomial methods, and equality phenomena are part
of an established literature. The statement above is the direct equality
form of the WOW-284 diameter-three criterion; it is not presented as a
classification theorem or a priority claim.
