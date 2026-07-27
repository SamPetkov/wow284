#!/usr/bin/env python3
"""Materialize the preserved expanded manuscript from deterministic chunks."""
from __future__ import annotations

import base64
import gzip
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
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
        return "single monolithic UTF-8 TeX file"
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
        if (candidate / "main.tex").is_file():
            return candidate
    inventory = sorted(path.relative_to(extracted).as_posix() for path in extracted.rglob("*"))
    raise AssertionError("bootstrap contains no main.tex; inventory=" + repr(inventory[:80]))


def copy_text(path: Path, destination: Path) -> None:
    data = path.read_bytes()
    if any(byte < 32 and byte not in {9, 10} for byte in data):
        raise AssertionError(f"forbidden control byte in {path}")
    text = data.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(text, encoding="utf-8", newline="\n")


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
        copy_text(path, OUTPUT / relative)
        copied.append(relative.as_posix())
    if "main.tex" not in copied:
        raise AssertionError("bootstrap is missing main.tex")

    for name in ("references.bib", "main.bbl"):
        if name not in copied:
            fallback = ROOT / name
            if fallback.is_file():
                copy_text(fallback, OUTPUT / name)
                copied.append(name)
    (OUTPUT / ".materialized").write_text(
        "Generated deterministically from scripts/.v22-bootstrap/main.*\n",
        encoding="utf-8",
        newline="\n",
    )
    return copied


def run_revision(script_name: str) -> None:
    subprocess.run(
        [sys.executable, str(ROOT / "scripts" / script_name)],
        cwd=ROOT,
        check=True,
    )


def apply_audited_revisions() -> None:
    run_revision("revise_v22_manuscript.py")
    run_revision("revise_v22_second_pass.py")
    run_revision("revise_v22_third_pass.py")


def publish_materialized_source_in_ci() -> None:
    """Commit ``v22/`` only in the dedicated writable materialization workflow."""

    if os.environ.get("GITHUB_ACTIONS") != "true":
        return
    if os.environ.get("GITHUB_WORKFLOW") != "Materialize expanded v2.2 manuscript":
        return
    head_ref = os.environ.get("GITHUB_HEAD_REF")
    if not head_ref:
        return

    def run(*args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            args,
            cwd=ROOT,
            check=check,
            text=True,
            capture_output=True,
        )

    run("git", "config", "user.name", "github-actions[bot]")
    run(
        "git",
        "config",
        "user.email",
        "41898282+github-actions[bot]@users.noreply.github.com",
    )
    run("git", "add", "v22")
    staged = run("git", "diff", "--cached", "--quiet", check=False)
    if staged.returncode == 0:
        print("materialized v2.2 source already committed")
        return
    if staged.returncode != 1:
        raise RuntimeError(staged.stderr or "git diff --cached failed")
    run(
        "git",
        "commit",
        "-m",
        "Materialize fully audited v2.2 manuscript source [skip ci]",
    )
    run("git", "push", "origin", f"HEAD:{head_ref}")
    print(f"materialized v2.2 source pushed to {head_ref}")


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
    apply_audited_revisions()
    print("v2.2 manuscript materialization and three revision passes: PASS")
    print(f"source files copied: {len(copied)}")
    for item in copied:
        print(item)
    publish_materialized_source_in_ci()


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
