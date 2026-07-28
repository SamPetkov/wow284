# Systematic proof-audit registry

This registry enforces a one-proof-at-a-time audit of the post-v1 WOW-284
research stack. A proof is promoted only after its exact statement,
hypotheses, dependencies, critical lemmas, failure modes, and independent
verification route have all been checked.

## Audit statuses

- `queued`: not yet audited beyond ordinary PR review;
- `in_progress`: one dedicated audit PR is active;
- `pass_after_correction`: the argument is valid after a recorded correction;
- `pass`: no theorem-strength correction was required;
- `blocked`: a theorem-strength gap remains;
- `superseded`: replaced by a stronger audited argument.

## Queue

| Audit | Result | Primary risk | Status |
| --- | --- | --- | --- |
| 01 | Edge-local exclusion of degree-six order 51 | walk-count identities, theorem scope, PSD entry bounds, cycle-incidence congruence | `pass_after_correction` |
| 02 | All-degree ceiling of the two-sided nonbacktracking LP method | dual feasibility for every degree, Chebyshev tail, exact match to the admissible coefficient cone | `pass` |
| 03 | Nonadjacent Moore-puncture distance spectrum | recomputed distances, invariant direct sum, injectivity, residual trace, multiplicities | `pass` |
| 04 | Every regular strict counterexample has degree at least six | diameter reductions, four `(5,5)`-cage exhaustion, interlacing direction | `pass` |
| 05 | One-vertex and adjacent-edge Moore-puncture spectra | quotient normalization, least-root comparison, multiplicity accounting | `pass_after_correction` |
| 06 | Order-50 local feasibility system | walk/cycle interpretation, Gram minors, moment Schur complements | `pass_after_correction` |
| 07 | Classification of 120 layer-respecting matching deletions | automorphism formulas, orbit exhaustion, exact least-root certificates | `pass_after_correction` |
| 08 | Prime-field diameter-three obstruction | Fourier decomposition, parameter scope, exact radical comparison | `pass_after_correction` |
| 09 | Jørgensen order-96 equality control | provenance, independent reconstruction, least-root certification | `pass_after_correction` |
| 10 | General endpoint-neighborhood diameter obstruction | support disjointness, cross-distance inequality direction, radical comparison, integer rounding | `pass_after_correction` |
| 11 | Diameter-four degree-at-most-nine exclusion | cross-pair count, 4-cycle exclusion, quotient normalization, threshold strictness | `queued` |
| 12 | Small-puncture Moore normal form | internally disjoint length-three paths, correction-matrix identity, exact dual-degree attainment | `queued` |
| 13 | Hoffman--Singleton deletion robustness radius five | generator provenance, orbit exhaustion, exact LDL signs, explicit six-deletion sharpness | `queued` |
| 14 | Integral optimal-slack and two Gram hierarchies | PSD kernel, irreducibility, integer rounding, least-eigenvalue classification, line-root arithmetic | `pass_after_correction` |

## Audit 01 outcome

The edge-local proof is sound after one substantive scope repair. Its original
research-note theorem stated a conclusion for every degree-six regular strict
counterexample, while the displayed spectral-window proof assumed diameter
three. The audit supplies the missing reduction:

1. a degree-six strict counterexample cannot have diameter at least four, by an
   explicit Rayleigh vector supported on two closed neighborhoods;
2. diameter two is impossible by the Moore identity and an integral
   characteristic-polynomial trace contradiction;
3. therefore every degree-six regular strict counterexample has diameter three.

With that dependency made explicit, the order-51 exclusion proves the global
statement it originally advertised.

## Audit 02 outcome

The all-degree LP-ceiling proof passes without a theorem-strength repair. The
audit makes the admissible cone explicit: coefficients of `F_1,...,F_4` are
unrestricted because their traces vanish at girth five, while coefficients from
degree five onward are nonnegative.

The audit independently verifies:

1. the primal quartic expansion;
2. positivity of the three-point dual measure;
3. exact moment matching through degree four;
4. strict slacks for degrees five through nine;
5. support inclusion and the uniform Chebyshev tail for every degree at least
   ten;
6. all signs in the weak-duality argument.

It also proves a stronger rigidity statement: equality in the polynomial
optimization occurs only for positive scalar multiples of the displayed
quartic optimizer. This follows because strict dual slacks kill all
coefficients of degree at least five, while equality on the positive dual
support forces the two endpoint roots and a double root at the interior point
`-2`.

The wording is narrowed to the exact method being optimized: the one-variable,
girth-five nonbacktracking LP cone. No statement is made about multipoint or
semidefinite hierarchies.

## Audit 03 outcome

