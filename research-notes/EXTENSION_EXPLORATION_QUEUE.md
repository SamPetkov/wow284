# WOW-284 extension exploration queue

This registry separates proved results from active searches. A route is
promoted only when it produces an explicit theorem, exact graph certificate,
or independently reproducible negative result.

| Mechanism | Current status | Next exact artifact required | Promotion gate |
| --- | --- | --- | --- |
| General diameter obstruction | **Closed analytically:** every regular strict counterexample has diameter at most four; diameter four requires degree at least ten | Dedicated independent proof audit and literature comparison for the endpoint-neighborhood Rayleigh bounds | Symbolic identity verifier, hypothesis audit, and priority review remain green |
| Small Moore punctures | **Closed analytically for `|S| <= k-1`:** connectedness, diameter at most three, exact dual degree `k-s/k`, and the distance-correction normal form | Independent audit of the internally disjoint path argument and equality case | Exact Hoffman--Singleton specializations and literature review remain green |
| Hoffman--Singleton puncture robustness | **Closed exactly:** every deletion of at most five vertices is a strict counterexample; an explicit six-vertex deletion fails, so the universal radius is five | Optional classification of all six-vertex deletion orbits and exact boundary cases | Verified automorphism-orbit exhaustion, rational dual degrees, and exact LDL certificates remain green |
| One-vertex punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Convert the block proof into manuscript-quality LaTeX; extend Lean only if useful | Institutional literature check and clean CI |
| Adjacent-edge punctured Moore graphs | Proved analytically; symbolic and `k=7` checks pass | Same as above | Same as above |
| Nonadjacent-pair punctures | **Closed spectrally:** complete generic distance characteristic factorization proved; strictness for `k>=6` follows from deletion stability | Optional least-quotient-root analysis and Lean formalization | Exact symbolic factorization, `k=7` specialization, and literature audit remain green |
| General deletion stability | Proved by interlacing and Weyl | Classify distance-increase matrices for larger structured deleted sets | State only as a standard matrix lemma with specialized corollaries |
| Regular degree-at-most-five obstruction | **Closed:** every regular strict counterexample has degree at least six | Optional Lean formalization of the scalar and finite cage checks | Exact low-degree verifier and cage provenance remain green |
| Regular degree-six classification | Reduced globally to `40 <= n <= 50` | Canonically generate connected 6-regular graphs with girth at least five in this order range; use adjacency-window and local-feasibility pruning | Reproducible generator version, canonical options, checksums, and exact survivors |
| Regular diameter-four regime | Open only for degree at least ten | Seek a stronger local Rayleigh/SDP bound or an explicit exact counterexample; screen distance-regular and edge-girth-regular families | No existence or restoration claim without an exact theorem or graph certificate |
| Irregular order 37 and below | Existing deletion/mutation screens are exploratory only | Canonical generation or a structural lower bound | No minimality language before exhaustive canonical elimination |
| Prime-field coordinate family | **Closed for diameter three:** no member with odd prime `q>=7` is a strict counterexample; regular diameter at least five is now impossible in general | Analyze any diameter-four members or different finite-field families | Do not infer a global infinite-family no-go from the diameter-three theorem |
| Higher-diameter transfer | Regular diameter at least five is excluded; the algebraic recurrence remains relevant to nonregular graphs and diameter four | Full theorem comparison with minimal-cage and distance-polynomial literature | No novelty claim without source-by-source comparison |
| Equality boundary | **Structural characterization proved:** equality is contact with `-1 +/- sqrt(2k-2)`; irrational contact has even nullity; exact order-96 control checked | Classify feasible contact spectra using association schemes or linear programming | Exact scalar and order-96 checks remain green; no classification claim yet |
| Negative-type graph metrics | Open | Search for a local Rayleigh or semidefinite certificate linking negative type to dual degree | A proof or explicit counterexample; no heuristic claim |
| Unconditional infinite family | Open | Seek unbounded-degree algebraic constructions in the diameter-two, diameter-three, or diameter-four regimes | One explicit verified family, not a conditional parameter theorem |
| Literature priority | Open for punctured spectra and the new diameter bounds | MathSciNet/zbMATH institutional search, citation-chain review, dissertation search | “New” only after positive priority evidence, never from search silence |

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

1. Audit the endpoint-neighborhood diameter theorem independently, including
   every sign reversal caused by negative cross terms.
2. Audit the small-puncture Moore theorem independently, especially internal
   vertex-disjointness and attainment of the dual-degree lower bound.
3. Investigate the regular diameter-four regime for degree at least ten.
4. Classify the six-vertex Hoffman--Singleton deletion orbits and locate all
   strict, equality, and failing types.
5. Implement the canonical degree-six search restricted to orders 40 through
   50 using the existing local-feasibility constraints.
6. Search MathSciNet and zbMATH for the exact puncture normal form, robustness
   radius, and diameter inequalities before any novelty wording enters a
   manuscript.
