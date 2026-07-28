#!/usr/bin/env python3
"""Generate one import-free WOW-284 Lean source from the verified module DAG."""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
import re

from generate_lean39_42 import render as render_lean39_42


ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
OUTPUT = LEAN / "Wow284Standalone.lean"
ROOT_MODULES = (
    "Wow284ExtensionAudit",
    "Wow284Generated3942Audit",
    "Wow284LPAudit",
)
IMPORT_RE = re.compile(r"^import\s+([A-Za-z0-9_.]+)\s*$")


def module_name(path: Path) -> str:
    return ".".join(path.relative_to(LEAN).with_suffix("").parts)


def committed_sources() -> dict[str, tuple[Path, str]]:
    sources: dict[str, tuple[Path, str]] = {}
    for path in sorted(LEAN.rglob("*.lean")):
        if path == OUTPUT or ".lake" in path.parts or path.name == "lakefile.lean":
            continue
        sources[module_name(path)] = (path, path.read_text(encoding="utf-8"))
    return sources


def all_sources() -> dict[str, tuple[Path, str]]:
    sources = committed_sources()
    for path, text in render_lean39_42().items():
        if path.suffix != ".lean" or not path.is_relative_to(LEAN):
            continue
        sources[module_name(path)] = (path, text)
    return sources


def imports(text: str) -> list[str]:
    result: list[str] = []
    for line in text.splitlines():
        match = IMPORT_RE.fullmatch(line)
        if match:
            result.append(match.group(1))
    return result


def dependency_order(
    sources: dict[str, tuple[Path, str]],
) -> tuple[list[str], list[str]]:
    ordered: list[str] = []
    external: list[str] = []
    state: dict[str, int] = {}

    def visit(module: str, trail: tuple[str, ...]) -> None:
        mark = state.get(module, 0)
        if mark == 2:
            return
        if mark == 1:
            cycle = " -> ".join((*trail, module))
            raise RuntimeError(f"internal import cycle: {cycle}")
        if module not in sources:
            if module not in external:
                external.append(module)
            return

        state[module] = 1
        for imported in imports(sources[module][1]):
            visit(imported, (*trail, module))
        state[module] = 2
        ordered.append(module)

    for root in ROOT_MODULES:
        if root not in sources:
            raise RuntimeError(f"missing standalone root module: {root}")
        visit(root, ())
    return ordered, external


def strip_imports(text: str) -> str:
    return "\n".join(
        line for line in text.splitlines() if not IMPORT_RE.fullmatch(line)
    ).strip()


def render_standalone() -> tuple[str, int, int]:
    sources = all_sources()
    ordered, external = dependency_order(sources)
    pieces = [*(f"import {module}" for module in external), ""]
    pieces.extend(
        [
            "/-!",
            "Deterministically generated single-file WOW-284 formal development.",
            "",
            "Regenerate with `python scripts/generate_lean_standalone.py`.",
            "The file contains the committed 50-, 38-, and 40-vertex developments,",
            "the generated 39- and 42-vertex developments, the analytic all-degree",
            "LP optimum-and-rigidity development, and their trust reports.",
            "-/",
            "",
        ]
    )

    for module in ordered:
        path, text = sources[module]
        relative = path.relative_to(ROOT).as_posix()
        body = strip_imports(text)
        pieces.extend(
            [
                f"/-! BEGIN FLATTENED MODULE: {module} ({relative}) -/",
                "section",
                body,
                "end",
                f"/-! END FLATTENED MODULE: {module} -/",
                "",
            ]
        )

    rendered = "\n".join(pieces).rstrip() + "\n"
    return rendered, len(ordered), len(external)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail unless the committed standalone file is current",
    )
    args = parser.parse_args()

    rendered, module_count, external_count = render_standalone()
    digest = hashlib.sha256(rendered.encode("utf-8")).hexdigest()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != rendered:
            raise SystemExit(f"stale generated standalone Lean file: {OUTPUT}")
        action = "PASS"
    else:
        OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
        action = "WROTE"

    print(
        f"standalone Lean: {action}; modules={module_count}; "
        f"external_imports={external_count}; sha256={digest}"
    )


if __name__ == "__main__":
    main()
