# Complete mathematical synthesis of the post-v1 WOW-284 programme

**Scope.** This document consolidates the mathematical content developed after
the prior v1 manuscript package. It is a theorem ledger and manuscript-planning
record, not a replacement for the individual proof notes. Every result is
classified by proof status, exact-verification status, and literature boundary.
No result in this document is automatically promoted into `main.tex`.

For a connected graph G, write

```text
D = D(G)
lambda_D(G) = lambda_min(D(G))
Phi(G) = delta*(G) + lambda_D(G)
```

Thus G is a strict counterexample to WOW-284 exactly when `Phi(G) > 0`.

## Status legend

- **v1:** already present in the prior v1 manuscript package.
- **proved / exact:** an analytic proof and an exact executable certificate are
  present in the stacked branch.
- **audited:** a separate one-proof-at-a-time audit has checked the statement,
  hypotheses, critical lemmas, and an independent verifier.
- **priority unresolved:** correctness is supported, but the literature search
  does not justify a novelty or first-priority claim.
- **computational classification:** all objects in a precisely defined finite
  family are covered exactly; this is not a classification outside that family.

The current stack is deliberately conservative. Search silence is never treated
as proof of novelty.

---

# Part I. The v1 core

## 1. Moore-graph disproof mechanism

Let M be a degree-k Moore graph of diameter two. Then

```text
|V(M)| = k^2 + 1
g(M) = 5
delta*(M) = k
A^2 = (k - 1) I - A + J
```

On the orthogonal complement of the all-ones vector, the two nonprincipal
adjacency eigenvalues are

```text
(-1 + sqrt(4k - 3))/2
(-1 - sqrt(4k - 3))/2.
```

Since every nonedge has distance two,

```text
D = 2J - 2I - A.
```

Therefore

```text
lambda_D(M) = -(3 + sqrt(4k - 3))/2
Phi(M) = k - (3 + sqrt(4k - 3))/2.
```

A Moore graph satisfies WOW-284 exactly for `k <= 3`, with equality at `k = 3`,
and is a strict counterexample for every realizable `k > 3`. The degree-seven
Hoffman--Singleton graph gives

```text
delta* = 7
lambda_D = -4
Phi = 3.
```

**Status:** v1; complete graph-level Lean formalisation for the 50-vertex
example.

## 2. Regular diameter-three spectral criterion

Let G be connected, k-regular, of girth at least five and diameter three. The
distance-two matrix is `A_2 = A^2 - kI`, so

```text
D = A + 2A_2 + 3(J - I - A - A_2)
  = 3J + (k - 3)I - 2A - A^2.
```

Equivalently,

```text
D + kI = 3J + (2k - 2)I - (A + I)^2.
```

On the orthogonal complement of the all-ones vector, a nonprincipal adjacency
eigenvalue theta maps to

```text
mu(theta) = k - 2 - (theta + 1)^2.
```

Consequently

```text
Phi(G) = 2k - 2 - max_{theta != k} (theta + 1)^2.
```

The graph is a strict counterexample exactly when

```text
|theta + 1| < sqrt(2k - 2)
```

for every nonprincipal adjacency eigenvalue theta. This shifted spectral window
is the organising principle for the entire post-v1 regular theory.

**Status:** v1; exact matrix checks on the regular order-40 and order-42
examples.

## 3. Explicit finite counterexamples in v1

The manuscript gives exact counterexamples of orders 38, 39, 40, 42, and 50.
Representative parameters are:

| order | minimum dual degree | least-distance information |
| ---: | ---: | --- |
| 38 | 17/3 | `-3 - sqrt(7)` |
| 39 | 35/6 | strictly greater than `-35/6` |
| 40 | 6 | `-5` |
| 42 | 6 | `-5` |
| 50 | 7 | `-4` |

All finite claims are reconstructed by integer BFS and exact rational or
algebraic certificates. Lean kernel-checks the complete 50-vertex theorem and
finite spectral certificates for orders 38, 39, 40, and 42.

---

# Part II. General structural extensions

