# Literature query log for the next WOW-284 directions

**Search date:** 24 July 2026  
**Purpose:** reproducible query families used for
`DEEP_LITERATURE_AUDIT_NEXT_DIRECTIONS.md`.

This log records discovery queries and interpretation rules. It is not a
bibliographic completeness proof.

## Search rules

1. Prefer primary papers, arXiv records, journal pages, and author publication
   pages.
2. Treat secondary graph databases only as discovery aids.
3. Separate adjacency perturbation from recomputed ordinary distance spectra.
4. Separate continuous metric graphs from finite vertex path metrics.
5. Separate one-sided \(\lambda_2\) bounds from the two-sided WOW adjacency
   window.
6. Never infer novelty from an unsuccessful query.

## Punctured Moore graphs and deletion

```text
"distance spectrum" "vertex-deleted" "Moore graph"
"distance matrix" "vertex deleted" strongly regular
"Hoffman-Singleton graph" "vertex-deleted" spectrum
"Hoffman-Singleton graph minus a vertex"
"punctured Moore graph" spectrum
"ordinary distance spectrum" deleted graph
"distance characteristic polynomial" "vertex-deleted" graph
"vertex deleted" "distance eigenvalues" graph
"distance spectral deck" graph
"x^2+4x-3" distance graph Hoffman Singleton
"x^2-94x+354" graph
"distance critical graphs" vertex deletion
"distance increase matrix" graph deletion
```

Terminology expansions:

```text
walk-regular vertex-deleted characteristic polynomial
almost distance-regular perturbations vertex deletion
subconstituent distance matrix deleted strongly regular graph
Terwilliger module punctured graph distance matrix
```

## Dual degree and local growth

```text
"dual degree" graph average neighbor degree
"average neighbor degree" second neighborhood C4-free graph
"2-degree" graph radius two ball
"sum of neighbor degrees" second neighborhood girth five
```

## Distance-polynomial and higher-diameter transfer

```text
"distance matrix" polynomial adjacency minimal cage
"distance-polynomial graph" adjacency algebra
quotient-polynomial graphs distance matrices adjacency algebra
predistance polynomials girth diameter distance matrix
spectral excess theorem predistance polynomials girth
nonbacktracking polynomials distance matrices regular graph
```

## Spectral Moore problem and small second eigenvalue

```text
"spectral Moore" regular graph second eigenvalue
"maximum order" regular graph second eigenvalue
"regular graphs with girth at least 5" small second largest eigenvalue
v(k,theta) regular graph second eigenvalue
Moore polygons spectral Moore bounds
linear programming bounds regular graphs girth eigenvalue
```

## Degree-six census and generation

```text
"6-regular" girth 5 graphs order 40 51 census
"sextic" girth 5 exhaustive generation
"regular graphs" girth 5 canonical generation degree 6
"edge-girth-regular" 6 5 20 42
GENREG degree 6 girth 5
nauty genreg girth 5 sextic
database regular graphs girth at least 5 order 51
```

## Small excess and near-Moore graphs

```text
"regular graph" girth 5 excess Moore bound
"girth 5" small second largest eigenvalue
"girth 5 graphs" relative difference sets
regular graphs order k^2+c girth 5
almost Moore graph girth five excess
```

## Finite-field and relative-difference-set constructions

```text
"family of regular graphs of girth 5" finite field
"girth 5 graphs from relative difference sets"
Murty graph girth 5 Hoffman Singleton
finite field graph girth 5 spectrum
Jorgensen 96 graph spectrum
```

## Infinite families

```text
"diameter three" Cayley graphs Moore bound
"Asymptotically approaching the Moore bound for diameter three"
"shifted adjacency spectrum" regular graph
regular graph second eigenvalue Moore bound infinite family
association scheme adjacency eigenvalues diameter three family
```

## Equality boundary

```text
"-1+sqrt(2k-2)" graph eigenvalue
"-1-sqrt(2k-2)" graph eigenvalue
distance eigenvalue equality girth 5 regular diameter 3
spectral Moore equality distance regular
Jorgensen 96 graph spectrum
Perkel graph distance spectrum
```

## Negative type and quadratic embedding

```text
"quadratic embedding constant" distance spectrum graph
"graph metric" negative type distance matrix
"conditionally negative definite" graph distance matrix
quadratic embedding dual degree graph
QEC average neighbor degree graph
metric graph theta negative type
```

## Irregular minimality

```text
"C3 C4-free graphs" exhaustive generation
"girth at least 5" graph generation canonical
irregular graph girth five exhaustive generation order 37
triangle square free graph census 37 vertices
canonical augmentation C3 C4-free graphs
```

## Search outcomes that must be interpreted cautiously

The following outcomes mean only “not located in the indexed routes used”:

- no direct ordinary distance spectrum for punctured Moore graphs;
- no complete 6-regular girth-five diameter-three census for orders 40--51;
- no direct classification of the WOW equality boundary;
- no link between dual degree and quadratic-embedding constants;
- no unconditional infinite family satisfying the full two-sided shifted
  adjacency window;
- no complete irregular \(C_3,C_4\)-free census through order 37.

None of these statements is a priority or nonexistence theorem.

## Institutional searches still required

Use ENS access to repeat the puncture and exact-factor queries in:

- MathSciNet;
- zbMATH Open;
- Web of Science;
- Scopus, if available;
- ProQuest Dissertations and Theses;
- Springer and Cambridge book chapters on distance-regular graphs and
  Terwilliger algebras.

Record positive hits, exact theorem numbers, and cited-by chains in the source
matrix. A failed institutional query must still not be converted into a
novelty claim.

## Exact matrix query strings not already listed verbatim

```text
"Hoffman-Singleton graph" "vertex-deleted" distance spectrum
"distance matrix" vertex deletion interlacing
"distance increase" graph vertex deletion
"predistance polynomials" girth diameter distance matrix
"regular graphs" girth 5 excess Moore bound
"Murty" graph girth 5 Hoffman Singleton
"regular graph" second eigenvalue Moore bound infinite family
"distance eigenvalue" equality girth 5 regular diameter 3
"spectral Moore" equality distance regular
"regular graph generation" canonicity girth
```
