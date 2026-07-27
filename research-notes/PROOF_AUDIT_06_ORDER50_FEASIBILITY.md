# Proof Audit 06: the degree-six order-50 feasibility system

**Audited results:** `ORDER50_LOCAL_FEASIBILITY.md` and
`ORDER50_R29_EXCLUSION.md`.

**Audit mode:** line-by-line, with the layer compression, local walk counts,
positive-semidefinite minors, global cycle identities, shifted moments, Schur
complements, and finite integer enumeration checked independently.

**Provisional verdict:** `pass_after_expository_correction`.

The necessary conditions and the count of 266 surviving coarse profiles are
correct.  Two presentation corrections are required:

1. the displayed distance-layer matrix is an average row quotient, not generally
   an equitable quotient; interlacing applies through its similar symmetric
   normalized compression;
2. the final theorem must incorporate the later `r=29` kernel exclusion rather
   than leave the stronger local table in a separate note.

No numerical bound or profile count changes.

## 1. Normalised theorem

Let \(G\) be a connected 6-regular graph of order 50, girth at least five, and
diameter three.  Assume \(G\) is a strict counterexample to WOW-284.  For an
edge \(e\), let \(\sigma_e\) denote the number of 5-cycles containing \(e\).
The audited edge-local theorem gives

\[
 \sigma_e\in\{12,13\}.
\]

Let \(H\) be the spanning subgraph whose edges have \(\sigma_e=13\), and write

\[
 m=|E(H)|.
\]

For a vertex \(v\), let \(\tau(v)\) be the number of 5-cycles through \(v\).
Then

\[
 \boxed{\tau(v)\in\{36,37,38\}},
 \qquad
 \boxed{d_H(v)=2\tau(v)-72\in\{0,2,4\}}.
\]

Consequently \(H\) is even, \(m\equiv0\pmod5\), and

\[
 \boxed{N_5=360+\frac m5}.
\]

For a two-edge path \(u-v-w\), define

\[
 \alpha_{uvw}=\#\{5\text{-cycles containing }u-v-w\},
\]

\[
 \beta_{uvw}=\#\{6\text{-cycles containing }u-v-w\},
 \qquad
 r_{uvw}=6\alpha_{uvw}+\beta_{uvw}.
\]

If the two incident edges are low-low, mixed, or high-high, respectively, then

\[
\begin{array}{c|c}
\text{type}&\text{allowed }r_{uvw}\\
\hline
\text{low--low}&30,31,32\\
\text{mixed}&30,31,32\\
\text{high--high}&30,31.
\end{array}
\]

Writing

\[
 S_2=\sum_v d_H(v)^2,
\]

the number \(N_6\) of 6-cycles satisfies

\[
 \boxed{N_6\ge1950-m},
\]

\[
 \boxed{N_6\le2200-\frac{5m}{6}-\frac{S_2}{12}},
\]

and independently

\[
 \boxed{
 N_6\ge\frac{43m^2-70200m+119632500}{58500}},
\]

\[
 \boxed{
 N_6\le\frac{4220000-2200m-7m^2}{2000}}.
\]

Exactly 266 triples \((n_0,n_2,n_4)\) survive these necessary conditions, where
\(n_i\) counts vertices of degree \(i\) in \(H\).  This is a feasibility
reduction, not an existence or nonexistence theorem.

## 2. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| 6-regular | layer sizes, walk moments, 150 edges, dual degree six |
| order 50 | distance-three layer size 13 and the centered Gram entries |
| girth at least five | unique two-step branches and walk-to-cycle bijections |
| diameter three | layer partition and shifted adjacency window |
| strict WOW violation | all nonprincipal shifted adjacency roots satisfy \(|y|<\sqrt{10}\) |
| audited edge-local theorem | every edge lies in 12 or 13 five-cycles |

## 3. Vertex layer compression

Fix \(v\).  The distance layers have sizes

\[
 1,\quad6,\quad30,\quad13.
\]

Every edge inside \(\Gamma_2(v)\) corresponds bijectively to a 5-cycle through
\(v\), so the average internal degree of that layer is \(\tau/15\).  The
average row quotient is

\[
 Q_\tau=
 \begin{pmatrix}
 0&6&0&0\\
 1&0&5&0\\
 0&1&\tau/15&5-\tau/15\\
 0&0&30(5-\tau/15)/13&6-30(5-\tau/15)/13
 \end{pmatrix}.
\]

This partition need not be equitable.  Let

\[
 N=\operatorname{diag}(1,6,30,13).
\]

Edge balance gives \(NQ_\tau=Q_\tau^{\mathsf T}N\), and

\[
 \widetilde Q_\tau=N^{1/2}Q_\tau N^{-1/2}
\]

