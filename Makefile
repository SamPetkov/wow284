.PHONY: all pdf verify data test sync check clean

all: sync

pdf:
	latexmk -pdf -bibtex -interaction=nonstopmode -halt-on-error -file-line-error main.tex

verify:
	python scripts/verify_exact.py --output results/verification.json
	python scripts/verify_optimal_slack_gram_unification.py
	python scripts/verify_integral_optimal_slack_collapse.py
	python scripts/verify_optimal_slack_excess_matrix.py
	python scripts/verify_two_gram_hierarchies.py
	python scripts/verify_four_to_one_excess_bound.py
	python scripts/materialize_four_to_one_note.py --check

data:
	python scripts/export_graph_data.py --output-dir results

test:
	python -m pytest -q

sync:
	python scripts/sync_manuscript_artifacts.py

check:
	python -m pytest -q
	python scripts/verify_exact.py --quiet
	python scripts/verify_optimal_slack_gram_unification.py
	python scripts/verify_integral_optimal_slack_collapse.py
	python scripts/verify_optimal_slack_excess_matrix.py
	python scripts/verify_two_gram_hierarchies.py
	python scripts/verify_four_to_one_excess_bound.py
	python scripts/materialize_four_to_one_note.py --check
	python scripts/sync_manuscript_artifacts.py --check
	python scripts/validate_repository.py

clean:
	latexmk -C main.tex
	rm -f main.bbl main.run.xml main.synctex.gz
