# Deep literature audit for the next WOW-284 research directions

**Audit date:** 24 July 2026  
**Scope:** proposed extensions and open directions after the submitted manuscript  
**Policy:** this audit controls wording and research priorities; it does not modify `main.tex` or the arXiv package.

## Executive assessment

The deeper search changes the emphasis of the extension program in three ways.

First, the regular diameter-three problem is not an isolated spectral search. Its upper-eigenvalue side lies directly inside the **spectral Moore problem**: for fixed valency \(k\) and threshold \(\theta<2\sqrt{k-1}\), one asks for the largest order of a connected \(k\)-regular graph with \(\lambda_2\le\theta\). Cioabă--Koolen--Nozaki--Vermette and the 2026 follow-up of Cioabă--Gupta--Nozaki--Xiang provide the closest general bounds. The WOW condition is stricter because it imposes the two-sided window
\[
  -1-\sqrt{2k-2}<\theta_i<-1+\sqrt{2k-2}
\]
on every nonprincipal adjacency eigenvalue.

Second, the higher-diameter distance-polynomial formula belongs to established distance-regular, distance-polynomial, quotient-polynomial, predistance-polynomial, and minimal-cage frameworks. Its value here is as a transparent WOW-284 specialization, not as an independently new general theory.

Third, the punctured-Moore calculations remain the most plausible genuinely distinctive extension. Searches located close work on vertex-deleted **adjacency** spectra, distance-critical deletion, intact Moore distance spectra, and subconstituents, but no direct source stating the recomputed ordinary distance spectra after deleting one Moore vertex, an edge's endpoints, or a nonadjacent pair. This is **priority unresolved**, not evidence of novelty.

> Search silence is not proof of novelty.

## Search method

The audit used independent query families across:

1. arXiv title, abstract, experimental HTML, and exact-formula search;
2. Crossref and publisher DOI pages;
3. journal and author publication pages;
4. citation-chain and terminology expansion from the closest primary papers;
5. exact polynomial-factor searches for punctured Hoffman--Singleton graphs;
6. named-graph, cage, subconstituent, Terwilliger, walk-regular, perturbation, spectral-Moore, quadratic-embedding, and negative-type terminology;
7. exhaustive-generation and graph-census terminology.

The machine-readable source matrix is
`research-notes/NEXT_DIRECTION_SOURCE_MATRIX.json`. Exact query families are
recorded in `research-notes/LITERATURE_QUERY_LOG_NEXT_DIRECTIONS.md`.

## 1. Dual degree and radius-two growth

Aouchiche and Hansen record WOW-284 in the dual-degree terminology used by the
manuscript. The same local statistic is also known elsewhere as average
neighbor degree or normalized 2-degree. The proposed identity
\[
  d^*(v)=\frac{|B_2(v)|-1}{d(v)}
\]
under the exclusion of triangles and 4-cycles follows immediately because the
sets \(N(u)\setminus\{v\}\), for \(u\in N(v)\), are pairwise disjoint.

No indexed source stating this exact radius-two formula was located. That
absence does not support a novelty claim. The correct label is:

> elementary counting lemma connecting established terminology to the WOW
> application.

It can be used freely, but should not be advertised as a new invariant or a
new theorem of independent significance.

Primary context:

- M. Aouchiche and P. Hansen, *Distance Spectra of Graphs: A Survey*,
  Linear Algebra Appl. 458 (2014), 301--386,
  DOI `10.1016/j.laa.2014.06.010`.

## 2. Ordinary distance spectra of punctured Moore graphs

### Closest literature layers

The literature separates into four nearby but distinct layers.

**Intact distance spectra.** Howlader and Panigrahi express distance matrices
of minimal cages as polynomials in adjacency and list the intact Moore cases.
Aalipour et al. provide broader distance-spectral context.

**Adjacency perturbations.** Dalfó, van Dam, and Fiol study cospectrality after
deleting a vertex, adding or deleting an edge, adding loops, amalgamating
vertices, and related operations. Their operator is the adjacency matrix.
This does not determine the ordinary graph-distance matrix after deletion,
because remaining pairwise distances can increase.

