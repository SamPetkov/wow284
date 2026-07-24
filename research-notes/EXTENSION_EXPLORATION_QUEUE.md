# WOW-284 extension exploration queue

This registry separates proved results from active searches. A route is
promoted only when it produces an explicit theorem, exact graph certificate,
or independently reproducible negative result.

| Mechanism | Current status | Next exact artifact required | Promotion gate |
| --- | --- | --- | --- |
| One-vertex punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Convert the block proof into manuscript-quality LaTeX; extend Lean only if useful | Institutional literature check and clean CI |
| Adjacent-edge punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Same as above | Same as above |
| Nonadjacent-pair punctures | Strictness proved for `k>=6` by deletion stability; exact `k=7` polynomial checked | Derive the complete generic distance spectrum or prove that the natural module decomposition is not spectrally closed | Exact invariant-subspace accounting and literature audit |
| General deletion stability | Proved by interlacing and Weyl | Classify distance-increase matrices for larger structured deleted sets | State only as a standard matrix lemma with specialized corollaries |
| Regular degree-at-most-five obstruction | **Closed:** every regular strict counterexample has degree at least six | Optional Lean formalization of the scalar and finite cage checks | Exact low-degree verifier and cage provenance remain green |
| Regular degree-six classification | Reduced to `40 <= n <= 51` for diameter three | Canonically generate connected 6-regular graphs with girth at least five in this order range; use adjacency-window pruning | Reproducible generator version, canonical options, checksums, and exact survivors |
| Irregular order 37 and below | Existing deletion/mutation screens are exploratory only | Canonical generation or a structural lower bound | No minimality language before exhaustive canonical elimination |
| Prime-field coordinate family | Known construction; diameter-three spectral obstruction partly derived | Exact Fourier-block theorem with all parameter ranges and a separate analysis of diameter `>=4` | Do not infer an infinite-family no-go from the diameter-three case |
| Higher-diameter transfer | Algebraic recurrence checked; framework is substantially known | Full theorem comparison with minimal-cage and distance-polynomial literature | No novelty claim without source-by-source comparison |
| Equality boundary | Exact order-96 equality example checked | Characterize spectra touching `-1 +/- sqrt(2k-2)` using association-scheme or linear-programming methods | At least one new exact classification or obstruction |
| Negative-type graph metrics | Open | Search for a local Rayleigh or semidefinite certificate linking negative type to dual degree | A proof or explicit counterexample; no heuristic claim |
| Unconditional infinite family | Open | Seek unbounded-degree algebraic constructions satisfying the shifted adjacency window | One explicit verified family, not a conditional parameter theorem |
| Literature priority | Open for punctured spectra | MathSciNet/zbMATH institutional search, citation-chain review, dissertation search | “New” only after positive priority evidence, never from search silence |

## Search discipline

For every computational route:

1. construct graphs canonically or record the exact fixed labeling;
2. reject loops, repeated edges, disconnected graphs, triangles, and 4-cycles;
3. compute dual degree from its definition using rational arithmetic;
4. use floating point only to rank candidates;
5. reconstruct every survivor exactly;
6. certify strictness by an exact characteristic polynomial, Sturm sequence,
   or positive-definite shifted distance matrix;
7. retain near-boundary graphs and equality cases;
8. record software versions, command lines, checksums, and negative results.

## Immediate next batch

1. Derive the generic nonadjacent-pair puncture spectrum.
2. Implement a canonical degree-six search restricted to orders 40 through 51.
3. Prove or refute the diameter-three Fourier obstruction for the full
   finite-field parameter range and keep higher-diameter cases separate.
4. Compare the higher-diameter recurrence theorem line by line with
   Howlader--Panigrahi and distance-polynomial sources.
5. Search MathSciNet and zbMATH for the exact puncture factors before any
   novelty wording enters a manuscript.
6. Investigate whether the negative-type restriction restores WOW-284.
