#!/usr/bin/env python3
"""Exact check of the two-vertex deletion dichotomy for R and X42.

For G = R (HS minus the Petersen set) and G = X42 (second subconstituent of
P_(0,0)), every pair {u, v} of distinct vertices is deleted and G - {u, v} is
decided exactly:
  * strict: Bareiss elimination of q D + p I (delta* = p/q), all leading
    principal minors positive;
  * not strict: an integer vector x with x^T (q D + p I) x < 0.
The script asserts that G - {u, v} is strict exactly when uv is an edge, with
minimum dual degree 17/3 in that case.  For one edge deletion of X42 it also
factors the distance characteristic polynomial and checks, by exact real-root
isolation, that its least root is -3 - sqrt 7 with multiplicity 4.

Writes data/hs_two_vertex_deletions/summary.json.
"""

from __future__ import annotations

import json
import os
import sys
from itertools import combinations

import numpy as np
import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import small_order_core as core  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def classify(name, g):
    n = g.shape[0]
    pairs = list(combinations(range(n), 2))
    out = {"edge": {"strict": 0, "not_strict": 0, "delta_star": set()},
           "non_edge": {"strict": 0, "not_strict": 0, "delta_star": set()}}
    for u, v in pairs:
        keep = [w for w in range(n) if w not in (u, v)]
        h = g[np.ix_(keep, keep)]
        phi, ds, lam, diam, cert, Q, p, q = core.batch_phi_certified(h[None])
        if cert[0]:
            strict = False
            dstar = "%d/%d" % (p[0], q[0])
        else:
            c = core.exact_certificate(h)
            strict = bool(c["strict"])
            dstar = c["delta_star"]
            assert strict, "uncertified non-strict pair needs a finer test"
        key = "edge" if g[u, v] else "non_edge"
        out[key]["strict" if strict else "not_strict"] += 1
        from fractions import Fraction
        out[key]["delta_star"].add(str(Fraction(dstar)))
    for key in out:
        out[key]["delta_star"] = sorted(out[key]["delta_star"])
    assert out["non_edge"]["strict"] == 0 and out["edge"]["not_strict"] == 0, (name, out)
    assert out["edge"]["delta_star"] == ["17/3"], (name, out)
    print(name, json.dumps(out), flush=True)
    return out


def x42_edge_charpoly(g):
    u, v = next((a, b) for a, b in combinations(range(g.shape[0]), 2) if g[a, b])
    keep = [w for w in range(g.shape[0]) if w not in (u, v)]
    d = sp.Matrix(core.all_distances(g[np.ix_(keep, keep)]).tolist())
    x = sp.symbols("x")
    poly = sp.Poly(d.charpoly(x).as_expr(), x)
    factors = sp.factor_list(poly.as_expr())[1]
    expected = {sp.Poly(x, x): 4, sp.Poly(x + 5, x): 11, sp.Poly(x**2 - 4*x + 2, x): 1,
                sp.Poly(x**2 + 6*x + 2, x): 4, sp.Poly(x**3 - 83*x**2 + 390*x - 414, x): 1,
                sp.Poly(x**3 + 2*x**2 - 20*x - 4, x): 4}
    got = {sp.Poly(f, x): m for f, m in factors}
    assert got == expected, got
    roots = poly.real_roots()
    least = min(roots)
    assert sp.simplify(least - (-3 - sp.sqrt(7))) == 0
    mult = sum(1 for r in roots if sp.simplify(r - least) == 0)
    assert mult == 4
    return {"deleted_edge_indices_in_X42": [int(u), int(v)],
            "charpoly_factors": {str(f.as_expr()): int(m) for f, m in got.items()},
            "least_root": "-3 - sqrt(7)", "least_root_multiplicity": int(mult)}


def main():
    r, _ = core.anstee_robertson_r()
    x42, _ = core.second_subconstituent_x42()
    summary = {"R": classify("R", r), "X42": classify("X42", x42),
               "X42_edge_deletion_spectrum": x42_edge_charpoly(x42)}
    out = os.path.join(ROOT, "data", "hs_two_vertex_deletions")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "summary.json"), "w", newline="\n") as fh:
        json.dump(summary, fh, indent=1)
        fh.write("\n")
    print("EDGE_DELETION_DICHOTOMY=PASS")


if __name__ == "__main__":
    main()
