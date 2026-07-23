#!/usr/bin/env python3
"""Exact isomorphism certificates for deletion classes of the 40-vertex graph.

The core verifier gives exact certificates for one one-vertex deletion (order
39) and one edge-end deletion (order 38).  This script proves that all forty
single deletions and all 120 edge deletions are isomorphic to those respective
representatives, by producing and directly checking explicit bijections.
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

from common_graphs import graph40, induced_indices  # noqa: E402


def nx_graph(graph: tuple[frozenset[int], ...]) -> nx.Graph:
    out = nx.Graph()
    out.add_nodes_from(range(len(graph)))
    out.add_edges_from((u, v) for u, row in enumerate(graph) for v in row if u < v)
    return out


def checked_isomorphism(source, target) -> dict[int, int]:
    matcher = nx.algorithms.isomorphism.GraphMatcher(nx_graph(source), nx_graph(target))
    if not matcher.is_isomorphic():
        raise AssertionError("graphs are not isomorphic")
    mapping = dict(matcher.mapping)
    if set(mapping) != set(range(len(source))) or set(mapping.values()) != set(range(len(target))):
        raise AssertionError("mapping is not a bijection")
    for u in range(len(source)):
        for v in range(len(source)):
            if (v in source[u]) != (mapping[v] in target[mapping[u]]):
                raise AssertionError((u, v))
    return mapping


def main() -> None:
    parent, _ = graph40()

    ref_single, _ = induced_indices(parent, {0})
    single_maps: dict[str, list[int]] = {}
    for deleted in range(40):
        candidate, _ = induced_indices(parent, {deleted})
        mapping = checked_isomorphism(candidate, ref_single)
        single_maps[str(deleted)] = [mapping[i] for i in range(39)]

    ref_neighbor = min(parent[0])
    ref_edge, _ = induced_indices(parent, {0, ref_neighbor})
    edges = [(u, v) for u, row in enumerate(parent) for v in row if u < v]
    if len(edges) != 120:
        raise AssertionError(len(edges))
    edge_maps: dict[str, list[int]] = {}
    for u, v in edges:
        candidate, _ = induced_indices(parent, {u, v})
        mapping = checked_isomorphism(candidate, ref_edge)
        edge_maps[f"{u},{v}"] = [mapping[i] for i in range(38)]

    certificate = {
        "single_deletion_reference": 0,
        "single_deletion_count": len(single_maps),
        "single_deletion_isomorphisms": single_maps,
        "edge_deletion_reference": [0, ref_neighbor],
        "edge_deletion_count": len(edge_maps),
        "edge_deletion_isomorphisms": edge_maps,
    }
    output = ROOT / "data" / "graph40_deletion_isomorphisms.json"
    output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("40-deletion isomorphism audit: PASS")
    print("  all 40 one-vertex deletions are isomorphic")
    print("  all 120 edge-end deletions are isomorphic")
    print(f"  certificate={output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
