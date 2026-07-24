# Direct-sum audit for the nonadjacent Moore puncture

**Status:** candidate closure of v2 Gate 4, pending independent review and green CI.  
**Companion theorem:** `research-notes/NONADJACENT_PUNCTURED_MOORE.md`.

Let \(M\) be a degree-\(k\) Moore graph of diameter two, \(k\ge5\), and delete
two nonadjacent vertices \(u,v\). Let \(w\) be their unique common neighbor and
write
\[
A=N(u)\setminus\{w\},\qquad
B=N(v)\setminus\{w\},\qquad
C=N(w)\setminus\{u,v\},
\]
with \(Z\) the remaining vertices. Their sizes are
\[
1,\quad k-1,\quad k-1,\quad k-2,\quad (k-1)(k-2).
\]

The five-cell partition is equitable for the recomputed distance matrix. The
constant-on-cell space \(\mathcal Q\) has dimension five and gives the quotient
factor
\[
  (x-k+3)R_k(x)
\]
recorded in the companion theorem.

## 1. Orthogonal images inside \(\mathbb R^Z\)

Identify \(A\) and \(B\) through their perfect matching. Let \(R_A,R_B,R_C\)
be the incidence matrices from the indicated cells to \(Z\). For
\[
  x\in\mathbf1^\perp\subseteq\mathbb R^A,
\qquad
  p=R_A^{\mathsf T}x,\quad q=R_B^{\mathsf T}x,
\]
the Moore incidence identities give
\[
  \|p\|^2=\|q\|^2=(k-2)\|x\|^2,
  \qquad
  \langle p,q\rangle=-\|x\|^2.
\]
Consequently
\[
  \boxed{\|p+q\|^2=2(k-3)\|x\|^2,}
\qquad
  \boxed{\|p-q\|^2=2(k-1)\|x\|^2.}
\]
Both maps are injective for \(k\ge5\), and
\[
  \langle p+q,p'-q'\rangle=0.
\]

For \(y\perp\mathbf1\) in \(\mathbb R^C\), the vector
\(R_C^{\mathsf T}y\) is orthogonal to both matched-neighborhood images because
\[
  R_AR_C^{\mathsf T}=R_BR_C^{\mathsf T}=J.
\]
The identity \(R_CR_C^{\mathsf T}=(k-1)I\) makes this map injective. All
three images are orthogonal to \(\mathbf1_Z\). Moreover
\(\mathbf1_A^{\mathsf T}R_A=\mathbf1_Z^{\mathsf T}\), so every vector in
\(\ker R_A\), and hence every vector in \(K\), is orthogonal to
\(\mathbf1_Z\). The row spaces of \(R_A,R_B,R_C\) are therefore exactly the
orthogonal sum of the constant, symmetric, antisymmetric, and common-neighbor
images. Hence
\[
\boxed{
\mathbb R^Z
=
\langle\mathbf1_Z\rangle
\mathbin{\perp}S_Z
\mathbin{\perp}A_Z
\mathbin{\perp}C_Z
\mathbin{\perp}K,
}
\]
where
\[
K=\ker R_A\cap\ker R_B\cap\ker R_C
\]
and the dimensions are
\[
1,\quad k-2,\quad k-2,\quad k-3,\quad (k-2)(k-4).
\]

## 2. Invariant modules for the full distance matrix

Combining each cell zero-sum space with its \(Z\)-image gives modules
\[
  \mathcal S,\qquad \mathcal A,\qquad \mathcal C.
\]
The incidence identities
\[
R_AT+R_B=J-R_A,\qquad
R_BT+R_A=J-R_B,\qquad
R_CT=J-R_C
\]
give, on zero-sum vectors,
\[
T(p+q)=-2(p+q),\qquad T(p-q)=0,\qquad
T R_C^{\mathsf T}y=-R_C^{\mathsf T}y.
\]
Together with
\[
D=2(J-I)-A(H)+F,
\]
where \(F\) records the two overlapping deleted-neighborhood cliques, these
identities prove that all three modules are invariant and yield the action
matrices below. Their dimensions are
\[
  2(k-2),\qquad 2(k-2),\qquad 2(k-3).
\]
In natural two-component coordinates, the distance matrix acts by
\[
\begin{pmatrix}-4&-(k-3)\\-1&0\end{pmatrix}
\quad\text{on }\mathcal S,
\]
\[
\begin{pmatrix}-2&-(k-1)\\-1&-2\end{pmatrix}
\quad\text{on }\mathcal A,
\]
and
\[
\begin{pmatrix}-2&-(k-1)\\-1&-1\end{pmatrix}
\quad\text{on }\mathcal C.
\]
Thus their characteristic factors are respectively
\[
(x^2+4x-k+3)^{k-2},
\]
\[
(x^2+4x-k+5)^{k-2},
\]
and
\[
(x^2+3x+3-k)^{k-3}.
\]

The same incidence identities show that \(K\) is \(T\)-invariant: if
\(z\in K\), then \(z\perp\mathbf1_Z\), and multiplying the three displayed
identities by \(z\) gives \(R_ATz=R_BTz=R_CTz=0\).
On \(K\), the bottom-right Moore identity therefore reduces to
\[
  T^2+T-(k-1)I=0,
\]
while the distance matrix acts as \(D=-2I-T\). The already accounted-for
trace of \(T\) on
\(\langle\mathbf1_Z\rangle\perp S_Z\perp A_Z\perp C_Z\)
is \(-2(k-2)\); because \(\operatorname{tr}T=0\),
\[
  \operatorname{tr}(T|_K)=2(k-2).
\]
Writing \(\Delta=\sqrt{4k-3}\), the two \(T|_K\) multiplicities are therefore
\[
  \frac{(k-2)(k+(k-4)\Delta)}{2\Delta},
\qquad
  \frac{(k-2)((k-4)\Delta-k)}{2\Delta}.
\]
After the map \(D=-2I-T\), and after adding the \(k-3\) copies from
\(\mathcal C\), these give exactly the multiplicities \(M_-\) and \(M_+\)
in the companion theorem.

The quotient space is orthogonal to the four nonconstant modules: each cell
component has zero sum, each incidence image has zero total sum, and
\(K\perp\mathbf1_Z\). The symmetric and antisymmetric modules are mutually
orthogonal by the norm identities, the common-neighbor image is orthogonal to
both, and \(K\) is orthogonal to every incidence image. Finally,
\[
\boxed{
\mathbb R^{V(M-\{u,v\})}
=
\mathcal Q\perp\mathcal S\perp\mathcal A\perp\mathcal C\perp K,
}
\]
and
\[
5+2(k-2)+2(k-2)+2(k-3)+(k-2)(k-4)=k^2-1.
\]
Every eigenspace and every multiplicity is therefore accounted for.

## 3. Independent finite audit at \(k=7\)

Run
```text
python scripts/verify_nonadjacent_direct_sum.py
```
The script constructs the punctured Hoffman--Singleton graph, builds all five
subspaces explicitly, verifies pairwise orthogonality and invariance, checks
that the complete basis has rank 48, and recovers coefficient-for-coefficient
the exact stored distance characteristic polynomial. No floating-point
eigenvalue ordering is used.
