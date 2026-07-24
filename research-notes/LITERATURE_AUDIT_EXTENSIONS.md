# Literature audit for the proposed WOW-284 extensions

**Audit date:** 24 July 2026  
**Scope:** structural and spectral extensions in
`VERIFIED_RESEARCH_EXTENSIONS.md` and
`REGULAR_LOW_DEGREE_OBSTRUCTION.md`. This file does not infer priority from
search silence.

## 1. Method

The audit used independent discovery routes rather than a single keyword
search:

1. arXiv title, abstract, and full-text search;
2. Crossref/DOI and publisher landing pages;
3. journal searches for *Linear Algebra and its Applications*, *Discrete
   Mathematics*, *Journal of Graph Theory*, *Electronic Journal of
   Combinatorics*, and related spectral-graph venues;
4. searches indexed through Semantic Scholar, OpenAlex, MaRDI/zbMATH-facing
   records, and Google Scholar-facing citation pages;
5. exact-formula searches for the characteristic-polynomial factors in the
   Hoffman--Singleton punctures;
6. named-graph, subconstituent, Terwilliger, walk-regular, and perturbation
   searches;
7. citation-chain inspection from the most relevant primary papers;
8. exact reconstruction of the four `(5,5)`-cages and comparison with the
   public House of Graphs labels.

