# Direct-sum audit for the nonadjacent Moore puncture

**Status:** candidate closure of v2 Gate 4, pending independent review and green CI.  
**Companion theorem:** `research-notes/NONADJACENT_PUNCTURED_MOORE.md`.

Let \(M\) be a degree-\(k\) Moore graph of diameter two, \(k\ge5\), and delete
two nonadjacent vertices \(u,v\). Let \(w\) be their unique common neighbor and
write
\[
A=N(u)\setminus\{w\},\quad
B=N(v)\setminus\{w\},\quad
C=N(w)\setminus\{u,v\},
\]
with \(Z\) the remaining vertices. Their sizes are
\[
1,\quad k-1,\quad k-1,\quad k-2,\quad (k-1)(k-2).
\]

The five-cell partition is equitable for the recomputed distance matrix. The
constant-on-cell space \(\mathcal Q\) has dimension five and gives the quotient
factor \((x-k+3)R_k(x)\) recorded in the companion theorem.

## 1. Orthogonal images inside \(\mathbb R^Z\)

Identify \(A\) and \(B\) through their perfect matching. Let \(R_A,R_B,R_C\)
be the incidence matrices from the indicated cells to \(Z\). For
\[
  x\in\mathbf1^\perp\subseteq\mathbb R^A,
  \qquad p=R_A^{\mathsf T}x,\quad q=R_B^{\mathsf T}x,
\]
the Moore incidence identities give
\[
  \|p\|^2=\|q\|^2=(k-2)\|x\|^2,
  \qquad \langle p,q\rangle=-\|x\|^2.
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
All three images are orthogonal to \(\mathbf1_Z\). Hence
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

Combining each cell zero-sum space with its \(Z\)-image gives invariant
modules \(\mathcal S,\mathcal A,\mathcal C\), of dimensions
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
Thus their characteristic factors are
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

On \(K\), the adjacency operator \(T=A(Z)\) satisfies
\[
  T^2+T-(k-1)I=0,
\]
while the distance matrix acts as \(D=-2I-T\). The already accounted-for
trace of \(T\) is \(-2(k-2)\); since \(\operatorname{tr}T=0\),
\[
  \operatorname{tr}(T|_K)=2(k-2).
\]
Writing \(\Delta=\sqrt{4k-3}\), the two \(T|_K\) multiplicities are
\[
  \frac{(k-2)(k+(k-4)\Delta)}{2\Delta},
  \qquad
  \frac{(k-2)((k-4)\Delta-k)}{2\Delta}.
\]
After applying \(D=-2I-T\) and adding the \(k-3\) copies from
\(\mathcal C\), these are exactly the multiplicities in the companion theorem.

Finally,
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
Every eigenspace and multiplicity is therefore accounted for.

## 3. Independent finite audit at \(k=7\)

Run
```text
python scripts/verify_nonadjacent_direct_sum.py
```
The script constructs the punctured Hoffman--Singleton graph, builds all five
subspaces explicitly, verifies pairwise orthogonality and invariance, checks
that the complete basis has rank 48, and recovers coefficient-for-coefficient
the exact stored distance characteristic polynomial. No floating-point
ordering is used.