## 4. Dual degree as radius-two growth

If G contains no triangle and no 4-cycle, then

```text
|Gamma_2(v)| = sum_{u in N(v)} (d(u) - 1).
```

Therefore

```text
d*(v) = (|B_2(v)| - 1)/d(v).
```

This converts the Graffiti quantity into normalised local growth. It is useful
for deletion arguments and local incidence counts, but the identity itself is
literature-established and is not claimed as new.

**Status:** proved / exact; literature-established.

## 5. Higher-diameter distance-polynomial transfer

Define the nonbacktracking polynomials by

```text
F_0(x) = 1
F_1(x) = x
F_2(x) = x^2 - k
F_i(x) = x F_{i-1}(x) - (k - 1) F_{i-2}(x),  i >= 3.
```

If G is connected and k-regular, has diameter d, and girth at least `2d - 1`,
then `A_i = F_i(A)` for `0 <= i <= d - 1`. Hence

```text
D = dJ + q_d(A)
q_d(x) = sum_{i=0}^{d-1} (i - d) F_i(x).
```

For example,

```text
q_3(x) = k - 3 - 2x - x^2
q_4(x) = -x^3 - 2x^2 + (2k - 4)x + 2k - 4.
```

**Status:** verified derivation; substantially overlaps established minimal-cage
and distance-polynomial theory, so no novelty claim is made.

---

# Part III. Diameter and degree obstructions

## 6. Regular counterexamples have degree at least six

### Theorem

If a connected regular graph of girth at least five is a strict WOW-284
counterexample, then its degree is at least six.

The first universal observation is

```text
lambda_D(G) <= -diameter(G),
```

obtained from the Rayleigh vector `e_u - e_v` on a diametral pair. Therefore a
k-regular strict counterexample must satisfy

```text
diameter(G) < k.
```

The degrees 2, 3, 4, and 5 are then closed as follows.

- `k = 2`: connected graphs are cycles and fail the strict diameter condition.
- `k = 3`: the graph would be the degree-three Moore graph and lies on equality.
- `k = 4`: diameter two is excluded by nonintegral Moore multiplicities;
  diameter three is excluded by distance-layer compression and interlacing.
- `k = 5`: diameter two is excluded by Moore multiplicities; diameter four is
  excluded by interlacing the distance matrix of a diametral path on five
  vertices; diameter three is reduced to the four `(5,5)`-cages, all of which
  have an exact distance eigenvalue at most `-5`.

Thus

```text
k >= 6.
```

**Status:** proved / exact; dedicated proof audit queued.

## 7. General endpoint-neighbourhood diameter bound

Let G be connected, have girth at least five, minimum degree delta, maximum
degree Delta, and diameter `d >= 5`. For diametral vertices u and v, put
`p = d(u)` and `q = d(v)`, and use a vector supported with opposite signs on
`N(u)` and `N(v)`. Optimisation gives

```text
lambda_D(G)
 <= p + q - 2 - sqrt((p - q)^2 + pq(d - 2)^2).
```

Write

```text
p = delta + alpha
q = delta + beta
t = d - 2.
```

The exact identity

```text
(p - q)^2 + p q t^2 - (p + q + delta(t - 2))^2
 = (t - 2) [delta t(alpha + beta) + (t + 2) alpha beta]
 >= 0
```

yields

```text
lambda_D(G) <= -delta(d - 4) - 2.
```

Since `delta*(G) <= Delta`, every strict counterexample must satisfy

```text
Delta > delta(d - 4) + 2.
```

Equivalently,

```text
diameter(G) <= 3 + ceil((Delta - 2)/delta).
```

For a k-regular graph this becomes

```text
diameter(G) <= 4.
```

More quantitatively, every regular graph in the hypotheses with `d >= 5`
satisfies

```text
Phi(G) <= k(5 - d) - 2 < 0.
```

**Status:** proved / exact symbolic audit; independent proof audit and priority
search queued.

## 8. Diameter-four obstruction

