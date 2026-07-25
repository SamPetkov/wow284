# Systematic proof-audit registry

This registry enforces a one-proof-at-a-time audit of the post-v1 WOW-284
research stack.  A proof is promoted only after its exact statement,
hypotheses, dependencies, critical lemmas, failure modes, and independent
verification route have all been checked.

## Audit statuses

- `queued`: not yet audited beyond ordinary PR review;
- `in_progress`: one dedicated audit PR is active;
- `pass_after_correction`: the argument is valid after a recorded correction;
- `pass`: no correction was required;
- `blocked`: a theorem-strength gap remains;
- `superseded`: replaced by a stronger audited argument.

## Queue

| Audit | Result | Primary risk | Status |
| --- | --- | --- | --- |
| 01 | Edge-local exclusion of degree-six order 51 | walk-count identities, theorem scope, PSD entry bounds, cycle-incidence congruence | `pass_after_correction` |
| 02 | All-degree ceiling of the two-sided nonbacktracking LP method | dual feasibility for every degree, Chebyshev tail, exact match to Nozaki hypotheses | `queued` |
| 03 | Nonadjacent Moore-puncture distance spectrum | invariant direct sum, injectivity, residual trace, multiplicities | `queued` |
| 04 | Every regular strict counterexample has degree at least six | diameter reductions, four `(5,5)`-cage exhaustion, interlacing direction | `queued` |
| 05 | One-vertex and adjacent-edge Moore-puncture spectra | quotient normalization, least-root comparison, multiplicity accounting | `queued` |
| 06 | Order-50 local feasibility system | walk/cycle interpretation, Gram minors, moment Schur complements | `queued` |
| 07 | Classification of 120 layer-respecting matching deletions | automorphism formulas, orbit exhaustion, exact least-root certificates | `queued` |
| 08 | Prime-field diameter-three obstruction | Fourier decomposition, parameter scope, exact radical comparison | `queued` |
| 09 | Jørgensen order-96 equality control | provenance, independent reconstruction, least-root certification | `queued` |

## Audit 01 outcome

The edge-local proof is sound after one substantive scope repair.  Its original
research-note theorem stated a conclusion for every degree-six regular strict
counterexample, while the displayed spectral-window proof assumed diameter
three.  The audit supplies the missing reduction:

1. a degree-six strict counterexample cannot have diameter at least four, by an
   explicit Rayleigh vector supported on two closed neighborhoods;
2. diameter two is impossible by the Moore identity and an integral
   characteristic-polynomial trace contradiction;
3. therefore every degree-six regular strict counterexample has diameter three.

With that dependency made explicit, the order-51 exclusion proves the global
statement it originally advertised.

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

No audit may silently strengthen a theorem.  If a missing reduction can be
proved, it must be stated as a separate lemma.  Otherwise the theorem statement
must be narrowed.