is the symmetric compression of \(A\) to the normalized layer indicators.
Thus \(Q_\tau\) and \(\widetilde Q_\tau\) have the same eigenvalues, and these
interlace the adjacency eigenvalues of \(G\).

The characteristic polynomial is

\[
 \det(xI-Q_\tau)=(x-6)q_\tau(x),
\]

where

\[
 q_\tau(x)=
 \frac{-43\tau x^2-30\tau x+228\tau
       +195x^3+2250x^2+105x-11250}{195}.
\]

At the upper WOW boundary \(u=-1+\sqrt{10}\),

\[
 195q_\tau(u)=(-215+56\sqrt{10})\tau
              +7350-1860\sqrt{10}.
\]

The coefficient of \(\tau\) is negative, because
\(56^2\cdot10<215^2\).  At \(\tau=39\), the value is

\[
 9(-115+36\sqrt{10})<0.
\]

Also

\[
 195q_\tau(6)=1500(75-\tau)>0.
\]

The last inequality is strict because \(\tau=75\) would leave no edge from the
second to the nonempty third layer.  Hence \(\tau\ge39\) would produce a
nonprincipal compression eigenvalue in \((u,6)\), contradicting interlacing and
the strict spectral window.  Therefore \(\tau\le38\).

The number of edges from \(\Gamma_2(v)\) to \(\Gamma_3(v)\) is

\[
 30\left(5-\frac\tau{15}\right)=150-2\tau.
\]

It is at most \(13\cdot6=78\), so \(\tau\ge36\).  This proves the vertex range.

## 4. The high-edge graph

Each 5-cycle through \(v\) uses two edges incident with \(v\).  Therefore

\[
 \sum_{e\ni v}\sigma_e=2\tau(v).
\]

The six incident edges contribute a baseline of \(6\cdot12=72\), and every
high edge contributes one extra unit.  Thus

\[
 d_H(v)=2\tau(v)-72\in\{0,2,4\}.
\]

If \(n_2,n_4\) count vertices of high degree two and four, then

\[
 m=n_2+2n_4,
 \qquad
 S_2=4n_2+16n_4.
\]

Counting edge--5-cycle incidences gives

\[
 5N_5=12\cdot150+m,
\]

so \(N_5=360+m/5\) and \(m\equiv0\pmod5\).

## 5. Walk-to-cycle identities for a two-path

Let \(u-v-w\) be a two-edge path.  Because the girth is at least five, \(v\)
is the unique common neighbour of \(u,w\).

Every length-three walk from \(u\) to \(w\) is a simple path internally
disjoint from \(v\); together with \(u-v-w\), it forms a unique 5-cycle.
Thus

\[
 (A^3)_{uw}=\alpha_{uvw}.
\]

For the length-four count, use

\[
 (A^4)_{uw}=\sum_z(A^2)_{uz}(A^2)_{zw}.
\]

The terms \(z=u,w\) contribute \(12\).  The four neighbours of \(v\) other
than \(u,w\) are at distance two from both endpoints and contribute four more.
Every remaining common distance-two vertex corresponds bijectively to the
vertex opposite the path on a 6-cycle containing \(u-v-w\).  Hence

\[
 \boxed{(A^4)_{uw}=16+\beta_{uvw}}.
\]

## 6. The three-vertex Gram minor

Set

\[
 f_6(x)=(x+2)^2(x^2+2x-9),
\]

and

\[
 M=-f_6(A)+\frac{2496}{50}J.
\]

The strict shifted adjacency window makes \(M\succeq0\).  After multiplying the
principal submatrix on \(u,v,w\) by 25, its diagonal entries are 48.  An edge
entry is

\[
 -2\quad(\sigma=12),
 \qquad
 -27\quad(\sigma=13),
\]

and the endpoint entry is

\[
 773-25r_{uvw}.
\]

The \(2\)-by-\(2\) endpoint minor gives \(29\le r\le32\).  The three determinant
factors are

\[
\begin{array}{c|c}
\text{type}&\det\\
\hline
\text{low--low}&-5000(r-29)(6r-197)\\
\text{mixed}&-7500(4r^2-247r+3803)\\
\text{high--high}&-3750(r-29)(8r-253).
\end{array}
\]

Determinant nonnegativity yields the preliminary table.  The value \(r=29\)
is impossible even when the determinant vanishes.  At \(r=29\), the endpoint
Gram entry equals the diagonal, so

\[
 (e_u-e_w)^{\mathsf T}M(e_u-e_w)=0.
\]

Positive semidefiniteness gives \(M(e_u-e_w)=0\).  On
\(\mathbf1^\perp\), the kernel of \(M\) is precisely the adjacency
\(-2\)-eigenspace, because

\[
 -f_6(x)=(x+2)^2(10-(x+1)^2)
\]

