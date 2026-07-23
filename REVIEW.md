# Mathematical and reproducibility review

**Object reviewed:** *Exact Counterexamples and Spectral Mechanisms for WOW-284*<br>
**Author:** Samuil Petkov<br>
**Manuscript version:** 19 July 2026<br>
**Review status:** Adversarial internal audit after conceptual revision; not external peer review

## Outcome

The revised counterexample proof and the degree-`k` Moore-graph theorem are
mathematically correct under the
definitions of dual degree and ordered distance eigenvalues used by Aouchiche
and Hansen. The coordinate graph is a simple connected 7-regular graph on 50
vertices with girth five. Its least distance eigenvalue is -4, so its minimum
dual degree 7 strictly violates the conjectured upper bound 4.

The 23 July extension also passes adversarial mathematical and computational
review. It adds exact counterexamples of orders 38, 39, 40, and 42; exact
finite statements for all 40 singleton and 120 edge-endpoint deletions of the
40-vertex graph; a regular diameter-three criterion; and a repaired
Moore-second-subconstituent mechanism. The 38-vertex least distance eigenvalue
is exactly `-3-sqrt(7)`. The three-vertex deletion screen remains explicitly
numerical and is not treated as a theorem or a minimality argument.

The revision materially improves the paper by replacing a graph-specific
calculation with a sharp structural statement: for every diameter-two Moore
graph of degree `k >= 2`, the least distance eigenvalue is
`-(3 + sqrt(4k - 3))/2`, and WOW-284 fails exactly when `k > 3`. The Petersen
equality is therefore the boundary case rather than an isolated coincidence.

No theorem-breaking gap was found. The three substantive editorial corrections
were attribution and proof-clarity corrections rather than changes to the
counterexample:

1. the manuscript now cites the precise published WOW-284 formulation; and
2. it credits Howlader and Panigrahi's 2022 prior publication of the same
   Hoffman-Singleton distance spectrum; and
3. it credits Hafner's published affine-coordinate presentation of the exact
   Robertson construction used in the manuscript.

It now also credits Howlader and Panigrahi for the general minimal-cage
distance-polynomial framework, rather than crediting only their degree-7
specialization.

## Adversarial journal assessment

The manuscript is now conceptually stronger and its novelty language is
appropriately narrow. A demanding referee should nevertheless distinguish
correctness from journal fit. The spectral ingredients were already available
in published work, and the new `k > 3` criterion is a short consequence once
they are placed beside WOW-284. This is a rigorous, useful research note and a
clear resolution of the stated conjecture; it is not represented here as a
broad spectral-graph-theory breakthrough. Suitability for a selective journal
will depend on that journal's appetite for concise counterexample notes.

The strongest remaining presentation risk is archival rather than
mathematical: a mutable repository URL should be replaced or supplemented by
a versioned release DOI before final journal submission. The explicit
50-vertex counterexample has a complete Lean spectral certificate; the
manuscript correctly excludes the 38/39/40/42 extension and generic criteria
from that formal-verification claim pending the expanded artifact.

The supplied expanded Lean source materially advances that artifact but does
not close it. For the 40-vertex graph it contains kernel-checkable finite
structure, semantic distance, inverse, diagonalization, and multiplicity
certificates; a final theorem connecting these to dual degree six, the least
distance eigenvalue `-5`, and WOW remains absent. For the 38-vertex graph, the
padded LDL identities and positive pivots are present, but the semantic
`3D+17I` identity, positive-definiteness transfer, and least-eigenvalue wrapper
are not completed. The earlier AXLE report cannot be reused for these new
modules.

## General Moore-graph audit

For a degree-`k`, diameter-two Moore graph, equality in the Moore bound gives
`n = 1 + k + k(k-1) = k^2 + 1`. From any root vertex, the `k(k-1)`
nonbacktracking walks of length two must terminate bijectively at the
`k(k-1)` nonneighbors. Hence adjacent pairs have no common neighbor and
nonadjacent pairs have exactly one. This excludes triangles and 4-cycles; an
edge together with one additional neighbor at each endpoint and the unique
common neighbor of those two vertices gives a 5-cycle.

The entrywise identity

\[
A^2=(k-1)I-A+J
\]

has the correct diagonal (`k-1+1=k`), edge (`-1+1=0`), and nonedge (`1`)
entries. On the orthogonal complement of the all-ones vector the adjacency
roots are `(-1 +/- sqrt(4k-3))/2`. Since `D=2J-2I-A`, the least distance
eigenvalue is `-(3 + sqrt(4k-3))/2`. Regularity gives `delta*(G)=k`.
Finally,

\[
(2k-3)^2-(4k-3)=4(k-1)(k-3),
\]

and `2k-3 > 0` for `k >= 2`; this proves the exact threshold. The cases
`k=2`, `k=3`, and `k=7` were checked separately against the 5-cycle,
Petersen, and Hoffman-Singleton spectra.

## Combinatorial audit

### Construction and edge multiplicity