The nonadjacent Moore-puncture factorisation is correct. The five-cell quotient,
incidence identities, invariant modules, residual quadratic relation, trace
calculation, multiplicities, and dual-degree minimum all pass independent exact
checks.

One logically necessary step was compressed in the original exposition. It
asserted

\[
D(H)=2(J-I)-A(H)+F
\]

without explicitly proving that pairs whose unique two-step path used a deleted
vertex still have distance exactly three. The audit supplies explicit surviving
length-three paths for:

1. a pair `w,a` inside one deleted neighbourhood;
2. two distinct vertices `a,a'` inside that neighbourhood;
3. the symmetric cases around the second deleted vertex.

This is an expository correction rather than a change to the theorem. The
metric lemma is now included in the primary note. With it, the direct sum has
dimensions

\[
5+2(k-2)+2(k-2)+2(k-3)+(k-2)(k-4)=k^2-1,
\]

so every distance eigenspace and algebraic multiplicity is accounted for.

## Audit 04 outcome

The theorem that every regular strict counterexample has degree at least six
passes without a theorem-strength correction. The audit verifies every degree
and diameter branch separately:

1. the Rayleigh vector `e_u-e_v` gives
   `lambda_min(D) <= -diam(G)`;
2. degrees zero, one, and two are excluded immediately;
3. degree three reaches the Moore boundary and gives equality;
4. degree-four and degree-five diameter-two cases fail the Moore multiplicity
   integrality test;
5. a degree-five diameter-four graph is excluded by the principal `D(P_5)`
   submatrix and Cauchy interlacing;
6. all remaining degree-five cages have an exact distance eigenvalue at most
   `-5`.

Using the already audited LP ceiling shortens the proof materially. At degree
four, diameter three forces `n=18`, leaving only the odd-dimensional
irreducible-quadratic contradiction. At degree five, diameter three leaves only
`n=30,31,32`; parity excludes `n=31`, so only excess four and six are needed.
The excess-five calculation is retained as a robustness check. The rank-one
positive-semidefinite derivative of the normalized layer compression supplies
the monotonicity used in the last two cases.

## Audit 05 outcome

The one-vertex and adjacent-edge Moore-puncture spectrum formulas are correct.
The one-vertex proof had compressed the metric replacement-path and
orthogonality arguments; the adjacent-edge result was only a proof outline.
The audit expands both into complete invariant-space proofs.

For one deleted vertex, the full decomposition has dimensions

\[
2+2(k-1)+k(k-2)=k^2.
\]

For the endpoints of an edge, the decomposition has dimensions

\[
3+2(2k-4)+(k-2)^2=k^2-1.
\]

The audit checks the normalized quotients, incidence-module matrices, residual
quadratic relation, trace-to-multiplicity equations, exact least-root
comparisons, dual-degree minima, and score thresholds. It also supplies
explicit surviving length-three paths for every pair whose unique length-two
route used a deleted vertex. No spectrum or threshold changes.

## Audit 06 outcome

The order-50 feasibility system passes. The vertex-cycle range, high-edge
subgraph constraints, refined two-path table, four bounds on the number of
6-cycles, and the 266-profile enumeration all survive independent exact checks.

Two expository corrections are required. First, the displayed layer matrix is
an average row quotient, not necessarily an equitable quotient. It is similar
to the symmetric normalized compression through the layer-size matrix, and
that symmetric compression is the object to which interlacing applies. Second,
the final theorem must combine the original determinant table with the later
kernel argument excluding `r=29`.

The audit proves the walk-to-cycle identities

\[
(A^3)_{uw}=\alpha_{uvw},
\qquad
(A^4)_{uw}=16+\beta_{uvw},
\]

checks the centered three-vertex Gram minors, reconstructs the shifted moments
through degree six from nonbacktracking trace identities, and verifies both
Schur complements. The result remains a necessary-condition and search-pruning
theorem; it does not prove nonexistence at order 50.

## Audit 07 outcome

The 120 layer-respecting matching deletions form exactly two isomorphism
classes. The 20 affine permutations have score `-7`, and the 100 nonaffine
permutations have score `-sqrt(61)`.

The original result is correct, but three logical transitions were compressed:

1. the perfect-matching assertion did not show explicitly why each `Q` vertex
   occurs once;
2. the cross-edge algebra for the type-preserving and type-swapping coordinate
   maps was omitted;
3. two coordinate orbits were not explicitly separated as graph-isomorphism
   classes until the different adjacency characteristic polynomials were used.

The audit checks all 400 coordinate maps on all 175 Hoffman--Singleton edges and
all 120 matchings, giving 48,000 exact matching-image checks. It then verifies
all 120 graph hypotheses, the 20/100 orbit exhaustion, both adjacency and
distance characteristic-polynomial pairs, and both exact Sturm least-root
certificates. The classification remains limited to the displayed
`M_pi` family and does not cover all perfect matchings.

