# Build and verification notes

## Python verification

```bash
python -m pip install -r requirements.txt
python scripts/verify_wow284_38_40_42.py
python scripts/verify_38_graph6_independent.py
python scripts/verify_descendant_families.py
python scripts/explore_generalizations.py
```

All proof assertions in the first three scripts are exact. The final script marks its one NumPy-based three-vertex deletion screen explicitly as exploratory.

## LaTeX

The report was compiled with pdfTeX 1.40.26. Standard sequence:

```bash
cd report
pdflatex wow284_extended_report.tex
bibtex wow284_extended_report
pdflatex wow284_extended_report.tex
pdflatex wow284_extended_report.tex
```

The package also includes the generated `.bbl` and PDF.

## Verified environment

- Python 3.13.5
- SymPy 1.14.0
- NetworkX 3.6.1
- NumPy 2.3.5
- TeX Live development snapshot / pdfTeX 1.40.26

## PDF inspection

The final PDF has nine A4 pages, embedded fonts, no unresolved citations or references, and no overfull/underfull-box warnings in the final log. It was rendered to PNG at 140 dpi for visual inspection.
