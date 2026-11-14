# Three irregular order-40 strict counterexamples inside the Hoffman-Singleton graph.
# Vertices: surviving HS coordinate labels in increasing order (P_(i,j) -> 5i+j, Q_(k,l) -> 25+5k+l), relabelled 0..39.
X40: HS minus P_(0,0), P_(0,1), P_(0,2), P_(0,3), P_(0,4), Q_(0,0), Q_(1,0), Q_(2,0), Q_(3,0), Q_(4,0)
Y40: HS minus P_(0,0), P_(0,1), P_(0,2), P_(0,3), P_(0,4), P_(1,0), Q_(0,0), Q_(0,2), Q_(2,2), Q_(4,4)
Z40: HS minus P_(0,0), P_(0,1), P_(0,2), P_(0,3), P_(0,4), P_(1,0), Q_(0,0), Q_(0,2), Q_(1,1), Q_(1,4)
Lean: Wow284.Induced40X / Induced40Y / Induced40Z (scripts/generate_lean40_hs_extra.py).
Exact LDL^T pivots of D + delta* I: recertify_order40.json (scripts/recertify_order40.py).
