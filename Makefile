.PHONY: all pdf verify data test sync check clean

all: sync

pdf:
	latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex

verify:
	python scripts/verify_exact.py --output results/verification.json

data:
	python scripts/export_graph_data.py --output-dir results

test:
	python -m pytest -q

sync:
	python scripts/sync_manuscript_artifacts.py

check:
	python -m pytest -q
	python scripts/verify_exact.py --quiet
	python scripts/sync_manuscript_artifacts.py --check
	python scripts/validate_repository.py

clean:
	latexmk -C main.tex
	rm -f main.bbl main.run.xml main.synctex.gz
