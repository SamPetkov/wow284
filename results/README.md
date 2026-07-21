# Exact result files

The files in this directory are deterministic outputs of the public Python
code.

- `verification.json` records the exhaustive structural checks, exact matrix
  identities, characteristic polynomials, rational LDL certificate, software
  versions, and source hashes.
- `edges.csv` contains all 175 unordered edges with numerical and coordinate
  labels.
- `adjacency_matrix.csv` is the complete 50-by-50 integer adjacency matrix.
- `distance_matrix.csv` is the complete 50-by-50 integer distance matrix built
  by breadth-first search.

Regenerate them with:

```bash
python scripts/verify_exact.py --output results/verification.json
python scripts/export_graph_data.py --output-dir results
```

The symbolic computation is exact. It is an independent verification route,
not a replacement for the proof or for external peer review.
