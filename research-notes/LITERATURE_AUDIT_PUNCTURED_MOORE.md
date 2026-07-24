# Literature audit focused on punctured Moore distance spectra

**Audit date:** 24 July 2026  
**Conclusion:** exact formulas for the ordinary distance spectra after deleting
one vertex, an adjacent pair, or a nonadjacent pair have been derived and
verified in this branch. No direct prior source was located in the searched
literature. This does **not** establish novelty or priority.

## 1. Objects and operators searched

The search distinguished four operators that are often grouped together by
keywords but are mathematically different:

1. the adjacency matrix of a vertex-deleted or edge-deleted graph;
2. the distance matrix of the intact distance-regular or strongly regular
   graph;
3. the ordinary distance matrix of the deleted graph, with all distances
   recomputed after deletion;
4. quantum-walk, Laplacian, distance-Laplacian, or generalized-distance
   matrices involving a deleted graph.

The extension theorems concern item 3.

## 2. Exact queries

Searches were run over arXiv full text, Crossref/DOI pages, publisher search,
Semantic Scholar, OpenAlex-facing results, MaRDI/zbMATH-facing records, and
general exact-phrase search. Representative queries were:

```text
"distance spectrum" "vertex-deleted" "Moore graph"
"distance spectrum" "vertex deleted" strongly regular graph
"distance matrix" "vertex-deleted subgraph" strongly regular
"Hoffman-Singleton graph" "vertex-deleted" spectrum
"Hoffman-Singleton graph minus a vertex"
"punctured Moore graph" spectrum
"deleted Moore graph" "distance matrix"
"x^2+4x-3" "Hoffman-Singleton"
"x^2 - 94x + 354" graph
"x^2 - 92x + 303" graph
"x^4 - 88x^3 - 125x^2 + 1740x - 778"
```

No relevant exact-formula match was returned.

## 3. Source-by-source comparison

### Howlader--Panigrahi: intact minimal cages

A. Howlader and P. Panigrahi, “On the Distance Spectrum of Minimal Cages
and Associated Distance Biregular Graphs,” *Linear Algebra and its
Applications* **636** (2022), 115–133,
DOI <https://doi.org/10.1016/j.laa.2021.11.014>,
arXiv <https://arxiv.org/abs/2109.05274>.

The full text states the standard recurrence for the distance matrices of a
distance-regular graph and derives a polynomial `D=p(A)` for intact minimal
cages. It also treats subdivisions, which are distance-biregular. Full-text
search returned no occurrence of “vertex-deleted,” and no theorem computes the
ordinary distance matrix after deleting a Moore vertex or pair.

**Relation:** establishes the intact Moore distance-polynomial framework; does
not give the punctured spectra.

### Aalipour et al.: general distance spectra

G. Aalipour et al., “On the Distance Spectra of Graphs,” *Linear Algebra and
its Applications* **497** (2016), 66–87,
DOI <https://doi.org/10.1016/j.laa.2016.02.018>.

This is a broad source on distance spectra and includes explicit families and
structural results. No indexed abstract or exact-formula search connected it to
vertex-deleted Moore graphs. Its cited-by chain was searched for the puncture
phrases above without a direct match.

**Relation:** general distance-spectrum background, not a located source for
the formulas.

### Biggs: second subconstituents

N. Biggs, “The Second Subconstituent of Some Strongly Regular Graphs,”
arXiv <https://arxiv.org/abs/1003.0175>.

The paper studies candidate second subconstituents of triangle-free strongly
regular graphs through equitable partitions. Full-text search returned no
occurrence of “distance spectrum” and no occurrence of “Hoffman--Singleton.”

**Relation:** close incidence-module and subconstituent methodology; not the
ordinary distance spectrum of a deletion.

### Fiol: quotient-polynomial graphs

M. A. Fiol, “Quotient-Polynomial Graphs,” *Linear Algebra and its
Applications* **488** (2016), 363–376,
DOI <https://doi.org/10.1016/j.laa.2015.09.053>,
arXiv <https://arxiv.org/abs/1506.04688>.

The paper proves that quotient-polynomial graphs are distance-polynomial and
generate symmetric association schemes. Full-text search returned no
“vertex-deleted” match.

**Relation:** supplies a general adjacency-algebra language; it does not state
the punctured characteristic factors.

### Dalfó--van Dam--Fiol: graph perturbations

C. Dalfó, E. R. van Dam, and M. A. Fiol, “On Perturbations of Almost
Distance-Regular Graphs,” arXiv <https://arxiv.org/abs/1202.3313>.

This paper explicitly studies deleting a vertex, adding a loop, adding a
pendant edge, adding or removing an edge, amalgamating vertices, and adding a
bridging vertex. The cospectrality under discussion is adjacency cospectrality
and punctual walk-regularity.

**Relation:** closest deletion vocabulary, but a different operator. The
ordinary distance matrix after deletion is not determined merely by the
vertex-deleted adjacency characteristic polynomial.

### Walk-regular vertex deletion

Classical results of Godsil--McKay, Delorme--Tillich, and Fiol--Garriga imply
that a graph is walk-regular if and only if all its vertex-deleted adjacency
subgraphs are cospectral. Modern summaries and token-graph papers restate this
equivalence.

**Relation:** explains why all one-vertex adjacency deletions of a Moore graph
share a characteristic polynomial. It does not compute the graph-distance
matrix after deletion.

### Quantum-walk use of a vertex-deleted adjacency matrix

A. Chan and H. Zhan, “The Average Search Probabilities of Discrete-Time
Quantum Walks,” arXiv <https://arxiv.org/abs/2108.09818>.

The average search probability on a distance-regular graph is expressed using
the adjacency matrix of a vertex-deleted subgraph.

**Relation:** another nearby use of the deleted adjacency matrix, not an
ordinary distance-spectrum result.

## 4. Exact factors searched

The branch obtains, for the 49-vertex Hoffman--Singleton puncture,

```text
(x-1)^14 (x+4)^21 (x^2-94x+354) (x^2+4x-3)^6.
```

For adjacent deleted vertices it obtains

```text
(x-3) (x-1)^9 (x+4)^16
(x^2-92x+303) (x^2+4x-3)^10.
```

For nonadjacent deleted vertices it obtains

```text
(x-4) (x+4)^15 (x-1)^8
(x^2+4x-4)^5 (x^2+4x-2)^5
(x^4-88x^3-125x^2+1740x-778).
```

Searches for the distinctive quadratic and quartic factors, both alone and
combined with “Hoffman--Singleton,” “Moore,” “distance,” and “graph,” did not
locate a matching paper, preprint, thesis, or database record.

## 5. Permitted wording

The evidence supports:

> We derive and exactly verify the distance spectrum of the graph obtained by
> deleting ... from a Moore graph.

The evidence does not support:

- “first computation”;
- “new distance spectrum”;
- “previously unknown”;
- “no one has studied this graph”;
- a priority statement based on negative search results.

## 6. Remaining priority checks

Before a journal submission uses novelty language, the author should perform
through ENS institutional access:

1. direct MathSciNet and zbMATH queries for the puncture phrases and exact
   factors;
2. cited-by inspection of Howlader--Panigrahi, Aalipour et al., Biggs, and
   Dalfó--van Dam--Fiol;
3. searches in monographs on distance-regular graphs, Terwilliger algebras,
   local spectra, and graph perturbations;
4. dissertation and conference-proceedings searches;
5. contact with experts if the result is to be advertised as a new spectral
   formula.

Until those checks produce positive priority evidence, the branch deliberately
uses derivation language without novelty language.
