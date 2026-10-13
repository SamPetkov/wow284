# WOW-284: current v2 manuscript package

The final bounded GPT-6 Pro review of each paper was completed on 13 October 2026. The checked local prose corrections are included here. No new theorem or hypothesis change was introduced by this final pass.

- `main.pdf`: the current 39-page paper.
- `main.tex`: editable LaTeX source.
- `WOW284-v2-arxiv-upload.zip`: the arXiv upload package.
- `MANIFEST.txt` and `SHA256SUMS`: the current scoped inventory and checksums for this directory. The checksum ledger excludes itself.
- `arxiv-abstract.txt` and `arxiv-comments.txt`: separate arXiv metadata.

The upload archive contains exactly `main.tex`, `main.bbl`, `references.bib`, and `petkov-preprint.sty`. Its exact extracted contents compiled successfully with pdfLaTeX on 13 October 2026, without warnings, unresolved references or citations, missing glyphs, or overfull/underfull boxes. All PDF fonts are embedded, and internal and external hyperlinks are present. Both papers use the same stylesheet.

## Formalization scope

The imported WOW release supplies finite coordinate and matrix certificates, scalar implications, and the full graph-independent LP optimum and rigidity. The actual graph-distance spectral assembly, graph trace bridge, and deletion theory retain the scope described in Appendix I.

The fresh kernel replay runs only on Procida, using Lean 4.31.0 and the pinned Mathlib revision `fabf563a7c95a166b8d7b6efca11c8b4dc9d911f`. It uses new project OLeans and a reused Mathlib cache. The SSH connection became unavailable before the full run could be retrieved. As of the last verified progress, WOW had checked 67 of 195 production-closure modules and Erdős had checked 194 of 480 under its required `autoImplicit=false` option, with no failures observed in those corrected runs. Full fresh closure, standalone and endpoint-patch completion are unconfirmed until the source-bound remote logs are retrieved. Earlier successful compilation evidence remains historical evidence; it is not described as a completed fresh replay.

Separately prepared unpublished endpoint patches are excluded from released formalization coverage. No Lean sources or toolchain were changed by this manuscript publication. This directory is ready for an author-managed arXiv replacement; no arXiv submission was made. No new AI-detector score is claimed.

The root manuscript files, root `MANIFEST.txt`, and root `SHA256SUMS` are historical July records. Use this directory for the current manuscript, upload package, and integrity record. The root `BUILD_VERIFICATION.txt` now identifies that distinction and corrects its formalization scope.
