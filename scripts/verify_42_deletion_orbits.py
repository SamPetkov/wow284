#!/usr/bin/env python3
"""Exact isomorphism certificates for deletion classes of the 42-vertex graph.

The exact characteristic polynomial and positive-definiteness certificate are
computed for one single-vertex deletion and one edge-end deletion by
``verify_42_descendants.py``.  This script proves that every candidate of the
same deletion type is isomorphic to the corresponding representative by
finding and directly checking an adjacency-preserving bijection.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

import networkx as nx

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from common_graphs import graph42, induced_indices  # noqa: E402


def nx_graph(graph: tuple[frozenset[int], ...]) -> nx.Graph:
    out = nx.Graph()
    out.add_nodes_from(range(len(graph)))
    out.add_edges_from((u, v) for u, row in enumerate(graph) for v in row if u < v)
    return out


def checked_isomorphism(source, target) -> dict[int, int]:
    gs = nx_graph(source)
    gt = nx_graph(target)
    matcher = nx.algorithms.isomorphism.GraphMatcher(gs, gt)
    if not matcher.is_isomorphic():
        raise AssertionError("graphs are not isomorphic")
    mapping = dict(matcher.mapping)
    if set(mapping) != set(range(len(source))):
        raise AssertionError("mapping domain is not complete")
    if set(mapping.values()) != set(range(len(target))):
        raise AssertionError("mapping is not bijective")
    for u in range(len(source)):
        for v in range(len(source)):
            if (v in source[u]) != (mapping[v] in target[mapping[u]]):
                raise AssertionError((u, v, mapping[u], mapping[v]))
    return mapping


def main() -> None:
    parent, _ = graph42()

    ref_single, _ = induced_indices(parent, {0})
    single_maps: dict[str, list[int]] = {}
    for deleted in range(42):
        candidate, _ = induced_indices(parent, {deleted})
        mapping = checked_isomorphism(candidate, ref_single)
        single_maps[str(deleted)] = [mapping[i] for i in range(41)]

    ref_neighbor = min(parent[0])
    ref_edge, _ = induced_indices(parent, {0, ref_neighbor})
    edge_maps: dict[str, list[int]] = {}
    edges = [(u, v) for u, row in enumerate(parent) for v in row if u < v]
    if len(edges) != 126:
        raise AssertionError(len(edges))
    for u, v in edges:
        candidate, _ = induced_indices(parent, {u, v})
        mapping = checked_isomorphism(candidate, ref_edge)
        edge_maps[f"{u},{v}"] = [mapping[i] for i in range(40)]

    certificate = {
        "single_deletion_reference": 0,
        "single_deletion_count": len(single_maps),
        "single_deletion_isomorphisms": single_maps,
        "edge_deletion_reference": [0, ref_neighbor],
        "edge_deletion_count": len(edge_maps),
        "edge_deletion_isomorphisms": edge_maps,
    }
    output = ROOT / "data" / "graph42_deletion_isomorphisms.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("42-deletion isomorphism audit: PASS")
    print("  all 42 one-vertex deletions are isomorphic")
    print("  all 126 edge-end deletions are isomorphic")
    print(f"  certificate={output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
