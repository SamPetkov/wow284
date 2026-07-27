# Proof Audit 03: nonadjacent Moore-puncture distance spectrum

**Audited result:** `NONADJACENT_PUNCTURED_MOORE.md` and
`NONADJACENT_DIRECT_SUM_AUDIT.md`.

**Audit mode:** line-by-line and theorem-by-theorem. Every displayed formula is
assigned to a separate lemma, and the finite Hoffman--Singleton check is
independent of the original two verification scripts.

**Verdict:** `pass`.

The characteristic factorisation, invariant-space dimensions, multiplicities,
and dual-degree calculation are correct. During the audit, one compressed
metric step was expanded: pairs whose unique length-two route used a deleted
vertex are now given explicit surviving paths of length three in both this
audit and the primary theorem note. This justifies the distance-matrix formula
without requiring the audit to be read as a separate patch.

## 1. Normalised theorem

Let \(M\) be a degree-\(k\) Moore graph of diameter two, \(k\ge5\). Let \(u,v\)
be nonadjacent, let \(w\) be their unique common neighbour, and put
\(H=M-\{u,v\}\). Set

\[
 \Delta=\sqrt{4k-3}.
\]

Define

\[
\begin{aligned}
 R_k(x)={}&x^4+(10-2k^2)x^3
 +(2k^3-17k^2-2k+36)x^2\\
 &+(12k^3-49k^2-4k+53)x
 -2k^4+17k^3-38k^2+5k+20,
\end{aligned}
\]

and

\[
 M_-=
 \frac{k(k-2)+(k^2-4k+2)\Delta}{2\Delta},
 \qquad
 M_+=
 \frac{-k(k-2)+(k^2-4k+2)\Delta}{2\Delta}.
\]

Then

\[
\begin{aligned}
 \chi_{D(H)}(x)={}&(x-k+3)R_k(x)
 (x^2+4x-k+3)^{k-2}\\
 &\cdot(x^2+4x-k+5)^{k-2}
 \left(x+\frac{\Delta+3}{2}\right)^{M_-}
 \left(x-\frac{\Delta-3}{2}\right)^{M_+},
\end{aligned}
\]

and

\[
 \delta^*(H)=k-\frac2k.
\]

The exponents are genuine nonnegative integers whenever the assumed Moore graph
exists; the formulas themselves also encode the usual integrality restrictions
on possible Moore degrees.

## 2. Hypothesis ledger

| Hypothesis | Use |
| --- | --- |
| finite simple graph | symmetric adjacency and distance matrices; no loops |
| Moore graph of diameter two | order \(k^2+1\), common-neighbour identity \(A^2=(k-1)I-A+J\) |
| \(u,v\) nonadjacent | unique common neighbour \(w\); five-cell geometry |
| girth five | no triangles or 4-cycles; uniqueness of the path constructions |
| \(k\ge5\) | all cells used in the module proof are nontrivial and \(p+q\ne0\) |

## 3. Critical lemma A: five-cell geometry

Put

\[
 A=N(u)\setminus\{w\},\quad
 B=N(v)\setminus\{w\},\quad
 C=N(w)\setminus\{u,v\},
\]

and let \(Z\) be the remaining vertices. Their sizes are

\[
 1,\quad k-1,\quad k-1,\quad k-2,\quad (k-1)(k-2).
\]

The Moore common-neighbour rule gives:

1. the \(A\)--\(B\) edges form a perfect matching;
2. every \(a\in A\) and \(b\in B\) has \(k-2\) neighbours in \(Z\);
3. every \(c\in C\) has \(k-1\) neighbours in \(Z\);
4. every \(z\in Z\) has one neighbour in each of \(A,B,C\), and \(k-3\)
   neighbours in \(Z\).

For example, for \(a\in A\), the vertices \(a,v\) are nonadjacent and their
unique common neighbour cannot be \(u\) or \(w\); it therefore lies in \(B\).
Uniqueness in both directions gives the perfect matching. The remaining counts
follow by applying the same rule to the pairs \((u,z),(v,z),(w,z)\).

## 4. Critical lemma B: recomputed distances

A surviving pair keeps its original distance unless its unique common neighbour
was \(u\) or \(v\). These exceptional pairs are exactly the distinct pairs
inside \(N(u)=\{w\}\cup A\) or inside \(N(v)=\{w\}\cup B\).

Such a pair has no surviving path of length two, but it always has a path of
length three:

- for \(w,a\) with \(a\in A\), choose \(c\in C\); the nonadjacent pair
  \(a,c\) has a unique common neighbour \(z\in Z\), giving
  \(w-c-z-a\);
