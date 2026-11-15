Exhaustive search for strict WOW-284 counterexamples on at most 19 vertices.

geng_counts.json lists, for each order n, the nauty geng command, the number
of connected girth->=5 graphs generated, the number surviving the exact
dual-degree filter, and the exact decisions (no strict graph occurs).

Reproduction (nauty 2.8.9, geng):
  geng -c -t -f n > all_n.g6                       (n = 3..14)
  python scripts/small_order_certify_g6.py all_n.g6 --out cert_n.json --girth-sample 0
  geng -c -t -f -D<Dmax> n r/8 | small_order_g6filter > surv_n_r.g6   (n = 15..19, r = 0..7)
  python scripts/small_order_certify_g6.py surv_n_*.g6 --out cert_n.json --girth-sample 0
with Dmax = 4 for n = 15..18 and 5 for n = 19, and small_order_g6filter
compiled from scripts/small_order_g6filter.c.
