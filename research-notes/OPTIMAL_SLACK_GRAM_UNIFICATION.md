# Optimal-slack Gram hierarchy and near-ceiling reductions

**Status:** exact project derivation under Proof Audit 14; manuscript promotion
still requires independent proof and literature review.  
**Purpose:** place the LP ceiling, edge-cycle bounds, order-50 two-path
constraints, and new near-ceiling exclusions inside one positive-semidefinite
matrix formalism.

## 1. The optimal slack matrix

Let \(G\) be connected, \(k\)-regular, of girth at least five and diameter three,
with adjacency matrix \(A\), order \(n\), and nonprincipal adjacency spectrum in

\[
 I_k=[-1-\sqrt{2k-2},-1+\sqrt{2k-2}].
\]

Define

\[
 g_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr),
 \qquad
 C_k=g_k(k)=(k+2)^2(k^2+3),
\]

and

\[
 \boxed{
 \mathcal M_k(G)=-g_k(A)+\frac{C_k}{n}J.
 }
\]

On the principal adjacency eigenspace the two terms cancel. On a nonprincipal
adjacency eigenvector of eigenvalue \(	heta\), the eigenvalue of
\(\mathcal M_k(G)\) is

\[
 \bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2.
\]

Therefore

\[
 \boxed{\mathcal M_k(G)\succeq0},
 \qquad
 \boxed{\mathcal M_k(G)\mathbf1=0}.
\]

The nonbacktracking expansion is

\[
 g_k
 =6(k+2)F_0+2(2k+7)F_1+(k+13)F_2+6F_3+F_4.
\]

Since girth at least five gives
\(\operatorname{tr}F_i(A)=0\) for \(1\le i\le4\),

\[
 \boxed{
 \operatorname{tr}\mathcal M_k(G)
 =C_k-6(k+2)n
 =6(k+2)(B_k-n),
 }
\]

where

\[
 B_k=\frac{(k+2)(k^2+3)}6.
\]

Equivalently,

\[
 \boxed{
 6(k+2)(B_k-n)
 =\sum_{\theta\ne k}
 \bigl(2k-2-(\theta+1)^2\bigr)(\theta+2)^2.
 }
\]

This is the spectral-defect identity behind the exact LP ceiling.

If the nonprincipal spectrum lies in the open interval, the endpoint factors do
not vanish and hence

\[
 \boxed{
 \ker\mathcal M_k(G)
 =\langle\mathbf1\rangle\oplus E_{-2}(A).
 }
\]

Thus the trace bound, edge-local inequalities, and order-50 two-path
inequalities are respectively the trace, \(2\times2\) principal-minor, and
\(3\times3\) principal-minor levels of the same matrix. Larger principal minors
provide a canonical local semidefinite hierarchy beyond the one-variable LP
ceiling.

## 2. Equality exclusion and entry formulas

The diagonal of \(\mathcal M_k(G)\) is constant:

\[
 a_{k,n}=\frac{C_k}{n}-6(k+2).
\]

For distinct \(u,v\), positive semidefiniteness gives

\[
 |(\mathcal M_k)_{uv}|\le a_{k,n}.
\]

In the strict-window regime, equality
\((\mathcal M_k)_{uv}=a_{k,n}\) is impossible. It would force
\(e_u-e_v\in E_{-2}(A)\), but the \(u\)-coordinate of
\(A(e_u-e_v)\) is \(-1\) if \(u\sim v\) and \(0\) otherwise, never \(-2\).

For an edge \(uv\), let \(\sigma_{uv}\) be the number of five-cycles through it.
Then

\[
 (g_k(A))_{uv}=4k+14+\sigma_{uv}.
\]

For vertices \(u,w\) at distance two, choose their unique common neighbour and
put

\[
 r_{uw}=6\alpha_{uw}+\beta_{uw},
\]

where \(\alpha\) and \(\beta\) count the five- and six-cycles through the
resulting two-path. Since \(F_2(u,w)=1\), \(F_3(u,w)=\alpha_{uw}\), and
\(F_4(u,w)=\beta_{uw}\),

