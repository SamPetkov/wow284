# Verified research extensions for WOW-284

**Status:** draft research note, not part of the submitted manuscript. Every
claim labelled **proved** below has an analytic proof and an exact check in
`scripts/verify_research_extensions.py`. Literature priority is handled
separately in `LITERATURE_AUDIT_EXTENSIONS.md`.

## 1. Radius-two interpretation of dual degree

### Proposition 1

Let `G` contain no triangle and no 4-cycle. For every vertex `v`,

\[
 d^*(v)=\frac{|B_2(v)|-1}{d(v)},
\]

where `B_2(v)` is the closed ball of radius two around `v`.

### Proof

For distinct neighbors `u,w` of `v`, the sets

\[
 N(u)\setminus\{v\},\qquad N(w)\setminus\{v\}
\]

are disjoint. An intersection would give a 4-cycle, while a member lying in
`N(v)` would give a triangle. These sets therefore partition the vertices at
distance two from `v`. Hence

\[
 |\Gamma_2(v)|=\sum_{u\in N(v)}(d(u)-1).
\]

Adding the center and first layer gives

\[
 |B_2(v)|
 =1+d(v)+\sum_{u\in N(v)}(d(u)-1)
 =1+\sum_{u\in N(v)}d(u).
\]

Division by `d(v)` proves the claim.

This identifies dual degree with normalized radius-two growth. The verifier
checks the identity at every vertex of five independently reconstructed
examples.

## 2. Operator form of the diameter-three mechanism

### Proposition 2

Let `G` be connected, `k`-regular, of girth at least five and diameter three.
Then

\[
 D=3J+(k-3)I-2A-A^2
\]

and

\[
 D+kI=3J+(2k-2)I-(A+I)^2.
\]

On the orthogonal complement of the all-ones vector,

\[
 (D+kI)|_{\mathbf1^\perp}
 =(2k-2)I-(A+I)^2.
\]

Consequently

\[
 \Phi(G)
 =2k-2-\left\|(A+I)|_{\mathbf1^\perp}\right\|^2.
\]

### Proof

Girth at least five implies that two vertices at distance two have exactly one
common neighbor, so the distance-two matrix is

\[
 A_2=A^2-kI.
\]

Diameter three gives `A_3=J-I-A-A_2`. Substitution in
`D=A+2A_2+3A_3` proves the first identity; completing the square proves the
second. On `\mathbf1^\perp`, `J` vanishes. The least eigenvalue of `D` is
therefore

\[
 k-2-\max_{\theta\ne k}(\theta+1)^2,
\]

and regularity gives `\delta^*=k`.

The exact verifier checks both matrix identities and the score formula for the
40- and 42-vertex graphs.

## 3. Deleting one vertex from a Moore graph

Let `M` be a degree-`k` Moore graph of diameter two and put

\[
 \Delta=\sqrt{4k-3}.
\]

### Theorem 3

For `H=M-v`,

\[
 |V(H)|=k^2,
 \qquad
 \delta^*(H)=k-\frac1k.
\]

Define

\[
 \rho_\pm
 =k^2-2\pm\sqrt{k(k^3-2k^2+3k-1)},
\]

\[
 m_+
 =\frac{k(k-2)(\Delta+1)}{2\Delta},
 \qquad
 m_-
 =\frac{k(k-2)(\Delta-1)}{2\Delta}.
\]

Then

\[
\begin{aligned}
 \operatorname{Spec}D(H)={}&\{\rho_+,\rho_-\}\\
 &\cup\{(-2+\sqrt{k})^{(k-1)},(-2-\sqrt{k})^{(k-1)}\}\\
 &\cup\left\{
 \left(-\frac{\Delta+3}{2}\right)^{(m_+)},
 \left(\frac{\Delta-3}{2}\right)^{(m_-)}
 \right\}.
\end{aligned}
\]

In particular,

\[
 \lambda_{\min}(D(H))=-2-\sqrt{k},
\]

and

\[
 \Phi(H)=k-\frac1k-2-\sqrt{k}.
\]

For integer `k\ge2`, the score is positive exactly when `k\ge5`.

### Proof

Partition the surviving vertices into

\[
 A=N(v),\qquad B=\Gamma_2(v),
\]

of sizes `k` and `k(k-1)`. Let `C` be the `A`-by-`B` incidence matrix and
let `B_0` be the adjacency matrix induced on `B`. The Moore identity gives

\[
 CC^{\mathsf T}=(k-1)I,
 \qquad
 CB_0=J-C,
\]

