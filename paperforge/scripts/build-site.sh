#!/usr/bin/env bash
set -euo pipefail

INSTANCE="$(cd "$(dirname "$0")/.." && pwd)"
python3 "$INSTANCE/scripts/assemble_site.py"
python3 "$INSTANCE/scripts/site_smoke_test.py"
