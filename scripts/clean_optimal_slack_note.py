#!/usr/bin/env python3
"""Repair escaped TeX control bytes and reject hidden source characters."""
from pathlib import Path

PATH = Path("research-notes/OPTIMAL_SLACK_GRAM_UNIFICATION.md")
data = PATH.read_bytes()

repairs = (
    (bytes([8]) + b"eta", bytes([92]) + b"beta", "beta"),
    (bytes([9]) + b"heta", bytes([92]) + b"theta", "theta"),
)
for needle, replacement, name in repairs:
    count = data.count(needle)
    if count not in {0, 1}:
        raise SystemExit(f"unexpected escaped-{name} count: {count}")
    if count == 1:
        data = data.replace(needle, replacement)

PATH.write_bytes(data)
for value in data:
    if value < 32 and value != 10:
        raise SystemExit(f"remaining control byte: {value}")
print("optimal-slack note control-byte cleanup: PASS")