Let G be connected, k-regular, of girth at least five and diameter four. Choose
diametral vertices u and v, put `U = N(u)`, `V = N(v)`, and let r be the number
of pairs `(a,b) in U x V` at distance two. Girth at least five gives

```text
r <= k(k - 1),
```

so

```text
sum_{a in U, b in V} d(a,b) >= 2k^2 + k.
```

A signed Rayleigh vector reduces to the two-by-two matrix

```text
[ -4          -2 sqrt(k) ]
[ -2 sqrt(k)       -3    ].
```

Therefore

```text
lambda_D(G) <= -(7 + sqrt(16k + 1))/2
Phi(G) <= k - (7 + sqrt(16k + 1))/2.
```

For `2 <= k <= 9`, the right-hand side is negative. Hence no regular strict
counterexample of degree at most nine has diameter four.

**Status:** proved / exact symbolic audit; independent proof audit and priority
search queued.

## 9. Regular-counterexample trichotomy

Every regular strict counterexample has exactly one of the following forms.

1. **Diameter two:** a Moore graph.
2. **Diameter three:** all nonprincipal adjacency eigenvalues lie in the strict
   shifted WOW window.
3. **Diameter four:** necessarily `k >= 10`.

There are no regular strict counterexamples of diameter at least five.

For fixed k, the search is finite. In the diameter-four regime the ordinary
Moore bound gives

```text
|V(G)| <= 1 + k sum_{i=0}^3 (k - 1)^i
       = k^4 - 2k^3 + 2k^2 + 1.
```

---

# Part IV. Diameter-three order bounds and method optimality

## 10. Fourth-moment score bound

For a k-regular girth-five diameter-three graph, write the nonprincipal
adjacency eigenvalues as theta_i and put `y_i = theta_i + 1`. Exact trace
identities give

```text
sum y_i^2 = (k + 1)(n - k - 1)
sum y_i^4 = (2k^2 + 5k + 1)n - (k + 1)^4.
```

If `R = max_i |y_i|`, then `sum y_i^4 <= R^2 sum y_i^2`, and
`Phi = 2k - 2 - R^2`. Therefore

```text
Phi(G)
 <= [(k + 1)^2(k^2 + 3) - (5k + 3)n]
    / [(k + 1)(n - k - 1)].
```

Every strict counterexample consequently satisfies

```text
n < (k + 1)^2(k^2 + 3)/(5k + 3).
```

This was the first general order bound in the extension stack.

## 11. Stronger fourth-moment identity

A sharper exact identity is

```text
sum_{i=1}^{n-1} (2k - 2 - y_i^2)(y_i + 1)^2
 = (k + 2)[(k + 2)(k^2 + 3) - 6n].
```

In a strict counterexample every factor `2k - 2 - y_i^2` is positive. The sum
cannot vanish, since vanishing would force every nonprincipal adjacency
eigenvalue to equal `-2`, contradicting the trace equation and `n >= k + 1`.
Hence

```text
n < B_k
B_k = (k + 2)(k^2 + 3)/6.
```

At `k = 6`, this gives `n < 52`, hence `n <= 51`.

**Status:** proved / exact; independent audit queued.

## 12. Exact ceiling of the standard nonbacktracking LP hierarchy

Let `F_i` be the standard nonbacktracking polynomials. Suppose

```text
f(x) = sum_i f_i F_i(x)
f_0 > 0
f_i >= 0 for i >= 5
f(x) <= 0 on [-1 - sqrt(2k - 2), -1 + sqrt(2k - 2)].
```

Then

```text
f(k)/f_0 >= B_k = (k + 2)(k^2 + 3)/6.
```

Equality is attained by

```text
f_*(x)
 = (x + 2)^2 [x^2 + 2x - (2k - 3)] / [6(k + 2)].
```

The lower bound is certified by a positive three-point dual measure supported
at

```text
-1 - sqrt(2k - 2),  -2,  -1 + sqrt(2k - 2),
```

with exact moment matching for `F_1,...,F_4`, explicit positive slacks for
`F_5,...,F_9`, and a uniform Chebyshev estimate for every `i >= 10`.