- for distinct \(a,a'\in A\), let \(b\in B\) be matched to \(a\); the
  nonadjacent pair \(b,a'\) has a unique common neighbour \(z\in Z\), giving
  \(a-b-z-a'\);
- the \(B\)-cases are symmetric.

Hence the exceptional distance is exactly three, not merely at least three.
If \(F\) is the adjacency matrix of the two copies of \(K_k\) on
\(\{w\}\cup A\) and \(\{w\}\cup B\), sharing \(w\), then

\[
 \boxed{D(H)=2(J-I)-A(H)+F.}
\]

This is the metric identity on which every later block calculation depends.

## 5. Critical lemma C: quotient factor

The five-cell partition is equitable for \(A(H)\), \(F\), and therefore \(D(H)\).
Its row-sum distance quotient is

\[
Q=
\begin{pmatrix}
0&3k-3&3k-3&k-2&2(k-1)(k-2)\\
3&3k-6&2k-3&2k-4&2k^2-7k+6\\
3&2k-3&3k-6&2k-4&2k^2-7k+6\\
1&2k-2&2k-2&2k-6&2k^2-7k+5\\
2&2k-3&2k-3&2k-5&2k^2-7k+5
\end{pmatrix}.
\]

The \(A/B\)-antisymmetric cell vector has eigenvalue \(k-3\). Exact determinant
expansion gives

\[
 \det(xI-Q)=(x-k+3)R_k(x).
\]

No symmetry of the row-sum quotient is required: it is the matrix of the
restriction of the symmetric distance operator to the five-dimensional
cell-constant invariant subspace.

## 6. Critical lemma D: incidence identities

Identify \(A\) and \(B\) through their matching. Let \(R_A,R_B,R_C\) be the
cell-to-\(Z\) incidence matrices and \(T\) the adjacency matrix on \(Z\). Block
comparison in

\[
 A(M)^2=(k-1)I-A(M)+J
\]

gives

\[
 R_AR_A^{\mathsf T}=R_BR_B^{\mathsf T}=(k-2)I,
 \qquad R_CR_C^{\mathsf T}=(k-1)I,
\]

\[
 R_AR_B^{\mathsf T}=J-I,
 \qquad R_AR_C^{\mathsf T}=R_BR_C^{\mathsf T}=J,
\]

\[
 R_AT+R_B=J-R_A,
 \quad R_BT+R_A=J-R_B,
 \quad R_CT=J-R_C,
\]

and

\[
 R_A^{\mathsf T}R_A+R_B^{\mathsf T}R_B+R_C^{\mathsf T}R_C+T^2
 =(k-1)I-T+J.
\]

Each identity has a direct common-neighbour interpretation; the audit verifier
checks every block numerically in the \(k=7\) graph.

## 7. Critical lemma E: orthogonal direct sum

For \(x\perp\mathbf1\) in \(\mathbb R^A\), put
\(p=R_A^{\mathsf T}x\) and \(q=R_B^{\mathsf T}x\). Then

\[
 \|p+q\|^2=2(k-3)\|x\|^2,
 \qquad
 \|p-q\|^2=2(k-1)\|x\|^2.
\]

Thus both maps are injective. Their images are orthogonal. The zero-sum
\(R_C^{\mathsf T}\)-image is injective and orthogonal to both. Every row of
\(R_A,R_B,R_C\) decomposes into its constant part and one of these zero-sum
images, so there are no unaccounted row-space directions. Therefore

\[
 \mathbb R^Z=
 \langle\mathbf1_Z\rangle\perp S_Z\perp A_Z\perp C_Z\perp K,
\]

where

\[
 K=\ker R_A\cap\ker R_B\cap\ker R_C
\]

and the dimensions are

\[
 1,\quad k-2,\quad k-2,\quad k-3,\quad (k-2)(k-4).
\]

The full vertex space decomposes orthogonally as

\[
 \mathcal Q\perp\mathcal S\perp\mathcal A\perp\mathcal C\perp K,
\]

with dimensions

\[
 5,\quad2(k-2),\quad2(k-2),\quad2(k-3),\quad(k-2)(k-4).
\]

Their sum is \(k^2-1\).

## 8. Critical lemma F: action matrices

Using the metric identity and the transposed incidence relations, the distance
operator has matrices

\[
 \begin{pmatrix}-4&-(k-3)\\-1&0\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-2\end{pmatrix},\qquad
 \begin{pmatrix}-2&-(k-1)\\-1&-1\end{pmatrix}
\]

on \(\mathcal S,\mathcal A,\mathcal C\), respectively. Their factors are

\[
 (x^2+4x-k+3)^{k-2},
 \quad (x^2+4x-k+5)^{k-2},
 \quad (x^2+3x+3-k)^{k-3}.
\]

On \(K\), one has \(D=-2I-T\) and

\[
 T^2+T-(k-1)I=0.
\]

The accounted trace of \(T\) outside \(K\) is \(-2(k-2)\). Since
\(\operatorname{tr}T=0\),

\[
 \operatorname{tr}(T|_K)=2(k-2).
\]

Dimension and trace determine the two residual multiplicities. Adding the
\(k-3\) copies contributed by \(\mathcal C\) yields \(M_-\) and \(M_+\).
This accounts for every factor and every algebraic multiplicity.

## 9. Critical lemma G: dual degree

In \(H\), the degrees are

\[
 d(w)=k-2,\qquad d(a)=d(b)=k-1,\qquad d(c)=d(z)=k.
\]

The corresponding dual degrees are

\[
 d^*(w)=k,\qquad
 d^*(a)=d^*(b)=k-\frac1{k-1},\qquad
 d^*(c)=d^*(z)=k-\frac2k.
\]

For \(k>2\), the last value is smallest, proving

\[
 \delta^*(H)=k-\frac2k.
\]

## 10. Independent finite audit

`scripts/verify_proof_audit_03_nonadjacent_puncture.py` reconstructs the
punctured Hoffman--Singleton graph directly from coordinates. It does not
import either original puncture verifier. It checks:

1. every cell and adjacency count;
2. the explicit length-three replacement paths behind the distance formula;
3. every incidence identity;
4. the quotient row sums and characteristic factor;
5. pairwise orthogonality, invariance, and full rank of the five modules;
6. the block action matrices and complete characteristic polynomial;
7. all vertex degrees and dual degrees;
8. an exact rational \(LDL^{\mathsf T}\) certificate for the strict \(k=7\)
   inequality.

## 11. Verdict

The spectrum theorem is valid. The logically material expository correction
has been inserted into the primary note before \(D=2(J-I)-A+F\). The proof is
complete and all multiplicities are accounted for.
