# Provenance audit for the Jørgensen order-96 equality graph

**Status:** candidate closure of v2 Gate 1, pending independent review and green CI.

## Source boundary

The graph construction and public adjacency list are attributed to Leif K.
Jørgensen:

- public adjacency list:
  `https://people.math.aau.dk/~leif/research/girth5/96.html`;
- published construction:
  L. K. Jørgensen, *Girth 5 Graphs from Relative Difference Sets*,
  Discrete Mathematics 293 (2005), 177--184,
  DOI `10.1016/j.disc.2004.08.029`.

The distance characteristic polynomial, least distance eigenvalue, and
WOW-284 equality are project-side exact computations. They are not attributed
to the source paper unless explicitly stated there.

## Stored artifacts

The directory `data/jorgensen96/` contains:

- a text snapshot of the page-visible source content;
- a canonical normalized adjacency list;
- a fixed-label graph6 representation;
- `PROVENANCE.json`, recording the source URL, retrieval time, normalization,
  file lengths, and SHA-256 digests.

## Independent reconstruction

Run
```text
python scripts/verify_jorgensen96_provenance.py
python scripts/verify_jorgensen_96.py
```
The provenance verifier reconstructs the graph through three paths:

1. a permissive row parser applied to the source snapshot;
2. an independent strict parser applied to the normalized adjacency file;
3. NetworkX graph6 decoding.

All three normalized adjacency structures must agree exactly.

The verifier then checks:

- 96 vertices and 432 edges;
- no loops and symmetric 9-regular adjacency;
- connectedness, girth five, and diameter three;
- the exact identity
  \[
    D=3J+6I-2A-A^2;
  \]
- the full adjacency and distance characteristic polynomials;
- by exact Sturm counting and exact factor multiplicity, that
  \[
    \lambda_{\min}(D)=-9
  \]
  with multiplicity eight;
- \(\delta^*=9\), hence WOW score zero.

No floating-point ordering is used.
