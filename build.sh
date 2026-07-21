#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
python scripts/verify_exact.py --output results/verification.json
python scripts/export_graph_data.py --output-dir results
python scripts/sync_manuscript_artifacts.py
python -m pytest -q
python scripts/validate_repository.py
