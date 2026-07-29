# The three-to-one integral excess theorem

**Status:** project derivation under Proof Audit 14.  
**Scope:** connected k-regular graphs of girth at least five and diameter three
whose nonprincipal adjacency spectrum lies in the open shifted WOW interval.  
**External input:** the classical classification of connected regular graphs
with least adjacency eigenvalue at least -2: above order 28, such a graph is a
line graph or a cocktail-party graph.

## 1. Optimal slack and integral excess

Put

```
g_k(x) = (x+2)^2 ((x+1)^2-(2k-2)),
C_k    = (k+2)^2 (k^2+3),
h_k    = 6(k+2).
```

For a graph G of order n with adjacency matrix A, define

```
M = -g_k(A) + (C_k/n) J
```

and

```
E = g_k(A) - (h_k+1) J + I.
```

The shifted spectral window gives

```
M is positive semidefinite,
M 1 = 0.
```

The matrix E is symmetric, integral, entrywise nonnegative, has zero diagonal,
and has constant row sum

```
epsilon = C_k - (h_k+1)n + 1.
```

On the orthogonal complement of the all-ones vector,

```
M = I-E.
```

Define the integral excess parameter

```
r = 2 epsilon - n - 2
  = 2 C_k - (12k+27)n.
```

The divisibility identity

```
128(2C_k-r)
 = (4k+9)(64k^3+112k^2+196k+327) + (129-128r)
```

implies

```
4k+9 divides 129-128r.
```

The previously audited least-eigenvalue classification argument gives r>0.
Section 2 records a uniform irreducibility lemma that removes the modular
irreducibility choices from that proof.

## 2. A uniform irreducibility lemma

For every integer k at least 6, except k=7,

```
g_k(x)+2
```

is irreducible over the rationals.

After the translation y=x+2, the polynomial is

```
y^4 - 2y^3 + (3-2k)y^2 + 2.
```

By Gauss' lemma, a quadratic factorization over the rationals would be a
factorization into monic integer quadratics

```
(y^2 + a y + b)(y^2 + c y + d)
```

with bd=2. The four possible ordered pairs (b,d) are

```
(1,2), (2,1), (-1,-2), (-2,-1).
```

The vanishing linear coefficient and the cubic coefficient -2 force k=4 in
the positive-constant cases and k=7 in the negative-constant cases. Rational
roots give only k=2 or k=4. Thus the only reducible integer cases are below the
present degree range or k=7.

In particular the exceptional degrees k=44, 62, and 158 appearing in the
r<=0 classification all have irreducible quartic annihilators. Their relevant
rational primary subspaces have dimensions 7406, 10219, and 332373,
respectively, none divisible by four. This replaces all degree-specific
modular certificates in the positivity proof.

## 3. The theorem

### Theorem

Under the hypotheses above,

```
r > 0
and
n <= 3r.
```

Consequently

```
n <= floor( 3 (k+2)^2 (k^2+3) / (18k+41) ).
```

The unrounded improvement over the exact one-variable LP ceiling is

```
(k+2)(k^2+3)/6
 - 3(k+2)^2(k^2+3)/(18k+41)
 =
5(k+2)(k^2+3)/(6(18k+41)).
```

This is asymptotic to 5k^2/108.

The point is structural: the LP theorem optimizes the abstract polynomial cone,
whereas the present improvement uses the integrality and graph-realizability of
g_k(A).

## 4. A doubled excess edge is impossible when n>3r

Assume for contradiction that n>3r and write

```
x = r/n,
rho = (1+x)/2.
```

Then 0<x<1/3 and

```
M = I-E+rho J.
```

The two-by-two principal minors show that every off-diagonal entry of E is at
most 2.

Suppose E_uv=2. For w outside {u,v}, put

```
s_w = E_uw + E_vw.
```

For p=e_u+e_v,

```
p^T M p       = 2x,
p^T M e_w     = 1+x-s_w,
e_w^T M e_w   = (3+x)/2.
```

Cauchy-Schwarz gives

```
(1+x-s_w)^2 <= x(3+x).
```

For 0<x<1/3 and integral nonnegative s_w, this forces s_w in {1,2}.
Summing the two row sums shows that exactly r vertices have s_w=2.
Let W be that set, let y be the sum of their coordinate vectors, and put

```
e_W = sum_{w<z in W} E_wz.
```

Then

```
p^T M y = r(x-1),
y^T M y = r + r^2 rho - 2e_W.
```

The two-dimensional Gram determinant is nonnegative, hence

```
2xr + r^2(3x-1) - 4x e_W >= 0.
```

Since e_W>=0,

```
2x + r(3x-1) >= 0,
```

which is equivalent to

```
n <= 3r+2.
```

Together with n>3r, one has n=3r+t with t=1 or 2.

Substitution into

```
r = 2C_k-(12k+27)n
```

gives

```
(36k+82)r = 2C_k-(12k+27)t.
```

Set m=18k+41. Since gcd(m,18)=1, m must divide a fixed integer remainder.
The exact remainders are

```
t=1: 167642 = 2*109*769,
t=2: 202634 = 2*71*1427.
```

No divisor m>=149 with m congruent to 5 modulo 18 occurs for t=1. For t=2
the sole necessary candidate is m=1427, hence k=77. It gives

```
r=25943, n=77831,
```

but kn is odd, contradicting the handshake lemma. Therefore E is simple.

