#!/usr/bin/env python3
"""Validate the machine-readable literature matrix for the WOW-284 extensions."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MATRIX = ROOT / "research-notes" / "NEXT_DIRECTION_SOURCE_MATRIX.json"
IDENTIFIER_FIELDS = ("doi", "arxiv", "url")


def no_duplicate_object_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    """Build a JSON object while rejecting duplicate keys at every level."""

    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON object key: {key!r}")
        result[key] = value
    return result


def require_unique(values: list[str], *, label: str) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    if duplicates:
        joined = ", ".join(sorted(duplicates))
        raise ValueError(f"duplicate {label}: {joined}")


def validate(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    data = json.loads(text, object_pairs_hook=no_duplicate_object_keys)

    if not isinstance(data, dict):
        raise TypeError("matrix root must be a JSON object")

    topics = data.get("topics")
    sources = data.get("sources")
    if not isinstance(topics, list):
        raise TypeError("topics must be a JSON array")
    if not isinstance(sources, dict):
        raise TypeError("sources must be a JSON object")

    topic_ids: list[str] = []
    referenced_sources: set[str] = set()

    for index, topic in enumerate(topics):
        if not isinstance(topic, dict):
            raise TypeError(f"topics[{index}] must be a JSON object")

        topic_id = topic.get("id")
        if not isinstance(topic_id, str) or not topic_id.strip():
            raise ValueError(f"topics[{index}].id must be a nonempty string")
        topic_ids.append(topic_id)

        status = topic.get("status")
        if not isinstance(status, str) or not status.strip():
            raise ValueError(f"topic {topic_id!r} must have a nonempty status")

        closest_sources = topic.get("closest_sources")
        if not isinstance(closest_sources, list) or not closest_sources:
            raise ValueError(f"topic {topic_id!r} must reference at least one source")
        if not all(isinstance(source_id, str) and source_id for source_id in closest_sources):
            raise TypeError(f"topic {topic_id!r} has a non-string source reference")
        require_unique(closest_sources, label=f"source references in topic {topic_id!r}")
        referenced_sources.update(closest_sources)

        boundary = topic.get("boundary")
        if not isinstance(boundary, str) or not boundary.strip():
            raise ValueError(f"topic {topic_id!r} must have a nonempty boundary")

    require_unique(topic_ids, label="topic IDs")

    source_ids = set(sources)
    missing_sources = sorted(referenced_sources - source_ids)
    if missing_sources:
        raise ValueError(f"referenced source IDs are missing: {missing_sources}")

    for source_id, source in sources.items():
        if not isinstance(source_id, str) or not source_id:
            raise ValueError("every source ID must be a nonempty string")
        if not isinstance(source, dict):
            raise TypeError(f"source {source_id!r} must be a JSON object")

        citation = source.get("citation")
        if not isinstance(citation, str) or not citation.strip():
            raise ValueError(f"source {source_id!r} must have a nonempty citation")

        identifiers = [source.get(field) for field in IDENTIFIER_FIELDS]
        if not any(isinstance(value, str) and value.strip() for value in identifiers):
            fields = ", ".join(IDENTIFIER_FIELDS)
            raise ValueError(
                f"source {source_id!r} must provide at least one of: {fields}"
            )

    unreferenced_sources = sorted(source_ids - referenced_sources)
    if unreferenced_sources:
        raise ValueError(f"unreferenced source IDs: {unreferenced_sources}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=DEFAULT_MATRIX,
        help="path to NEXT_DIRECTION_SOURCE_MATRIX.json",
    )
    args = parser.parse_args()
    validate(args.path)
    print(
        "next-direction source matrix: PASS "
        f"({args.path.as_posix()})"
    )


if __name__ == "__main__":
    main()