\[
 (g_k(A))_{uw}=k+13+r_{uw}.
\]

For vertices \(u,z\) at distance three, define

\[
 q_{uz}=6(A^3)_{uz}+(A^4)_{uz}.
\]

No uniqueness of a length-three geodesic is assumed. One has

\[
 (g_k(A))_{uz}=q_{uz}.
\]

The \(2\times2\) minors therefore yield

\[
 2k-2\le\sigma_{uv}
 \le \frac{2C_k}{n}-10k-26,
\]

\[
 5k-1\le r_{uw}
 \le \frac{2C_k}{n}-7k-25,
\]

and

\[
 6k+12\le q_{uz}
 \le \frac{2C_k}{n}-6k-12.
\]

The lower endpoint in each interval is excluded in the strict-window regime by
the preceding kernel argument.

## 3. The order-50 signed-root reduction

Assume \(k=6\), \(n=50\), and the shifted window is strict. Put

\[
 g_6(x)=(x+2)^2((x+1)^2-10),
 \qquad
 \boxed{T=50J-g_6(A)-2I}.
\]

Then

\[
 \boxed{T\mathbf1=2\mathbf1},
 \qquad
 \boxed{T+2I\succeq0},
\]

and

\[
 \boxed{25\mathcal M_6=25(T+2I)-2J}.
\]

The edge-local radius-two lower bound and the interval squeezes give

\[
 \sigma_{uv}\in\{12,13\},
 \qquad
 r_{uw}\in\{29,30,31,32\},
 \qquad
 q_{uz}\in\{48,49,50,51\}.
\]

The lower endpoints \(r=29\) and \(q=48\) are forbidden by the kernel argument.
Consequently \(T\) has zero diagonal and every off-diagonal entry belongs to
\(\{-1,0,1\}\):

\[
 T_{uv}=12-\sigma_{uv}\in\{0,-1\}
 \quad(u\sim v),
\]

\[
 T_{uw}=31-r_{uw}\in\{1,0,-1\}
 \quad(d(u,w)=2),
\]

\[
 T_{uz}=50-q_{uz}\in\{1,0,-1\}
 \quad(d(u,z)=3).
\]

Thus a hypothetical order-50 candidate produces fifty norm-\(\sqrt2\) vectors
with pairwise inner products in \(\{-1,0,1\}\) and constant signed row sum two.
This is a root-type Gram reformulation of the unresolved boundary case.

### A seven-vertex neighbourhood inequality

Let \(H\) be the high-edge subgraph, so \(uv\in E(H)\) precisely when \(uv\)
lies in thirteen five-cycles. For a vertex \(v\), put

\[
 d=d_H(v)\in\{0,2,4\},
 \qquad
 R_v=\sum_{\{u,w\}\subseteq N(v)}r_{uvw}.
\]

Apply \(T+2I\succeq0\) to

\[
 x=a e_v+\sum_{u\in N(v)}e_u.
\]

Since \(T_{vu}=-1\) on a high edge and \(0\) on a low edge, while
\(T_{uw}=31-r_{uvw}\) for two neighbours of \(v\),

\[
 x^{\mathsf T}(T+2I)x
 =2a^2-2da+942-2R_v\ge0.
\]

Minimizing at \(a=d/2\) gives \(R_v\le471-d^2/4\). Equality would put \(x\)
in \(\ker(T+2I)\), which is orthogonal to \(\mathbf1\), but
\(\mathbf1^{\mathsf T}x=6+d/2>0\). Hence

\[
 \boxed{R_v\le470-\frac{d_H(v)^2}{4}}.
\]

Thus the local upper bounds are \(470,469,466\) for high-edge degrees
\(0,2,4\). Summing and using

\[
 \sum_vR_v=30N_5+6N_6,
 \qquad N_5=360+\frac m5,
 \qquad S_2=\sum_vd_H(v)^2,
\]

gives

\[
 \boxed{
 N_6\le\frac{6350}{3}-m-\frac{S_2}{24}.
 }
\]

