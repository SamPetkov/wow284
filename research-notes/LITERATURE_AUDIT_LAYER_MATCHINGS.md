# Literature audit: perfect-matching deletions of the Hoffman--Singleton graph

**Audit date:** 24 July 2026  
**Scope:** the explicit family \(G_{HS}-M_\pi\) studied in
`LAYER_MATCHING_DELETIONS.md`  
**Rule:** unsuccessful indexed search is not evidence of novelty.

## Search distinctions

The search kept the following subjects separate:

1. existence and enumeration of perfect matchings in the Hoffman--Singleton
   graph;
2. matching-preclusion questions, where one deletes edges to destroy all perfect
   matchings;
3. graph products such as crown graphs, which are themselves obtained by
   deleting a perfect matching from a complete bipartite graph;
4. ordinary distance spectra after deleting one specified perfect matching from
   a fixed strongly regular graph;
5. adjacency spectra and interlacing under edge deletion.

Only item 4 matches the operator and construction in the present experiment.

## Query families

Representative queries included:

```text
"Hoffman-Singleton graph" "perfect matching" deletion spectrum
"Hoffman-Singleton" "perfect matching" distance matrix
"distance spectrum" graph minus perfect matching strongly regular
"perfect matching deletion" "distance spectrum"
"Hoffman-Singleton" matching polynomial deleted matching
```

The searches covered arXiv, Crossref-facing results, publisher pages, named-graph
records, and exact-factor fragments from the two characteristic polynomials.

## Closest located literature

- G. Aalipour et al., *On the Distance Spectra of Graphs*, Linear Algebra and
  its Applications 497 (2016), 66--87,
  DOI `10.1016/j.laa.2016.02.018`, provides general distance-spectral context
  and spectra of several highly structured graph families.  It does not state
  the present matching-deletion spectra.
- The Hoffman--Singleton graph and its strongly regular parameters are
  classical.  The coordinate construction used here is already attributed in
  the main project.
- Matching-preclusion literature studies minimum edge sets whose removal
  destroys perfect or almost-perfect matchings.  That is a different problem:
  the present construction removes a perfect matching and studies the distance
  matrix of the surviving graph.
- Recent distance-spectrum papers on crown-related graphs concern special graph
  products arising from `K_(n,n)` minus a perfect matching, not deletion from
  the Hoffman--Singleton graph.

## Search outcome

No direct indexed source was located that states either of the two ordinary
distance spectra in `LAYER_MATCHING_DELETIONS.md`, or that classifies the 120
coordinate matchings into the affine and nonaffine distance-spectral classes.

The permitted wording is therefore:

> We exactly classify this explicit 120-member coordinate family and derive its
> two distance spectra.

The following wording is not justified:

- first classification;
- previously unknown;
- new distance spectra;
- all perfect matchings of the Hoffman--Singleton graph;
- all 6-regular order-50 spanning subgraphs.

## Priority status

`project_exact_classification_priority_unresolved`

A stronger priority statement would require direct MathSciNet and zbMATH
searches, a cited-by review of the closest Hoffman--Singleton and distance
spectrum papers, and a search of dissertations or computational graph-spectrum
catalogues.