**Distance-critical deletion.** Cooper and Tauscheck define a graph to be
distance critical when deleting every vertex changes at least one remaining
pairwise distance. Their Proposition 2.4 characterizes distance criticality
using determining pairs, and their Lemma 3.1 shows that minimum degree at
least two together with girth greater than four implies distance
criticality. This is directly relevant to the support of the distance-increase
matrix, but not to its spectrum.

**Subconstituents.** Biggs and the distance-regular/Terwilliger literature
analyze local and second-subconstituent modules. Those modules are close to
the decompositions used in the puncture proofs, but the punctured ordinary
distance operator is different.

### Search outcome

No direct indexed statement was located for any of the following:

- the ordinary distance spectrum of \(M-v\) for a diameter-two Moore graph;
- the ordinary distance spectrum of \(M-\{u,v\}\) for \(uv\in E(M)\);
- the ordinary distance spectrum after deleting a nonadjacent pair;
- the exact Hoffman--Singleton puncture factors appearing in the project.

Queries covered graph names, “punctured Moore graph,” “vertex-deleted
distance spectrum,” adjacency-versus-distance terminology, and exact
polynomial factors.

### Permitted wording

Use:

> We derive and exactly verify the ordinary distance spectrum of ...

Do not use:

- first;
- new spectrum;
- previously unknown;
- no one has studied;
- complete novelty.

Institutional MathSciNet and zbMATH searches, dissertation searches, and a
full cited-by review remain required before stronger priority language.

Primary sources:

- C. Dalfó, E. R. van Dam, and M. A. Fiol, *On perturbations of almost
  distance-regular graphs*, arXiv:1202.3313.
- J. Cooper and G. Tauscheck, *Distance Critical Graphs*,
  arXiv:2405.09656, current version 22 March 2026.
- G. Aalipour et al., *On the Distance Spectra of Graphs*,
  Linear Algebra Appl. 497 (2016), 66--87,
  DOI `10.1016/j.laa.2016.02.018`.
- N. Biggs, *The Second Subconstituent of Some Strongly Regular Graphs*,
  arXiv:1003.0175.

## 3. Deletion stability and the distance-increase matrix

The proposed matrix
\[
  E_S=D(G-S)-D(G)[V(G-S)]
\]
records the metric effect of deletion. Cooper--Tauscheck supplies a
structural language for when \(E_{\{v\}}\neq0\). It does not study the least
eigenvalue of \(E_S\).

The inequality obtained from principal-submatrix interlacing and Weyl's
inequality is a standard matrix consequence. Its specialized application to
WOW-284 and Moore punctures is useful, but the general inequality should not
be given a novelty label.

A productive literature-facing formulation is:

> Distance criticality identifies when the perturbation is nonzero; the WOW
> application asks how negative its least eigenvalue can be relative to the
> surviving dual degree.

This makes the new problem precise without overstating the linear algebra.

## 4. Higher-diameter distance-polynomial transfer

Howlader--Panigrahi explicitly state that the distance matrices \(A_i\) of a
distance-regular graph are adjacency polynomials and hence
\(D=p(A)\). Their Theorems 2.2--2.5 derive these polynomials for minimal
cages, including
\[
  D=2A^2+A-2kI
\]
for minimal \((k,5)\)-cages.

Fiol's quotient-polynomial graphs are walk-regular and distance-polynomial.
Distance mean-regular graphs and spectral-excess theory provide further
orthogonal-polynomial and distance-layer frameworks. Nozaki's linear
programming work connects large girth, few eigenvalues, and extremal
second eigenvalues.

Therefore the proposed recurrence
\[
  F_0=1,\quad F_1=x,\quad F_2=x^2-k,\quad
  F_i=xF_{i-1}-(k-1)F_{i-2},
\]
and the formula \(D=dJ+q_d(A)\) under a strong girth hypothesis belong to an
established framework.

Permitted label:

> a short specialization of distance-polynomial machinery to the WOW
> inequality.

