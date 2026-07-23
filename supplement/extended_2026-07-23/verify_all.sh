#!/usr/bin/env bash
set -euo pipefail
python scripts/verify_wow284_38_40_42.py
python scripts/verify_38_graph6_independent.py
python scripts/verify_descendant_families.py
python scripts/explore_generalizations.py
python scripts/export_graphs.py
sha256sum -c SHA256SUMS
