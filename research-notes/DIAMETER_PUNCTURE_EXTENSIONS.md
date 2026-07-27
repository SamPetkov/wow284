# Diameter obstructions and puncture robustness for WOW-284

**Status:** exact project derivations with an exact verifier; pending independent
mathematical review and literature-priority clearance.  This note is not part of
the submitted v1 manuscript, and no novelty claim is made here.

Write

\[
\Phi(G)=\delta^*(G)+\lambda_{\min}(D(G)).
\]

Thus a graph is a strict counterexample to WOW-284 exactly when
\(\Phi(G)>0\).

## 1. Endpoint-neighborhood bound

### Theorem 1

Let \(G\) be connected, have girth at least five, minimum degree \(\delta\),
maximum degree \(\Delta\), and diameter \(d\ge5\).  Then

\[
\boxed{
\lambda_{\min}(D(G))\le -\delta(d-4)-2.
}
\]

Consequently, every strict counterexample satisfies

\[
\boxed{
\Delta>\delta(d-4)+2
}
\]

and therefore

\[
\boxed{
\operatorname{diam}(G)
\le 3+\left\lceil\frac{\Delta-2}{\delta}\right\rceil.
}
\]

### Proof

Choose vertices \(u,v\) with \(d_G(u,v)=d\), and put

\[
p=d(u),\qquad q=d(v).
\]

For positive \(a,b\), define \(x\in\mathbb R^{V(G)}\) by

\[
x_w=
\begin{cases}
 a,&w\in N(u),\\
-b,&w\in N(v),\\
 0,&\text{otherwise}.
\end{cases}
\]

Because \(d\ge5\), the two neighborhoods are disjoint.  Two distinct
neighbors of one center are at distance exactly two: the center gives a
length-two path, while adjacency would create a triangle.  For
\(r\in N(u)\) and \(s\in N(v)\), the triangle inequality gives

\[
d_G(r,s)\ge d-2.
\]

Since the cross-coordinate products are negative,

\[
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
\le
\frac{
2p(p-1)a^2+2q(q-1)b^2-2pq(d-2)ab
}{pa^2+qb^2}.
\]

After the change of variables \((\sqrt p\,a,\sqrt q\,b)\), the right-hand side
is the Rayleigh quotient of

\[
\begin{pmatrix}
2(p-1)&-(d-2)\sqrt{pq}\\
-(d-2)\sqrt{pq}&2(q-1)
\end{pmatrix}.
\]

Hence

\[
\lambda_{\min}(D(G))
\le
p+q-2-
\sqrt{(p-q)^2+pq(d-2)^2}.
\tag{1}
\]

Set

\[
p=\delta+\alpha,
\qquad
q=\delta+\beta,
\qquad
t=d-2.
\]

The exact identity

\[
\begin{aligned}
&(p-q)^2+pqt^2-
\bigl(p+q+\delta(t-2)\bigr)^2\\
&\quad=(t-2)
\left[
\delta t(\alpha+\beta)+(t+2)\alpha\beta
\right]
\ge0
\end{aligned}
\]

shows that

\[
\sqrt{(p-q)^2+pqt^2}
\ge p+q+\delta(t-2).
\]

Substituting in (1) gives

\[
\lambda_{\min}(D(G))
\le -2-\delta(t-2)
=-2-\delta(d-4).
\]

Finally, \(\delta^*(G)\le\Delta\).  If \(\Phi(G)>0\), then

\[
\Delta\ge\delta^*(G)>-\lambda_{\min}(D(G))
\ge\delta(d-4)+2,
\]

which proves the remaining assertions.  \(\square\)

### Corollary 2

Every regular strict counterexample to WOW-284 has diameter at most four.
More precisely, a \(k\)-regular graph of girth at least five and diameter
\(d\ge5\) satisfies

\[
\Phi(G)\le k(5-d)-2<0.
\]

Thus, for every fixed degree, the regular counterexample problem is finite.
The ordinary diameter-four Moore bound gives

\[
|V(G)|
\le
1+k\sum_{i=0}^{3}(k-1)^i
=k^4-2k^3+2k^2+1.
\]

## 2. The remaining diameter-four regime

### Theorem 3

Let \(G\) be connected, \(k\)-regular, have girth at least five, and diameter
four.  Then

\[
\boxed{
\lambda_{\min}(D(G))
\le -\frac{7+\sqrt{16k+1}}2.
}
\]

Consequently,

\[
\boxed{
\Phi(G)
\le k-\frac{7+\sqrt{16k+1}}2.
}
\]

