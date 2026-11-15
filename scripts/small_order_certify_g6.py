#!/usr/bin/env python3
"""Decide WOW-284 strictness exactly for every graph in graph6 files.

For each graph: girth >= 5 is re-checked; connected graphs get an exact
integer non-strictness certificate when possible
(small_order_core.batch_phi_certified); every connected graph without one is
decided by Bareiss elimination (small_order_core.exact_certificate).

Output: JSON with counts per order and the exact data of every graph that is
not certified non-strict by an integer vector.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import small_order_core as core  # noqa: E402


def decode_block(lines, n):
    """Vectorized graph6 decode for a list of order-n graph6 strings."""
    nb = (n * (n - 1) // 2 + 5) // 6
    raw = np.frombuffer("".join(l[1:1 + nb] for l in lines).encode("ascii"), dtype=np.uint8)
    raw = raw.reshape(len(lines), nb).astype(np.int16) - 63
    bits = ((raw[:, :, None] >> np.arange(5, -1, -1)) & 1).reshape(len(lines), nb * 6)
    iu = [(i, j) for j in range(1, n) for i in range(j)]
    a = np.zeros((len(lines), n, n), dtype=np.uint8)
    ii = np.array([p[0] for p in iu])
    jj = np.array([p[1] for p in iu])
    a[:, ii, jj] = bits[:, : len(iu)]
    a[:, jj, ii] = bits[:, : len(iu)]
    return a


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    ap.add_argument("--batch", type=int, default=20000)
    ap.add_argument("--girth-sample", type=int, default=200,
                    help="re-check girth >= 5 exactly on this many graphs per file (all if 0)")
    args = ap.parse_args()
    t0 = time.time()
    per = {}
    special = []
    for fn in args.files:
        with open(fn) as fh:
            lines = [l.strip() for l in fh if l.strip() and not l.startswith(">")]
        by_n = {}
        for l in lines:
            by_n.setdefault(ord(l[0]) - 63, []).append(l)
        for n, ls in sorted(by_n.items()):
            rec = per.setdefault(n, {"graphs": 0, "connected": 0, "certified_nonstrict": 0,
                                     "bareiss_strict": 0, "bareiss_nonstrict": 0, "max_float_phi": None,
                                     "girth_checked": 0})
            for start in range(0, len(ls), args.batch):
                block = ls[start:start + args.batch]
                a = decode_block(block, n)
                if args.girth_sample == 0 or rec["girth_checked"] < args.girth_sample:
                    for g in a[: (len(a) if args.girth_sample == 0 else args.girth_sample)]:
                        assert core.is_girth_at_least5(g)
                        rec["girth_checked"] += 1
                phi, ds, lam, diam, cert, Q, p, q = core.batch_phi_certified(a)
                conn = np.isfinite(phi)
                rec["graphs"] += len(block)
                rec["connected"] += int(conn.sum())
                rec["certified_nonstrict"] += int(cert.sum())
                if conn.any():
                    m = float(phi[conn].max())
                    rec["max_float_phi"] = m if rec["max_float_phi"] is None else max(rec["max_float_phi"], m)
                for i in np.flatnonzero(conn & ~cert).tolist():
                    c = core.exact_certificate(a[i])
                    c["float_phi"] = float(phi[i])
                    special.append(c)
                    if c["strict"]:
                        rec["bareiss_strict"] += 1
                    else:
                        rec["bareiss_nonstrict"] += 1
    for n, rec in per.items():
        rec["all_connected_decided"] = rec["certified_nonstrict"] + rec["bareiss_strict"] + rec["bareiss_nonstrict"] == rec["connected"]
    out = {"files": args.files, "seconds": time.time() - t0,
           "per_order": {str(k): v for k, v in sorted(per.items())},
           "not_certified_by_vector": special}
    with open(args.out, "w") as fh:
        json.dump(out, fh, indent=1)
    for n, rec in sorted(per.items()):
        print("n=%d graphs=%d connected=%d certified_nonstrict=%d bareiss_strict=%d bareiss_nonstrict=%d decided=%s maxphi=%s"
              % (n, rec["graphs"], rec["connected"], rec["certified_nonstrict"], rec["bareiss_strict"],
                 rec["bareiss_nonstrict"], rec["all_connected_decided"], rec["max_float_phi"]), flush=True)


if __name__ == "__main__":
    main()