Not permitted without a theorem-by-theorem comparison:

> a new general higher-diameter transfer theorem.

Primary sources:

- A. Howlader and P. Panigrahi, LAA 636 (2022), 115--133,
  DOI `10.1016/j.laa.2021.11.014`, arXiv:2109.05274.
- M. A. Fiol, *Quotient-Polynomial Graphs*, LAA 488 (2016), 363--376,
  DOI `10.1016/j.laa.2015.09.053`, arXiv:1506.04688.
- V. Diego and M. A. Fiol, *Distance Mean-Regular Graphs*,
  arXiv:1508.03835.
- H. Nozaki, *Linear Programming Bounds for Regular Graphs*,
  Graphs Combin. 31 (2015), 1973--1984,
  DOI `10.1007/s00373-015-1613-7`, arXiv:1407.4562.

## 5. The spectral Moore problem is the principal overlap

For fixed \(k\) and \(\theta<2\sqrt{k-1}\), Cioabă--Koolen--Nozaki--Vermette
study the maximum order \(v(k,\theta)\) of a connected \(k\)-regular graph
with \(\lambda_2\le\theta\). Their bounds derive from Nozaki's linear
programming method. Equality graphs are distance-regular Moore polygons.

The 2026 paper of Cioabă--Gupta--Nozaki--Xiang develops this program further,
proves nonexistence results for Moore polygons, and determines new exact
values such as
\[
  v(4,\sqrt2)=14,\qquad
  v(5,\sqrt2)=v(5,\sqrt5-1)=16.
\]
It also proves a sharp second-eigenvalue jump for connected 5-regular graphs.

For regular girth-five diameter-three graphs, WOW requires
\[
  \max_{\theta_i\ne k}|\theta_i+1|<\sqrt{2k-2}.
\]
The upper endpoint is the one-sided spectral-Moore condition
\[
  \lambda_2<-1+\sqrt{2k-2}.
\]
The lower endpoint is extra:
\[
  \lambda_{\min}(A)>-1-\sqrt{2k-2}.
\]

Hence:

- spectral-Moore bounds can reduce the candidate order;
- they do not by themselves prove WOW violation;
- the two-sided lower-tail test remains essential;
- the project's moment and distance-layer bounds should be compared against
  these LP bounds before any independent-strength claim.

This is the most important literature correction for the next research phase.

Primary sources:

- S. M. Cioabă, J. H. Koolen, H. Nozaki, and J. R. Vermette,
  SIAM J. Discrete Math. 30 (2016), 1509--1525,
  DOI `10.1137/15M1030935`, arXiv:1503.06286.
- S. M. Cioabă, V. Gupta, H. Nozaki, and Z. Xiang,
  *The Non-Existence of Some Moore Polygons and Spectral Moore Bounds*,
  arXiv:2512.09680.
- T. Koledin, *Regular Graphs with Girth at Least 5 and Small Second
  Largest Eigenvalue*, LAA 439 (2013), 1229--1244,
  DOI `10.1016/j.laa.2013.04.006`.

## 6. Degree-six search and canonical generation

No published or indexed complete census was located for all connected
6-regular girth-five diameter-three graphs of orders 40 through 51.

What is available:

- Meringer's orderly canonical generation of regular graphs and GENREG;
- the exact generation of the four \((5,5)\)-cages;
- Goedgebeur--Jooken's specialized generator for edge-girth-regular graphs;
- the result \(n(6,5,20)=42\) in that structured subclass;
- Koledin and spectral-Moore bounds for small \(\lambda_2\).

These do not constitute a census of the required class.

A defensible exhaustive-search specification must record:

1. generator and version;
2. exact command line and canonical options;
3. counts before and after girth, connectedness, diameter, and spectral
   pruning;
4. graph6 checksums for every survivor and boundary graph;
5. exact reconstruction of every candidate;
6. exact characteristic-polynomial, Sturm, or shifted-positive-definite
   certificates;
7. all equality and near-boundary cases.

Until that exists, the statement is:

> no complete census in the exact range was located.

It is not:

> the range has never been searched.

Primary sources:

- M. Meringer, J. Graph Theory 30 (1999), 137--146,
  DOI `10.1002/(SICI)1097-0118(199902)30:2<137::AID-JGT7>3.0.CO;2-G`.
- J. Goedgebeur and J. Jooken,
  *Exhaustive Generation of Edge-Girth-Regular Graphs*,
  arXiv:2401.08271.
- T. Koledin, LAA 439 (2013), 1229--1244.

## 7. Small excess, cages, and finite-field constructions

The excess
\[
  c=n-k^2-1
\]
places the degree-three discussion inside a long-established small-excess and
cage program.

Jørgensen constructs girth-five graphs from relative difference sets,
including the degree-7 Hoffman--Singleton graph and a degree-9 graph on
96 vertices. Abreu--Funk--Labbate--Napolitano give a finite-field family
generalizing Murty's construction. Later work improves constructive upper
bounds for regular girth-five graphs.

The correct distinction is:

- the graph families are known;
- their use as WOW test families is an application;
- the Fourier-block obstruction for diameter three may be a specialized
  result, but priority is unresolved;
- no conclusion about higher-diameter members follows from the
  diameter-three obstruction.

Primary sources:

- L. K. Jørgensen, *Girth 5 Graphs from Relative Difference Sets*,
  Discrete Math. 293 (2005), 177--184,
  DOI `10.1016/j.disc.2004.08.029`.
- M. Abreu, M. Funk, D. Labbate, and V. Napolitano,
  *A Family of Regular Graphs of Girth 5*,
  Discrete Math. 308 (2008), 1810--1815,
  DOI `10.1016/j.disc.2007.04.031`.

## 8. Infinite-family prospects

Bachratý--Šiagiová--Širáň construct Cayley graphs of diameter three and
order
\[
  d^3-O(d^{2.5})
\]
for an infinite sequence of degrees. This shows that the combinatorial Moore
bound can be approached by vertex-transitive graphs.

That result does not control the two-sided shifted adjacency window required
by WOW. The spectral-Moore literature gives one-sided upper-eigenvalue
control and also explains why, for each fixed \(k\), only finitely many graphs
can lie below a threshold \(2\sqrt{k-1}\).

No unconditional infinite family satisfying the full WOW window was located.
This is an open construction problem, not a nonexistence theorem.

The most promising source classes remain:

- association schemes and low-rank permutation actions;
- subconstituents of distance-regular graphs;
- nonbipartite covers with explicit new-spectrum control;
- unbounded-degree Cayley constructions whose lower adjacency tail can also
  be bounded.

Primary source:

- M. Bachratý, J. Šiagiová, and J. Širáň,
  *Asymptotically Approaching the Moore Bound for Diameter Three by Cayley
  Graphs*, arXiv:1709.09760.

## 9. Equality boundary

The regular diameter-three equality condition is
\[
  \max_{\theta_i\ne k}|\theta_i+1|=\sqrt{2k-2}.
\]

No direct classification of this exact boundary was located. The closest
frameworks are:

- spectral Moore equality and Moore polygons;
- distance-regular graph classification;
- association schemes;
- LP-bound equality conditions.

The 96-vertex degree-9 graph from Jørgensen's construction is an exact
project-side equality example. Its equality status is a verified
computation, not a published classification.

A next theorem should distinguish:

1. rational boundary, when \(2k-2\) is a square;
2. irrational conjugate boundary, where algebraic conjugacy constrains
   multiplicities;
3. equality graphs attaining an LP or quotient bound;
4. equality graphs that are not distance regular.

The literature currently supports the framework, not a complete answer.

## 10. Negative type and quadratic embedding

For a finite graph, Choudhury--Nandi define the quadratic embedding constant
as
\[
  \operatorname{QEC}(G)
  =
  \max\{x^{\mathsf T}D x:\|x\|=1,\ x\perp\mathbf1\}.
\]