\[
 B_0^2+C^{\mathsf T}C=(k-1)I-B_0+J.
\]

The distance matrix is

\[
 D(H)=
 \begin{pmatrix}
 3(J-I)&2J-C\\
 2J-C^{\mathsf T}&2(J-I)-B_0
 \end{pmatrix}.
\]

There are three mutually orthogonal invariant parts.

1. On vectors constant on `A` and `B`, the normalized quotient is

   \[
   Q_1=
   \begin{pmatrix}
   3(k-1)&(2k-1)\sqrt{k-1}\\
   (2k-1)\sqrt{k-1}&2k^2-3k-1
   \end{pmatrix},
   \]

   whose eigenvalues are `\rho_\pm`.

2. For `z\perp\mathbf1_A`, the space spanned by `(z,0)` and
   `(0,C^{\mathsf T}z)` carries the matrix

   \[
   \begin{pmatrix}-3&-(k-1)\\-1&-1\end{pmatrix},
   \]

   with eigenvalues `-2\pm\sqrt{k}`. Each occurs `k-1` times.

3. On `\ker C`, the matrix `B_0` satisfies

   \[
   B_0^2+B_0-(k-1)I=0.
   \]

   Its two eigenvalues are `(-1\pm\Delta)/2`. The dimension and trace
   equations give multiplicities `m_+` and `m_-`; the corresponding distance
   eigenvalues are `-(\Delta+3)/2` and `(\Delta-3)/2`.

The dimensions add to

\[
 2+2(k-1)+k(k-2)=k^2.
\]

The smaller eigenvalue of `Q_1` is greater than `-2-\sqrt{k}`: after adding
`(2+\sqrt{k})I`, its first diagonal entry is positive and, with
`t=\sqrt{k}`, its determinant is

\[
 t^2(2t^4+2t^3-3t^2+2)>0.
\]

Also `\Delta<1+2\sqrt{k}`, so
`-(\Delta+3)/2>-2-\sqrt{k}`. This proves the least eigenvalue claim.

For `k\ge5`, positivity of the score is equivalent to

\[
 (k^2-2k-1)^2-k^3>0.
\]

After writing `k=m+5`, the left side is

\[
 m^4+15m^3+77m^2+149m+71>0.
\]

The cases `k=2,3,4` are negative by direct substitution.

## 4. Deleting the endpoints of an edge

### Theorem 4

Let `uv\in E(M)` and `H=M-\{u,v\}`. For `k\ge3`,

\[
 |V(H)|=k^2-1,
 \qquad
 \delta^*(H)=k-\frac2k.
\]

Define

\[
 \sigma_\pm
 =k^2-3\pm\sqrt{k^4-2k^3+3k^2-8k+7},
\]

\[
 a_+
 =\frac{(k-2)(k+(k-2)\Delta)}{2\Delta},
\]

\[
 a_-
 =\frac{(k-2)((k-2)\Delta-k)}{2\Delta}.
\]

Then

\[
\begin{aligned}
 \operatorname{Spec}D(H)={}&\{\sigma_+,\sigma_-,k-4\}\\
 &\cup\{(-2+\sqrt{k})^{(2k-4)},(-2-\sqrt{k})^{(2k-4)}\}\\
 &\cup\left\{
 \left(-\frac{\Delta+3}{2}\right)^{(a_+)},
 \left(\frac{\Delta-3}{2}\right)^{(a_-)}
 \right\}.
\end{aligned}
\]

Thus

\[
 \lambda_{\min}(D(H))=-2-\sqrt{k}
\]

and

\[
 \Phi(H)=k-\frac2k-2-\sqrt{k},
\]

which is positive exactly for integers `k\ge5`.

### Proof outline

Put

\[
 A=N(u)\setminus\{v\},
 \qquad
 B=N(v)\setminus\{u\},
\]

and let `C` be the remaining `(k-1)^2` vertices. The constant-on-cell
space splits into the antisymmetric line on `A\sqcup B`, with distance
eigenvalue `k-4`, and a two-dimensional symmetric quotient

\[
 Q_2=
 \begin{pmatrix}
 5k-8&\sqrt{(k-1)(2k-3)(4k-6)}\\
 \sqrt{(k-1)(2k-3)(4k-6)}&2k^2-5k+2
 \end{pmatrix},
\]

whose eigenvalues are `\sigma_\pm`.

The two incidence modules, one from `A` and one from `B`, each give the
matrix from Theorem 3 and therefore contribute `-2\pm\sqrt{k}`, each with
total multiplicity `2k-4`. The common kernel has dimension `(k-2)^2` and
inherits the Moore quadratic relation. Its trace is `k-2`, which yields
multiplicities `a_+` and `a_-`.

