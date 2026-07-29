# Proof Audit 14B: degree-six order-50 exclusion

**Audited result:** `ORDER50_COMPONENT_DESIGN_EXCLUSION.md`  
**Audit mode:** independent theorem-by-theorem replay, with the signed-root input,
component partition, incidence design and block trace identity checked as
separate gates.  
**Provisional verdict:** `pass`, conditional only on the cited
Cameron--Goethals--Seidel--Shult signed root-system theorem.

## 1. Normalized theorem

Let \(G\) be a connected 6-regular graph of order \(50\), girth at least five
and diameter three.  If every nonprincipal adjacency eigenvalue lies in

\[
 (-1-\sqrt{10},-1+\sqrt{10}),
\]

then no such graph exists.  Consequently every connected 6-regular strict
WOW-284 counterexample has

\[
 \boxed{|V(G)|\le49}.
\]

## 2. Hypothesis ledger

| Hypothesis | Use |
|---|---|
| 6-regular | polynomial constants, principal eigenspace, row sums |
| order 50 | signed degree two, trace congruence, component sizes |
| girth at least five | nonbacktracking traces; no triangles or 4-cycles in the incidence reduction |
| diameter three | shifted WOW spectral equivalence |
| open shifted window | positive semidefinite slack, exact kernel, exclusion of the cubic conjugate |
| connected | simple principal adjacency eigenspace and the WOW distance setting |

No exhaustive graph generation or floating-point eigenvalue ordering is used.

## 3. Signed trace parity

The independent recurrence solve gives

\[
\begin{aligned}
 (g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
 &+352F_5+78F_6+12F_7+F_8.
\end{aligned}
\]

For lengths below ten, a closed nonbacktracking walk in a girth-five graph is a
directed simple cycle: a repeated vertex would split the walk into two closed
nonbacktracking walks, each of length at least five.  Hence

\[
 \operatorname{tr}F_i(A)=2iN_i\quad(5\le i\le8).
\]

After removing the principal adjacency contribution and restoring the
principal signed eigenvalue two,

\[
 \operatorname{tr}S^2
 =8(440N_5+117N_6+21N_7+2N_8-604100).
\]

If \(N_-\) is the number of negative signed edges, signed regularity gives

\[
 \operatorname{tr}S^2=100+4N_-.
\]

Thus \(N_-\) is odd.  Every coefficient and principal correction is checked
independently; no cycle count is estimated numerically.

## 4. Connected signed complement

The previous order-50 moment theorem gives

\[
 \operatorname{rank}(S+2I)\ge30.
\]

If \(S\) were connected, the classical signed root-system theorem would
represent it in \(D_m\) or \(E_8\).  Rank excludes \(E_8\), leaving roots
\(\pm e_i\pm e_j\).

For \(B^{\mathsf T}B=S+2I\) and \(s=B\mathbf1\), one has

\[
 b_e\cdot s=4,
 \qquad
 \|s\|^2=200.
\]

After coordinate switching, the support levels form one of three connected
families.

1. Levels divisible by four are excluded by \(16\nmid200\).
2. Levels congruent to two modulo four reduce to the three exact multiplicity
   pairs
   \[
   (n_2,n_6)=(50,0),(41,1),(32,2).
   \]
   In every case the negative-edge parity is \(6n_6\equiv0\pmod2\), contrary
   to Section 3.
3. For odd levels, flow balance on the two chains gives
   \[
   \frac{200-3v}{32}
   =\sum_{t\ge1}\binom{t+1}{2}(A_t+B_t).
   \]
   Hence \(v\equiv24\pmod{32}\), impossible for \(30\le v\le51\).

This proves that \(S\) is disconnected.  The audit checks that connectedness of
the root support follows from connectedness of the represented signed graph and
that \(v\le51\) follows from a connected support graph with fifty roots.

## 5. Component eigenspace and equitable partition

Every component indicator belongs to \(E_2(S)\).  On \(\mathbf1^\perp\),

\[
 S=-2I-g_6(A).
\]

The cubic factor of \(g_6(x)+4\) is irreducible and has one root above
\(-1+\sqrt{10}\).  Since \(A\) is integral, that factor cannot occur partially:
if one conjugate occurred, the full irreducible factor would divide the
characteristic polynomial.  Thus \(A=-4I\) on
\(E_2(S)\cap\mathbf1^\perp\).

The component partition is therefore equitable with

\[
 q_{ij}=n_j/5\quad(i\ne j),
 \qquad
 q_{ii}=n_i/5-4.
\]

Nonnegative integrality leaves only \(20+30\) or \(25+25\).  The latter would
induce a 1-regular graph on 25 vertices and is impossible.  In the surviving
split, the 20-part is independent, the 30-part is 2-regular, and the cross
incidence matrix has row sum six and column sum four.

## 6. Incidence design

No two incidence rows meet twice.  Counting the six row pairs inside every
column gives 180 intersecting pairs among the 190 pairs of rows.  More locally,
each row meets exactly eighteen distinct rows and is disjoint from exactly one.
The disjointness relation is therefore a perfect matching \(P\), and

\[
 CC^{\mathsf T}=5I+J-P.
\]

The eigenvalues \(24,6,4\) with multiplicities \(1,10,9\) and the trace data

\[
 \operatorname{tr}B=120,
 \qquad
 \operatorname{tr}B^2=1080,
 \qquad B=C^{\mathsf T}C
\]

are recomputed directly.  Triangle- and 4-cycle-freeness give

\[
 \operatorname{tr}(BR)=0,
 \qquad
 \operatorname{tr}(BR^2)=240.
\]

## 7. Off-block polynomial identity

Direct block multiplication gives

\[
 (g_6(A))_{XY}
 =C(BR+RB+R^3+6B+6R^2+3R-28I).
\]

Since the corresponding signed block vanishes, multiplication by
\(C^{\mathsf T}\) and taking traces yields

\[
 2\operatorname{tr}(RB^2)+\operatorname{tr}(BR^3)=1440.
\]

For an edge \(yz\) of the 2-regular part, let \(t_{yz}\le4\) count perfect
matching pairs crossing between its two four-subsets in the 20-part.  Then

\[
 \operatorname{tr}(RB^2)=960-2T,
 \qquad T=\sum_{yz}t_{yz}\le120.
\]

Because \(B,R^3\) are entrywise nonnegative,

\[
 0\le\operatorname{tr}(BR^3)=4T-480.
\]

Thus \(T=120\), so every edge has \(t_{yz}=4\).  The incidence neighborhoods
therefore alternate under the perfect-matching involution.  After two edges of
a cycle, the original neighborhood returns unchanged, contradicting the
absence of a 4-cycle.

## 8. Claim boundary

The result excludes only the regular degree-six order-50 case.  It does not
claim that order 49 is attainable or impossible, does not classify irregular
counterexamples, and does not improve the known explicit order-40 regular
example.

The signed root-system theorem is external.  The trace parity, coordinate-level
exclusion, equitable partition, incidence design and block trace contradiction
are project-derived.

## 9. Independent executable replay

The scripts

```
scripts/verify_order50_component_design_exclusion.py
scripts/verify_proof_audit_14_order50_exclusion.py
```

independently check the recurrence expansion, parity, finite level arithmetic,
component sizes, incidence spectrum, symbolic block multiplication and final
trace squeeze.  Neither script attempts to replace the external root-system
classification theorem.
