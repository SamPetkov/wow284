# arXiv submission notes

These notes prepare an upload; they do not authorize or represent an actual
arXiv submission.

## Suggested metadata

**Title:** Moore Graphs of Diameter Two and the Failure of WOW-284

**Author:** Samuil Petkov

**Primary category:** `math.CO`

**Optional cross-list:** `math.SP` only if the submitter judges that the
distance-spectrum content meets that category's current scope.

**Comments:** Self-contained research note with exact Python verification and
a complete Lean 4.31 formalization of the explicit counterexample; includes a
source and priority ledger.
The PDF page count should be copied from `BUILD_VERIFICATION.txt` after the
final rebuild.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Abstract:**

> WOW-284 asserts that the minimum dual degree of every connected graph of
> order at least three and girth at least five is at most the negative of its
> least distance eigenvalue. We isolate its behavior on Moore graphs of
> diameter two. For such a graph of degree k >= 2, the minimum dual degree is
> k, while the least distance eigenvalue is -(3 + sqrt(4k - 3))/2. Thus
> WOW-284 holds for k = 2, is an equality for k = 3, and fails for every
> realizable degree k > 3. The degree-7 instance is the Hoffman-Singleton
> graph: it has 50 vertices, girth five, and distance spectrum
> {91^(1),1^(21),(-4)^(28)}, giving a strict gap of 3. We provide a
> self-contained coordinate certificate over F_5 and an independent exact
> computational check. The distance spectra of minimal cages were determined
> previously; the point here is their consequence for WOW-284.

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
- do not change the formal-verification wording to present tense unless the
  final Lean spectral theorem, strict audit, and CI have all passed; and
- rerun the novelty search immediately before announcement if priority
  language is changed.

Do not add a claim of first discovery, a new distance spectrum, or minimality
without new evidence.
