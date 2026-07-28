#!/usr/bin/env python3
"""Repair the one escaped beta control byte in the Audit 14 Markdown note."""
from pathlib import Path

PATH = Path("research-notes/OPTIMAL_SLACK_GRAM_UNIFICATION.md")
data = PATH.read_bytes()
needle = bytes([8]) + b"eta"
replacement = bytes([92]) + b"beta"
count = data.count(needle)
if count not in {0, 1}:
    raise SystemExit(f"unexpected escaped-beta count: {count}")
if count == 1:
    data = data.replace(needle, replacement)
    PATH.write_bytes(data)
for value in data:
    if value < 32 and value not in {9, 10}:
        raise SystemExit(f"remaining control byte: {value}")
print("optimal-slack note control-byte cleanup: PASS")