This aggregate argument replaces the separate three- and four-vertex type
enumerations used in the provisional four-to-one proof.

## 5. The complement has at most two components

Let

```
X = complement(E).
```

Then X is regular of degree

```
d = (n-r-4)/2
```

and has least adjacency eigenvalue at least -2.

If X had at least three components, each would have at least d+1 vertices.
Therefore

```
n >= 3(d+1),
```

so n<=3r+6. Since n>3r, write n=3r+t with 1<=t<=6.

The same fixed-remainder calculation gives:

| t | remainder | necessary (m,k) candidates |
|---|-----------|-----------------------------|
| 1 | 167642 | none |
| 2 | 202634 | (1427,77), excluded by handshake parity |
| 3 | 237626 | (6989,386), but the corresponding r is not integral |
| 4 | 272618 | none |
| 5 | 307610 | none |
| 6 | 342602 | none |

Thus X has at most two components.

## 6. Connected complement

Since n>=k^2+2>=38, the large regular least-eigenvalue-minus-two
classification applies. The cocktail-party case would force r=-n, so X must
be a line graph L(Y). A connected regular line graph has a root Y that is
regular or bipartite semiregular.

### 6.1 Regular root

Let Y be q-regular on v vertices. Then

```
q = (n-r)/4 > n/6,
v = 2n/q < 12.
```

Simplicity gives q<=v-1. Together with n>=38, the only arithmetic
possibilities are

```
(q,v,n,r) =
(8,10,40,8),
(9,10,45,9),
(8,11,44,12),
(10,11,55,15).
```

The radius-two lower bound gives k<=7. Direct substitution in the exact
formula for r excludes all four cases.

### 6.2 Bipartite semiregular root

Let the part sizes be a>=b>=2 and the degrees be p=n/a<=q=n/b. Then

```
p+q = (n-r)/2 > n/3,
```

so q>n/6 and therefore b<6.

The relation

```
(b-2)n = b(r+2p)
```

handles the remaining values.

- b=2 forces r<0.
- b=5 and n>3r force n<38.
- b=4 leaves only `(p,q,a,b,n,r)=(4,10,10,4,40,12)` and
  `(4,11,11,4,44,14)`; the radius bound gives k=6, and the exact r formula
  excludes both.
- b=3 has p=2 or p=3. These give n=3r+12 and n=3r+18.

For the last two families, m=18k+41 would have to divide

```
552554 = 2*276277
```

or

```
762506 = 2*381253.
```

The two odd cofactors are prime and are congruent to 13 modulo 18, whereas m
is congruent to 5 modulo 18. Hence neither family is possible.

Thus X cannot be connected.

## 7. Two-component complement

For k=6,7,8, the interval imposed by r>0 and n>3r contains no admissible
integer order. Hence k>=9, and the same inequalities force n>150. Each
component then has order greater than 28, so the classification applies to
each component.

A regular line-graph root is impossible: its degree is greater than n/6,
while its number of vertices is less than eight.

For a bipartite semiregular root of one component, if its order is N then

```
1/a + 1/b = (d+2)/N >= (n-r)/(n+r+2).
```

Since n>3r and n>150,

```
(n-r)/(n+r+2) > 49/100.
```

If b>=3, the only possible pairs have product at most 18, smaller than the
component order. The remaining case b=2 is necessarily the complete
bipartite root K_{d,2}; its line graph has order 2d.

Therefore every component is one of:

```
K_{d+1},
a cocktail-party graph of order d+2,
L(K_{d,2}) of order 2d.
```

Two components of the first two types would give r<=0. One L(K_{d,2})
component gives

```
n=3r+10
```

or

```
n=3r+8.
```

The fixed-remainder constants are

```
t=10: 482570 = 2*5*11*41*107,
t=8 : 412586 = 2*67*3079.
```

The t=8 case has no admissible divisor. The t=10 case has the sole necessary
candidate k=123, which yields an odd product kn and is excluded by the
handshake lemma.

If both components are L(K_{d,2}), then n=2r+8. The corresponding linear
remainder is

```
1792898 = 2*896449,
```

and has no admissible divisor of the form 24k+55.

This contradiction completes the proof of n<=3r.

## 8. Numerical effect

Before parity, the bound gives:

| k | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---|---|---|---|----|----|----|----|----|----|----|----|----|----|----|----|
| n max | 50 | 75 | 108 | 150 | 201 | 263 | 336 | 422 | 521 | 635 | 765 | 911 | 1075 | 1257 | 1459 | 1681 |

Parity improves every odd-degree entry to the preceding even integer.

The first visible improvement over the provisional four-to-one floor occurs
at k=21: 1681 instead of 1682. The theorem is nevertheless conceptually
stronger for every degree because its unrounded defect improvement is larger.

## 9. Verification and claim boundary

The independent verifier is

```
scripts/verify_three_to_one_excess_bound.py
```

It checks:

1. the slack, excess, divisibility, and order-bound identities;
2. the uniform irreducibility exceptional set for g_k(x)+2;
3. all three exceptional r<=0 multiplicity obstructions;
4. the doubled-edge aggregate Gram calculation;
5. every fixed linear remainder and divisor candidate;
6. the connected regular- and semiregular-root reductions;
7. the two-component classification arithmetic;
8. the exact order table.

The least-eigenvalue-minus-two classification is an external theorem, not
reproved by the script. The theorem should remain in the research-audit layer
until its citation and every classification invocation receive a separate
line-by-line review.