In particular, no regular strict counterexample of degree at most nine has
diameter four.

### Proof

Choose vertices \(u,v\) at distance four, and put

\[
U=N(u),\qquad V=N(v).
\]

The sets \(U,V\) are disjoint.  Let \(r\) be the number of pairs
\((a,b)\in U\times V\) at distance two.  For fixed \(a\in U\), every such
pair has a unique common neighbor.  Two distinct vertices of \(V\) cannot use
the same common neighbor, since that would create a 4-cycle through \(v\).
There are only \(k-1\) possible common neighbors other than \(u\), so

\[
r\le k(k-1).
\]

Every other pair in \(U\times V\) has distance at least three.  Therefore

\[
\sum_{a\in U,\,b\in V}d_G(a,b)
\ge 2r+3(k^2-r)
\ge 2k^2+k.
\tag{2}
\]

For positive \(\alpha,\beta\), define

\[
x_u=\alpha,
\quad x_a=\beta\ (a\in U),
\quad x_v=-\alpha,
\quad x_b=-\beta\ (b\in V),
\]

and set all other coordinates to zero.  The within-neighborhood distances are
two.  Moreover

\[
d(u,v)=4,
\qquad
d(u,b),d(a,v)\ge3.
\]

Using (2) for the cross-neighborhood contribution gives

\[
\frac{x^{\mathsf T}D(G)x}{x^{\mathsf T}x}
\le
\frac{-4\alpha^2-4k\alpha\beta-3k\beta^2}
{\alpha^2+k\beta^2}.
\]

After the change of variables \((\alpha,\sqrt{k}\,\beta)\), this is the
Rayleigh quotient of

\[
\begin{pmatrix}
-4&-2\sqrt{k}\\
-2\sqrt{k}&-3
\end{pmatrix}.
\]

Its least eigenvalue is

\[
-\frac{7+\sqrt{16k+1}}2.
\]

For \(2\le k\le9\), this quantity is strictly below \(-k\), proving the final
claim.  \(\square\)

### Corollary 4: regular counterexample trichotomy

Every regular strict counterexample has one of the following forms.

1. Diameter two: it is a Moore graph.
2. Diameter three: its nonprincipal adjacency spectrum lies in the strict
   shifted WOW window
   \[
   |\theta+1|<\sqrt{2k-2}.
   \]
3. Diameter four: necessarily \(k\ge10\).

There are no regular strict counterexamples of diameter at least five.

This does not prove that diameter-four counterexamples exist.  Whether every
regular girth-five diameter-four graph satisfies WOW-284 is left as an explicit
open direction.

## 3. A small-puncture normal form for Moore graphs

Let \(M\) be a degree-\(k\) Moore graph of diameter two, let
\(S\subseteq V(M)\), and put \(H=M-S\).

### Theorem 5

If \(|S|=s\le k-1\), then \(H\) is connected, has diameter at most three, and

\[
\boxed{
\delta^*(H)=k-\frac{s}{k}.
}
\]

Let \(B\) be the \(|V(H)|\times s\) incidence matrix

\[
B_{xz}=
\begin{cases}
1,&x\sim_M z,\\
0,&\text{otherwise},
\end{cases}
\qquad x\in V(H),\ z\in S.
\]

Then

\[
\boxed{
D(H)=2(J-I)-A(H)+BB^{\mathsf T}
-\operatorname{diag}(BB^{\mathsf T}).
}
\tag{3}
\]

### Proof

Any two nonadjacent vertices of a Moore graph have a unique common neighbor.
Suppose surviving vertices \(x,y\) have their unique common neighbor deleted.
For every

\[
a\in N(x)\setminus\{z\},
\]

where \(z\) is that deleted common neighbor, the nonadjacent pair \(a,y\) has a
unique common neighbor \(b_a\).  The paths

\[
x-a-b_a-y
\]

are internally vertex-disjoint as \(a\) ranges over the \(k-1\) choices; any
collision would create a triangle or a 4-cycle.  Since at most \(s-1\le k-2\)
of their internal vertices are deleted, one length-three path survives.  Thus
\(H\) is connected and has diameter at most three.

Deletion changes a surviving pair's distance only when the pair was
nonadjacent and its unique common neighbor belongs to \(S\); the distance then
changes from two to three.  For distinct surviving vertices \(x,y\), the
entry \((BB^{\mathsf T})_{xy}\) is exactly the number of their deleted common
neighbors, hence either zero or one.  Its diagonal entry counts deleted
neighbors of \(x\).  This proves (3).

