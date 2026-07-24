# Literature audit for the proposed WOW-284 extensions

**Audit date:** 24 July 2026  
**Scope:** structural and spectral extensions in
`VERIFIED_RESEARCH_EXTENSIONS.md`; this file does not assert priority from
search silence.

## 1. Method

The audit used several independent discovery routes:

1. arXiv title, abstract, and full-text search;
2. Crossref/DOI and publisher landing pages;
3. journal databases for *Linear Algebra and its Applications*, *Discrete
   Mathematics*, *Journal of Graph Theory*, and the *Electronic Journal of
   Combinatorics*;
4. searches indexed through Semantic Scholar, OpenAlex, and zbMATH-facing web
   results;
5. exact-formula searches for the characteristic-polynomial factors occurring
   in the Hoffman--Singleton punctures;
6. named-graph and subconstituent searches;
7. citation-chain checks from the most relevant primary papers.

Representative exact queries included:

```text
"distance spectrum" "vertex-deleted" "Moore graph"
"distance matrix" "vertex deleted" strongly regular
"Hoffman-Singleton graph" "vertex-deleted" spectrum
"Hoffman-Singleton graph minus a vertex"
"punctured Moore graph" spectrum
"x^2+4x-3" "distance" graph Hoffman Singleton
"x^2 - 94x + 354" graph
Moore graph second subconstituent intersection array
quotient-polynomial graphs distance matrices adjacency algebra
spectral excess theorem predistance polynomials girth
```

A failed query is evidence only that the indexed search did not locate a
matching source. It is not a proof of novelty.

## 2. Claim-by-claim assessment

| Proposed claim | Closest located literature | Assessment |
| --- | --- | --- |
| Moore-graph distance spectrum and the degree threshold behind the 50-vertex example | Hoffman--Singleton (1960); Howlader--Panigrahi (2022) | The graph family, adjacency spectrum, and distance-polynomial mechanism are established. Do not claim a new spectrum. The WOW-284 application and exact packaging require conservative priority language. |
| Radius-two interpretation `d*(v)=(|B_2(v)|-1)/d(v)` under no triangles or 4-cycles | No direct indexed statement found; follows immediately from disjoint second-neighborhood branches | Treat as an elementary lemma, not a novelty claim. |
| Diameter-three identity and adjacency-window criterion | Closest frameworks: distance-polynomial and quotient-polynomial graphs; minimal cages; spectral-excess theory | The polynomial-in-adjacency viewpoint is known. The exact WOW-284 criterion is a specialized application; priority not established. |
| 42-vertex second subconstituent | Biggs (2010) and the broader distance-regular/subconstituent literature; the graph is standard | The graph and adjacency structure are known. Do not claim the construction or adjacency spectrum as new. |
| Exact distance spectrum after deleting one Moore vertex | No direct source found after phrase, formula, arXiv, Crossref, OpenAlex, Semantic Scholar, and zbMATH-oriented searches | The derivation is proved and exact, but novelty is **not established**. Use wording such as “we derive” rather than “we determine for the first time.” |
| Exact distance spectrum after deleting an edge's endpoints from a Moore graph | Same search outcome as the one-vertex case | Proved in the extension note; priority unresolved. |
| Deletion-stability inequality from a principal distance submatrix and the distance-increase matrix | Cauchy interlacing and Weyl inequalities are standard matrix analysis | The lemma is a direct standard consequence. Do not present the matrix inequality itself as a new theorem of independent priority; the Moore/WOW application may still be useful. |
| Fourth-moment order bound and distance-layer compression | Standard spectral moments, quotient interlacing, predistance polynomials, and spectral Moore bounds | The tools are established. The particular WOW-284 bounds may be new applications, but this needs a focused comparison with recent spectral Moore-bound papers. |
| Higher-diameter transfer `D=dJ+q_d(A)` | Howlader--Panigrahi's minimal-cage distance polynomials; Fiol's distance-polynomial framework; spectral-excess literature | This belongs to a known framework. The current note should not claim the general transfer formula as new without a theorem-by-theorem comparison. |
| Exactly four `(5,5)`-cages | Meringer (1999) | Established. Any degree-five no-go theorem must import all four graphs and recompute the needed spectra locally. |
| Prime-field coordinate family | Murty's construction and Abreu--Funk--Labbate--Napolitano (2008) | The family is known. Only a carefully scoped spectral obstruction could be new. |
| Direct public refutation of WOW-284 | Roucairol--Cazenave (2024) still treated the relevant set as open; a non-peer-reviewed AGNT Labs note dated 23 July 2026 records an independent exact verification and makes an external-agent priority claim | The external priority claim has not been independently authenticated here. Retain the manuscript's existing no-priority language and record the note in the provenance ledger rather than asserting priority. |

## 3. Primary and near-primary sources

### Moore graphs and distance spectra