Thus no polynomial degree in this standard one-point nonbacktracking LP
hierarchy improves the bound `n < B_k`. Any stronger theorem must use local
intersection information, multipoint semidefinite constraints, cycle
realizability, or canonical generation.

**Status:** proved / exact; proof audit and literature-priority clearance queued.

## 13. Equality boundary

A regular girth-five diameter-three graph satisfies equality in WOW-284 exactly
when

```text
max_{theta != k} |theta + 1| = sqrt(2k - 2).
```

Equivalently, `D + kI` is positive semidefinite and singular. If `2k - 2` is
not a square, algebraic conjugacy forces the two boundary adjacency eigenvalues

```text
-1 + sqrt(2k - 2)
-1 - sqrt(2k - 2)
```

to have the same multiplicity, so the distance eigenvalue `-k` has even
multiplicity. If `2k - 2` is a square, then `k = 2r^2 + 1`.

Jorgensen's 9-regular order-96 girth-five graph is an exact boundary control:

```text
delta* = 9
lambda_D = -9
Phi = 0.
```

The distance factor `(x + 9)^8` matches the contact adjacency eigenvalues 3 and
-5.

**Status:** proved / exact; graph provenance independently reconstructed.

---

# Part V. The degree-six programme

## 14. Closing the n <= 51 gate by distance-layer compression

Write

```text
n = 37 + c.
```

For a fixed vertex the layer sizes are `1, 6, 30, c`. At the smallest feasible
internal degree of the distance-two layer, the nonprincipal compression factor
is

```text
p_{6,c}(x) = 5x^3 + (c + 5)x^2 - 25x - 6c.
```

At the upper WOW boundary `r = -1 + sqrt(10)`,

```text
p_{6,c}(r) = -(2 sqrt(10) - 5)(c - 15).
```

For `c >= 15`, the largest compression root is at least the boundary; by
interlacing strict violation is impossible. Therefore

```text
c <= 14
n <= 51.
```

The stronger fourth-moment identity gives the same bound independently.

## 15. Diameter reduction at degree six

A connected 6-regular strict counterexample cannot have diameter at least four.
For vertices at distance `d >= 4`, use the signed vector with weights

```text
3 at u
1 on N(u)
-3 at v
-1 on N(v).
```

The exact estimate is

```text
x^T D x / ||x||^2 <= (204 - 81d)/15 <= -8,
```

contradicting `delta* = 6`. Diameter two would force

```text
chi_A(x) = (x - 6)(x^2 + x - 5)^18,
```

whose trace is -12, contradicting `trace(A) = 0`. Hence every 6-regular strict
counterexample has diameter three.

**Status:** audited; the original scope gap was repaired explicitly in PR #19.

## 16. Edge-local spectral inequality

For general k, put

```text
f_k(x) = (x + 2)^2 [x^2 + 2x - (2k - 3)]
C_k = f_k(k) = (k + 2)^2(k^2 + 3)
M = -f_k(A) + (C_k/n) J.
```

The matrix M is positive semidefinite. If `sigma_uv` is the number of 5-cycles
through an edge uv, then exact diagonal and edge entries of M, followed by the
two-by-two PSD condition, give

```text
sigma_uv >= 2k - 2
sigma_uv <= 2(k + 2)^2(k^2 + 3)/n - 10k - 26.
```

Independently, if `n = k^2 + 1 + c`, radius-two ball intersection gives

```text
sigma_uv >= (k - 1)^2 - c.
```

At `k = 6` and `n = 51`, these bounds force `sigma_uv = 11` on every edge. But

```text
5 N_5 = 153 * 11 = 1683
```

is impossible. Thus

```text
every connected 6-regular strict counterexample has n <= 50.
```

**Status:** audited after the diameter-scope correction; exact independent
verifier present.

## 17. Exact structure at order 50

For a hypothetical order-50 candidate, every edge lies in 12 or 13 five-cycles.
Let H be the spanning subgraph of the 13-cycle edges and let `m = |E(H)|`. If
`tau(v)` is the number of 5-cycles through v, then distance-layer compression
yields

