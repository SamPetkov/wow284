# The order-50 signed complement is disconnected

**Status:** exact project derivation with one external signed-root theorem.

Let \(G\) be a hypothetical connected \(6\)-regular order-\(50\), girth-five,
diameter-three strict WOW candidate, put

\[
g_6(x)=(x+2)^2((x+1)^2-10),
\qquad
S=50J-g_6(A)-2I.
\]

The signed-complement construction gives

\[
S\mathbf1=2\mathbf1,\qquad S+2I\succeq0,\qquad
S_{uu}=0,\qquad S_{uv}\in\{-1,0,1\}\quad(u\ne v).
\]

Then the underlying signed graph of \(S\) is disconnected.

## Corrected trace parity

For the degree-six nonbacktracking polynomials \(F_i\),

\[
\begin{aligned}
(g_6+2)^2={}&28144F_0+18220F_1+8838F_2+3576F_3+1233F_4\\
&+352F_5+78F_6+12F_7+F_8.
\end{aligned}
\]

The length-seven and length-eight traces contain the one-edge-tailed walks
around shorter cycles:

\[
\operatorname{tr}F_7(A)=14N_7+40N_5,\qquad
\operatorname{tr}F_8(A)=16N_8+48N_6.
\]

Consequently

\[
\operatorname{tr}S^2
=8(500N_5+123N_6+21N_7+2N_8-604100).
\]

If \(P_+\) and \(P_-\) count positive and negative signed edges, then

\[
P_+-P_-=50,\qquad
\operatorname{tr}S^2=2(P_++P_-)=100+4P_-.
\]

Thus \(P_-\) is odd.

## Signed-root contradiction

Assume that \(S\) is connected. The exact moment bound gives
\(\operatorname{rank}(S+2I)\ge30\). The strict shifted window is used here to
exclude the two endpoint roots \(-1\pm\sqrt{10}\), so
\(\ker(S+2I)=E_{-2}(A)\).

The connected signed-root representation theorem places \(S+2I\) in a root
system of type \(D_m\) or \(E_8\). The rank bound excludes \(E_8\), so

\[
B^{\mathsf T}B=S+2I
\]

for an integral matrix whose columns are roots
\(\pm e_i\pm e_j\). Put \(s=B\mathbf1\). Then

\[
b_u\cdot s=4\quad\text{for every column }b_u,
\qquad
\|s\|^2=200.
\]

After changing signs of coordinate axes, take \(s_i\ge0\). The coordinate
support multigraph is connected, and if \(v\) coordinates are used, then

\[
30\le v\le51.
\]

The equation \(\pm s_i\pm s_j=4\), together with support connectedness, puts
all coordinate levels in one of three families:

\[
0,4,8,\ldots;\qquad
2,6,10,\ldots;\qquad
1,3,5,\ldots.
\]

The first family is impossible because it would make \(\|s\|^2\) divisible
by \(16\), whereas \(200\equiv8\pmod {16}\).

In the second family, the rank bound excludes levels at least \(10\). If
\(n_2,n_6\) count levels \(2,6\), then

\[
n_2+9n_6=50,\qquad
v=n_2+n_6=50-8n_6\ge30,
\]

so

\[
(n_2,n_6)\in\{(50,0),(41,1),(32,2)\}.
\]

Every root is either \(e_i+e_j\) with \(s_i=s_j=2\), or \(e_i-e_j\) with
\(s_i=6\) and \(s_j=2\), after ordering the coordinates. The sign pattern is
unique on a fixed coordinate support, and duplicate columns would have inner
product \(2\), so distinct roots share at most one coordinate in this
restricted family. At a level-two coordinate let \(p_i,m_i\) be its positive
and negative incidences. Then \(p_i-m_i=2\), while every level-six coordinate
contributes six negative incidences at level two. Negative Gram products occur
precisely at one level-two coordinate with opposite incidence signs, and hence

\[
P_-=\sum_{i:s_i=2}p_im_i.
\]

Therefore

\[
P_-\equiv\sum_{i:s_i=2}p_im_i
\equiv\sum_i m_i
=6n_6
\equiv0\pmod2,
\]

contradicting the corrected trace parity.

For the odd family, let \(A_t,B_t\) count levels \(4t+1,4t+3\). Difference
roots cancel when signed incidences are summed within either chain. The
positive roots between levels \(1\) and \(3\), the only cross-chain root type,
contribute equally to the two sums, giving

\[
\sum_{t\ge0}(4t+1)A_t
=\sum_{t\ge0}(4t+3)B_t.
\]

Combining this with \(\|s\|^2=200\) gives

\[
\frac{200-3v}{32}
=\sum_{t\ge1}\binom{t+1}{2}(A_t+B_t).
\]

Thus \(v\equiv24\pmod {32}\), impossible for \(30\le v\le51\). All three
families are excluded, so \(S\) is disconnected.

The external representation theorem is the Cameron--Goethals--Seidel--Shult
root-system theorem as recorded for edge-signed graphs by Greaves, Koolen,
Munemasa, Sano, and Taniguchi. The exact arithmetic audit is
`scripts/verify_order50_signed_complement_disconnected.py`.
