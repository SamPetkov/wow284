#!/usr/bin/env python3
"""Materialize the reviewed v2.2 manuscript source from deterministic chunks."""
from __future__ import annotations

import base64
import gzip
import io
import json
from pathlib import Path
import shutil
import tarfile
import tempfile
import traceback
import zipfile

ROOT = Path(__file__).resolve().parents[1]
CHUNK_DIR = ROOT / "scripts" / ".v22-bootstrap"
OUTPUT = ROOT / "v22"
DIAGNOSTIC = ROOT / "v22-materialization-error.txt"
ALLOWED_SUFFIXES = {".tex", ".bib", ".bbl", ".md", ".json"}
ALLOWED_NAMES = {"latexmkrc", "Makefile"}


def safe_relative(path: Path) -> Path:
    if path.is_absolute() or ".." in path.parts:
        raise AssertionError(f"unsafe archive path: {path}")
    return path


def extract_payload(payload: bytes, target: Path) -> str:
    bio = io.BytesIO(payload)
    try:
        with tarfile.open(fileobj=bio, mode="r:*") as archive:
            members = archive.getmembers()
            for member in members:
                safe_relative(Path(member.name))
            archive.extractall(target, filter="data")
            return f"tar ({len(members)} members)"
    except tarfile.ReadError:
        pass

    bio.seek(0)
    if zipfile.is_zipfile(bio):
        with zipfile.ZipFile(bio) as archive:
            names = archive.namelist()
            for name in names:
                safe_relative(Path(name))
            archive.extractall(target)
            return f"zip ({len(names)} members)"

    try:
        text = payload.decode("utf-8")
    except UnicodeDecodeError as error:
        raise AssertionError(
            "gzip payload is neither tar, zip, nor UTF-8; "
            f"prefix={payload[:32].hex()} length={len(payload)}"
        ) from error
    try:
        mapping = json.loads(text)
    except json.JSONDecodeError:
        (target / "main.tex").write_text(text, encoding="utf-8", newline="\n")
        return "single UTF-8 file"
    if not isinstance(mapping, dict):
        raise AssertionError("JSON bootstrap must be a path-to-content object")
    for name, content in mapping.items():
        path = safe_relative(Path(str(name)))
        if not isinstance(content, str):
            raise AssertionError(f"non-text bootstrap value for {name}")
        destination = target / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8", newline="\n")
    return f"JSON map ({len(mapping)} files)"


def find_source_root(extracted: Path) -> Path:
    candidates = [extracted]
    candidates.extend(path for path in extracted.rglob("*") if path.is_dir())
    for candidate in candidates:
        if (candidate / "main.tex").is_file() and (candidate / "sections").is_dir():
            return candidate
    inventory = sorted(path.relative_to(extracted).as_posix() for path in extracted.rglob("*"))
    raise AssertionError(
        "bootstrap does not contain main.tex and sections/; inventory="
        + repr(inventory[:80])
    )


def copy_sources(source: Path) -> list[str]:
    if OUTPUT.exists():
        shutil.rmtree(OUTPUT)
    OUTPUT.mkdir(parents=True)
    copied: list[str] = []
    for path in sorted(source.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(source)
        if path.suffix not in ALLOWED_SUFFIXES and path.name not in ALLOWED_NAMES:
            continue
        destination = OUTPUT / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        data = path.read_bytes()
        if any(byte < 32 and byte not in {9, 10} for byte in data):
            raise AssertionError(f"forbidden control byte in {relative}")
        text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
        destination.write_text(text, encoding="utf-8", newline="\n")
        copied.append(relative.as_posix())
    required = {"main.tex", "references.bib", "main.bbl"}
    missing = required - set(copied)
    if missing:
        raise AssertionError(f"bootstrap is missing publication files: {sorted(missing)}")
    if not any(item.startswith("sections/") and item.endswith(".tex") for item in copied):
        raise AssertionError("bootstrap contains no modular section sources")
    (OUTPUT / ".materialized").write_text(
        "Generated deterministically from scripts/.v22-bootstrap/main.*\n",
        encoding="utf-8",
        newline="\n",
    )
    return copied


def materialize() -> None:
    chunks = sorted(CHUNK_DIR.glob("main.*"))
    if not chunks:
        raise AssertionError("no bootstrap chunks found")
    encoded = "".join(path.read_text(encoding="ascii").strip() for path in chunks)
    compressed = base64.b64decode(encoded, validate=True)
    payload = gzip.decompress(compressed)
    print(f"bootstrap chunks: {len(chunks)}")
    print(f"compressed bytes: {len(compressed)}")
    print(f"payload bytes: {len(payload)}")
    print(f"payload prefix: {payload[:48].hex()}")
    with tempfile.TemporaryDirectory(prefix="wow284-v22-") as directory:
        extracted = Path(directory)
        payload_type = extract_payload(payload, extracted)
        print(f"payload type: {payload_type}")
        source = find_source_root(extracted)
        print(f"source root: {source.relative_to(extracted)}")
        copied = copy_sources(source)
    print("v2.2 manuscript materialization: PASS")
    print(f"source files copied: {len(copied)}")
    for item in copied:
        print(item)


def main() -> None:
    try:
        materialize()
    except Exception:
        DIAGNOSTIC.write_text(traceback.format_exc(), encoding="utf-8", newline="\n")
        print(DIAGNOSTIC.read_text(encoding="utf-8"))
        raise
    else:
        DIAGNOSTIC.unlink(missing_ok=True)


if __name__ == "__main__":
    main()
