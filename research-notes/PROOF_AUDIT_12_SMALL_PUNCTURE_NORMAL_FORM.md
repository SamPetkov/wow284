# Proof Audit 12: the small-puncture Moore normal form

**Audited result:** Theorem 5 of `DIAMETER_PUNCTURE_EXTENSIONS.md`.

**Verdict:** `pass_after_proof_expansion`.

The theorem is correct. The audit expands the internally vertex-disjoint
replacement-path argument and the equality case in the minimum dual-degree
calculation. No formula or parameter range changes.

## 1. Audited theorem

Let \(M\) be a degree-\(k\) Moore graph of diameter two, let
\(S\subseteq V(M)\) have size \(s\le k-1\), and put \(H=M-S\). Then \(H\) is
connected, has diameter at most three, and

\[
\boxed{\delta^*(H)=k-\frac{s}{k}.}
\]

Let \(B\) be the surviving-vertex by deleted-vertex incidence matrix,

\[
B_{xz}=\mathbf 1_{\{x\sim_M z\}},
\qquad x\in V(H),\ z\in S.
\]

Then

\[
\boxed{
D(H)=2(J-I)-A(H)+BB^{\mathsf T}
-\operatorname{diag}(BB^{\mathsf T}).
}
\tag{1}
\]

## 2. Hypothesis ledger

| Hypothesis | Exact use |
| --- | --- |
| Moore graph of diameter two | adjacent pairs have no common neighbor; nonadjacent pairs have exactly one; \(|V(M)|=k^2+1\) |
| \(s\le k-1\) | at most \(k-2\) internal vertices outside the deleted common neighbor can be removed from \(k-1\) disjoint replacement paths |
| induced deletion \(H=M-S\) | surviving adjacency is inherited and distances can only increase |

The theorem includes the boundary cases \(s=0\) and \(s=k-1\).

## 3. Replacement paths after deleting a common neighbor

Let \(x,y\in V(H)\) be nonadjacent in \(M\), and suppose their unique common
neighbor \(z\) lies in \(S\). For each

\[
a\in N_M(x)\setminus\{z\},
\]

the vertices \(a\) and \(y\) are nonadjacent; otherwise \(a\) would be a second
common neighbor of \(x,y\). Let \(b_a\) be their unique common neighbor. Then

\[
x-a-b_a-y
\]

is a length-three path.

The \(k-1\) paths are internally vertex-disjoint. Their first internal vertices
are distinct. If \(b_a=b_{a'}\) for \(a\ne a'\), then

\[
x-a-b_a-a'-x
\]

is a 4-cycle. If \(b_a=a'\), then \(a,a'\) are adjacent neighbors of \(x\),
forming a triangle. Thus no internal vertex is shared.

Besides \(z\), at most \(s-1\le k-2\) vertices are deleted. Since the \(k-1\)
paths have pairwise disjoint internal vertex sets, at least one survives.
Therefore a pair whose unique length-two path is destroyed has distance exactly
three in \(H\). This proves connectedness and diameter at most three.

## 4. Distance-matrix normal form

For distinct surviving vertices \(x,y\):

- if \(x\sim_M y\), their distance remains one and they have no common neighbor;
- if \(x\not\sim_M y\) and their unique common neighbor survives, their distance
  remains two;
- if that common neighbor lies in \(S\), their distance becomes three.

The off-diagonal entry \((BB^{\mathsf T})_{xy}\) counts deleted common
neighbors. In a Moore graph it is zero or one, and it is one exactly in the
third case. The diagonal of \(BB^{\mathsf T}\) counts deleted neighbors and is
subtracted to retain the zero diagonal of a distance matrix. This proves (1)
entry by entry.

## 5. Minimum dual degree

For \(x\in V(H)\), let

\[
t_x=|N_M(x)\cap S|.
\]

Then \(d_H(x)=k-t_x\). For each surviving neighbor \(y\in N_H(x)\), \(t_y\)
counts deleted neighbors of \(y\). A deleted neighbor of \(x\) cannot be
adjacent to \(y\), by triangle-freeness. Each deleted vertex not adjacent to
\(x\) has at most one common neighbor with \(x\). Hence

\[
\sum_{y\in N_H(x)}t_y\le s-t_x.
\]

Therefore

\[
\begin{aligned}
d_H^*(x)
&=k-\frac{\sum_{y\in N_H(x)}t_y}{k-t_x}\\
&\ge k-\frac{s-t_x}{k-t_x}\\
&\ge k-\frac{s}{k}.
\end{aligned}
\]

The last comparison is exact because

\[
\left(k-\frac{s-t}{k-t}\right)-\left(k-\frac{s}{k}\right)
=\frac{t(k-s)}{k(k-t)}\ge0.
\]

## 6. Attainment

Every distance-two sphere in \(M\) has \(k^2-k\) vertices, so its complement
has \(k+1\) vertices. The union bound gives

\[
\left|\bigcap_{z\in S}\Gamma_2(z)\right|
\ge k^2+1-s(k+1)\ge2.
\]

Choose \(x\) in this intersection. Then \(x\notin S\) and \(x\) is at distance
two from every deleted vertex, so \(t_x=0\). For each \(z\in S\), the unique
common neighbor \(y_z\) of \(x,z\) survives: if \(y_z\in S\), then \(x\) would
be adjacent to a deleted vertex, contradicting \(x\in\Gamma_2(y_z)\). Thus
each deleted vertex contributes exactly once to

\[
\sum_{y\in N_H(x)}t_y,
\]

which equals \(s\). Hence \(d_H^*(x)=k-s/k\), proving attainment.

## 7. Independent exact verification

Run

```text
python scripts/verify_proof_audit_12_small_puncture.py
```

The script does not import the original puncture verifier. It checks:

- the symbolic dual-degree comparison and boundary intersection count;
- every permitted deletion in \(C_5\) and the Petersen graph;
- every Hoffman--Singleton deletion of size at most two;
- deterministic Hoffman--Singleton controls through the boundary size six;
- connectivity, diameter, the exact normal form (1), and minimum dual degree;
- all destroyed common-neighbor pairs, their \(k-1\) internally disjoint
  replacement paths, and existence of a surviving path;
- an explicit attaining vertex for every audited deletion.

No floating-point arithmetic or numerical eigensolver is used.

## 8. Claim boundary

The theorem determines the metric correction and the minimum dual degree. It
does not give the complete distance spectrum for arbitrary \(S\), and it does
not assert that every deletion in the allowed range remains a WOW-284
counterexample. The spectral sign still depends on the deletion geometry.
