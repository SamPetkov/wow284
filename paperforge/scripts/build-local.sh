#!/usr/bin/env bash
set -euo pipefail

PAPERFORGE_COMMIT="726cc7d679441e28f39cfd52d3e2dd0251c79a6d"
PRETEXT_VERSION="2.43.2"
INSTANCE="$(cd "$(dirname "$0")/.." && pwd)"
REPOSITORY="$(cd "$INSTANCE/.." && pwd)"
CACHE_ROOT="${PAPERFORGE_CACHE_ROOT:-$REPOSITORY/.cache/paperforge-site}"
TOOL_ROOT="$CACHE_ROOT/paperforge-tool"
VENV="$CACHE_ROOT/venv"

mkdir -p "$CACHE_ROOT"
if [[ ! -d "$TOOL_ROOT/.git" ]]; then
  git clone https://github.com/roed-math/paperforge.git "$TOOL_ROOT"
fi
git -C "$TOOL_ROOT" fetch --depth=1 origin "$PAPERFORGE_COMMIT"
git -C "$TOOL_ROOT" checkout --detach "$PAPERFORGE_COMMIT"

if [[ ! -x "$VENV/bin/python" ]]; then
  python3 -m venv "$VENV"
fi
"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install "pretext==$PRETEXT_VERSION"
"$VENV/bin/python" -m pip install -e "$TOOL_ROOT" -e "$TOOL_ROOT/validators"

export PATH="$VENV/bin:$PATH"
export PAPERFORGE_COMMIT
export SOURCE_COMMIT="$(git -C "$REPOSITORY" rev-parse HEAD)"

paperforge init "$INSTANCE" \
  --force \
  --title "Counterexamples, Spectral Obstructions, and Deletion Stability for WOW-284" \
  --slug wow284 \
  --draft ../main.tex \
  --no-lean \
  --site \
  --non-interactive

python "$INSTANCE/scripts/hydrate_paperforge_assets.py" "$TOOL_ROOT"
paperforge ingest "$INSTANCE" --bootstrap
paperforge build web "$INSTANCE"
paperforge build site "$INSTANCE"

printf '\nSite ready at %s\n' "$INSTANCE/output/site/index.html"
