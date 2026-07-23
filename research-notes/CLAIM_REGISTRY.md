# Claim registry

| Claim | Evidence | Status |
| --- | --- | --- |
| The coordinate edge set is simple and has 50 vertices and 175 edges. | Direct set construction; exact exporter; tests. | Proved and checked. |
| Every vertex has degree 7. | Explicit neighborhood formulas; exhaustive degree check. | Proved and checked. |
| Adjacent pairs have 0 common neighbors and nonadjacent pairs have 1. | Complete modular case split; all 1,225 pairs checked. | Proved and checked. |
| The graph is connected with diameter 2. | Common-neighbor certificate; BFS. | Proved and checked. |
| The graph has girth 5. | No triangles/4-cycles from certificate; explicit P-layer 5-cycle; BFS girth. | Proved and checked. |
| `A^2 = 6I - A + J`. | Entrywise certificate; exact matrix equality. | Proved and checked. |
| Adjacency spectrum is `{7^1,2^28,(-3)^21}`. | Quadratic identity, trace, dimensions; symbolic charpoly. | Proved and checked. |
| Distance spectrum is `{91^1,1^21,(-4)^28}`. | Diameter-two matrix formula; symbolic BFS charpoly; prior publication. | Proved, checked, and attributed. |
| Minimum dual degree is 7. | Regularity and definition; exact fractions. | Proved and checked. |
| WOW-284 fails by strict gap 3. | `7 > 4`, with `partial_50=-4`. | Proved and checked. |
| The graph is a Hoffman-Singleton realization. | Exact agreement, after `k -> -k` on the `Q`-layers, with Hafner's Theorem 2.1; independently, parameters `(50,7,0,1)` and Hoffman-Singleton uniqueness. | Published construction cited; named-graph identification is not needed for the counterexample proof. |
| The Petersen deletion gives the 40-vertex `(6,5)`-cage with distance spectrum `{75^1,3^5,0^16,(-5)^18}`. | Analytic block proof; exact coordinate/BFS/characteristic-polynomial verifier; classical cage sources. | Proved, checked, and attributed. |
| Deleting one vertex from the 40-vertex graph gives a strict order-39 counterexample with `delta*=35/6`. | Exact rational dual degrees and positive-definite `6D+35I`; common exact characteristic polynomial for all 40 labels. | Proved by finite exact computation. |
| Deleting an edge's endpoints gives an order-38 counterexample with `delta*=17/3` and least distance eigenvalue `-3-sqrt(7)`. | Structural degree proof; exact characteristic polynomial and Sturm count; positive-definite `3D+17I`; independent graph6/integer-BFS/Fraction-LDL audit. | Proved and checked. |
| All 40 labelled singleton deletions and all 120 labelled edge-endpoint deletions are strict counterexamples. | Exhaustive exact characteristic-polynomial and dual-degree computation; one exact Sturm audit for each common polynomial. | Proved by finite exact computation; no isomorphism assumption. |
| The 42-vertex second subconstituent is a strict counterexample with distance spectrum `{81^1,4^6,0^14,(-5)^21}`. | Repaired analytic Moore-subconstituent proof; exact coordinate verifier; published adjacency spectrum. | Proved, checked, and attributed. |
| The regular diameter-three identity and spectral criterion hold. | Exact distance-matrix polynomial derivation from girth and diameter. | Proved analytically. |
| The 9,880 tested three-vertex deletions contain no positive numerical score. | Exhaustive floating-point screen of this fixed deletion class. | Exploratory only; not a theorem or order-37 elimination. |
| The Lean development covers the explicit 50-vertex certificate and scalar Moore threshold and finite spectral certificates for orders 38, 39, 40, and 42. | Lean/Mathlib 4.31 GitHub build, strict shortcut scan, and endpoint axiom reports. | The 50-vertex result is fully formalized; the non-50 results are kernel-checked finite spectral certificates. Generic criteria and descendant families remain conventional/exact-computational. |
| This is the smallest counterexample. | No exhaustive search over all smaller graphs was performed. | Not claimed. |
| This is the first observation of the counterexample. | Targeted search found no explicit prior connection, but cannot prove priority. | Not claimed. |