This bound does not reduce the current 266 coarse profiles because the existing
shifted-moment upper bound is stronger after aggregation. Its value is
structural: it is a genuine seven-vertex constraint not visible in the separate
three-vertex minors.

## 4. Improved near-ceiling order windows

The same slack matrix sharpens three low-degree order bounds.

### Degree seven

If \(k=7,n=76\), then \(a_{7,76}=27/19\). The integer interval squeezes and the
strict exclusion of their lower endpoints show that every off-diagonal entry of
\(\mathcal M_7\) is \(8/19\) or \(-11/19\). Let \(X\) join the pairs of the first
type. Then

\[
 19\mathcal M_7=38I-11J+19A(X).
\]

The zero row sum makes \(X\) 42-regular. On \(\mathbf1^\perp\), positivity gives
\(\lambda_{\min}(A(X))\ge-2\). Since \(42>(76-2)/2\), \(X\) is connected.

The classical classification of connected regular graphs with least eigenvalue
at least \(-2\) and more than 28 vertices implies that \(X\) is a line graph or
a cocktail-party graph. It is not cocktail-party, whose degree would be 74. If
\(X=L(Y)\), regularity forces \(Y\) to be regular or semiregular bipartite. In
the regular case \(Y\) would have degree 22 and

\[
 |V(Y)|=\frac{2\cdot76}{22}=\frac{76}{11},
\]

impossible. In the semiregular case, the two degrees divide 76 and sum to 44;
no pair of divisors of 76 has that sum. Therefore order 76 is impossible, and
odd degree forces even order, so

\[
 \boxed{n\le74}
\]

in the diameter-three degree-seven case.

### Degree eight

For \(k=8,n=110\), every off-diagonal slack entry is forced to be \(-1/11\),
contradicting \(\mathcal M_8\mathbf1=0\).

For \(k=8,n=109\), every off-diagonal entry is \(51/109\) or \(-58/109\). If \(X\)
joins the first type, then

\[
 109\mathcal M_8=218I-58J+109A(X).
\]

Thus \(X\) is connected, 56-regular, and has least eigenvalue at least \(-2\).
It is not cocktail-party. A regular line-graph root would have degree 29 and
\(218/29\) vertices, while a semiregular bipartite root would require two
divisors of the prime 109 summing to 58. Both are impossible. Hence

\[
 \boxed{n\le108}
\]

for degree-eight strict counterexamples.

### Degree nine

For \(k=9,n=152\), every off-diagonal slack entry is forced to be \(-5/38\),
again contradicting the zero row sum. Since \(9n\) is even,

\[
 \boxed{n\le150}.
\]

The resulting windows are

\[
 \boxed{
 \begin{array}{rcl}
 k=6&:&n\le50,\\
 k=7&:&n=50\text{ in diameter two, or }n\le74\text{ in diameter three},\\
 k=8&:&n\le108,\\
 k=9&:&n\le150.
 \end{array}
 }
\]

## 5. Literature boundary and promotion recommendation

The slack matrix and its specialization to the shifted WOW window are
project-derived. The near-ceiling degree-seven and degree-eight exclusions use
one classical external theorem: a connected regular graph with more than 28
vertices and least eigenvalue at least \(-2\) is a line graph or a cocktail-party
graph. See Cvetkovi\'c, Rowlinson and Simi\'c, *Spectral Generalizations of Line
Graphs*, Cambridge University Press, 2004, Theorem 3.12.2 and Chapter 4. The
line-graph arithmetic after this theorem is proved above and checked exactly by
the accompanying verifier.

The general slack-matrix proposition and spectral-defect identity should be
promoted because they unify three existing proof levels with little additional
length. The improved low-degree windows are clean theorem-level gains after an
independent citation audit of the classical classification input. The order-50
signed-root reduction is useful as a structural reformulation and guide to the
next local semidefinite step. The neighbourhood \(N_6\) inequality is exact but
should be presented as structural rather than as a numerical breakthrough.