The dimensions add to

\[
 3+2(2k-4)+(k-2)^2=k^2-1.
\]

The smaller eigenvalue of `Q_2` is greater than `-2-\sqrt{k}`. With
`t=\sqrt{k}`, the determinant of `Q_2+(2+t)I` is

\[
 (t-1)(t+1)(2t^4+2t^3-3t^2+2t+6)>0
\]

for `k\ge3`. The remaining comparisons are immediate. The threshold
calculation reduces, for `k=m+5`, to

\[
 m^4+15m^3+75m^2+133m+44>0.
\]

## 5. A deletion-stability inequality

### Proposition 5

Let `G` be connected, let `S\subseteq V(G)`, and suppose `H=G-S` is
connected. Let

\[
 D_0=D(G)[V(H)],
 \qquad
 E_S=D(H)-D_0.
\]

Set

\[
 a=\delta^*(G),
 \qquad
 b=\delta^*(H),
 \qquad
 \gamma=a+\lambda_{\min}(D(G)).
\]

Then

\[
 \boxed{
 \Phi(H)\ge\gamma-(a-b)+\lambda_{\min}(E_S).
 }
\]

### Proof

We have

\[
 D(H)+bI=(D_0+aI)+E_S-(a-b)I.
\]

Cauchy interlacing gives

\[
 \lambda_{\min}(D_0+aI)\ge\gamma,
\]

and Weyl's inequality gives the displayed bound.

### Moore-graph consequences

For one deleted vertex,

\[
 E_S=A(K_k)\oplus0,
 \qquad
 \lambda_{\min}(E_S)=-1,
 \qquad
 a-b=\frac1k.
\]

For the endpoints of an edge,

\[
 E_S=A(K_{k-1})\oplus A(K_{k-1})\oplus0,
 \qquad
 \lambda_{\min}(E_S)=-1,
 \qquad
 a-b=\frac2k.
\]

For two nonadjacent vertices, the distance-increase graph is two copies of
`K_k` meeting in their unique common vertex. Its least eigenvalue is

\[
 \frac{k-2-\sqrt{k^2+4k-4}}2.
\]

The resulting sufficient lower bound for the child score is positive for every
integer `k\ge6`. After the necessary exact squarings, the sign reduces to
positivity of

\[
\begin{aligned}
 P(k)={}&4k^8-39k^7+95k^6+9k^5-173k^4\\
 &-36k^3+116k^2+80k+16.
\end{aligned}
\]

For `k=m+6`,

\[
\begin{aligned}
 P(m+6)={}&4m^8+153m^7+2489m^6+22329m^5\\
 &+119437m^4+382236m^3+685268m^2\\
 &+559616m+75952>0.
\end{aligned}
\]

Hence deleting any two vertices of a degree-`k` Moore graph preserves strict
violation for `k\ge6`; for adjacent pairs, `k\ge5` suffices.

## 6. A fourth-moment order bound

### Proposition 6

Let `G` be `k`-regular, of girth at least five and diameter three, on `n`
vertices. Let `k=\theta_0,\theta_1,\ldots,\theta_{n-1}` be its adjacency
eigenvalues and put `y_i=\theta_i+1` for `i\ge1`. Then

\[
 \sum_{i=1}^{n-1}y_i^2=(k+1)(n-k-1),
\]

\[
 \sum_{i=1}^{n-1}y_i^4
 =(2k^2+5k+1)n-(k+1)^4.
\]

Consequently

\[
 \boxed{
 \Phi(G)\le
 \frac{(k+1)^2(k^2+3)-(5k+3)n}
 {(k+1)(n-k-1)}.
 }
\]

Every regular diameter-three counterexample therefore satisfies

\[
 \boxed{
 n<\frac{(k+1)^2(k^2+3)}{5k+3}.
 }
\]

### Proof

The girth condition gives

\[
 \operatorname{tr}A^3=0,
 \qquad
 \operatorname{tr}A^4=nk(2k-1).
\]

The second identity follows by summing squares of the entries of `A^2`: the
diagonal contribution is `nk^2`, and the ordered distance-two pairs contribute
`nk(k-1)`. Removing the principal eigenvalue and expanding
`(\theta_i+1)^2` and `(\theta_i+1)^4` gives the two moment identities.

If `R=\max_{i\ge1}|y_i|`, then

\[
 \sum y_i^4\le R^2\sum y_i^2.
\]

Since `\Phi(G)=2k-2-R^2`, substitution gives the bound.