- A. J. Hoffman and R. R. Singleton, “On Moore Graphs with Diameters 2
  and 3,” *IBM Journal of Research and Development* **4** (1960), 497–504.
  DOI: <https://doi.org/10.1147/rd.45.0497>.
- A. Howlader and P. Panigrahi, “On the Distance Spectrum of Minimal Cages
  and Associated Distance Biregular Graphs,” *Linear Algebra and its
  Applications* **636** (2022), 115–133.
  DOI: <https://doi.org/10.1016/j.laa.2021.11.014>;
  arXiv: <https://arxiv.org/abs/2109.05274>.
- G. Aalipour et al., “On the Distance Spectra of Graphs,” *Linear Algebra
  and its Applications* **497** (2016), 66–87.
  DOI: <https://doi.org/10.1016/j.laa.2016.02.018>.
- V. Faber and J. Keegan, “Existence of a Moore Graph of Degree 57 Is Still
  Open,” arXiv: <https://arxiv.org/abs/2210.09577>.

### Distance-polynomial and spectral-excess frameworks

- M. A. Fiol, “Quotient-Polynomial Graphs,” *Linear Algebra and its
  Applications* **488** (2016), 363–376.
  DOI: <https://doi.org/10.1016/j.laa.2015.09.053>;
  arXiv: <https://arxiv.org/abs/1506.04688>.
- E. R. van Dam, “The Spectral Excess Theorem for Distance-Regular Graphs:
  A Global (Over)view,” *Electronic Journal of Combinatorics* **15** (2008),
  R129. DOI: <https://doi.org/10.37236/853>.
- E. R. van Dam and M. A. Fiol, “A Short Proof of the Odd-Girth Theorem,”
  arXiv: <https://arxiv.org/abs/1205.0153>.
- M. A. Fiol and S. Penjić, “On Symmetric Association Schemes and
  Associated Quotient-Polynomial Graphs,” arXiv:
  <https://arxiv.org/abs/2009.05343>.

### Subconstituents and cages

- N. Biggs, “The Second Subconstituent of Some Strongly Regular Graphs,”
  arXiv: <https://arxiv.org/abs/1003.0175>.
- M. Meringer, “Fast Generation of Regular Graphs and Construction of
  Cages,” *Journal of Graph Theory* **30** (1999), 137–146.
  DOI:
  <https://doi.org/10.1002/(SICI)1097-0118(199902)30:2%3C137::AID-JGT7%3E3.0.CO;2-G>.
- M. Abreu, M. Funk, D. Labbate, and V. Napolitano, “A Family of Regular
  Graphs of Girth 5,” *Discrete Mathematics* **308** (2008), 1810–1815.
  DOI: <https://doi.org/10.1016/j.disc.2007.04.031>.

### Conjecture-search context

- M. Roucairol and T. Cazenave, “Refutation of Spectral Graph Theory
  Conjectures with Search Algorithms,” arXiv:
  <https://arxiv.org/abs/2409.18626>.
- AGNT Labs, “Graffiti 284 Refuted by Hoffman--Singleton: An Independent
  Exact Verification,” 23 July 2026:
  <https://agnt.gg/whitepapers/graffiti-284-refutation.html>.
  This is a web verification note, not a peer-reviewed publication. Its
  priority narrative is recorded but not adopted as an independently verified
  fact.

## 4. Novelty labels permitted by this audit

The following labels are defensible:

- **Known framework, new application not priority-cleared:** the
  diameter-three operator identity as used for WOW-284, moment bounds, and
  layer compression.
- **Exact derivation, no direct prior source located:** the one-vertex and
  adjacent-edge punctured Moore distance spectra.
- **Standard matrix lemma, useful specialized consequence:** deletion
  stability.
- **Known graph construction:** the Moore graphs, 40-vertex cage, 42-vertex
  second subconstituent, `(5,5)`-cages, and prime-field girth-five family.

The following labels are not justified:

- “first,” “new spectrum,” “previously unknown,” or “minimal”;
- “unconditional infinite family”;
- “complete classification of regular counterexamples” before the four
  `(5,5)`-cages are imported and checked;
- novelty of the higher-diameter distance-polynomial transfer.

## 5. Additional literature work still required

Before moving the punctured-Moore theorems into a journal version:

1. inspect the full texts and cited-by lists of Howlader--Panigrahi (2022),
   Aalipour et al. (2016), and Biggs (2010), not only their abstracts;
2. search MathSciNet and zbMATH directly through institutional access for
   “vertex-deleted Moore graph,” “distance spectrum of a deleted strongly
   regular graph,” and the exact polynomial factors;
3. inspect books and chapters on Terwilliger algebras and subconstituents for
   an equivalent module decomposition;
4. check dissertations and conference proceedings not indexed by general web
   search;
5. add every located close result to `SOURCE_LEDGER.md` before making any
   novelty statement.

The present audit is rigorous enough to control wording in a draft PR. It is
not a proof that the punctured spectra are absent from all published or
unpublished literature.
