# Exact local feasibility system for a degree-six order-50 candidate

**Status:** proved necessary conditions with exact symbolic and integer checks.  
**Scope:** a hypothetical connected 6-regular strict WOW-284 counterexample of
order 50, girth at least five, and diameter three.  
**Nonclaim:** these conditions do not eliminate order 50.

Let \(G\) satisfy the hypotheses.  PR #16 proves that every edge lies in either
12 or 13 five-cycles.  Let

\[
 H=\{e\in E(G):e\text{ lies in 13 five-cycles}\}
\]

be the spanning high-edge subgraph, and write

\[
 m=|E(H)|.
\]

## 1. Five-cycles through a vertex

Fix \(v\), and let \(\tau(v)\) be the number of 5-cycles containing \(v\).
The distance layers around \(v\) have sizes

\[
 1,\quad 6,\quad 30,\quad 13.
\]

The average internal degree in the distance-two layer is \(\tau(v)/15\).  The
row-sum compression of the adjacency matrix is therefore

\[
 Q_v=
 \begin{pmatrix}
 0&6&0&0\\
 1&0&5&0\\
 0&1&\tau/15&5-\tau/15\\
 0&0&30(5-\tau/15)/13&6-30(5-\tau/15)/13
 \end{pmatrix}.
\]

Its characteristic polynomial is \((x-6)q_\tau(x)\), where

\[
 q_\tau(x)=
 \frac{-43\tau x^2-30\tau x+228\tau+195x^3+2250x^2+105x-11250}{195}.
\]

At the upper WOW boundary \(u=-1+\sqrt{10}\),

\[
 195q_\tau(u)
 =(-215+56\sqrt{10})\tau+7350-1860\sqrt{10}.
\]

The coefficient of \(\tau\) is negative, and at \(\tau=39\) the value is

\[
 9(-115+36\sqrt{10})<0.
\]

Moreover,

\[
 195q_\tau(6)=1500(75-\tau)>0
\]

for a connected diameter-three graph.  Hence \(\tau\ge39\) would place a
nonprincipal compression eigenvalue in \((u,6)\), contradicting the strict WOW
window.  The elementary edge count inside the distance-three layer gives
\(\tau\ge36\).  Therefore

\[
 \boxed{\tau(v)\in\{36,37,38\}.}
\]

Since

\[
 \sum_{e\ni v}\sigma_e=2\tau(v),
\]

where \(\sigma_e\in\{12,13\}\), it follows that

\[
 \boxed{d_H(v)=2\tau(v)-72\in\{0,2,4\}.}
\]

Thus \(H\) is an even spanning subgraph of maximum degree four.  If
\(n_2,n_4\) denote the numbers of vertices of high degree two and four, then

\[
 m=n_2+2n_4,
 \qquad
 \sum_vd_H(v)^2=4n_2+16n_4.
\]

The edge--5-cycle incidence count gives

\[
 N_5=360+\frac m5,
 \qquad
 \boxed{m\equiv0\pmod5.}
\]

## 2. Constraints on every two-edge path

Let \(u-v-w\) be a two-edge path.  Because the girth is at least five, \(v\) is
the unique common neighbor of \(u,w\).  Define

- \(\alpha_{uvw}\): the number of 5-cycles containing the path \(u-v-w\);
- \(\beta_{uvw}\): the number of 6-cycles containing the path \(u-v-w\);
- \(r_{uvw}=6\alpha_{uvw}+\beta_{uvw}\).

The nonbacktracking recurrences give

\[
 (A^3)_{uw}=\alpha_{uvw},
 \qquad
 (A^4)_{uw}=16+\beta_{uvw}.
\]

Use the centered positive-semidefinite matrix from PR #16,

\[
 M=-f_6(A)+\frac{2496}{50}J,
 \qquad
 f_6(x)=(x+2)^2(x^2+2x-9).
\]

After multiplying the principal submatrix on \(u,v,w\) by 25, its diagonal is
48.  An edge entry is

