#!/usr/bin/env python3
"""Exhaustive LABELED vertex-deletion screen for a fixed parent graph.

For a parent graph P on N vertices and an integer k, every k-subset S of
V(P) is enumerated (no symmetry reduction), and Phi(P - S) is computed in
floating point.  Disconnected deletions are counted and skipped.  For every connected
deletion an EXACT integer certificate of non-strictness is attempted
(``small_order_core.batch_phi_certified``: integer vector x with
x^T (qD + pI) x < 0, delta* = p/q exact); every connected deletion without
such a certificate is decided exactly by Bareiss elimination
(``small_order_core.exact_certificate``).  Float Phi values are reported for
ranking only.

Output: one JSON summary per (parent, k) with the count of connected
deletions, the maximum float Phi, the 25 best deletions, and exact
certificates of every deletion with float Phi > -TOL.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
import time
from itertools import combinations, islice
from multiprocessing import Pool

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import small_order_core as core  # noqa: E402

PARENT = None


def parents():
    out = {}
    hs = core.hoffman_singleton()
    out["HS"] = (hs, list(range(50)))
    r, keep = core.anstee_robertson_r()
    out["R"] = (r, keep)
    x, keep = core.second_subconstituent_x42()
    out["X42"] = (x, keep)
    # HS minus two pentagons P_0, P_1 and HS minus two pentagrams Q_0, Q_1.
    for name, dele in [
        ("HSm2pent", [core.hs_index_p(i, j) for i in (0, 1) for j in range(5)]),
        ("HSm2gram", [core.hs_index_q(i, j) for i in (0, 1) for j in range(5)]),
    ]:
        keep = [v for v in range(50) if v not in set(dele)]
        out[name] = (core.induced(hs, keep), keep)
    # HS minus the closed neighbourhoods of an edge / a non-edge.
    v = core.hs_index_p(0, 0)
    w_adj = core.hs_index_p(0, 1)
    w_non = core.hs_index_p(0, 2)
    for name, w in [("HSmNN_edge", w_adj), ("HSmNN_nonedge", w_non)]:
        dele = {v, w} | set(np.flatnonzero(hs[v]).tolist()) | set(np.flatnonzero(hs[w]).tolist())
        keep = [u for u in range(50) if u not in dele]
        out[name] = (core.induced(hs, keep), keep)
    for name, g in core.cages55().items():
        out[name] = (g, list(range(g.shape[0])))
    rob = core.robertson_graph_by_search()
    out["robertson45"] = (rob, list(range(19)))
    return out


def init(name):
    global PARENT
    PARENT = parents()[name][0]


def work(combos):
    combos = np.asarray(combos, dtype=np.int64)
    a = PARENT
    n = a.shape[0]
    b, k = combos.shape
    mask = np.ones((b, n), dtype=bool)
    mask[np.arange(b)[:, None], combos] = False
    keep = np.nonzero(mask)[1].reshape(b, n - k)
    sub = a[keep[:, :, None], keep[:, None, :]]
    phi, ds, lam, diam, cert, Q, p, q = core.batch_phi_certified(sub)
    conn = np.isfinite(phi)
    order = np.argsort(-phi)[:25]
    top = [(float(phi[i]), float(ds[i]), float(lam[i]), float(diam[i]), combos[i].tolist()) for i in order if np.isfinite(phi[i])]
    # every connected deletion without an integer non-strictness certificate
    # is re-checked exactly (Bareiss) by the caller
    hits = [combos[i].tolist() for i in np.flatnonzero(conn & ~cert)]
    return int(b), int(conn.sum()), int(cert.sum()), top, hits


def chunks(n, k, size):
    it = combinations(range(n), k)
    while True:
        block = list(islice(it, size))
        if not block:
            return
        yield block


def ncr(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--parent", required=True)
    ap.add_argument("--k", type=int, nargs="+", required=True)
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--chunk", type=int, default=4000)
    ap.add_argument("--outdir", default="small_order_out")
    args = ap.parse_args()
    os.makedirs(args.outdir, exist_ok=True)
    allp = parents()
    a, labels = allp[args.parent]
    n = a.shape[0]
    for k in args.k:
        t0 = time.time()
        total = conn = ncert = 0
        top = []
        hits = []
        with Pool(args.workers, initializer=init, initargs=(args.parent,)) as pool:
            for b, c, ce, t, h in pool.imap_unordered(work, chunks(n, k, args.chunk)):
                total += b
                conn += c
                ncert += ce
                top = sorted(top + t, key=lambda z: -z[0])[:25]
                hits.extend(h)
        certs = []
        for comb in hits:
            keep = [v for v in range(n) if v not in set(comb)]
            cert = core.exact_certificate(core.induced(a, keep))
            cert["deleted_parent_indices"] = comb
            certs.append(cert)
        summary = {
            "parent": args.parent,
            "parent_order": n,
            "parent_vertex_labels_in_HS_or_self": labels,
            "k_deleted": k,
            "order": n - k,
            "subsets_enumerated": total,
            "expected_subsets": ncr(n, k),
            "connected": conn,
            "certified_nonstrict_integer_vector": ncert,
            "uncertified_connected": conn - ncert,
            "max_float_phi": top[0][0] if top else None,
            "top25": [
                {"phi": z[0], "delta_star": z[1], "lambda_min": z[2], "diameter": z[3], "deleted": z[4]}
                for z in top
            ],
            "uncertified_rechecked_exactly": len(hits),
            "exact_certificates": certs,
            "exact_strict_count": sum(1 for c in certs if c.get("strict")),
            "exact_nonstrict_by_bareiss": sum(1 for c in certs if not c.get("strict")),
            "all_connected_decided_exactly": ncert + len(certs) == conn,
            "seconds": time.time() - t0,
        }
        assert total == ncr(n, k)
        fn = os.path.join(args.outdir, "del_%s_k%d.json" % (args.parent, k))
        with open(fn, "w") as fh:
            json.dump(summary, fh, indent=1)
        print("%s k=%d order=%d subsets=%d connected=%d certified_nonstrict=%d uncertified=%d exact_strict=%d exact_nonstrict=%d decided=%s maxphi=%s %.1fs" % (
            args.parent, k, n - k, total, conn, ncert, len(hits), summary["exact_strict_count"],
            summary["exact_nonstrict_by_bareiss"], summary["all_connected_decided_exactly"],
            summary["max_float_phi"], summary["seconds"]), flush=True)


if __name__ == "__main__":
    main()