```text
tau(v) in {36, 37, 38}
d_H(v) = 2 tau(v) - 72 in {0, 2, 4}.
```

Thus H is an even spanning subgraph of maximum degree four. Moreover,

```text
N_5 = 360 + m/5
m = 0 mod 5.
```

For a two-edge path `u-v-w`, define

```text
alpha = number of 5-cycles containing u-v-w
beta = number of 6-cycles containing u-v-w
r = 6 alpha + beta.
```

Three-vertex Gram minors and the kernel refinement give:

| incident edge types | allowed r |
| --- | --- |
| low--low | 30, 31, 32 |
| mixed | 30, 31, 32 |
| high--high | 30, 31 |

The value `r = 29`, which determinant nonnegativity alone permits in two cases,
is impossible because equality would put `e_u - e_w` in the adjacency
-2-eigenspace, contradicting the u-coordinate.

Writing

```text
S_2 = sum_v d_H(v)^2,
```

the local table gives

```text
N_6 >= 1950 - m
N_6 <= 2200 - 5m/6 - S_2/12.
```

Independent shifted-moment and localising-matrix Schur complements give

```text
N_6 >= (43m^2 - 70200m + 119632500)/58500
N_6 <= (4220000 - 2200m - 7m^2)/2000.
```

Exact integer enumeration leaves 266 coarse degree profiles. Therefore the
present constraints are strong necessary conditions and useful canonical-search
filters, but they do not eliminate order 50.

**Status:** proved necessary conditions / exact; dedicated proof audit queued.

---

# Part VI. Moore-puncture theory

## 18. One deleted Moore vertex

Let M be a degree-k Moore graph and `H = M - v`. Then

```text
|V(H)| = k^2
delta*(H) = k - 1/k
lambda_D(H) = -2 - sqrt(k).
```

Hence

```text
Phi(H) = k - 1/k - 2 - sqrt(k),
```

which is positive exactly for integers `k >= 5`.

The full distance spectrum is obtained by an orthogonal decomposition into the
constant quotient, incidence modules, and the residual Moore kernel.

**Status:** proved / exact; priority unresolved; proof audit queued.

## 19. Deleting the endpoints of an edge

Let `uv in E(M)` and `H = M - {u,v}`. Then

```text
|V(H)| = k^2 - 1
delta*(H) = k - 2/k
lambda_D(H) = -2 - sqrt(k).
```

Therefore

```text
Phi(H) = k - 2/k - 2 - sqrt(k),
```

which is positive exactly for integers `k >= 5`.

**Status:** proved / exact; priority unresolved; proof audit queued.

## 20. Deleting two nonadjacent Moore vertices

Let u and v be nonadjacent vertices of a degree-k Moore graph, `k >= 5`, and put
`H = M - {u,v}`. Then

```text
delta*(H) = k - 2/k.
```

Write `Delta = sqrt(4k - 3)`. The exact distance characteristic polynomial is

```text
chi_D(x)
 = (x - k + 3) R_k(x)
   (x^2 + 4x - k + 3)^(k - 2)
   (x^2 + 4x - k + 5)^(k - 2)
   (x + (Delta + 3)/2)^M_minus
   (x - (Delta - 3)/2)^M_plus,
```

where

```text
R_k(x)
 = x^4 + (10 - 2k^2)x^3
   + (2k^3 - 17k^2 - 2k + 36)x^2
   + (12k^3 - 49k^2 - 4k + 53)x
   - 2k^4 + 17k^3 - 38k^2 + 5k + 20,

M_minus
 = [k(k - 2) + (k^2 - 4k + 2)Delta]/(2Delta),

M_plus
 = [-k(k - 2) + (k^2 - 4k + 2)Delta]/(2Delta).
```

The factorisation follows from a five-cell equitable partition and a complete
orthogonal decomposition into constant, matched symmetric, matched
antisymmetric, common-neighbour, and residual-kernel modules.

A deletion-stability estimate proves strictness for every realizable `k >= 6`,
even though the least root of the quartic quotient does not simplify uniformly.

