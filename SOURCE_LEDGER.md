# Source, novelty, and dependency ledger

**Author:** Samuil Petkov<br>
**Manuscript date:** 19 July 2026<br>
**Last targeted search:** 23 July 2026

## Claim-level source map

| Item | Source and status | Role in this repository |
| --- | --- | --- |
| WOW-284 formulation | Aouchiche and Hansen, *Linear Algebra and its Applications* 458 (2014), Conjecture 7.16, DOI `10.1016/j.laa.2014.06.010` | Authoritative published formulation used in the introduction. |
| Original WOW attribution | Siemion Fajtlowicz, *Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti*, University of Houston technical report (1998) | Cited through the survey's bibliography and attribution. |
| Online WOWII catalogue | Ermelinda DeLaViña, *Written on the Wall II*, `http://cms.dt.uh.edu/faculty/delavinae/research/wowII/list.htm` | The URL is valid and was reachable during the 22 July 2026 re-audit, but it is a separate Graffiti.pc catalogue with independent numbering: its item 284 is unrelated to the conjecture studied here. It is therefore documented in this ledger but not cited as a source for WOW-284 in the manuscript. |
| Hoffman-Singleton graph | A. J. Hoffman and R. R. Singleton, *IBM Journal of Research and Development* 4 (1960), 497-504, DOI `10.1147/rd.45.0497` | Historical source for the named graph; no named-graph theorem is used in the proof. |
| Exact coordinate realization | Paul R. Hafner, *Journal of Algebraic Combinatorics* 18 (2003), Theorem 2.1, DOI `10.1023/A:1025136524481` | Published affine-coordinate form of Robertson's pentagon-and-pentagram construction; after reindexing the `Q`-layers by `k -> -k`, its adjacency rules are exactly those used here. |
| Distance spectra of minimal cages | Aditi Howlader and Pratima Panigrahi, *Linear Algebra and its Applications* 636 (2022), Theorems 2.3 and 2.5(1), DOI `10.1016/j.laa.2021.11.014`, arXiv:2109.05274 | Prior distance-polynomial framework for minimal `(k,5)`-cages and explicit Petersen, Hoffman-Singleton, and hypothetical degree-57 spectra; explicitly credited. |
| Classical 40-vertex `(6,5)`-cage | O'Keefe and Wong, *Journal of Combinatorial Theory B* 26 (1979), DOI `10.1016/0095-8956(79)90052-2`; Wong, *Journal of Graph Theory* 3 (1979), DOI `10.1002/jgt.3190030413` | Construction and uniqueness of the classical cage; this is a minimum-order statement among 6-regular girth-five graphs, not among WOW-284 counterexamples. |
| Petersen deletion realization | Klin, Muzychuk, and Ziv-Av, *Michigan Mathematical Journal* 58 (2009), Section 3.6, DOI `10.1307/mmj/1242071692` | Published structural context for obtaining the 40-vertex graph from Hoffman-Singleton. |
| Hoffman-Singleton second subconstituent | van Dam and Haemers, *Linear Algebra and its Applications* 373 (2003), Table 3, DOI `10.1016/S0024-3795(03)00483-X` | Published identification and adjacency spectrum of the classical 42-vertex graph. |
| Symbolic software | Meurer et al., *PeerJ Computer Science* 3 (2017), e103, DOI `10.7717/peerj-cs.103` | Citation for SymPy, used for exact characteristic polynomials, Sturm counts, and rational certificates. |
| Graph software | Hagberg, Schult, and Swart, *Proceedings of SciPy 2008*, DOI `10.25080/TCWV9851` | Citation for NetworkX, used in the graph6-based integer-BFS audit and standard-family controls. |
| Lean 4 | Leonardo de Moura and Sebastian Ullrich, CADE 28 (2021), DOI `10.1007/978-3-030-79876-5_37` | System reference for the verified explicit-counterexample formalization. |
| Mathlib | The mathlib Community, CPP 2020, DOI `10.1145/3372885.3373824` | Library reference for the verified explicit-counterexample formalization. |
| Current degree-57 status | Derek H. Smith and Roberto Montemanni, *Axioms* 15 (2026), 332, DOI `10.3390/axioms15050332` | Peer-reviewed 2026 confirmation that existence of the degree-57 Moore graph remains open; the paper rules out only a cyclic-derangement construction. |

## Exact relationship to prior work

Howlader and Panigrahi already derive distance spectra for minimal `(k,5)`
cages and explicitly record the Hoffman-Singleton graph's full distance
spectrum. Since the graph is 7-regular, its minimum dual degree is 7. Their
published spectrum gives least distance eigenvalue -4. Placing these facts
beside WOW-284 yields

```text
7 = delta*(G) > 4 = -partial_50(G).
```

Their general formulas also contain the spectral ingredients behind the
degree-`k` calculation. Accordingly, this repository does **not** claim a new
spectrum or a new Moore-graph spectral formula. Its defensible mathematical
contribution is the sharp WOW-284 criterion `k > 3`, the explicit connection,
the exact induced counterexamples and descendant-family certificates, the
diameter-three criterion, and a compact self-contained reproducibility
package. No priority claim is made for an unpublished observation, and the
classical graph spectra are not claimed as new.

## Targeted novelty search

The following searches were run on 21--23 July 2026:

- full-web exact and phrase searches for `WOW-284`, `minimum dual degree`,
  `least distance eigenvalue`, and `Hoffman-Singleton` in combinations;
- Crossref bibliographic queries for the same combinations;
- arXiv API and arXiv full-text searches;
- searches within Aouchiche-Hansen (2014), Howlader-Panigrahi (2022), and
  later distance-spectrum papers located from their bibliographies;
- the supplied *Written on the Wall II* catalogue URL and its advertised
  open/resolved endpoints (reachable during the 22 July 2026 re-audit, with
  numbering confirmed to be independent of WOW-284);
- GitHub public code search for `WOW-284` and the Hoffman-Singleton/dual-degree
  combinations.

The searches found the 2014 conjecture statement and the 2022 prior spectral
calculation, but no accessible source explicitly stating that the
Hoffman-Singleton graph refutes WOW-284. Search coverage is never complete,
particularly for unpublished notes, private correspondence, non-indexed
reports, and differently worded observations.

## Permitted and forbidden novelty language

Permitted:

- "We record that the Hoffman-Singleton graph is a counterexample to WOW-284."
- "A targeted search did not locate an earlier explicit connection."
- "The note supplies a self-contained coordinate certificate."
- "For diameter-two Moore graphs, the WOW-284 inequality fails precisely in
  realizable degrees greater than three."

Not supported:

- "This is the first counterexample."
- "The distance spectrum is new."
- "The counterexample is minimal or smallest."
- "No one previously knew this observation."
- "The Moore-graph distance spectrum is new."

The manuscript follows the permitted language.
