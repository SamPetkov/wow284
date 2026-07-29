#!/usr/bin/env python3
"""Materialize the exact Proof Audit 14C sources from a compressed payload."""
from __future__ import annotations

import base64
import io
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parents[1]
CHUNKS = ROOT / "scripts" / ".audit14c-bootstrap"
EXPECTED = {
    "scripts/verify_order50_lift_exclusion.py",
    "scripts/verify_proof_audit_14c_order50_lifts.py",
    "scripts/order50_lift_independent.cpp",
    "scripts/order50_completion_filter.cpp",
    "research-notes/ORDER50_LIFT_EXCLUSION.md",
    "research-notes/PROOF_AUDIT_14C_ORDER50_LIFTS.md",
}


def safe_name(name: str) -> Path:
    path = Path(name)
    if path.is_absolute() or ".." in path.parts:
        raise AssertionError(f"unsafe payload path: {name}")
    while path.parts and path.parts[0] == ".":
        path = Path(*path.parts[1:])
    return path


def main() -> None:
    chunks = sorted(CHUNKS.glob("payload.*"))
    if not chunks:
        raise AssertionError("missing Audit 14C payload chunks")
    encoded = "".join(path.read_text(encoding="ascii").strip() for path in chunks)
    compressed = base64.b64decode(encoded, validate=True)

    written: set[str] = set()
    with tarfile.open(fileobj=io.BytesIO(compressed), mode="r:gz") as archive:
        for member in archive.getmembers():
            if not member.isfile():
                continue
            relative = safe_name(member.name)
            name = relative.as_posix()
            if name not in EXPECTED:
                raise AssertionError(f"unexpected Audit 14C payload member: {name}")
            source = archive.extractfile(member)
            if source is None:
                raise AssertionError(f"cannot read payload member: {name}")
            data = source.read()
            if any(byte < 32 and byte not in {9, 10} for byte in data):
                raise AssertionError(f"control byte in payload member: {name}")
            destination = ROOT / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
            if destination.suffix == ".py":
                destination.chmod(0o755)
            written.add(name)

    if written != EXPECTED:
        raise AssertionError(
            f"Audit 14C payload mismatch: missing={sorted(EXPECTED-written)}, "
            f"extra={sorted(written-EXPECTED)}"
        )
    print("Proof Audit 14C materialization: PASS")
    for name in sorted(written):
        print(name)


if __name__ == "__main__":
    main()