**Status:** proved / exact; direct-sum audit artifact present; priority
unresolved; dedicated proof audit queued.

## 21. General deletion-stability inequality

Let `H = G - S` be connected, and define

```text
D_0 = D(G)[V(H)]
E_S = D(H) - D_0
a = delta*(G)
b = delta*(H)
gamma = Phi(G).
```

Cauchy interlacing and Weyl's inequality give

```text
Phi(H) >= gamma - (a - b) + lambda_min(E_S).
```

For Moore punctures, `E_S` is a structured distance-increase graph. This proves
that deleting any two vertices preserves strict violation for `k >= 6`, while
adjacent pairs already work for `k >= 5`.

**Status:** proved / exact specialised checks; standard matrix ingredients.

## 22. Small-puncture Moore normal form

Let M be a degree-k Moore graph, let `S` be a vertex set of size `s <= k - 1`,
and write `H = M - S`. Then H is connected, has diameter at most three, and

```text
delta*(H) = k - s/k.
```

Let B be the surviving-vertex by deleted-vertex incidence matrix. The exact
distance matrix is

```text
D(H) = 2(J - I) - A(H) + B B^T - diag(B B^T).
```

The connectivity proof constructs `k - 1` internally vertex-disjoint
length-three replacement paths whenever a deleted common neighbour destroys a
length-two path. The dual-degree lower bound follows from

```text
sum_{y in N_H(x)} |N_M(y) intersect S|
 <= s - |N_M(x) intersect S|,
```

and equality is attained using

```text
|intersection_{z in S} Gamma_2(z)|
 >= k^2 + 1 - s(k + 1)
 >= 2.
```

This theorem unifies all small Moore punctures at the metric and dual-degree
level; the detailed spectra still depend on the deletion geometry.

**Status:** proved / exact finite specialisation; proof audit and priority search
queued.

## 23. Hoffman--Singleton deletion robustness radius

For the Hoffman--Singleton graph M, every deletion of at most five vertices
remains a strict WOW-284 counterexample. The exact automorphism-orbit counts for
deleted sets of sizes 1, 2, 3, 4, and 5 are

```text
1, 2, 4, 11, 33.
```

For every orbit representative the verifier reconstructs the punctured graph,
checks the small-puncture distance formula and

```text
delta*(M - S) = (49 - |S|)/7,
```

and proves

```text
7 D(M - S) + (49 - |S|) I is positive definite.
```

Thus every labelled deletion set with `|S| <= 5` is strict.

Sharpness is witnessed by

```text
S = {P_(2,4), P_(3,1), P_(3,4), Q_(2,1), Q_(3,4), Q_(4,4)}.
```

For this 44-vertex graph,

```text
delta* = 43/7,
```

and an exact rational LDL decomposition of `7D + 43I` has exactly one negative
pivot and no zero pivot. Hence it is not a strict counterexample.

Therefore

```text
the universal Hoffman--Singleton vertex-deletion robustness radius is 5.
```

**Status:** exact finite classification inside the full labelled deletion
family; proof audit and automorphism-provenance review queued.

---

# Part VII. Construction obstructions and negative controls

## 24. Prime-field diameter-three obstruction

For an odd prime `q >= 7` and `1 <= m <= q`, define the balanced layer graph
`G(q,m)` on `2qm` vertices by

```text
P_(i,j) adjacent to P_(i,j+1) and P_(i,j-1)
Q_(k,l) adjacent to Q_(k,l+2) and Q_(k,l-2)
P_(i,j) adjacent to Q_(k,ik+j).
```

It is `(m + 2)`-regular and has girth at least five. Fourier decomposition under
translation in the second coordinate gives zero-mode eigenvalues

```text
m + 2
2 - m
2 with multiplicity 2m - 2.
```

The strict WOW window reduces possible m to 4, 5, and 6. A nonzero Fourier
block has an eigenvalue at least

```text
sqrt(m) + cos(pi/7) - 1/2,
```

which lies above the upper WOW boundary for `m = 4,5,6`. Therefore