- The two vertex families each have (5^2=25) vertices and are disjoint.
- The (P)-edges with step (+1) form five distinct 5-cycles, hence 25 edges.
- The (Q)-edges with step (+2) also form five distinct 5-cycles; in
  (mathbb F_5), step (+2) does not duplicate the reverse orientation, so
  there are 25 edges.
- A cross edge is uniquely determined by its (P_{i,j}) endpoint and the first
  coordinate (k) of its (Q)-endpoint. Hence there are (25\cdot5=125)
  distinct cross edges.
- All endpoints are distinct and the edge set consists of unordered pairs, so
  loops and parallel edges are absent.
- Each vertex has two same-type neighbors and five cross neighbors. The graph
  is 7-regular and the edge total (175) agrees with (50\cdot7/2).

### Common-neighbor certificate

Every case was checked separately.

- **Same (P)-layer:** the layer is (C_5). Adjacent pairs have no common
  (P)-neighbor; nonadjacent pairs have one. A common (Q)-neighbor would
  force the two intercepts to agree.
- **Different (P)-layers:** no (P)-neighbor can be common. The equation
  ((i-i')k=j'-j) has one solution because (i-i'\ne0) in a field.
- **Same (Q)-layer:** identical to the (P)-case after noting that the
  5-cycle is generated by steps (pm2).
- **Different (Q)-layers:** the equations for a common (P)-neighbor have
  the unique solution (i=(\ell-\ell')/(k-k')), (j=\ell-ik).
- **Cross pair:** with (r=\ell-(ik+j)), residue (0) means the pair is
  adjacent and has no common neighbor; residues (pm1) give exactly one
  common (P)-neighbor; residues (pm2) give exactly one common
  (Q)-neighbor. These five residues are exhaustive and disjoint.

Thus adjacent pairs have zero common neighbors and nonadjacent pairs have
exactly one.

### Connectivity and girth

- The certificate makes every distinct pair adjacent or joined by a two-edge
  path, so the graph is connected with diameter at most two.
- Since degree 7 is less than 49, the graph is not complete, so its diameter is
  exactly two.
- A triangle would give an adjacent pair a common neighbor.
- Opposite vertices of a 4-cycle would have two distinct common neighbors.
- Both configurations contradict the certificate.
- Each fixed (P)-layer is an explicit 5-cycle, so the girth is exactly five.

## Spectral audit

The entrywise common-neighbor counts give

\[
A^2=6I-A+J.
\]

The diagonal check is easy to miss: the right-hand diagonal is (6+1=7),
matching the degree. On the all-ones vector, (A) has eigenvalue 7. On its
orthogonal complement, (J=0), so

\[
A^2+A-6I=(A-2I)(A+3I)=0.
\]

The eigenvalue 7 is simple because
\(x^{\mathsf T}(7I-A)x=\sum_{\{u,v\}\in E}(x_u-x_v)^2\), and connectedness
forces equality only for constant \(x\). The remaining multiplicities satisfy

\[
m_2+m_{-3}=49,
\qquad 7+2m_2-3m_{-3}=\operatorname{tr}A=0,
\]

giving (m_2=28), (m_{-3}=21).

Diameter two gives (D=2J-2I-A). Hence the distance eigenvalue on the
all-ones vector is (100-2-7=91); on the orthogonal complement it is
(-2-\theta). Therefore adjacency eigenvalues 2 and -3 produce distance
eigenvalues -4 and 1 with multiplicities 28 and 21. The least distance
eigenvalue is -4.

The signs, ordering convention, trace equations, and multiplicity totals were
checked independently. The characteristic polynomial has degree 50 and
constant-term sign consistent with the eigenvalue product.

## Dual-degree and conjecture audit

In a 7-regular graph, every neighbor of every vertex has degree 7. Therefore

\[
d^*(v)=\frac{1}{7}\sum_{u\in N(v)}7=7
\]

for every vertex. Aouchiche-Hansen order the distance eigenvalues decreasingly,
so (partial_{50}=-4). WOW-284 would require (7\le4), which is false.
The strict violation is (7+(-4)=3).

## Computational independence and limits

The exact script reconstructs distances by BFS from the coordinate edge set;
it does not use (D=2J-2I-A). SymPy then checks the full characteristic
polynomial and an exact rational (LDL^{\mathsf T}) decomposition of (D+7I).
The regression tests separately check all 1,225 unordered vertex pairs.

The Python computation is independent of the paper's spectral shortcut, but
it is distinct from the Lean development and does not establish novelty or
minimality. Numerical matching is not used as proof; the symbolic and matrix
operations are exact.

## Remaining external obligations

- Independent expert review has not occurred.
- arXiv moderation and endorsement have not occurred.
- The targeted novelty search cannot rule out unpublished or non-indexed prior
  observations.
- No exhaustive search over all graphs below order 38 was attempted.
- The complete explicit 50-vertex certificate and scalar threshold pass strict
  Lean 4.31 checking; the other constructions and generic derivations remain
  analytic and exact-computational results.
