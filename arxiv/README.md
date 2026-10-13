# WOW-284 revised v2 manuscript

Current sources and matching PDF after two separate rounds of GPT-6 Pro review, prepared 13 October 2026. The completed reports were independently adjudicated before accepting changes. No arXiv replacement has been submitted.

Download [main.pdf](main.pdf) (39 pages) or [WOW284-v2-arxiv-upload.zip](WOW284-v2-arxiv-upload.zip). The legacy archive wow284_arxiv_source.zip contains the same package. Main text: about 23.5 pages, with supporting material and references following. Shared preprint typography and coloured links are preserved.

This round records 15 source changes:

- Name both contents of Appendix H: the relocated degree comparison table and the divisor checks.
- Restore the diameter-three qualification in the prime-field summary.
- State the different scopes of the two construction exclusions.
- Avoid suggesting an unconditional exclusion of the whole prime-field family in the heading.
- Put the prime-field diameter assumption in the subsection title.
- Describe the actual verifier coverage and link the companion nonpositive-excess check.
- Distinguish the row sum of the Gram matrix from that of its signed adjacency matrix.
- Name the three vertices in the forbidden triangle.
- Use the constant-vector eigenvalue rather than Perron terminology for a signed matrix.
- Explain the line-root dichotomy before its first use.
- Remove the definition now supplied before the line-root case split.
- Replace the repeated line-root explanation by a reference to its earlier derivation.
- Use the previously proved diameter exclusions instead of repeating their Rayleigh calculation.
- Use the general deletion-distance theorem instead of repeating the one-deletion path proof.
- Use the general deletion theorem for adjacent two-deletion paths, retaining its size condition.

The principal conclusions and their exact graph/phase hypotheses are retained. The review is not a proof certification or new Lean replay; the manuscript retains its precise formal-verification scope and assistance disclosure.

The four-file ZIP contains main.tex, main.bbl, references.bib and petkov-preprint.sty at its root. Compile main.tex with pdflatex or latexmk -pdf. Separate abstract and comments metadata are provided. The exact upload sources compile without warnings or errors; the PDF has embedded fonts, bookmarks and internal/external links.

The [version submitted for this review](https://github.com/SamPetkov/wow284/tree/bf139ad169219d84fecc2605532140cf28e433ea/arxiv) remains in Git history.

Root manuscript mirrors and main.md are legacy artifacts; use this directory’s TeX and PDF for v2.