## 7. Distance-layer compression

Write

\[
 n=k^2+1+c.
\]

Fix a vertex and let `a` be the average internal degree of its distance-two
layer. The normalized compression of `A` to the four distance layers is

\[
 S(a)=
 \begin{pmatrix}
 0&\sqrt{k}&0&0\\
 \sqrt{k}&0&\sqrt{k-1}&0\\
 0&\sqrt{k-1}&a&(k-1-a)\sqrt{\frac{k(k-1)}c}\\
 0&0&(k-1-a)\sqrt{\frac{k(k-1)}c}&
 k-\frac{k(k-1)(k-1-a)}c
 \end{pmatrix}.
\]

Feasibility gives

\[
 a\ge a_0:=k-1-\frac{c}{k-1}.
\]

Moreover, `S(a)-S(a_0)` is a positive semidefinite rank-one matrix. The
nonprincipal characteristic factor at `a_0` is

\[
 \frac{p_{k,c}(x)}{k-1},
\]

where

\[
 p_{k,c}(x)
 =(k-1)x^3+(c+k-1)x^2-(k-1)^2x-ck.
\]

The factor `1/(k-1)` is important: `p_{k,c}` has the correct roots but is not
itself the monic characteristic polynomial. Interlacing gives

\[
 \lambda_2(A)\ge r_{k,c},
\]

where `r_{k,c}` is the largest root of `p_{k,c}`.

For `k=6,c=15`,

\[
 p_{6,15}(x)=5(x+2)(x^2+2x-9),
\]

whose largest root is the WOW boundary `-1+\sqrt{10}`. Thus any strict
6-regular diameter-three counterexample has `c\le14`, and hence `n\le51`.

## 8. Higher-diameter distance-polynomial transfer

This section is a verified derivation but is **not** presented as a novelty
claim; it lies in the established distance-polynomial and minimal-cage
framework.

Define

\[
 F_0(x)=1,
 \qquad
 F_1(x)=x,
 \qquad
 F_2(x)=x^2-k,
\]

and for `i\ge3`,

\[
 F_i(x)=xF_{i-1}(x)-(k-1)F_{i-2}(x).
\]

If `G` is connected and `k`-regular, with diameter `d` and girth at least
`2d-1`, then for `0\le i\le d-1`,

\[
 A_i=F_i(A).
\]

Indeed, a nonbacktracking walk of length `i\le d-1` that is not geodesic
would create a cycle of length at most `2i-1`, and two distinct such walks
with the same endpoints would create a cycle of length at most `2i`.

Since

\[
 A_d=J-\sum_{i=0}^{d-1}A_i,
\]

we obtain

\[
 \boxed{
 D=dJ+q_d(A),
 \qquad
 q_d(x)=\sum_{i=0}^{d-1}(i-d)F_i(x).
 }
\]

The first two cases are

\[
 q_3(x)=k-3-2x-x^2,
\]

\[
 q_4(x)=-x^3-2x^2+(2k-4)x+2k-4.
\]

The exact verifier specifically checks the coefficient of `x^2` in `q_3`;
this corrected an earlier exploratory transcription error.

## 9. Exact computational coverage

Run

```text
python scripts/verify_research_extensions.py
```

The script checks, without floating point in any asserted conclusion:

- the radius-two dual-degree identity on five finite representatives;
- the operator identity and score formula on the 40- and 42-vertex graphs;
- exact characteristic polynomials and rational `LDL^T` certificates for
  one-vertex, adjacent-pair, and nonadjacent-pair punctures of the
  Hoffman--Singleton graph;
- the spectra of the three distance-increase matrices;
- the symbolic quotient factors, discriminants, multiplicities, and threshold
  polynomials for the one-vertex and edge-punctured Moore theorems;
- the nonadjacent-pair deletion-stability polynomial;
- the shifted spectral moments and the normalized layer factor;
- the `q_3` and `q_4` distance polynomials.

## 10. Claims deliberately not promoted

The following remain outside the proved core:

- **Regular counterexamples have degree at least six.** The analytic reduction
  is strong, but the last `(5,5)`-cage case still needs all four canonical graph
  records imported and checked locally.
- **The prime-field coordinate construction gives no infinite family.** The
  current Fourier argument excludes its diameter-three members for the tested
  parameter regime, not every higher-diameter member.
- **Order 38 is minimal.** No exhaustive canonical search below order 38 has
  been completed.
- **The punctured-Moore spectra are new.** The formulas are proved here, but
  literature priority is not established by failure to find a source.
- **An unconditional infinite family exists.** None has been proved.