```text
q >= 7 prime and diameter(G(q,m)) = 3
implies G(q,m) is not a strict counterexample.
```

This closes a natural attempt to turn the Hoffman--Singleton coordinates into
an unconditional diameter-three infinite family.

**Status:** proved / exact; construction literature-established; proof audit
queued.

## 25. Layer-respecting perfect-matching deletions

For a permutation pi in `S_5`, delete the perfect matching

```text
M_pi = {P_(i,j) Q_(pi(i), i pi(i) + j) : i,j in F_5}
```

from the Hoffman--Singleton graph. The resulting 120 graphs are 6-regular, have
girth five and diameter four. Explicit coordinate automorphisms split the
family into exactly two isomorphism orbits:

```text
20 affine permutations
100 nonaffine permutations.
```

For the affine orbit,

```text
lambda_D = -13
Phi = -7.
```

For the nonaffine orbit,

```text
lambda_D = -6 - sqrt(61)
Phi = -sqrt(61).
```

Thus all 120 members are exact negative controls. A natural order-50 regular
construction obtained by deleting one cross-layer perfect matching cannot
produce a counterexample.

**Status:** exact finite classification; proof audit and priority search queued.

---

# Part VIII. Derived low-degree windows

The new diameter bounds and the LP ceiling yield concise global restrictions.

## 26. Degree six

The audited edge-local theorem gives

```text
k = 6 implies n <= 50.
```

## 27. Degree seven

Diameter four and larger are impossible. The diameter-two case is a Moore graph
and has order 50. In diameter three,

```text
n < B_7 = 9*52/6 = 78.
```

A 7-regular graph has even order, hence

```text
k = 7:
order 50 in diameter two,
or order at most 76 in diameter three.
```

## 28. Degree eight

Diameter four and larger are impossible, and a degree-eight Moore graph is
excluded by the standard multiplicity integrality condition. The LP ceiling
gives `n <= 111`. If `n = 111`, the edge-local inequalities force every edge
to lie in exactly 14 five-cycles. Since

```text
|E| = 8*111/2 = 444,
```

edge--cycle incidence would give

```text
5 N_5 = 14*444 = 6216,
```

which is impossible. Therefore

```text
k = 8 implies n <= 110.
```

## 29. Degree nine

Diameter four and larger are impossible, and the diameter-two Moore
multiplicities are nonintegral. The LP ceiling gives

```text
n < B_9 = 11*84/6 = 154.
```

A 9-regular graph has even order, so

```text
k = 9 implies n <= 152.
```

These are corollaries of the current stack rather than independent principal
theorems.

---

# Part IX. Dependency graph and audit state

## 30. Logical dependencies

The principal dependency chain is

```text
girth-five local geometry
  -> diameter-three operator identity
  -> shifted spectral window.
```

From the shifted window, three programmes emerge.

### Order-bound branch

```text
trace moments
  -> n < B_k
  -> LP optimality ceiling.
```

At degree six,

```text
n <= 51
  -> edge-local cycle bounds
  -> n <= 50
  -> order-50 feasibility system.
```

### Puncture branch

```text
Moore common-neighbour identity
  -> structured distance-increase matrices
  -> one- and two-vertex spectra and deletion stability.
```

The small-puncture normal form then supplies the metric and dual-degree layer
for arbitrary `s <= k - 1`, and exact automorphism orbit exhaustion gives the
Hoffman--Singleton radius-five theorem.

### Diameter branch

```text
endpoint-neighbourhood Rayleigh vector
  -> diameter at most four for regular strict counterexamples
  -> diameter-four degree at least ten.
```

## 31. Current proof-audit state

The edge-local order-51 exclusion has passed a dedicated audit after one
substantive theorem-scope correction. The following remain queued for separate
audits:

1. all-degree nonbacktracking LP ceiling;
2. nonadjacent Moore-puncture direct sum and factorisation;
3. regular degree-at-least-six theorem;
4. one-vertex and adjacent-edge Moore spectra;
5. order-50 local feasibility system;
6. layer-matching deletion classification;
7. prime-field obstruction;
8. Jorgensen equality control;
9. endpoint-neighbourhood diameter theorem;
10. diameter-four theorem;
11. small-puncture Moore normal form;
12. Hoffman--Singleton robustness-radius classification.

