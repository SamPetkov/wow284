#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
python scripts/verify_exact.py --output results/verification.json
python scripts/export_graph_data.py --output-dir results
python scripts/verify_optimal_slack_gram_unification.py
python scripts/verify_integral_optimal_slack_collapse.py
python scripts/verify_optimal_slack_excess_matrix.py
python scripts/verify_two_gram_hierarchies.py
python scripts/verify_four_to_one_excess_bound.py
python scripts/materialize_four_to_one_note.py --check
python scripts/sync_manuscript_artifacts.py
python -m pytest -q
python scripts/validate_repository.py
