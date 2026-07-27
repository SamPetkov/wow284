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
| 03 | Nonadjacent Moore-puncture distance spectrum | recomputed distances, invariant direct sum, injectivity, residual trace, multiplicities | `pass_after_correction` |
| 04 | Every regular strict counterexample has degree at least six | diameter reductions, four `(5,5)`-cage exhaustion, interlacing direction | `queued` |
| 05 | One-vertex and adjacent-edge Moore-puncture spectra | quotient normalization, least-root comparison, multiplicity accounting | `queued` |
| 06 | Order-50 local feasibility system | walk/cycle interpretation, Gram minors, moment Schur complements | `queued` |
| 07 | Classification of 120 layer-respecting matching deletions | automorphism formulas, orbit exhaustion, exact least-root certificates | `queued` |
| 08 | Prime-field diameter-three obstruction | Fourier decomposition, parameter scope, exact radical comparison | `queued` |
| 09 | Jørgensen order-96 equality control | provenance, independent reconstruction, least-root certification | `queued` |
| 10 | General endpoint-neighborhood diameter obstruction | support disjointness, cross-distance inequality direction, radical comparison, integer rounding | `queued` |
| 11 | Diameter-four degree-at-most-nine exclusion | cross-pair count, 4-cycle exclusion, quotient normalization, threshold strictness | `queued` |
| 12 | Small-puncture Moore normal form | internally disjoint length-three paths, correction-matrix identity, exact dual-degree attainment | `queued` |
| 13 | Hoffman--Singleton deletion robustness radius five | generator provenance, orbit exhaustion, exact LDL signs, explicit six-deletion sharpness | `queued` |

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

This is an expository correction rather than a change to the theorem. Once the
metric lemma is inserted, the direct sum has dimensions

\[
5+2(k-2)+2(k-2)+2(k-3)+(k-2)(k-4)=k^2-1,
\]

so every distance eigenspace and algebraic multiplicity is accounted for.

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