A green exact verifier is necessary but not sufficient for manuscript
promotion.

---

# Part X. Recommended v2 selection

A coherent v2 should not simply paste every result into one manuscript. The
strongest theorem narrative is:

1. the counterexample and diameter-three spectral mechanism;
2. regular counterexamples have degree at least six;
3. every regular strict counterexample has diameter at most four, with the
   diameter-four regime beginning only at degree ten;
4. the sharp all-degree ceiling of the standard one-point LP method;
5. the audited degree-six bound `n <= 50`;
6. the Moore-puncture normal form and the Hoffman--Singleton robustness radius.

The following are better placed in appendices or a companion note:

- full quartic and high-degree characteristic-polynomial factorisations;
- all order-50 moment matrices and the 266 surviving coarse profiles;
- the 120 matching-deletion negative controls;
- full automorphism orbit tables and LDL pivot ledgers;
- Lean implementation details beyond the precise formal-scope statement.

A possible manuscript theorem hierarchy is:

- **Theorem A:** explicit counterexamples and Moore threshold;
- **Theorem B:** diameter-three shifted-spectrum criterion;
- **Theorem C:** regular counterexamples have degree at least six and diameter
  at most four;
- **Theorem D:** exact LP ceiling `n < B_k`;
- **Theorem E:** every degree-six regular strict counterexample has `n <= 50`;
- **Theorem F:** small Moore punctures and Hoffman--Singleton robustness radius
  five.

This selection would move the paper from an isolated disproof toward a
structural study of where failure can occur and how stable the principal
counterexample is.

---

# Part XI. Exact artifacts

| Result | Exact entry point |
| --- | --- |
| base exact spectra | `scripts/verify_exact.py` |
| general structural extensions | `scripts/verify_research_extensions_exact.py` |
| regular degree at least six | `scripts/verify_regular_low_degree.py` |
| nonadjacent puncture factorisation | `scripts/verify_nonadjacent_punctured_moore.py` |
| nonadjacent direct-sum audit | `scripts/verify_nonadjacent_direct_sum.py` |
| prime-field obstruction | `scripts/verify_prime_field_obstruction.py` |
| equality boundary | `scripts/verify_equality_boundary.py` |
| Jorgensen control | `scripts/verify_jorgensen96_provenance.py` |
| degree-six n at most 51 | `scripts/verify_degree_six_gate.py` |
| LP ceiling | `scripts/verify_two_sided_lp_ceiling.py` |
| edge-local n at most 50 | `scripts/verify_edge_local_order50.py` |
| matching deletions | `scripts/verify_layer_matching_deletions.py` |
| order-50 feasibility | `scripts/verify_order50_local_feasibility.py` |
| r = 29 exclusion | `scripts/verify_order50_r29_exclusion.py` |
| proof audit 01 | `scripts/verify_proof_audit_01_edge_local.py` |
| diameter and puncture robustness | `scripts/verify_diameter_puncture_extensions.py` |
| degree-seven to degree-nine windows | `scripts/verify_low_degree_windows.py` |

The exact workflow rejects floating-point spectral decisions on every asserted
proof path.

---

# Part XII. Deliberate nonclaims

The current stack does **not** prove any of the following.

- Order 38 is the minimum order of a counterexample.
- No degree-six order-50 counterexample exists.
- Every six-vertex deletion of Hoffman--Singleton fails.
- A regular diameter-four counterexample exists.
- Every regular diameter-four graph satisfies WOW-284.
- The punctured-Moore spectra, LP dual certificate, diameter bounds, or
  robustness theorem have established literature priority.
- An unconditional infinite family of strict counterexamples exists.
- Exact computation or Lean checking substitutes for independent mathematical
  review of theorem statements and proof architecture.

These boundaries should remain explicit in any v2 manuscript and public
announcement.
