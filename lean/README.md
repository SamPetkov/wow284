# Lean verification

This directory uses Lean 4.31 and Mathlib 4.31. It contains the completed
50-vertex certificate, the Moore scalar threshold, and explicit counterexample
certificates for orders 38, 39, 40, and 42.

A claim-by-claim description of the non-50 developments is in
[`NON50_CERTIFICATES.md`](NON50_CERTIFICATES.md).

## Completed 50-vertex development

The default `Wow284` library checks:

- the coordinate graph, symmetry, irreflexivity, and degree seven;
- the common-neighbour certificate, diameter two, and girth five;
- the adjacency-square and distance-matrix identities;
- an exact rational eigenbasis and two-sided inverse;
- the exact distance diagonalization `91^1, (-4)^28, 1^21`; and
- the scalar Moore threshold, with equality at degree three and failure above
  degree three.

The generated spectral proof clears denominators and checks bounded integer
matrix identities in separate shards.

## Orders 38 and 40

The separate Lake target `Wow284Extension` imports the committed order-38 and
order-40 sources.

For order 38, Lean proves the exact minimum dual degree `17/3` and positive
definiteness of `3D+17I`, which is already a complete strict counterexample
certificate. For order 40, Lean proves the complete exact distance
diagonalization, minimum eigenvalue `-5`, dual degree six, and gap one.

```text
cd lean
lake build Wow284Extension
lake env lean Wow284ExtensionAudit.lean
```

## Orders 39 and 42

These larger generated source sets are produced deterministically during CI:

```text
python scripts/generate_lean39_42.py
cd lean
lake env lean Wow284Generated3942.lean
lake env lean Wow284Generated3942Audit.lean
```

The order-39 endpoint proves minimum dual degree `35/6` and
`6D+35I` positive definite. The order-42 endpoint proves minimum dual degree
six and `D+6I` positive definite. In each case the positive-definiteness theorem
implies a strict positive WOW gap for every real distance eigenpair.

To rerun only the exact Python-side generation checks without writing Lean
files:

```text
python scripts/generate_lean39_42.py --verify-only
```

## Trust and source hygiene

The CI source audit rejects imported occurrences of:

```text
sorry
admit
native_decide
bv_decide
unsafe declarations
new axiom declarations
```

The axiom-report files print the transitive assumptions used by representative
public endpoints. The intended final reports should contain only standard
Mathlib foundations such as `propext`, `Classical.choice`, and `Quot.sound`.

Files ending in `.lean.template` remain outside all imported roots. They record
generic mechanisms that are not part of any completed explicit-counterexample
claim.
