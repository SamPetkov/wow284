# arXiv submission notes

These notes prepare an upload; they do not authorize or represent an actual
arXiv submission.

## Suggested metadata

**Title:** The Hoffman-Singleton Graph Refutes WOW-284

**Author:** Samuil Petkov

**Primary category:** `math.CO`

**Optional cross-list:** `math.SP` only if the submitter judges that the
distance-spectrum content meets that category's current scope.

**Comments:** Self-contained research note with exact Python verification;
includes a source and priority ledger. The PDF page count should be copied from
`BUILD_VERIFICATION.txt` after the final rebuild.

**License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

**Abstract:**

> WOW-284 asserts that the minimum dual degree of every connected graph of
> order at least three and girth at least five is at most the negative of its
> least distance eigenvalue. We record a counterexample on 50 vertices. The
> graph is given by an explicit coordinate construction over F_5. It is
> 7-regular, has girth five, and has distance spectrum
> {91^(1),1^(21),(-4)^(28)}. Consequently its minimum dual degree is 7,
> whereas the negative of its least distance eigenvalue is 4. The strict gap
> is therefore 3. The graph is the Hoffman-Singleton graph, but the proof uses
> no classification or named-graph property: a direct common-neighbor
> certificate yields connectedness, girth, and the full spectrum. Exact
> verification code builds the distance matrix independently by breadth-first
> search and checks the characteristic polynomial over the integers.

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
- rerun the novelty search immediately before announcement if priority
  language is changed.

Do not add a claim of first discovery, a new distance spectrum, or minimality
without new evidence.
