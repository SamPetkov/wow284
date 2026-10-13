# WOW-284 revised v2 manuscript

Current reviewed v2 sources and PDF, prepared 13 October 2026, with a shorter main text. This prepares an arXiv replacement; none has been submitted.

Download [main.pdf](main.pdf) (39 pages) or [WOW284-v2-arxiv-upload.zip](WOW284-v2-arxiv-upload.zip). The legacy archive name wow284_arxiv_source.zip contains the same package.

The main text occupies about 23.4 pages, down from 31.5. Appendix A contains the secondary order-50 restrictions; Appendix B contains the full one- and two-deletion spectral calculations. The main text keeps the central order bounds, changed-distance formula, stability results and useful deletion scores. Complete mathematical arguments remain in the PDF, so the total page count stays 39.

The archive contains main.tex, main.bbl, references.bib and petkov-preprint.sty at the root. Compile main.tex using pdflatex or latexmk -pdf. arxiv-abstract.txt and arxiv-comments.txt provide separate metadata. The shared preprint sizing and coloured links are preserved.

The exact extracted upload sources compile with PDFLaTeX/MiKTeX without warnings or errors. The 41 theorem-like statements, abstracts, citations and display equations were checked against the preceding reviewed version. In 625, one repeated expectation-bound display was removed and arbitrary parameters in the shared amplification proof were renamed. WOW's bibliography entries are unchanged; their generated order follows the new citation order. These checks do not claim a new formal verification or detector score.

[Before the main-text shortening](https://github.com/SamPetkov/wow284/tree/37493c6196ea401fc8393a9b88e15fc0777b4bc0/arxiv) is preserved in Git history.

main.md and root manuscript mirrors are legacy artifacts; use this directory's current TeX and PDF for v2.
