# Source, novelty, and dependency ledger

**Author:** Samuil Petkov<br>
**Manuscript date:** 19 July 2026<br>
**Last targeted search:** 21 July 2026

## Claim-level source map

| Item | Source and status | Role in this repository |
| --- | --- | --- |
| WOW-284 formulation | Aouchiche and Hansen, *Linear Algebra and its Applications* 458 (2014), Conjecture 7.16, DOI `10.1016/j.laa.2014.06.010` | Authoritative published formulation used in the introduction. |
| Original WOW attribution | Siemion Fajtlowicz, *Written on the Wall: Conjectures Derived on the Basis of the Program Galatea Gabriella Graffiti*, University of Houston technical report (1998) | Cited through the survey's bibliography and attribution. |
| Online WOWII catalogue | Ermelinda DeLaViña, *Written on the Wall II*, `http://cms.dt.uh.edu/faculty/delavinae/research/wowII/list.htm` | User-supplied public-catalogue URL, corroborated as the WOWII site by DeLaViña's history paper and later literature. The server timed out during the 21 July 2026 audit, so the exact conjecture wording is taken from the published survey, not inferred from the unavailable page. |
| Hoffman-Singleton graph | A. J. Hoffman and R. R. Singleton, *IBM Journal of Research and Development* 4 (1960), 497-504, DOI `10.1147/rd.45.0497` | Historical source for the named graph; no named-graph theorem is used in the proof. |
| Exact coordinate realization | Paul R. Hafner, *Journal of Algebraic Combinatorics* 18 (2003), Theorem 2.1, DOI `10.1023/A:1025136524481` | Published affine-coordinate form of Robertson's pentagon-and-pentagram construction; after reindexing the `Q`-layers by `k -> -k`, its adjacency rules are exactly those used here. |
| Published distance spectrum | Aditi Howlader and Pratima Panigrahi, *Linear Algebra and its Applications* 636 (2022), Theorem 2.5(1b), DOI `10.1016/j.laa.2021.11.014`, arXiv:2109.05274 | Prior publication of `Spec(D)={91,(-4)^28,1^21}`; explicitly credited. |
| Symbolic software | Meurer et al., *PeerJ Computer Science* 3 (2017), e103, DOI `10.7717/peerj-cs.103` | Citation for SymPy, used only in the independent exact certificate. |

## Exact relationship to prior work

Howlader and Panigrahi already record both the Hoffman-Singleton graph as the
minimal `(7,5)` cage and its full distance spectrum. Since the graph is
7-regular, its minimum dual degree is 7. Their published spectrum gives least
distance eigenvalue -4. Placing these facts beside WOW-284 yields

```text
7 = delta*(G) > 4 = -partial_50(G).
```

Accordingly, this repository does **not** claim a new spectrum. Its defensible
contribution is the explicit connection to WOW-284 together with a compact
self-contained coordinate proof and exact reproducibility package.

## Targeted novelty search

The following searches were run on 21 July 2026:

- full-web exact and phrase searches for `WOW-284`, `minimum dual degree`,
  `least distance eigenvalue`, and `Hoffman-Singleton` in combinations;
- Crossref bibliographic queries for the same combinations;
- arXiv API and arXiv full-text searches;
- searches within Aouchiche-Hansen (2014), Howlader-Panigrahi (2022), and
  later distance-spectrum papers located from their bibliographies;
- the supplied *Written on the Wall II* catalogue URL and its advertised
  open/resolved endpoints (the server was unavailable during the audit);
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

Not supported:

- "This is the first counterexample."
- "The distance spectrum is new."
- "The counterexample is minimal or smallest."
- "No one previously knew this observation."

The manuscript follows the permitted language.
