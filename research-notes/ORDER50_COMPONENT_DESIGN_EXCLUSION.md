# Excluding the degree-six order-50 boundary

**Status:** project derivation under Proof Audit 14; manuscript promotion requires
an independent proof replay and a final citation audit.  
**Scope:** a hypothetical connected 6-regular graph \(G\) of order \(50\), girth
at least five and diameter three satisfying the strict shifted WOW window.

## 1. Signed complement

Put

\[
 g_6(x)=(x+2)^2((x+1)^2-10)
       =x^4+6x^3+3x^2-28x-36
\]

and

\[
 S=50J-g_6(A)-2I.
\]

The optimal-slack construction gives

\[
 S\mathbf 1=2\mathbf 1,
 \qquad S+2I\succeq0,
\]

and every off-diagonal entry of \(S\) belongs to
\(\{-1,0,1\}\).  Moreover,

\[
 E_{-2}(S)=E_{-2}(A).
\]

The moment argument in
`research-notes/ORDER50_MINUS_TWO_MULTIPLICITY.md` gives

\[
 m_{-2}(A)\le20,
 \qquad
 \operatorname{rank}(S+2I)\ge30.
\]

We first prove that the underlying signed graph of \(S\) is disconnected.

## 2. A parity invariant

Let \(F_i\) be the degree-six nonbacktracking polynomials.  Exact expansion gives

