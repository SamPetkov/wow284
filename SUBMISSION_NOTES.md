# arXiv submission notes

These notes prepare an upload; they do not authorize or represent an actual
arXiv submission.

## Suggested metadata

**Title:** Exact Counterexamples and Spectral Mechanisms for WOW-284

**Author:** Samuil Petkov

**Primary category:** `math.CO`

**Optional cross-list:** `math.SP` only if the submitter judges that the
distance-spectrum content meets that category's current scope.

**Comments:** Self-contained research note with exact Python verification for
counterexamples of orders 38, 39, 40, 42, and 50. The explicit 50-vertex
certificate and scalar Moore threshold have a complete Lean 4.31
formalization; the additional results are not yet Lean-formalized. Includes a
source and priority ledger.
The PDF page count should be copied from `BUILD_VERIFICATION.txt` after the
final rebuild.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Abstract:**

> WOW-284 asserts that the minimum dual degree of every connected graph of
> order at least three and girth at least five is at most the negative of its
> least distance eigenvalue. We disprove the conjecture by exact constructions
> of orders 38, 39, 40, 42, and 50, all obtained from Hoffman-Singleton
> coordinates. The 38-vertex graph has minimum dual degree 17/3 and least
> distance eigenvalue -3-sqrt(7), giving the positive gap 8/3-sqrt(7).
> Exact exhaustive computation further proves that every one of the 40
> labelled single-vertex deletions of the 40-vertex graph, and every one of
> its 120 labelled edge-endpoint deletions, is a strict counterexample. We
> establish a spectral criterion for regular girth-at-least-five graphs of
> diameter three and derive a parameterized construction from Moore second
> subconstituents. No minimality, first-discovery, or unconditional
> infinite-family claim is made. The 50-vertex certificate and scalar Moore
> threshold are verified in Lean 4.31; the additional constructions are
> analytic and exact-computational pending the expanded formalization.

## Upload artifact

Upload `arxiv/wow284_arxiv_source.zip`. It contains exactly:

```text
main.tex
references.bib
main.bbl
```

The archive intentionally excludes the compiled PDF, logs, caches, code,
audits, checksums, and GitHub files. arXiv's current TeX guidance says not to
include extraneous files and permits a matching `.bbl` and `.bib`. The source
uses a fixed date, not `\today`.

## Final account-level checks

Before clicking submit, Samuil Petkov should:

- confirm the displayed name, ENS/PSL affiliation, and email address;
- review the arXiv-generated PDF page by page, even though the local PDF was
  rendered and checked;
- choose the final category and CC BY 4.0 option in the arXiv interface;
- confirm title capitalization, abstract, comments, and author order;
- verify that the `.bbl` is recognized and all DOI/arXiv references render;
- confirm any required endorsement or institutional-email step;
- decide whether the public AI-assistance disclosure is satisfactory; and
- do not extend the formal-verification claim beyond the 50-vertex certificate
  and scalar threshold until the expanded Lean artifact passes strict audit;
- rerun the novelty search immediately before announcement if priority
  language is changed.

Do not add a claim of first discovery, a new distance spectrum, or minimality
without new evidence.
