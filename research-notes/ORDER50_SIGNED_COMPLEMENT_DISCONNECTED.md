# The order-50 signed complement is disconnected

**Status:** exact project derivation under Proof Audit 14.  
**Scope:** a hypothetical connected 6-regular order-50 strict diameter-three WOW
counterexample.  
**External input:** the Cameron--Goethals--Seidel--Shult root representation for
connected signed graphs with smallest eigenvalue at least \(-2\).

## 1. Statement

Let

\[
 g_6(x)=(x+2)^2((x+1)^2-10)
\]

and

\[
 S=50J-g_6(A)-2I.
\]

The optimal-slack construction gives

\[
 S\mathbf1=2\mathbf1,
 \qquad
 S+2I\succeq0,
 \qquad
 S_{uv}\in\{-1,0,1\}\quad(u\ne v).
\]

Then

\[
 \boxed{
 	ext{the underlying signed graph of }S	ext{ is disconnected.}
 }
\]

This theorem is independent of the later factorization of \(g_6(x)+4\).

## 2. Negative-edge parity

Let \(F_i\) be the degree-six nonbacktracking polynomials.  Exact expansion gives

\[
\begin{aligned}
 (g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
 &+352F_5+78F_6+12F_7+F_8.
\end{aligned}
\]

Since the girth is at least five,

\[
 \operatorname{tr}F_i(A)=0\quad(1\le i\le4).
\]

For \(5\le i\le8\), every closed nonbacktracking walk is a directed traversal
of a simple \(i\)-cycle, so

\[
 \operatorname{tr}F_i(A)=2iN_i.
\]

After removing the principal adjacency contribution and restoring the principal
signed eigenvalue \(2\),

\[
 \operatorname{tr}S^2
 =8(440N_5+117N_6+21N_7+2N_8-604100).
\]

Let \(P_+\) and \(P_-\) be the numbers of positive and negative signed edges.
The signed row sum gives

\[
 P_+-P_-=50,
\]

whereas

\[
 \operatorname{tr}S^2=2(P_++P_-)=100+4P_-.
\]

Therefore

\[
 \boxed{P_-	ext{ is odd}.}
\]

## 3. Root representation under connectedness

Suppose that \(S\) were connected.  The separately audited moment bound gives

\[
 \operatorname{rank}(S+2I)\ge30.
\]

The external signed-root theorem represents a connected signed graph with
smallest eigenvalue at least \(-2\) inside a \(D_m\) or \(E_8\) root system.  The
rank bound excludes \(E_8\).  Hence there is an integral matrix \(B\), whose
columns are roots

\[
 b_e\in\{\pm e_i\pm e_j:i\ne j\},
\]

such that

\[
 B^{\mathsf T}B=S+2I.
\]

Put

\[
 s=B\mathbf1=\sum_e b_e.
\]

Since \((S+2I)\mathbf1=4\mathbf1\),

\[
 b_e\cdot s=4\quad\text{for every root }b_e,
 \qquad
 \|s\|^2=200.
\]

After switching coordinate axes, assume \(s_i\ge0\).  The coordinate support
graph of the fifty roots is connected.  If \(v\) is the number of used
coordinates, then

\[
 30\le v\le51.
\]

The lower bound is the Gram rank.  The upper bound follows because a connected
support graph with fifty root-edges has at most fifty-one vertices.

For every root, two used coordinate levels have signed sum four.  Connectivity
of the support graph forces all levels into exactly one of the following three
families:

\[
 0,4,8,\ldots;
 \qquad
 2,6,10,\ldots;
 \qquad
 1,3,5,7,\ldots.
\]

## 4. Excluding the three level families

### 4.1 Multiples of four

If every level is divisible by four, then \(\|s\|^2\) is divisible by sixteen,
contrary to

\[
 200\equiv8\pmod{16}.
\]

### 4.2 Levels congruent to two modulo four

The constraints \(v\ge30\) and \(\|s\|^2=200\) exclude every level at least ten:
one level ten and twenty-nine baseline levels two already contribute \(216\).
Thus only levels two and six occur.  If their multiplicities are \(n_2,n_6\),
then

\[
 4n_2+36n_6=200,
 \qquad
 v=n_2+n_6=50-8n_6.
\]

Hence

\[
 (n_2,n_6)\in\{(50,0),(41,1),(32,2)\}.
\]

A root incident with a level-six coordinate must have signs \(+6-2=4\), so
that coordinate is incident with exactly six roots, all with the same sign.  At
a level-two coordinate, let \(p_i,m_i\) be the positive and negative incidences.
Then

\[
 p_i-m_i=2,
 \qquad
 p_im_i\equiv m_i\pmod2.
\]

Distinct roots share at most one coordinate, because an off-diagonal Gram entry
is in \(\{-1,0,1\}\).  Therefore the parity of the number of negative signed
edges is

\[
 P_-\equiv\sum_i p_im_i
       \equiv\sum_i m_i
       =6n_6
       \equiv0\pmod2,
\]

contradicting the oddness of \(P_-\).

### 4.3 Odd levels

Let \(A_t\) and \(B_t\) count coordinates at levels \(4t+1\) and \(4t+3\),
respectively.  Flow balance along the two level chains and
\(\|s\|^2=200\) give

\[
 \boxed{
 \frac{200-3v}{32}
 =\sum_{t\ge1}\binom{t+1}{2}(A_t+B_t).
 }
\]

The right-hand side is an integer, so

\[
 3v\equiv200\equiv8\pmod{32},
 \qquad
 v\equiv24\pmod{32}.
\]

There is no such integer in \(30\le v\le51\).

All three level families are impossible.  Therefore \(S\) is disconnected.

## 5. Verification and claim boundary

The exact arithmetic verifier is

```text
scripts/verify_order50_signed_complement_disconnected.py
```

It checks the nonbacktracking expansion, trace parity, rank input, even-level
multiplicities, negative-edge parity, and odd-level congruence.  The signed-root
representation theorem is an external input and is not replaced by the script.