## Audit 08 outcome

The balanced prime-field diameter-three obstruction is correct. The zero
character reduces the possible layer count to `m in {4,5,6}`. A nonzero
character block then contains a nonprincipal adjacency eigenvalue above the
upper WOW boundary.

Three proof transitions were expanded:

1. the full common-neighbor case split now separately excludes triangles and
   4-cycles;
2. a singular-vector pair for the cross matrix gives an explicit invariant
   two-dimensional Hermitian block;
3. the exact `q=7` controls now certify a nonprincipal root beyond the upper
   boundary, rather than merely recomputing characteristic polynomials.

The independent verifier checks the graph hypotheses for all seven `q=7`
members, the complete characteristic polynomials for `m=4,5,6`, and exact
Sturm counts beyond rational separators. The theorem remains conditional on
diameter three and does not address higher-diameter or different finite-field
families.

## Audit 09 outcome

The Jørgensen order-96 equality calculation is correct:

\[
\delta^*=9,
\qquad
\lambda_{\min}(D)=-9
\]

with multiplicity eight, so the score is zero.

The audit makes three evidentiary distinctions explicit. First, the source-page
snapshot, normalized adjacency list, and graph6 file are independently parsed
representations of one public adjacency list, not three independent historical
sources. Second, the recorded SHA-256 values certify local-file integrity but do
not authenticate the remote page. Third, the least-root proof is recast as an
exact adjacency-interval certificate, avoiding ambiguity about endpoint
conventions in a root-counting API.

A handwritten graph6 decoder agrees with the two row parsers. Exact Sturm
sequences place every root of the quartic adjacency factor in `(-5,3)`, while
the remaining nonprincipal factors lie in `[-5,3]` with boundary roots `3` and
`-5`. Thus `D+9I` is positive semidefinite and has an eight-dimensional kernel.
A separate distance-polynomial Sturm certificate confirms that no root lies
below `-9` after the boundary factor is removed. The graph construction and
public adjacency data remain attributed to Jørgensen; no uniqueness or novelty
claim is made.

## Audit 10 outcome

The endpoint-neighborhood diameter obstruction is sound after a strengthening
and one previously implicit sign check. The spectral inequality does not use
girth at least five: it holds for every connected finite simple graph whose
chosen endpoints are at distance at least five. The audit supplies an explicit
positive eigenvector for the least eigenvalue of the compressed two-by-two
matrix, records the radical comparison without an unproved sign choice, and
writes out the strict integer-rounding step in the diameter consequence.

The independent verifier checks the characteristic polynomial, eigenvector,
radical identity, rounding implication, regular specialization, Moore bound,
and exact finite-graph controls. The result is an obstruction rather than a
classification; in particular, it does not settle the remaining
diameter-four regular case.

## Audit 14 outcome

The optimal-slack hierarchy is sound after correcting two generic
off-diagonal formulas inherited from a degree-six specialization. For
distance-two pairs the constant term is \(k+13\), and for distance-three
pairs the parameter is
\[
 6(A^3)_{uz}+(A^4)_{uz};
\]
no uniqueness of a length-three geodesic is assumed.

The audit verifies the positive-semidefinite slack, its exact trace defect,
the strict kernel description, and the nonnegative integral excess matrix.
The one-level collapse is impossible because \(g_k(x)+1\) is irreducible over
\(\mathbb Q\); rational canonical form would otherwise force
\(n-1=2k/3\), contradicting \(n\ge k+1\). This yields the strengthened
universal order bound.

At the simple-excess level, the complementary relation graph has least
eigenvalue at least \(-2\). The degree-seven and degree-eight exclusions use
the external Cameron--Goethals--Seidel--Shult classification; the subsequent
regular and semiregular line-root divisibility arguments are exact. The
original draft's book theorem number was corrected to the original 1976
source and a later journal statement. A hidden control byte and a
self-mutating workflow step were also removed before promotion.

## Required structure of every audit

Each audit PR must contain:

1. the exact theorem statement and a claim-boundary note;
2. a hypothesis ledger showing where every assumption is used;
3. a dependency graph for imported results;
4. separate proofs of each critical lemma;
5. adversarial checks for sign, strictness, multiplicity, and endpoint errors;
6. an independent exact verifier that does not merely call the original
   verifier;
7. a list of discovered corrections, including wording-only corrections;
8. a CI entry and inclusion in the no-floating proof-path audit.

No audit may silently strengthen a theorem. If a missing reduction can be
proved, it must be stated as a separate lemma. Otherwise the theorem statement
must be narrowed.
