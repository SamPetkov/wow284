# Lean verification

This directory contains the Lean 4.31/Mathlib 4.31 verification of the
explicit 50-vertex WOW-284 counterexample and the scalar Moore-degree
threshold.

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
