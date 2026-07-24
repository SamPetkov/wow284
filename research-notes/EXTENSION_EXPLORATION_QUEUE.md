# WOW-284 extension exploration queue

This registry separates proved results from active searches. A route is
promoted only when it produces an explicit theorem, exact graph certificate,
or independently reproducible negative result.

| Mechanism | Current status | Next exact artifact required | Promotion gate |
| --- | --- | --- | --- |
| One-vertex punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Convert the block proof into manuscript-quality LaTeX; extend Lean only if useful | Institutional literature check and clean CI |
| Adjacent-edge punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Same as above | Same as above |
| Nonadjacent-pair punctures | **Closed spectrally:** complete generic distance characteristic factorization proved; strictness for `k>=6` follows from deletion stability | Optional least-quotient-root analysis and Lean formalization | Exact symbolic factorization, `k=7` specialization, and literature audit remain green |
| General deletion stability | Proved by interlacing and Weyl | Classify distance-increase matrices for larger structured deleted sets | State only as a standard matrix lemma with specialized corollaries |
| Regular degree-at-most-five obstruction | **Closed:** every regular strict counterexample has degree at least six | Optional Lean formalization of the scalar and finite cage checks | Exact low-degree verifier and cage provenance remain green |
| Regular degree-six classification | Reduced to `40 <= n <= 51` for diameter three | Canonically generate connected 6-regular graphs with girth at least five in this order range; use adjacency-window pruning | Reproducible generator version, canonical options, checksums, and exact survivors |
| Irregular order 37 and below | Existing deletion/mutation screens are exploratory only | Canonical generation or a structural lower bound | No minimality language before exhaustive canonical elimination |
| Prime-field coordinate family | **Closed for diameter three:** no member with odd prime `q>=7` is a strict counterexample | Analyze diameter `>=4` members or different finite-field families | Do not infer a global infinite-family no-go from the diameter-three theorem |
| Higher-diameter transfer | Algebraic recurrence checked; framework is substantially known | Full theorem comparison with minimal-cage and distance-polynomial literature | No novelty claim without source-by-source comparison |
| Equality boundary | **Structural characterization proved:** equality is contact with `-1 +/- sqrt(2k-2)`; irrational contact has even nullity; exact order-96 control checked | Classify feasible contact spectra using association schemes or linear programming | Exact scalar and order-96 checks remain green; no classification claim yet |
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

1. Implement a canonical degree-six search restricted to orders 40 through 51.
2. Analyze higher-diameter members of the finite-field family without reusing
   the diameter-three criterion outside its hypotheses.
3. Compare the higher-diameter recurrence theorem line by line with
   Howlader--Panigrahi and distance-polynomial sources.
4. Search MathSciNet and zbMATH for the exact puncture factors before any
   novelty wording enters a manuscript.
5. Investigate whether the negative-type restriction restores WOW-284.
6. Develop linear-programming constraints for equality and the remaining
   degree-six window.