\[
 -2\quad\text{if the edge is low},
 \qquad
 -27\quad\text{if the edge is high},
\]

and the \(u,w\) entry is

\[
 773-25r_{uvw}.
\]

The two-by-two minors first give

\[
 29\le r_{uvw}\le32.
\]

The three-by-three determinants factor as follows:

\[
\begin{array}{c|c|c}
\text{edge types}&\det&\text{allowed }r\\
\hline
\text{low--low}&-5000(r-29)(6r-197)&29,30,31,32\\
\text{mixed}&-7500(4r^2-247r+3803)&30,31,32\\
\text{high--high}&-3750(r-29)(8r-253)&29,30,31
\end{array}
\]

Hence a mixed two-path cannot have \(r=29\), and a high--high two-path cannot
have \(r=32\).

## 3. Global six-cycle inequalities

Every 5-cycle contributes five two-edge paths, and every 6-cycle contributes
six.  Summing \(r=6\alpha+\beta\) over all 750 two-edge paths gives

\[
 \sum r=30N_5+6N_6=10800+6m+6N_6.
\]

Let

\[
 S_2=\sum_vd_H(v)^2=4n_2+16n_4.
\]

At a vertex of high degree \(d\), the number of mixed incident edge pairs is
\(d(6-d)\), while the number of high--high pairs is \(\binom d2\).  Summing the
local table yields

\[
 \boxed{
 N_6\ge 1825+m-\frac{S_2}{6}
 }
\]

and

\[
 \boxed{
 N_6\le 2200-\frac{5m}{6}-\frac{S_2}{12}.
 }
\]

These are rational inequalities; the integer variable \(N_6\) is understood to
lie between the corresponding ceiling and floor.

## 4. Independent shifted-moment inequalities

Let \(\theta_1,\ldots,\theta_{49}\) be the nonprincipal adjacency eigenvalues
and put \(y_i=\theta_i+1\).  The strict WOW window gives

\[
 |y_i|<\sqrt{10}.
\]

Using the trace identities through degree six, the shifted moments are

\[
\begin{aligned}
s_0&=49,&s_1&=43,&s_2&=301,&s_3&=607,\\
s_4&=2749,&s_5&=6343+2m,&
 s_6&=1801+12m+12N_6.
\end{aligned}
\]

The moment matrix \([s_{i+j}]_{i,j=0}^3\) is positive semidefinite.  Its leading
three-by-three block has determinant 5,850,000, so its Schur complement gives

\[
 \boxed{
 N_6\ge
 \frac{43m^2-70200m+119632500}{58500}.
 }
\]

Likewise, since \(10-y_i^2>0\), the localizing matrix

\[
 [10s_{i+j}-s_{i+j+2}]_{i,j=0}^2
\]

is positive semidefinite.  Its leading two-by-two block has determinant 18,000,
and its Schur complement gives

\[
 \boxed{
 N_6\le
 \frac{4220000-2200m-7m^2}{2000}.
 }
\]

## 5. Exact coarse-profile experiment

The verifier enumerates all triples

\[
 (n_0,n_2,n_4),
 \qquad n_0+n_2+n_4=50,
\]

with

\[
 m=n_2+2n_4\equiv0\pmod5,
\]

and intersects the two local six-cycle bounds with the two shifted-moment
bounds.  Exactly 266 coarse profiles survive.  The surviving values of \(m\)
are

\[
 0,5,10,\ldots,100.
\]

This is a negative experimental conclusion: the present one-point and
three-vertex constraints do **not** eliminate order 50.  They are nevertheless
exact pruning conditions for a future canonical generation or semidefinite
search.

## 6. Research boundary

The natural next steps are:

1. impose realizability of the even high-edge subgraph inside a girth-five
   6-regular graph;
2. add four-vertex Gram minors and local intersection consistency;
3. incorporate exact 5/6-cycle incidence matrices rather than only their totals;
4. use the constraints as a fail-fast filter in a canonical degree-six search.

No claim of minimality, nonexistence at order 50, or novelty is made.
