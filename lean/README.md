# Lean verification

This directory contains the Lean 4.31/Mathlib 4.31 verification of the
explicit 50-vertex WOW-284 counterexample and the scalar Moore-degree
threshold, together with a separately built staging target for induced
examples.

The public development checks:

- the 50-vertex coordinate graph, symmetry, irreflexivity, and degree seven;
- the exhaustive common-neighbor certificate, diameter two, girth five, and
  the adjacency-square and distance-matrix identities;
- an exact rational eigenbasis and two-sided inverse;
- the exact diagonalization with eigenvalues `91`, `-4`, and `1`, with
  multiplicities `1`, `28`, and `21`; and
- the scalar WOW inequality precisely for natural degrees `k <= 3` when
  `k >= 2`, with equality at `k = 3` and failure for `k > 3`.

The spectral proof is generated deterministically by
`../scripts/generate_lean_diagonalization.py`. It clears denominators, checks
bounded integer matrix identities in 20 shards, and assembles them into the
public rational theorems. Run:

```text
python scripts/generate_lean_diagonalization.py --check
cd lean
lake build
```

Release scans reject `sorry`, `admit`, `native_decide`, `bv_decide`, unsafe
declarations, and new axioms. Strict AXLE audits of every computational shard
and public wrapper pass under `lean-4.31.0`. Representative axiom reports list
only `propext`, `Classical.choice`, and `Quot.sound`.

The paper's generic Moore-graph-to-spectrum derivation is not encoded in full;
the completed formal-verification claim is limited to the explicit
counterexample and the scalar threshold.

## Staged induced-graph extension

`Wow284Extended.lean` is exposed through the separate Lake target
`Wow284Extension`. It imports generated finite certificates for the induced
40-vertex graph and exact finite/LDL data for the 38-vertex graph. Run:

```text
python scripts/generate_lean40_structural.py --check
python scripts/generate_lean40_diagonalization.py --check
python scripts/generate_lean38_certificates.py --check
python scripts/generate_lean38_ldl.py --check
cd lean
lake build Wow284Extension
```

The 40-vertex source currently lacks the final public theorem combining dual
degree six, least distance eigenvalue `-5`, and the strict WOW inequality. The
38-vertex source additionally lacks the `Matrix.PosDef` congruence and
principal-submatrix bridge from its padded LDL data to the spectral claim.
Files ending in `.lean.template` are deliberately excluded and contain the
remaining proof sketches. The punctured-Moore skeleton is also excluded from
the staging root because its interface is only a semantic placeholder.

The previous AXLE strict report covers the completed 50-vertex/scalar target,
not this extension. A fresh AXLE audit and representative `#print axioms`
reports are release gates for any expanded formal-verification claim.
