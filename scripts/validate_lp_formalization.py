#!/usr/bin/env python3
"""Deterministic static audit for the frozen WOW-284 Audit-02 Lean scope.

This script deliberately does not invoke Lean, Lake, Git, or a network
service.  It checks only the source-level invariants that can be established
without kernel replay:

* the exact LP module inventory and import order;
* forbidden proof escape hatches in the LP proof modules;
* the frozen release target and normalized theorem-signature SHA-256;
* the exact source SHA-256 of the semantic LP definitions;
* the normalized signature SHA-256 of the non-vacuous combined endpoint;
* the presence of named public audit endpoints; and
* exact synchronization of the committed ``#print axioms`` trust report.

The default ``check`` command is release-strict.  During implementation,
``check --allow-incomplete`` reports missing suffix modules and endpoints as
pending while still failing on source hygiene, import, DAG, or signature
drift.  A successful static audit is necessary but never sufficient: hosted
AXLE and warning-fatal Lean/Mathlib 4.31 replay remain required.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import hashlib
from pathlib import Path
import re
import sys
import tempfile
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
LEAN_DIR = ROOT / "lean" / "Wow284"
AUDIT_PATH = ROOT / "lean" / "Wow284LPAudit.lean"

FROZEN_DECLARATION = "Wow284.LP.twoSidedLP_optimal_and_rigid"
FROZEN_SOURCE = "lean/Wow284/LPCeiling.lean"
FROZEN_SIGNATURE_SHA256 = (
    "0f9e266f380fca6145d287318401b81b00eaa22e444dbc3fcf9ffc8e2fd6b6ce"
)
DEFINITIONS_SOURCE = "lean/Wow284/LPDefinitions.lean"
DEFINITIONS_SOURCE_SHA256 = (
    "a313b77c59ff59e9c0d4d8774b14724a6b603d0566f56716b75370d6d85c0158"
)
EXACT_FINAL_DECLARATION = (
    "Wow284.LP.twoSidedLP_exact_optimum_and_coefficient_rigidity"
)
EXACT_FINAL_SOURCE = "lean/Wow284/LPCeiling.lean"
EXACT_FINAL_SIGNATURE_SHA256 = (
    "d53bf2db2994ad9fc840cb81559b2d01a157fda856a7c2559f6c53cb1e400327"
)


@dataclass(frozen=True)
class ModuleSpec:
    filename: str
    imports: tuple[str, ...]

    @property
    def path(self) -> Path:
        return LEAN_DIR / self.filename

    @property
    def module(self) -> str:
        return f"Wow284.{Path(self.filename).stem}"


# This order is the intended Audit-02 topological order.  Import order inside
# a source file is also exact, notably Chebyshev-tail before finite-dual in
# LPWeakDuality.
MODULES: tuple[ModuleSpec, ...] = (
    ModuleSpec("LPDefinitions.lean", ("Mathlib",)),
    ModuleSpec("LPRecurrence.lean", ("Wow284.LPDefinitions",)),
    ModuleSpec("LPPrimal.lean", ("Wow284.LPRecurrence",)),
    ModuleSpec("LPDualFinite.lean", ("Wow284.LPPrimal",)),
    ModuleSpec("LPChebyshevTail.lean", ("Wow284.LPDualFinite",)),
    ModuleSpec(
        "LPWeakDuality.lean",
        ("Wow284.LPChebyshevTail", "Wow284.LPDualFinite"),
    ),
    ModuleSpec("LPRigidity.lean", ("Wow284.LPWeakDuality",)),
    ModuleSpec("LPCeiling.lean", ("Wow284.LPRigidity",)),
)
ROLE_ORDER = (
    "strict_slack",
    "witness",
    "attainment",
    "objective",
    "rigidity",
    "coefficient_rigidity",
    "positive_ray_rigidity",
    "final",
    "exact_final",
)
DEFAULT_ENDPOINTS = {
    "strict_slack": "Wow284.LP.all_slacks_positive",
    "witness": "Wow284.LP.extremalCoefficients_admissible",
    "attainment": "Wow284.LP.extremalCoefficients_attains",
    "objective": "Wow284.LP.twoSidedLP_objective_ge",
    "rigidity": "Wow284.LP.twoSidedLP_equality_iff",
    "coefficient_rigidity": "Wow284.LP.twoSidedLP_coefficient_equality_iff",
    "positive_ray_rigidity": (
        "Wow284.LP.twoSidedLP_positive_ray_equality_iff"
    ),
    "final": FROZEN_DECLARATION,
    "exact_final": EXACT_FINAL_DECLARATION,
}

IMPORT_RE = re.compile(
    r"(?m)^[ \t]*import[ \t]+([A-Za-z0-9_.'-]+)[ \t]*(?:--[^\n]*)?$"
)
DECLARATION_RE = re.compile(
    r"(?m)^[ \t]*(?P<prefix>(?:(?:noncomputable|private|protected|nonrec)"
    r"[ \t]+)*)(?P<kind>theorem|lemma|def|abbrev|opaque)"
    r"[ \t]+(?P<name>[A-Za-z_][A-Za-z0-9_']*)\b"
)
NAMESPACE_RE = re.compile(r"^namespace[ \t]+([A-Za-z0-9_.'-]+)[ \t]*$")
SECTION_RE = re.compile(
    r"^(?:(?:noncomputable|private)[ \t]+)?"
    r"section(?:[ \t]+[A-Za-z0-9_.'-]+)?[ \t]*$"
)
END_RE = re.compile(r"^end(?:[ \t]+[A-Za-z0-9_.'-]+)?[ \t]*$")

FORBIDDEN = {
    "sorry": re.compile(r"\bsorry\b"),
    "admit": re.compile(r"\badmit\b"),
    # LP production modules intentionally contain no `#print axioms`, so a
    # token-level rejection is both strict and robust to declaration modifiers
    # such as `protected`, `private`, or `local`.
    "axiom": re.compile(r"\baxioms?\b"),
    "unsafe": re.compile(r"\bunsafe\b"),
    "native_decide": re.compile(r"\bnative_decide\b"),
    "bv_decide": re.compile(r"\bbv_decide\b"),
    "implemented_by": re.compile(r"\bimplemented_by\b"),
}


class AuditError(RuntimeError):
    """A deterministic LP source-audit failure."""


@dataclass(frozen=True)
class Declaration:
    qualified_name: str
    source: Path
    private: bool


@dataclass(frozen=True)
class AuditResult:
    present_modules: tuple[ModuleSpec, ...]
    missing_modules: tuple[ModuleSpec, ...]
    declarations: dict[str, Declaration]
    endpoints: dict[str, str]
    pending_endpoints: tuple[str, ...]


def relative(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def normalize_signature(value: str) -> str:
    """Match the normalization used by the frozen formalization DAG."""

    return re.sub(r"\s+", " ", value).strip()


def signature_hash(value: str) -> str:
    return hashlib.sha256(normalize_signature(value).encode("utf-8")).hexdigest()


def source_hash(path: Path) -> str:
    """Return the exact SHA-256 of a frozen Lean source file."""

    return hashlib.sha256(path.read_bytes()).hexdigest()


def enclosing_namespace(text: str, position: int) -> str:
    """Recover the namespace at ``position`` for the simple project style."""

    blocks: list[list[str]] = []
    for raw_line in text[:position].splitlines():
        line = raw_line.split("--", 1)[0].strip()
        namespace_match = NAMESPACE_RE.fullmatch(line)
        if namespace_match:
            blocks.append(namespace_match.group(1).split("."))
        elif SECTION_RE.fullmatch(line):
            blocks.append([])
        elif END_RE.fullmatch(line) and blocks:
            blocks.pop()
    return ".".join(part for block in blocks for part in block)


def extract_signature(path: Path, declaration: str) -> str:
    """Extract a theorem header through the token immediately before ``:=``."""

    if not path.is_file():
        raise AuditError(f"missing frozen target source: {relative(path)}")
    text = path.read_text(encoding="utf-8")
    code = strip_comments_and_strings(text)
    local_name = declaration.rsplit(".", 1)[-1]
    candidates = [
        match
        for match in DECLARATION_RE.finditer(code)
        if match.group("name") == local_name and match.group("kind") == "theorem"
    ]
    for match in candidates:
        namespace = enclosing_namespace(code, match.start())
        qualified = f"{namespace}.{local_name}" if namespace else local_name
        if qualified != declaration:
            continue
        body_start = code.find(":=", match.end())
        if body_start < 0:
            raise AuditError(
                f"{relative(path)}: {declaration} has no ':=' after its header"
            )
        return code[match.start() : body_start].strip()
    raise AuditError(f"{relative(path)}: declaration not found: {declaration}")


def strip_comments_and_strings(text: str) -> str:
    """Erase Lean comments and strings while retaining line/column positions."""

    result: list[str] = []
    i = 0
    block_depth = 0
    in_string = False
    escaped = False
    while i < len(text):
        pair = text[i : i + 2]
        char = text[i]

        if block_depth:
            if pair == "/-":
                result.extend((" ", " "))
                block_depth += 1
                i += 2
            elif pair == "-/":
                result.extend((" ", " "))
                block_depth -= 1
                i += 2
            else:
                result.append("\n" if char == "\n" else " ")
                i += 1
            continue

        if in_string:
            result.append("\n" if char == "\n" else " ")
            if escaped:
                escaped = False
            elif char == "\\":
                escaped = True
            elif char == '"':
                in_string = False
            i += 1
            continue

        if pair == "/-":
            result.extend((" ", " "))
            block_depth = 1
            i += 2
        elif pair == "--":
            while i < len(text) and text[i] != "\n":
                result.append(" ")
                i += 1
        elif char == '"':
            result.append(" ")
            in_string = True
            i += 1
        else:
            result.append(char)
            i += 1

    if block_depth:
        raise AuditError("unterminated Lean block comment encountered during audit")
    if in_string:
        raise AuditError("unterminated Lean string encountered during audit")
    return "".join(result)


def line_number(text: str, position: int) -> int:
    return text.count("\n", 0, position) + 1


def scan_forbidden(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    code = strip_comments_and_strings(text)
    findings: list[str] = []
    for label, pattern in FORBIDDEN.items():
        for match in pattern.finditer(code):
            findings.append(f"{label} at {relative(path)}:{line_number(code, match.start())}")
    if findings:
        raise AuditError("forbidden Lean construct(s):\n  " + "\n  ".join(findings))


def imports_of(path: Path) -> tuple[str, ...]:
    text = path.read_text(encoding="utf-8")
    code = strip_comments_and_strings(text)
    return tuple(IMPORT_RE.findall(code))


def validate_module_inventory(allow_incomplete: bool) -> tuple[
    tuple[ModuleSpec, ...], tuple[ModuleSpec, ...]
]:
    expected_names = {spec.filename for spec in MODULES}
    actual_names = {
        path.name
        for path in LEAN_DIR.glob("LP*.lean")
        if path.is_file()
    }
    unexpected = sorted(actual_names - expected_names)
    if unexpected:
        raise AuditError(f"unexpected LP proof module(s): {', '.join(unexpected)}")

    present = tuple(spec for spec in MODULES if spec.path.is_file())
    missing = tuple(spec for spec in MODULES if not spec.path.is_file())
    if missing and not allow_incomplete:
        raise AuditError(
            "missing required LP proof module(s): "
            + ", ".join(spec.filename for spec in missing)
        )
    module_index = {spec.module: index for index, spec in enumerate(MODULES)}
    present_modules = {spec.module for spec in present}
    for spec in present:
        actual_imports = imports_of(spec.path)
        if actual_imports != spec.imports:
            raise AuditError(
                f"{relative(spec.path)}: import order drift; "
                f"expected {spec.imports}, got {actual_imports}"
            )
        for imported in actual_imports:
            if imported not in module_index:
                continue
            if module_index[imported] >= module_index[spec.module]:
                raise AuditError(
                    f"{relative(spec.path)}: non-topological import {imported}"
                )
            if imported not in present_modules:
                raise AuditError(
                    f"{relative(spec.path)}: imports missing local module {imported}"
                )
        scan_forbidden(spec.path)

    return present, missing


def validate_frozen_targets() -> None:
    target_path = ROOT / FROZEN_SOURCE
    target_signature = extract_signature(target_path, FROZEN_DECLARATION)
    actual_hash = signature_hash(target_signature)
    if actual_hash != FROZEN_SIGNATURE_SHA256:
        raise AuditError(
            f"{relative(target_path)}: frozen signature hash drift; "
            f"expected {FROZEN_SIGNATURE_SHA256}, got {actual_hash}"
        )

    definitions_path = ROOT / DEFINITIONS_SOURCE
    if not definitions_path.is_file():
        raise AuditError(
            f"missing frozen semantic definitions: {DEFINITIONS_SOURCE}"
        )
    actual_definitions_hash = source_hash(definitions_path)
    if actual_definitions_hash != DEFINITIONS_SOURCE_SHA256:
        raise AuditError(
            f"{relative(definitions_path)}: frozen semantic-source hash drift; "
            f"expected {DEFINITIONS_SOURCE_SHA256}, "
            f"got {actual_definitions_hash}"
        )

    exact_final_path = ROOT / EXACT_FINAL_SOURCE
    exact_final_signature = extract_signature(
        exact_final_path, EXACT_FINAL_DECLARATION
    )
    actual_exact_final_hash = signature_hash(exact_final_signature)
    if actual_exact_final_hash != EXACT_FINAL_SIGNATURE_SHA256:
        raise AuditError(
            f"{relative(exact_final_path)}: exact-final signature hash drift; "
            f"expected {EXACT_FINAL_SIGNATURE_SHA256}, "
            f"got {actual_exact_final_hash}"
        )


def collect_declarations(paths: Iterable[Path]) -> dict[str, Declaration]:
    declarations: dict[str, Declaration] = {}
    for path in paths:
        text = path.read_text(encoding="utf-8")
        code = strip_comments_and_strings(text)
        for match in DECLARATION_RE.finditer(code):
            namespace = enclosing_namespace(code, match.start())
            local_name = match.group("name")
            qualified = f"{namespace}.{local_name}" if namespace else local_name
            declaration = Declaration(
                qualified_name=qualified,
                source=path,
                private="private" in match.group("prefix").split(),
            )
            if qualified in declarations:
                previous = declarations[qualified]
                raise AuditError(
                    f"duplicate declaration {qualified}: "
                    f"{relative(previous.source)} and {relative(path)}"
                )
            declarations[qualified] = declaration
    return declarations


def parse_endpoint_overrides(values: Sequence[str]) -> dict[str, str]:
    endpoints = dict(DEFAULT_ENDPOINTS)
    for value in values:
        if "=" not in value:
            raise AuditError(
                f"endpoint override must have ROLE=QUALIFIED_NAME form: {value!r}"
            )
        role, name = value.split("=", 1)
        if role not in ROLE_ORDER:
            raise AuditError(
                f"unknown endpoint role {role!r}; expected one of {ROLE_ORDER}"
            )
        if not re.fullmatch(
            r"[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)+",
            name,
        ):
            raise AuditError(f"invalid qualified Lean declaration name: {name!r}")
        endpoints[role] = name
    if endpoints["final"] != FROZEN_DECLARATION:
        raise AuditError(
            "the final endpoint is frozen and cannot be overridden: "
            f"{FROZEN_DECLARATION}"
        )
    if endpoints["exact_final"] != EXACT_FINAL_DECLARATION:
        raise AuditError(
            "the exact-final endpoint is frozen and cannot be overridden: "
            f"{EXACT_FINAL_DECLARATION}"
        )
    return endpoints


def validate_endpoints(
    declarations: dict[str, Declaration],
    endpoints: dict[str, str],
    allow_incomplete: bool,
) -> tuple[str, ...]:
    pending: list[str] = []
    for role in ROLE_ORDER:
        name = endpoints[role]
        declaration = declarations.get(name)
        if declaration is None:
            pending.append(role)
            continue
        if declaration.private:
            raise AuditError(
                f"{role} endpoint is private and cannot be audited: {name}"
            )
    if pending and not allow_incomplete:
        details = ", ".join(f"{role}={endpoints[role]}" for role in pending)
        raise AuditError(f"missing public LP audit endpoint(s): {details}")
    return tuple(pending)


def validate_committed_axiom_report(
    declarations: dict[str, Declaration],
    endpoints: dict[str, str],
    allow_incomplete: bool,
) -> None:
    """Require the committed trust report to probe every public endpoint."""

    if not AUDIT_PATH.is_file():
        if allow_incomplete:
            return
        raise AuditError(f"missing LP axiom report: {relative(AUDIT_PATH)}")

    text = AUDIT_PATH.read_text(encoding="utf-8")
    code = strip_comments_and_strings(text)
    actual_imports = tuple(IMPORT_RE.findall(code))
    expected_imports = ("Wow284.LPCeiling",)
    if actual_imports != expected_imports:
        raise AuditError(
            f"{relative(AUDIT_PATH)}: import drift; "
            f"expected {expected_imports}, got {actual_imports}"
        )

    probe_re = re.compile(
        r"(?m)^[ \t]*#print[ \t]+axioms[ \t]+"
        r"([A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']*)+)"
        r"[ \t]*$"
    )
    actual_probes = tuple(probe_re.findall(code))
    expected_probes = tuple(
        endpoints[role]
        for role in ROLE_ORDER
        if endpoints[role] in declarations
    )
    if actual_probes != expected_probes:
        raise AuditError(
            f"{relative(AUDIT_PATH)}: axiom-probe drift; "
            f"expected {expected_probes}, got {actual_probes}"
        )


def run_audit(
    *,
    allow_incomplete: bool,
    endpoint_overrides: Sequence[str],
) -> AuditResult:
    endpoints = parse_endpoint_overrides(endpoint_overrides)
    present, missing = validate_module_inventory(allow_incomplete)
    validate_frozen_targets()
    declarations = collect_declarations(spec.path for spec in present)
    pending = validate_endpoints(declarations, endpoints, allow_incomplete)
    validate_committed_axiom_report(
        declarations, endpoints, allow_incomplete
    )
    return AuditResult(
        present_modules=present,
        missing_modules=missing,
        declarations=declarations,
        endpoints=endpoints,
        pending_endpoints=pending,
    )


def render_axiom_probes(result: AuditResult) -> str:
    found = {
        role: result.declarations.get(result.endpoints[role])
        for role in ROLE_ORDER
    }
    source_modules: list[str] = []
    for spec in MODULES:
        if any(
            declaration is not None and declaration.source == spec.path
            for declaration in found.values()
        ):
            source_modules.append(spec.module)
    if "Wow284.LPCeiling" in source_modules:
        imports = ["Wow284.LPCeiling"]
    else:
        imports = source_modules

    lines = [
        "/- Generated by scripts/validate_lp_formalization.py.",
        "Run only with hosted AXLE or warning-fatal Lean/Mathlib 4.31.",
        "Expected reported axioms are limited to propext, Classical.choice,",
        "and Quot.sound.  This source-level generator does not inspect output. -/",
        *[f"import {module}" for module in imports],
        "",
    ]
    for role in ROLE_ORDER:
        name = result.endpoints[role]
        if found[role] is None:
            lines.append(f"-- PENDING {role}: {name}")
        else:
            lines.append(f"#print axioms {name}")
    return "\n".join(lines) + "\n"


def self_test() -> None:
    expected = "a b c"
    if normalize_signature("  a\n\tb   c ") != expected:
        raise AuditError("self-test: signature normalization failed")
    if signature_hash("  a\n\tb   c ") != hashlib.sha256(
        expected.encode("utf-8")
    ).hexdigest():
        raise AuditError("self-test: signature hashing failed")

    sample = """import Mathlib