\[
\begin{aligned}
 (g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
 &+352F_5+78F_6+12F_7+F_8.
\end{aligned}
\]

Since the girth is at least five,
\(\operatorname{tr}F_i(A)=0\) for \(1\le i\le4\).  For \(5\le i\le8\), every
closed nonbacktracking walk of length \(i<10\) is a directed traversal of a
simple \(i\)-cycle, so

\[
 \operatorname{tr}F_i(A)=2iN_i.
\]

The principal adjacency eigenvalue contributes
\((g_6(6)+2)^2=2498^2\), whereas the principal signed eigenvalue is \(2\).
Consequently

\[
\begin{aligned}
 \operatorname{tr}S^2
 ={}&-4\,832\,800+3520N_5+936N_6+168N_7+16N_8\\
 ={}&8(440N_5+117N_6+21N_7+2N_8-604100).
\end{aligned}
\]

Thus

\[
 oxed{\operatorname{tr}S^2\equiv0\pmod8}.
\]

If \(P\) and \(N\) denote the numbers of positive and negative signed edges,
then the signed row sum gives \(P-N=50\), while
\(\operatorname{tr}S^2=2(P+N)\).  Hence

\[
 \operatorname{tr}S^2=100+4N,
\]

and therefore

\[
 oxed{N\text{ is odd}.}
\]

## 3. A connected signed complement would be of \(D\)-type

Assume that \(S\) is connected.  The Cameron--Goethals--Seidel--Shult theorem
represents a connected signed graph with least eigenvalue at least \(-2\) by a
subset of a \(D_m\) or \(E_8\) root system.  The rank bound above rules out an
\(E_8\) representation.  Hence there is an integral matrix \(B\) whose columns
are roots

\[
 b_e\in\{\pm e_i\pm e_j:i\ne j\}
\]

and

\[
 B^{\mathsf T}B=S+2I.
\]

Put

\[
 s=B\mathbf1=\sum_e b_e.
\]

Since \((S+2I)\mathbf1=4\mathbf1\),

\[
 b_e\cdot s=4\quad\text{for every }e,
 \qquad
 \|s\|^2=200.
\]

After changing signs of coordinate axes, assume \(s_i\ge0\).  The coordinate
support graph of the roots is connected; otherwise the signed graph represented
by the roots would be disconnected.  For every root, either its two coordinate
levels sum to four or their absolute difference is four.  The used coordinate
levels therefore lie in exactly one of the following connected families:

\[
 0,4,8,\ldots;
 \qquad
 2,6,10,\ldots;
 \qquad
 1,3,5,7,\ldots.
\]

Let \(v\) be the number of used coordinates.  Since
\(\operatorname{rank}B\ge30\) and the support graph is connected with fifty
edges,

\[
 30\le v\le51.
\]

### 3.1 Levels divisible by four

If every level is divisible by four, then \(\|s\|^2\) is divisible by sixteen,
contrary to \(200\equiv8\pmod{16}\).

### 3.2 Levels congruent to two modulo four

The lower bound \(v\ge30\) excludes any level at least ten: replacing one
baseline level \(2\) by \(10\) already gives norm at least
\(4\cdot30+96>200\).  Thus only levels two and six occur.  If their
multiplicities are \(n_2,n_6\), then

\[
 4n_2+36n_6=200,
 \qquad
 v=n_2+n_6=50-8n_6.
\]

Therefore

\[
 (n_2,n_6)\in\{(50,0),(41,1),(32,2)\}.
\]

A level-six coordinate is incident with exactly six roots, all carrying the
same sign there.  At a level-two coordinate, write \(p_i,m_i\) for the numbers
of positive and negative root entries.  Since \(p_i-m_i=2\),
\(p_im_i\equiv m_i\pmod2\).  Distinct roots share at most one coordinate in
this family, and the number of negative signed edges is congruent to

\[
 \sum_i p_im_i\equiv\sum_i m_i=6n_6\equiv0\pmod2.
\]

This contradicts the oddness proved in Section 2.

### 3.3 Odd levels

Write \(A_t\) and \(B_t\) for the numbers of coordinates at levels
\(4t+1\) and \(4t+3\), respectively.  Let \(e\) be the number of roots joining
levels one and three.  Flow balance along the two level chains gives

\[
 e=\sum_{t\ge0}(4t+1)A_t
  =\sum_{t\ge0}(4t+3)B_t.
\]

Using \(\|s\|^2=200\), subtracting the two equal flow sums yields the exact
identity

\[
 oxed{
 \frac{200-3v}{32}
 =\sum_{t\ge1}\binom{t+1}{2}(A_t+B_t).
 }
\]

The right-hand side is a nonnegative integer.  Hence

\[
 3v\equiv200\equiv8\pmod{32},
 \qquad v\equiv24\pmod{32}.
\]

No integer in \(30\le v\le51\) satisfies this congruence.  This excludes the
third family.

All three level families are impossible, so

\[
 oxed{S\text{ is disconnected}.}
\]

## 4. The components force an equitable \(20+30\) partition

Let the connected components of the underlying signed graph of \(S\) have
vertex sets \(V_1,\ldots,V_c\), of sizes \(n_1,\ldots,n_c\).  Every component
has signed row sum two, so the span of their indicator vectors lies in the
\(S\)-eigenspace for eigenvalue two.

On \(\mathbf1^\perp\),

\[
 S=-2I-g_6(A).
\]

The factorization

\[
 g_6(x)+4=(x+4)(x^3+2x^2-8x-4)
\]

has an irreducible cubic factor.  At the upper endpoint
\(u=-1+\sqrt{10}\), that cubic equals \(-5+\sqrt{10}<0\), while its value at
\(3\) is positive.  Hence one of its conjugate roots lies outside the strict
WOW interval.  Since \(A\) is an integral symmetric matrix, the cubic cannot
occur in its characteristic polynomial.  Therefore

\[
 A=-4I
\]

on the part of the \(S\)-eigenspace for eigenvalue two orthogonal to
\(\mathbf1\).

For a vector \(x\) constant with value \(c_i\) on \(V_i\), put

\[
 \bar c=\frac1{50}\sum_i n_ic_i.
\]

Then

\[
 Ax=-4x+10\bar c\,\mathbf1.
\]

Taking \(x=\mathbf1_{V_j}\) shows that the component partition is equitable for
\(G\), with

\[
 q_{ij}=\frac{n_j}{5}\quad(i\ne j),
 \qquad
 q_{ii}=\frac{n_i}{5}-4.
\]

These are nonnegative integers.  Thus every component size is divisible by five
and at least twenty.  Since the sizes sum to fifty and \(c\ge2\), there are
exactly two components, with sizes \(20,30\) or \(25,25\).  The second option
would induce a 1-regular graph on each 25-vertex part, impossible by the
handshake lemma.  Hence the parts have sizes \(20\) and \(30\).

Write them as \(X,Y\), respectively.  Relative to this partition,

\[
 A=\begin{pmatrix}0&C\\ C^{\mathsf T}&R\end{pmatrix},
\]

where

* \(C\) is a \(20\times30\) zero-one matrix with row sum six and column sum
  four;
* \(R\) is the adjacency matrix of a 2-regular graph on thirty vertices;
* every cycle of \(R\) has length at least five.

## 5. The incidence design

Two rows of \(C\) meet in at most one column, or \(G\) contains a 4-cycle.  Each
column contains four ones, so the total number of intersecting row pairs is

\[
 30\binom42=180.
\]

For a fixed row, its six columns meet \(6\cdot3=18\) distinct other rows.
Thus each row is disjoint from exactly one other row.  The disjointness relation
is a perfect matching with permutation matrix \(P\), and

\[
 oxed{CC^{\mathsf T}=5I+J-P.}
\]

Put

\[
 B=C^{\mathsf T}C.
\]

The nonzero eigenvalues of \(B\) are

\[
 24^{(1)},\qquad6^{(10)},\qquad4^{(9)}.
\]

In particular,

\[
 \operatorname{tr}B=120,
 \qquad
 \operatorname{tr}B^2=1080.
\]

If \(yz\) is an edge of the 2-regular graph, then \(B_{yz}=0\), since a common
neighbor in \(X\) would create a triangle.  If \(y,z\) are at distance two in
that graph, again \(B_{yz}=0\), since a common neighbor in \(X\) would create a
4-cycle.  Consequently

\[
 \operatorname{tr}(BR)=0,
 \qquad
 \operatorname{tr}(BR^2)=240.
\]

## 6. The off-block polynomial identity

The off-diagonal block of \(S\) between \(X\) and \(Y\) is zero.  Hence

\[
 (g_6(A))_{XY}=50J_{20,30}.
\]

A direct block multiplication gives

\[
 (g_6(A))_{XY}=CH,
\]

where

\[
 H=BR+RB+R^3+6B+6R^2+3R-28I.
\]

Multiplying by \(C^{\mathsf T}\) yields

\[
 BH=200J_{30}.
\]

Taking traces and using the identities above gives

\[
 2\operatorname{tr}(RB^2)+\operatorname{tr}(BR^3)=1440.
\]

For an edge \(yz\) of \(R\), let

\[
 t_{yz}=(C^{\mathsf T}PC)_{yz}.
\]

The two four-subsets of \(X\) incident with \(y,z\) are disjoint, and
\(t_{yz}\) counts matching pairs crossing between them.  Thus
\(0\le t_{yz}\le4\).  Since

\[
 B^2=C^{\mathsf T}(5I+J-P)C=5B+16J-C^{\mathsf T}PC,
\]

one has

\[
 \operatorname{tr}(RB^2)
 =2\sum_{yz\in E(R)}(16-t_{yz})
 =960-2T,
 \qquad
 T=\sum_{yz\in E(R)}t_{yz}\le120.
\]

Both \(B\) and \(R^3\) are entrywise nonnegative, so
\(\operatorname{tr}(BR^3)\ge0\).  Substitution gives

\[
 \operatorname{tr}(BR^3)=4T-480.
\]

It follows that \(T=120\), and therefore

\[
 t_{yz}=4
\]

for every edge \(yz\) of \(R\).  If \(\pi\) denotes the perfect-matching
involution on \(X\), then

\[
 N_X(z)=\pi(N_X(y))
\]

for every edge \(yz\) of \(R\).  Along a two-edge path \(y-z-w\) in a cycle of
\(R\), this gives

\[
 N_X(w)=\pi^2(N_X(y))=N_X(y).
\]

But \(y,w\) are distinct vertices at distance two in \(R\), so a common neighbor
in \(X\) would form a 4-cycle in \(G\).  This contradiction proves:

\[
 oxed{
 \text{No connected 6-regular strict WOW counterexample of order }50\text{
 exists.}
 }
\]

Combining this with the integral optimal-slack order bound gives

\[
 oxed{
 k=6\quad\Longrightarrow\quad n\le49.
 }
\]

## 7. Verification and external input

The exact verifier

```
scripts/verify_order50_component_design_exclusion.py
```

checks the nonbacktracking expansion, trace congruence, level-family arithmetic,
component-size enumeration, incidence spectra, block-polynomial identity, and
final trace squeeze.  A second independent verifier replays the algebra without
importing the first script.

The only external classification input is the Cameron--Goethals--Seidel--Shult
root-system theorem for connected signed graphs with least eigenvalue at least
\(-2\).  It must be cited explicitly when the theorem is promoted to the
manuscript; the executable checks do not reprove it.
