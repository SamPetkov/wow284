# Lean verification

This directory uses Lean 4.31 and Mathlib 4.31. It contains the completed
50-vertex development, the Moore scalar threshold, and explicit finite spectral
certificates for orders 38, 39, 40, and 42.

A claim-by-claim description of the non-50 developments is in
[`NON50_CERTIFICATES.md`](NON50_CERTIFICATES.md).

## Exact all-degree LP optimum

The default `Wow284` library also imports the completed analytic
formalization of the all-degree two-sided nonbacktracking linear program.
For every natural number \(k\ge4\) and every admissible finitely supported
coefficient family, Lean proves

\[
  B_k c_0\le f(k),
  \qquad
  B_k=\frac{(k+2)(k^2+3)}6,
\]

Lean also constructs the normalized finitely supported optimizer explicitly,
proves its admissibility and objective value, and proves that equality holds
exactly when the complete coefficient family is the positive scalar \(c_0\)
times that optimizer. Thus the result is non-vacuous and rigid at both the
coefficient and represented-polynomial levels. The dependency closure
includes exact degree and linear independence of the nonbacktracking basis,
the primal quartic certificate, positivity and exact moments of the
three-point dual, strict slacks in degrees \(5\) through \(9\), the universal
Chebyshev tail for every degree at least \(10\), finite-support weak duality,
and equality rigidity.

This is a completed formalization of the analytic one-variable, all-degree
two-sided nonbacktracking LP optimum, attainment, and rigidity only. It does
not formalize the separate graph trace/spectral bridge, nor any graph-order,
deletion, puncture, or counterexample theorem derived from that bridge.

The warnings-fatal theorem and trust checks are:

```text
cd lean
lake build Wow284.LPCeiling --wfail
lake env lean -DwarningAsError=true Wow284LPAudit.lean
cd ..
python scripts/validate_lp_formalization.py check
```

The frozen polynomial-level endpoint is
`Wow284.LP.twoSidedLP_optimal_and_rigid`. The stronger non-vacuous endpoint,
including the explicit optimizer and literal coefficient-family uniqueness,
is
`Wow284.LP.twoSidedLP_exact_optimum_and_coefficient_rigidity`.
The release-static audit freezes the exact source of `LPDefinitions.lean`,
both endpoint signatures, every public trust probe, and the production-module
inventory. That source audit is necessary but not sufficient: warning-fatal
Lean/Mathlib 4.31 replay and inspection of the printed axiom sets remain the
kernel-level gates. The word “ceiling” here denotes the exact real-valued
optimum \(B_k\), not
`Nat.ceil`.

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

For order 38, Lean proves the exact minimum dual degree `17/3`, positive
definiteness of `3D+17I`, and the resulting strict inequality for every
nonzero real eigenpair of the formal matrix. For order 40, Lean proves a
two-sided invertible exact diagonalization, minimum diagonal entry `-5`, dual
degree six, and gap one.

```text
cd lean
lake build Wow284Extension
lake env lean Wow284ExtensionAudit.lean
```

## Orders 39 and 42

These larger generated source sets are checked in for direct small-file
replay and reproduced deterministically by the generator:

```text
python scripts/generate_lean39_42.py
cd lean
lake build Wow284Generated3942
lake env lean -DwarningAsError=true Wow284Generated3942.lean
lake env lean -DwarningAsError=true Wow284Generated3942Audit.lean
```

On a server where Lake's default whole-DAG parallelism is too memory-hungry,
run the warnings-fatal bounded builder from the repository root:

```text
bash scripts/build_lean3942_bounded.sh
```

The order-39 endpoint proves minimum dual degree `35/6` and
`6D+35I` positive definite. The order-42 endpoint proves minimum dual degree
six and `D+6I` positive definite. In each case the positive-definiteness theorem
implies a strict positive WOW gap for every nonzero real eigenpair of the
formal matrix.

To rerun only the exact Python-side generation checks without writing Lean
files:

```text
python scripts/generate_lean39_42.py --verify-only
```

## Standalone full development

The deterministic standalone generator flattens both the committed module
graph and the generated order-39/order-42 graph into one Lean source. The
result retains only Mathlib imports, so it does not depend on any local
`Wow284.*` module.

```text
python scripts/generate_lean_standalone.py
python scripts/generate_lean_standalone.py --check
cd lean
lake env lean -DwarningAsError=true Wow284Standalone.lean
```

The standalone file includes the trust reports from
`Wow284ExtensionAudit.lean`, `Wow284Generated3942Audit.lean`, and
`Wow284LPAudit.lean`. It is a packaging of the formal scope described above;
it does not enlarge that scope.

## Trust and source hygiene

Run the core trust report separately with:

```text
cd lean
lake env lean -DwarningAsError=true Wow284CoreAudit.lean
```

The CI source audit rejects imported occurrences of:

```text
sorry
admit
native_decide
bv_decide
unsafe declarations
new axiom declarations
implemented_by
```

The axiom-report files print the transitive assumptions used by representative
public endpoints. The intended final reports should contain only standard
Mathlib foundations such as `propext`, `Classical.choice`, and `Quot.sound`.

For the non-50 constructions, separate finite structural lemmas are present,
but the public spectral endpoints do not bundle all graph hypotheses or
identify the semantic `0/1/2/3` matrix with Mathlib's `SimpleGraph.dist` in one
theorem. See `NON50_CERTIFICATES.md` for the exact claim boundary.

Files ending in `.lean.template` remain outside all imported roots. They record
generic mechanisms that are not part of any completed explicit-counterexample
claim.
