#!/usr/bin/env python3
"""Static consistency audit for the patch-style Lean extension.

This is not a Lean parser and is not a substitute for kernel compilation.  It
checks source hygiene, import closure within the extension plus the documented
base modules, and the deliberate separation of non-imported templates.
"""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LEAN = ROOT / "lean"
OUTPUT = ROOT / "data" / "lean_static_audit.txt"

BASE_IMPORTS = {
    "Mathlib",
    "Wow284",
    "Wow284.Basic",
    "Wow284.Coordinate",
    "Wow284.DiagonalizationData",
    "Wow284.MooreThreshold",
}
FORBIDDEN = {
    "sorry": re.compile(r"\bsorry\b"),
    "admit": re.compile(r"\badmit\b"),
    "native_decide": re.compile(r"\bnative_decide\b"),
    "bv_decide": re.compile(r"\bbv_decide\b"),
    "unsafe declaration": re.compile(r"\bunsafe\s+(?:def|theorem|lemma|instance)\b"),
    "axiom declaration": re.compile(r"(?m)^\s*axiom\s+"),
}
IMPORT = re.compile(r"(?m)^import\s+([A-Za-z0-9_.]+)\s*$")


def module_path(module: str) -> Path:
    parts = module.split(".")
    if parts[0] != "Wow284":
        raise ValueError(module)
    if len(parts) == 1:
        return LEAN / "Wow284.lean"
    return LEAN.joinpath(*parts).with_suffix(".lean")


def main() -> None:
    # Restrict the scan to this project's sources.  A configured checkout has
    # Mathlib under ``lean/.lake/packages``; recursively scanning all of
    # ``lean`` is both slow and outside this audit's trust boundary.
    lean_files = sorted((LEAN / "Wow284").rglob("*.lean"))
    for root_module in (LEAN / "Wow284.lean", LEAN / "Wow284Extended.lean"):
        if root_module.exists():
            lean_files.append(root_module)
    lean_files.sort()
    templates = sorted((LEAN / "Wow284").rglob("*.lean.template"))
    findings: dict[str, list[str]] = {key: [] for key in FORBIDDEN}
    missing_imports: list[str] = []
    template_imports: list[str] = []

    for path in lean_files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        for name, pattern in FORBIDDEN.items():
            if pattern.search(text):
                findings[name].append(rel)
        for module in IMPORT.findall(text):
            if module in BASE_IMPORTS or module == "Mathlib":
                continue
            if not module.startswith("Wow284"):
                continue
            expected = module_path(module)
            if not expected.exists():
                missing_imports.append(f"{rel}: {module}")
            if expected.with_name(expected.name + ".template").exists():
                template_imports.append(f"{rel}: {module}")

    template_sorries = []
    for path in templates:
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            if re.search(r"\bsorry\b", line):
                template_sorries.append(f"{path.relative_to(ROOT).as_posix()}:{lineno}")

    if any(findings.values()):
        raise SystemExit(f"forbidden imported-source tokens: {findings}")
    if missing_imports:
        raise SystemExit("missing imports:\n" + "\n".join(missing_imports))
    if template_imports:
        raise SystemExit("template imported:\n" + "\n".join(template_imports))

    report = [
        "LEAN STATIC AUDIT",
        "=================",
        f"Imported Lean files: {len(lean_files)}",
        f"Induced40 imported files: {len(list((LEAN / 'Wow284' / 'Induced40').glob('*.lean')))}",
        f"Induced38 imported files: {len(list((LEAN / 'Wow284' / 'Induced38').glob('*.lean')))}",
        f"Non-imported templates: {len(templates)}",
        f"Visible sorry occurrences in templates: {len(template_sorries)}",
        "Imported sorry occurrences: 0",
        "Imported admit occurrences: 0",
        "Imported native_decide occurrences: 0",
        "Imported bv_decide occurrences: 0",
        "Imported unsafe declaration occurrences: 0",
        "Imported axiom declaration occurrences: 0",
        "Missing extension imports: 0",
        "Imported templates: 0",
        "",
        "Template sorry locations:",
        *(f"  {item}" for item in template_sorries),
        "",
        "LIMITATION",
        "----------",
        "This is a textual/import-closure audit, not Lean kernel compilation.",
    ]
    OUTPUT.write_text("\n".join(report) + "\n", encoding="utf-8", newline="\n")
    print("Lean static audit: PASS")
    print(f"  imported .lean files={len(lean_files)}")
    print(f"  non-imported templates={len(templates)}")
    print(f"  template sorry occurrences={len(template_sorries)}")


if __name__ == "__main__":
    main()