Thus QEC controls the **maximum** restricted distance quadratic form.
WOW-284 concerns the **least** unrestricted distance eigenvalue. The same
distance matrix appears, but the extremal directions are opposite.

This invalidates a tempting shortcut:

> negative type does not automatically supply the lower spectral estimate
> required by WOW-284.

Campbell--Hendrey--Lund--Tompkins classify negative type for continuous
metric graphs using theta submetrics. Their objects are metric realizations
of graphs, not automatically the finite vertex path metric used in WOW.

No source linking dual degree to QEC, conditional negative definiteness, or
negative type was located.

The restricted conjecture remains legitimate:

> Does WOW-284 hold for finite graph metrics of quadratic-embedding class?

But it currently has neither proof nor counterexample in this audit.

Primary sources:

- P. N. Choudhury and R. Nandi,
  *Quadratic Embedding Constants of Graphs: Bounds and Distance Spectra*,
  arXiv:2306.15589, current version 22 March 2026.
- R. Campbell, K. Hendrey, B. Lund, and C. Tompkins,
  *Metric Graphs of Negative Type*, arXiv:2501.07098.
- Z. Lou, N. Obata, and Q. Huang,
  *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752.

## 11. Irregular minimality below order 38

No complete canonical census of all connected irregular triangle- and
4-cycle-free graphs through order 37 was located.

Regular-graph and structured-subclass generators do not solve this problem.
A viable minimality computation needs additional mathematics before
generation:

- lower bounds from \(\delta^*>\operatorname{diam}(G)\);
- degree-sequence restrictions;
- minimum-degree and leaf elimination;
- radius-two growth constraints;
- articulation and block-structure pruning;
- spectral interlacing from induced paths or local configurations;
- canonical augmentation preserving the girth filter.

Any numerical mutation or deletion search remains exploratory. Minimality
language is forbidden until a canonical exhaustive computation with exact
post-certification is complete.

## 12. Priority labels permitted by this audit

| Topic | Permitted label |
| --- | --- |
| Radius-two identity | elementary reformulation of established dual degree |
| Intact Moore spectrum | known |
| Diameter-three adjacency window | specialized WOW application; priority unresolved |
| Punctured ordinary distance spectra | exact derivation; no direct source located; priority unresolved |
| Deletion stability | standard matrix lemma with a specialized application |
| Higher-diameter transfer | established distance-polynomial framework |
| Moment and layer bounds | specialized WOW consequences; compare with spectral Moore bounds |
| Degree-six census | no complete census located; new computation required |
| Finite-field families | known constructions; specialized obstruction priority unresolved |
| Infinite family | open |
| Equality boundary | open specialized classification |
| Negative-type restriction | open |
| Order-38 minimality | unproved and unsearched exhaustively |

## 13. Required institutional follow-up

Before any journal or arXiv revision uses novelty language for punctured Moore
spectra:

1. search MathSciNet directly for vertex-deleted Moore graphs, deleted
   strongly regular graphs, distance matrices after deletion, and the exact
   polynomial factors;
2. repeat in zbMATH Open with classification codes `05C50`, `05E30`, and
   `15A18`;
3. inspect cited-by chains of Howlader--Panigrahi, Dalfó--van Dam--Fiol,
   Biggs, and Aalipour et al.;
4. search dissertations, conference proceedings, and books on Terwilliger
   algebras and graph perturbations;
5. add all close results to the source matrix;
6. retain “we derive” unless a positive priority argument is established.

## 14. Recommended next work

The research order should be:

1. compare the degree-six \(40\le n\le51\) window against the explicit
   spectral-Moore LP bound before generating graphs;
2. specify and run a canonical degree-six census only if the literature bound
   does not already collapse the range;
3. test the quadratic-embedding subclass on exact graph databases;
4. classify the equality boundary in known distance-regular and
   association-scheme families;
5. continue punctured-Moore literature clearance through institutional
   databases;
6. treat the irregular order-37 problem only after stronger structural
   pruning is proved.

This order avoids duplicating established spectral-Moore work and preserves
the project's exact-certification standard.