Representative queries included:

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
walk-regular vertex-deleted characteristic polynomial
perturbations almost distance-regular graphs vertex deletion
spectral excess predistance polynomials girth
```

A failed query says only that the indexed search did not locate a matching
source. It is not a proof of novelty.

## 2. Literature layers that must not be conflated

### 2.1 Distance spectra of the intact Moore graph

Hoffman--Singleton supplies the strongly regular structure. Howlader and
Panigrahi derive distance polynomials for minimal cages and explicitly place
Moore graphs in that framework. Their full text states that the distance
matrices of a distance-regular graph are polynomials in its adjacency matrix
and develops the corresponding minimal-cage distance spectrum.

This literature covers the 50-vertex distance spectrum. It does not make the
spectrum new in the present project.

### 2.2 Vertex-deleted **adjacency** spectra

There is a substantial perturbation literature for adjacency matrices:
walk-regular graphs are characterized by equality of all vertex-deleted
adjacency spectra, and Dalfó--van Dam--Fiol study cospectrality under deleting
a vertex, adding or deleting an edge, amalgamating vertices, and related
operations.

These results are close in vocabulary but not in operator: they concern the
adjacency characteristic polynomial or local adjacency spectrum. They do not
supply the ordinary graph-distance matrix of the deleted graph, whose entries
can increase after deletion.

### 2.3 Distance-polynomial and quotient-polynomial structure

Fiol's quotient-polynomial graphs are walk-regular and distance-polynomial;
spectral-excess and predistance-polynomial theory gives a general language for
recovering distance layers from adjacency spectra. The higher-diameter transfer
in the extension note belongs to this established framework.

### 2.4 Subconstituents and local modules

Biggs studies second subconstituents of triangle-free strongly regular graphs
through equitable partitions. The 42-vertex Hoffman--Singleton second
subconstituent is a standard object in distance-regular and subconstituent
literature. The graph and its adjacency structure are not new.

The one-vertex and edge-puncture calculations in the extension note use
similar incidence modules, but the operator being diagonalized is the distance
matrix of the punctured graph.

## 3. Claim-by-claim assessment

| Proposed claim | Closest located literature | Assessment |
| --- | --- | --- |
| Moore-graph distance spectrum and the degree threshold behind the 50-vertex example | Hoffman--Singleton (1960); Howlader--Panigrahi (2022) | The graph family, adjacency spectrum, and distance-polynomial mechanism are established. Do not claim a new spectrum. The WOW-284 application should retain conservative priority language. |
| Radius-two interpretation `d*(v)=(|B_2(v)|-1)/d(v)` under no triangles or 4-cycles | No direct indexed statement found; immediate from disjoint second-neighborhood branches | Treat as an elementary lemma, not a novelty claim. |
| Diameter-three identity and adjacency-window criterion | Distance-polynomial and quotient-polynomial graphs; minimal cages; spectral-excess theory | The polynomial-in-adjacency viewpoint is known. The precise WOW-284 operator norm and window are specialized applications; priority not established. |
| 42-vertex second subconstituent | Biggs and the broader distance-regular/subconstituent literature | Known graph and adjacency structure. Do not claim the construction or adjacency spectrum as new. |
| Exact distance spectrum after deleting one Moore vertex | Full-text and exact-formula searches located adjacency-deletion and quantum-walk applications, but no source stating this ordinary distance spectrum | The derivation is proved and exact. Novelty remains **not established**. Use “we derive,” not “for the first time.” |
| Exact distance spectrum after deleting the endpoints of a Moore edge | Same distinction and search outcome as the one-vertex case | Proved in the extension note; priority unresolved. |
| Deletion-stability inequality from a principal distance submatrix and distance-increase matrix | Cauchy interlacing and Weyl inequalities | A direct standard matrix consequence. The Moore/WOW application is useful; the matrix lemma itself should not carry a novelty claim. |
| Fourth-moment order bound and distance-layer compression | Spectral moments, quotient interlacing, predistance polynomials, spectral Moore bounds | Established tools. The exact WOW-284 bounds appear to be a specialized application; this is not a priority finding. |
| Higher-diameter transfer `D=dJ+q_d(A)` | Howlader--Panigrahi minimal-cage distance polynomials; Fiol distance-polynomial framework; spectral-excess literature | Known framework. Do not claim the general transfer formula as new without a theorem-by-theorem comparison. |
| Exactly four `(5,5)`-cages | Meringer (1999) | Established exhaustive result. The branch now imports four fixed records and independently recomputes all data used in the proof. |
| Every regular strict counterexample has degree at least six | Uses Meringer's exhaustive cage theorem plus new exact application of distance and layer bounds | The proof is now complete and reproducible. It should be described as a theorem derived here, without a first-proof claim until further literature review. |
| Prime-field coordinate family | Murty and Abreu--Funk--Labbate--Napolitano | The construction is known. Only a carefully scoped spectral obstruction could be additional. |
| Direct public refutation of WOW-284 | Roucairol--Cazenave (2024) still treated the relevant collection as open; a non-peer-reviewed AGNT Labs note dated 23 July 2026 records an independent exact verification and an external-agent priority narrative | The external priority narrative is not independently authenticated here. Retain the manuscript's no-priority wording and record the note in provenance rather than adopting its claim. |

## 4. Primary and near-primary sources

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
- S. M. Cioabă, J. H. Koolen, H. Nozaki, and J. R. Vermette, “Maximizing
  the Order of a Regular Graph of Given Valency and Second Eigenvalue,”
  *SIAM Journal on Discrete Mathematics* **30** (2016), 1509–1525.

### Adjacency perturbations and local spectra

- C. Dalfó, E. R. van Dam, and M. A. Fiol, “On Perturbations of Almost
  Distance-Regular Graphs,” arXiv: <https://arxiv.org/abs/1202.3313>.
- C. Dalfó and M. A. Fiol, “A General Method to Obtain the Spectrum and
  Local Spectra of a Graph from Its Regular Partitions,” *Electronic Journal
  of Linear Algebra* **36** (2020), 446–460.
  DOI: <https://doi.org/10.13001/ela.2020.5225>.
- The classical equivalence between walk-regularity, spectral regularity, and
  equality of all vertex-deleted adjacency spectra is recorded in work of
  Godsil--McKay, Delorme--Tillich, and Fiol--Garriga and summarized in modern
  walk-regular references.

### Subconstituents and cages

- N. Biggs, “The Second Subconstituent of Some Strongly Regular Graphs,”
  arXiv: <https://arxiv.org/abs/1003.0175>.
- M. Meringer, “Fast Generation of Regular Graphs and Construction of
  Cages,” *Journal of Graph Theory* **30** (1999), 137–146.
  DOI:
  <https://doi.org/10.1002/(SICI)1097-0118(199902)30:2%3C137::AID-JGT7%3E3.0.CO;2-G>.
- K. Coolsaet, S. D'hondt, and J. Goedgebeur, “House of Graphs 2.0: A
  Database of Interesting Graphs and More,” *Discrete Applied Mathematics*
  **325** (2023), 97–107.
  DOI: <https://doi.org/10.1016/j.dam.2022.10.013>.
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

## 5. Exact cage provenance and closure

Meringer's primary paper proves that exactly four `(5,5)`-cages exist. The
branch contains one fixed graph6 record for each public House of Graphs label:
Foster, Meringer, Robertson--Wegner, and Wong.

The local verifier checks, for every record:

- the first ten public adjacency rows shown by House of Graphs;
- order 30, size 75, degree five, connectedness, girth five, and diameter
  three;
- the complete exact adjacency and distance characteristic polynomials;
- the expected automorphism-group order;
- pairwise nonisomorphism.

The four automorphism orders are 30, 96, 20, and 120. Meringer's exhaustive
count and the four nonisomorphic exact records close the only finite external
case used in the degree-at-least-six theorem.

## 6. Novelty labels permitted by this audit

Defensible wording:

- **Known framework, specialized WOW-284 application:** the diameter-three
  operator identity, moment bounds, and layer compression.
- **Exact derivation; no direct prior source located:** the one-vertex and
  adjacent-edge punctured Moore distance spectra.
- **Standard matrix lemma; specialized consequence:** deletion stability.
- **Known graph construction:** the Moore graphs, 40-vertex cage, 42-vertex
  second subconstituent, `(5,5)`-cages, and prime-field girth-five family.
- **Proved in this project, priority not asserted:** regular strict
  counterexamples have degree at least six.

Not justified:

- “first,” “new spectrum,” “previously unknown,” or “minimal”;
- “unconditional infinite family”;
- novelty of the general higher-diameter distance-polynomial transfer;
- a claim that no puncture formula exists elsewhere merely because the indexed
  searches were negative.

## 7. Further literature work before a journal novelty claim

1. Search MathSciNet and zbMATH directly through institutional access for
   “vertex-deleted Moore graph,” “distance spectrum of a deleted strongly
   regular graph,” and the exact polynomial factors.
2. Inspect the cited-by lists and full references of Howlader--Panigrahi,
   Aalipour et al., Biggs, and Dalfó--van Dam--Fiol.
3. Search books and chapters on Terwilliger algebras, local spectra, and
   subconstituents for an equivalent module decomposition.
4. Check dissertations, conference proceedings, and non-indexed technical
   reports.
5. Add every close source to `SOURCE_LEDGER.md` before using any novelty
   language.

The present audit is strong enough to control a draft PR and to separate the
proved content from known frameworks. It is not a proof that the punctured
spectra are absent from all published or unpublished literature.