and the second factor is strictly positive on the open window.  Hence

\[
 A(e_u-e_w)=-2(e_u-e_w).
\]

At coordinate \(u\), the left side is \(A_{uu}-A_{uw}=0\), while the right
side is \(-2\), a contradiction.  This proves the final local table.

## 7. Global local-count bounds

There are

\[
 50\binom62=750
\]

unoriented two-edge paths.  Each 5-cycle contributes five of them to the sum of
\(\alpha\), and each 6-cycle contributes six to the sum of \(\beta\).  Therefore

\[
 \sum r=30N_5+6N_6=10800+6m+6N_6.
\]

Since every path has \(r\ge30\),

\[
 \boxed{N_6\ge1950-m}.
\]

At a vertex of high degree \(d\), exactly \(\binom d2\) incident edge pairs are
high-high and have upper value 31; all other incident pairs have upper value
32.  Summing over vertices gives

\[
 \sum r\le24000-\sum_v\binom{d_H(v)}2
 =24000-\frac{S_2-2m}{2}.
\]

Substitution yields

\[
 \boxed{N_6\le2200-\frac{5m}{6}-\frac{S_2}{12}}.
\]

## 8. Exact shifted moments

Let \(\theta_1,\ldots,\theta_{49}\) be the nonprincipal adjacency eigenvalues
and \(y_i=\theta_i+1\).  The strict window gives \(|y_i|<\sqrt{10}\).

The girth-five trace identities are

\[
 \operatorname{tr}A=\operatorname{tr}A^3=0,
 \quad
 \operatorname{tr}A^2=300,
 \quad
 \operatorname{tr}A^4=3300.
\]

The fifth nonbacktracking polynomial has no lower odd trace contribution, so

\[
 \operatorname{tr}A^5=10N_5=3600+2m.
\]

For \(k=6\),

\[
 F_6(x)=x^6-26x^4+165x^2-150.
\]

Its trace counts the 12 orientations and starting points of each 6-cycle, so

\[
 \operatorname{tr}A^6=43800+12N_6.
\]

Expanding \(\operatorname{tr}(A+I)^j-7^j\) gives

\[
\begin{aligned}
 s_0&=49,&s_1&=43,&s_2&=301,&s_3&=607,\\
 s_4&=2749,&s_5&=6343+2m,&
 s_6&=1801+12m+12N_6.
\end{aligned}
\]

## 9. Moment and localizing Schur complements

The Hankel moment matrix

\[
 [s_{i+j}]_{i,j=0}^3
\]

is positive semidefinite.  Its leading \(3\)-by-\(3\) block has determinant
\(5{,}850{,}000>0\), so the Schur complement gives

\[
 \boxed{
 N_6\ge\frac{43m^2-70200m+119632500}{58500}}.
\]

Likewise,

\[
 [10s_{i+j}-s_{i+j+2}]_{i,j=0}^2\succeq0,
\]

because it is the Gram matrix weighted by \(10-y_i^2>0\).  Its leading
\(2\)-by-\(2\) block has determinant \(18{,}000>0\).  The Schur complement gives

\[
 \boxed{
 N_6\le\frac{4220000-2200m-7m^2}{2000}}.
\]

Both inequalities use exact rational arithmetic.

## 10. Finite profile enumeration

Let \(n_0,n_2,n_4\) be the numbers of vertices of degrees \(0,2,4\) in \(H\).
The verifier enumerates all nonnegative triples satisfying

\[
 n_0+n_2+n_4=50,
 \qquad
 m=n_2+2n_4\equiv0\pmod5,
\]

and intersects the two local and two moment bounds, with integer ceiling and
floor applied only after the exact rational bounds are combined.  Exactly 266
profiles survive, and every value

\[
 m=0,5,10,\ldots,100
\]

occurs among them.

This confirms that the current constraints are nontrivial pruning conditions
but do not eliminate order 50.

## 11. Independent verification

`scripts/verify_proof_audit_06_order50_feasibility.py` does not import either
original order-50 verifier.  It checks:

1. the row-quotient/symmetric-compression similarity;
2. the characteristic factor and exact boundary signs;
3. the vertex-cycle and high-edge identities;
4. both walk-to-cycle bijections on independent degree-six controls;
5. every Gram determinant and the `r=29` kernel contradiction;
6. both global cycle-count inequalities;
7. the nonbacktracking trace formulas and shifted moments;
8. both Schur-complement calculations;
9. the complete exact integer enumeration and its 266-profile output.

## 12. Verdict

The feasibility theorem passes.  The required corrections are organizational:
state explicitly that the layer matrix is similar to a symmetric compression,
and incorporate the `r=29` exclusion into the main theorem.  The result remains
a necessary-condition system, not an order-50 nonexistence theorem.