/- sorry /- axiom hidden -/ still hidden -/
namespace Wow284.LP
noncomputable section
theorem clean : True := by
  -- admit
  exact True.intro
end
end Wow284.LP
"""
    stripped = strip_comments_and_strings(sample)
    if any(pattern.search(stripped) for pattern in FORBIDDEN.values()):
        raise AuditError("self-test: comment stripping produced a false finding")
    if tuple(IMPORT_RE.findall(stripped)) != ("Mathlib",):
        raise AuditError("self-test: import parsing failed")

    with tempfile.TemporaryDirectory(prefix="wow284-lp-audit-") as directory:
        cases = {
            "sorry": "theorem bad : True := by\n  sorry\n",
            "protected axiom": "protected axiom hidden : True\n",
            "modifier-stacked axiom": "private protected axiom hidden : True\n",
        }
        for label, source in cases.items():
            path = Path(directory) / f"Bad-{label.replace(' ', '-')}.lean"
            path.write_text(source, encoding="utf-8")
            try:
                scan_forbidden(path)
            except AuditError as exc:
                expected_label = "sorry" if label == "sorry" else "axiom"
                if expected_label not in str(exc):
                    raise AuditError(
                        "self-test: forbidden-token scan reported the wrong "
                        f"finding for {label}"
                    ) from exc
            else:
                raise AuditError(
                    f"self-test: forbidden-token scan missed {label}"
                )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("check", "probes"):
        subparser = subparsers.add_parser(command)
        subparser.add_argument(
            "--allow-incomplete",
            action="store_true",
            help="report missing modules/endpoints as pending",
        )
        subparser.add_argument(
            "--endpoint",
            action="append",
            default=[],
            metavar="ROLE=QUALIFIED_NAME",
            help=(
                "override a non-frozen endpoint name; roles are "
                + ", ".join(ROLE_ORDER)
            ),
        )
    subparsers.add_parser("self-test")
    return parser


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
    args = build_parser().parse_args()
    try:
        if args.command == "self-test":
            self_test()
            print("LP static-audit self-test: PASS")
            return 0

        result = run_audit(
            allow_incomplete=args.allow_incomplete,
            endpoint_overrides=args.endpoint,
        )
        if args.command == "probes":
            sys.stdout.write(render_axiom_probes(result))
            return 0

        print("LP static audit: PASS")
        print(
            "  modules present: "
            + ", ".join(spec.filename for spec in result.present_modules)
        )
        if result.missing_modules:
            print(
                "  modules pending: "
                + ", ".join(spec.filename for spec in result.missing_modules)
            )
        else:
            print("  modules pending: none")
        print(f"  frozen signature: {FROZEN_SIGNATURE_SHA256}")
        print(
            "  frozen LPDefinitions source: "
            f"{DEFINITIONS_SOURCE_SHA256}"
        )
        print(
            "  frozen exact-final signature: "
            f"{EXACT_FINAL_SIGNATURE_SHA256}"
        )
        if result.pending_endpoints:
            print(
                "  endpoints pending: "
                + ", ".join(
                    f"{role}={result.endpoints[role]}"
                    for role in result.pending_endpoints
                )
            )
        else:
            print("  endpoints pending: none")
        print(
            "  limitation: static source audit only; Lean 4.31 kernel replay "
            "and axiom-output inspection remain required"
        )
        return 0
    except (AuditError, OSError, ValueError) as exc:
        print(f"LP static audit: FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