For a surviving vertex \(x\), set

\[
t_x=|N_M(x)\cap S|.
\]

Then \(d_H(x)=k-t_x\).  A deleted neighbor of \(x\) cannot be adjacent to a
surviving neighbor of \(x\), by triangle-freeness.  Every other deleted vertex
has at most one common neighbor with \(x\).  Therefore

\[
\sum_{y\in N_H(x)}t_y\le s-t_x.
\]

It follows that

\[
\begin{aligned}
d_H^*(x)
&=k-\frac{\sum_{y\in N_H(x)}t_y}{k-t_x}\\
&\ge k-\frac{s-t_x}{k-t_x}\\
&\ge k-\frac{s}{k}.
\end{aligned}
\tag{4}
\]

To attain equality, observe that every distance-two sphere in \(M\) has
\(k^2-k\) vertices, while its complement has \(k+1\) vertices.  Hence

\[
\left|\bigcap_{z\in S}\Gamma_2(z)\right|
\ge k^2+1-s(k+1)
\ge2.
\]

Choose \(x\) in this intersection.  Such an \(x\) is automatically outside
\(S\), has \(t_x=0\), and each deleted vertex contributes once to
\(\sum_{y\in N_H(x)}t_y\).  Equality holds in (4), proving the formula for
\(\delta^*(H)\).  \(\square\)

## 4. Exact Hoffman--Singleton robustness radius

Specialize Theorem 5 to the degree-seven Hoffman--Singleton graph \(M\).  For
any deleted set \(S\) of size \(s\le6\),

\[
\delta^*(M-S)=7-\frac{s}{7}=\frac{49-s}{7}.
\]

### Theorem 6

For every \(S\subseteq V(M)\) with \(|S|\le5\), the induced graph \(M-S\) is a
strict counterexample to WOW-284.

This is sharp in the universal sense: there exists a six-vertex set \(S\) for
which \(M-S\) is not a strict counterexample.  Equivalently, the universal
vertex-deletion robustness radius of the Hoffman--Singleton counterexample is
exactly five.

### Exact finite certificate

The verifier embeds two explicit permutations on the 50 standard vertices.  It
then:

1. reconstructs their 175-edge pair orbit;
2. verifies a fixed relabeling to the manuscript's \(P/Q\) coordinate graph;
3. conjugates the permutations and checks every edge image directly;
4. partitions every labelled deletion set into verified automorphism orbits;
5. reconstructs every punctured distance matrix by integer BFS;
6. checks the dual degree from its definition using rational arithmetic;
7. checks (3) exactly; and
8. proves positive definiteness by exact rational \(LDL^{\mathsf T}\).

The orbit counts are

\[
\begin{array}{c|ccccc}
s&1&2&3&4&5\\
\hline
\text{orbits}&1&2&4&11&33.
\end{array}
\]

For every representative with \(s\le5\), the verifier proves

\[
\boxed{
7D(M-S)+(49-s)I\succ0.
}
\]

Therefore

\[
\lambda_{\min}(D(M-S))> -\frac{49-s}{7}
=-\delta^*(M-S),
\]

so all labelled deletion sets of size at most five give strict
counterexamples.

For sharpness, delete

\[
S=\{
P_{2,4},P_{3,1},P_{3,4},
Q_{2,1},Q_{3,4},Q_{4,4}
\}.
\]

The verifier reconstructs the 44-vertex graph, checks

\[
\delta^*(M-S)=\frac{43}{7},
\]

and gives an exact rational \(LDL^{\mathsf T}\) decomposition of

\[
7D(M-S)+43I
\]

with exactly one negative pivot and no zero pivot.  Hence

\[
\lambda_{\min}(D(M-S))< -\frac{43}{7},
\]

so this six-vertex deletion is not a strict counterexample.

## 5. Claim boundary and next work

This note proves no global minimality statement for order 38 and does not
classify all six-vertex deletions.  It also does not establish literature
priority for Theorems 1, 3, 5, or 6.  Before manuscript promotion, each result
requires:

1. a dedicated independent proof audit;
2. MathSciNet/zbMATH and citation-chain review;
3. confirmation that the embedded automorphism data have an appropriate source
   attribution even though correctness is checked internally; and
4. a selective manuscript plan, rather than automatic inclusion of every
   computational detail.

Run the exact verifier with

```text
python scripts/verify_diameter_puncture_extensions.py
```
