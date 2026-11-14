Induced subgraphs HS - S of the coordinate Hoffman-Singleton graph, up to Aut(HS).

orbit_counts.json: for |S| = 0..14 (orders 50..36), the number of Aut(HS)-orbits
of deleted sets (orderly generation; equal to the Burnside count), the number with
HS - S connected, the number certified Phi < 0 by an integer vector, and the
numbers with Phi > 0 (strict) and Phi = 0.

strict_and_equality_orbits_orders_38_49.json: one representative per orbit that is
strict or has Phi = 0 (orders 38..49), with delta*, degrees, diameter, girth and
graph6. order43_equality.graph6 is the unique orbit with Phi = 0.

Reproduction:
  python scripts/small_order_hs_orbits.py --maxdepth 12 --rootdepth 7 --exact-max-order 49 --out depth12.json
  python scripts/small_order_hs_orbits.py --maxdepth 14 --rootdepth 8 --out depth14.json
(Linux; the workers share the automorphism table by fork.)

Direct check of the order-43 equality case (seconds, pure Python):
  python scripts/verify_order43_equality.py
It rebuilds E43 from the paper's definition and also reads
order43_equality.graph6. For both it checks the order, edges, degrees, girth,
diameter and delta* = 6, and certifies that D + 6I is positive semidefinite of
rank 41: a 41 x 41 principal submatrix has an exact LDL^T factorization with
positive pivots, and two explicit rational kernel vectors are checked entry by
entry.
