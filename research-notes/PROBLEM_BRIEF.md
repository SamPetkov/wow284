# Confirmed research brief

Confirmed by the user on 21 July 2026, with the manuscript date fixed to
19 July 2026.

## Exact target

Determine whether the supplied coordinate graph over `F_5` is a valid
counterexample to WOW-284 and, if it is, prepare a public GitHub and arXiv-ready
proof package credited to Samuil Petkov at ENS.

## Definitions and conventions

- Graphs are finite, simple, undirected, and connected.
- Distance eigenvalues are ordered decreasingly, so `partial_n` is the least.
- `d*(v)` is the average degree of the neighbors of `v`, and `delta*` is its
  minimum over vertices.
- All coordinate arithmetic is modulo 5.
- The fixed manuscript date is 19 July 2026.
- The repository license is CC BY 4.0.

## Acceptance criteria

- Direct proof of simplicity, connectedness, girth, dual degree, and spectrum.
- Independent exact computation from BFS distances.
- Source and novelty audit with explicit prior-work attribution.
- Synchronized TeX, Markdown, PDF, arXiv ZIP, code, tests, data, citation,
  licensing, provenance, and checksums.
- Exact one-inch margins and style continuity with the author's Erdos 625 and
  Erdos 593 manuscripts, without modifying either reference repository.
- Public GitHub repository `SamPetkov/wow284`.

## Explicit non-goals

- No minimality claim.
- No exhaustive search below 50 vertices.
- No claim that the distance spectrum is new.
- No claim of absolute priority without additional evidence.
- No arXiv submission on the author's behalf; only a ready upload artifact.

## Validation routes

1. Direct common-neighbor and spectral derivation.
2. Exact BFS, characteristic-polynomial, and rational LDL certificate.
3. Adversarial checks of modular signs, edge multiplicities, eigenvalue
   ordering, trace equations, and bibliography.
4. PDF compilation, rendering, and visual inspection.
