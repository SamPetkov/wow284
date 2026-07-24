#!/usr/bin/env python3
"""Fail closed if an asserted WOW-284 proof path uses floating-point spectra.

Exploratory scripts may use numerical eigenvalues, but the exact extension
workflow may not use floating conversion to select, order, or sign-test an
eigenvalue. The legacy extension module is imported only for exact helpers;
its historical floating reporter is classified as unreachable.
"""
from __future__ import annotations

import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "research-extensions.yml"
EXACT_ENTRYPOINTS = (
    "scripts/verify_research_extensions_exact.py",
    "scripts/verify_regular_low_degree.py",
    "scripts/verify_nonadjacent_punctured_moore.py",
    "scripts/verify_nonadjacent_direct_sum.py",
    "scripts/verify_prime_field_obstruction.py",
    "scripts/verify_equality_boundary.py",
    "scripts/verify_jorgensen_96.py",
    "scripts/verify_jorgensen96_provenance.py",
    "scripts/verify_degree_six_gate.py",
    "scripts/verify_spectral_moore_comparison.py",
)
LEGACY = ROOT / "scripts" / "verify_research_extensions.py"


def qualified_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        prefix = qualified_name(node.value)
        return f"{prefix}.{node.attr}" if prefix else node.attr
    return ""


def banned_calls(path: Path) -> list[dict[str, object]]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    parent_function: list[str] = []
    hits: list[dict[str, object]] = []

    class Visitor(ast.NodeVisitor):
        def visit_FunctionDef(self, node: ast.FunctionDef) -> None:
            parent_function.append(node.name)
            self.generic_visit(node)
            parent_function.pop()

        def visit_AsyncFunctionDef(self, node: ast.AsyncFunctionDef) -> None:
            parent_function.append(node.name)
            self.generic_visit(node)
            parent_function.pop()

        def record(self, node: ast.AST, kind: str) -> None:
            hits.append({
                "line": node.lineno,
                "function": parent_function[-1] if parent_function else "<module>",
                "kind": kind,
            })

        def visit_Import(self, node: ast.Import) -> None:
            for alias in node.names:
                if alias.name == "numpy" or alias.name.startswith("numpy."):
                    self.record(node, f"import {alias.name}")
            self.generic_visit(node)

        def visit_ImportFrom(self, node: ast.ImportFrom) -> None:
            if node.module == "numpy" or (
                node.module is not None and node.module.startswith("numpy.")
            ):
                self.record(node, f"from {node.module} import ...")
            self.generic_visit(node)

        def visit_Call(self, node: ast.Call) -> None:
            name = qualified_name(node.func)
            forbidden = (
                name in {"float", "complex", "sp.N", "sympy.N"}
                or name.endswith(".evalf")
                or name.startswith("np.linalg.")
                or name.startswith("numpy.linalg.")
            )
            if forbidden:
                self.record(node, name)
            self.generic_visit(node)

    Visitor().visit(tree)
    return hits


def main() -> None:
    exact_hits: dict[str, list[dict[str, object]]] = {}
    for relative in EXACT_ENTRYPOINTS:
        path = ROOT / relative
        if not path.is_file():
            raise AssertionError(f"missing exact proof entrypoint: {relative}")
        hits = banned_calls(path)
        if hits:
            exact_hits[relative] = hits
    if exact_hits:
        raise AssertionError(
            "floating-point operation in exact proof path:\n"
            + json.dumps(exact_hits, indent=2, sort_keys=True)
        )

    workflow = WORKFLOW.read_text(encoding="utf-8")
    for command in (
        "python scripts/verify_research_extensions_exact.py",
        "python scripts/audit_no_float_proof_paths.py",
    ):
        if command not in workflow:
            raise AssertionError(f"workflow missing exact command: {command}")
    if "run: python scripts/verify_research_extensions.py" in workflow:
        raise AssertionError("workflow still executes the legacy floating reporter")

    wrapper = (ROOT / "scripts" / "verify_research_extensions_exact.py").read_text(
        encoding="utf-8"
    )
    for reference in ("legacy.verify_operator_identity(", "legacy.main("):
        if reference in wrapper:
            raise AssertionError(f"exact wrapper reaches forbidden legacy path: {reference}")

    legacy_hits = banned_calls(LEGACY)
    expected_legacy = {
        ("verify_operator_identity", "float"),
        ("verify_operator_identity", "sp.N"),
    }
    observed_legacy = {
        (str(hit["function"]), str(hit["kind"])) for hit in legacy_hits
    }
    if observed_legacy != expected_legacy:
        raise AssertionError(
            "legacy floating classification changed; review required:\n"
            + json.dumps(legacy_hits, indent=2, sort_keys=True)
        )

    result = {
        "exact_entrypoints_scanned": list(EXACT_ENTRYPOINTS),
        "exact_banned_call_count": 0,
        "legacy_classified_unreachable_calls": legacy_hits,
        "workflow_uses_exact_wrapper": True,
    }
    print("no-floating-proof-path audit: PASS")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
