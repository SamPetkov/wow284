# Proof Audit 01: edge-local exclusion of degree-six order 51

**Audited result:** the edge-local theorem in
`EDGE_LOCAL_ORDER50_OBSTRUCTION.md`.  
**Verdict:** `pass_after_correction`.  
**Correction found:** the original theorem statement omitted the diameter-three
hypothesis used by its proof.  The new lemma
`DEGREE_SIX_DIAMETER_REDUCTION.md` supplies the missing reduction and restores
the global degree-six statement.

## 1. Normalized theorem statement

Let \(G\) be a connected 6-regular graph of girth at least five.  If \(G\) is a
strict counterexample to WOW-284, then

\[
 |V(G)|\le50.
\]

The proof has two logically separate stages.

1. The diameter-reduction lemma proves that every such graph has diameter
   three.
2. The edge-local positive-semidefinite argument excludes order \(51\), while
   the preceding moment/layer argument already gives order at most \(51\).

No conclusion is claimed for irregular graphs.

## 2. Hypothesis ledger

| Hypothesis | Where it is used |
| --- | --- |
| simple graph | adjacency walk counts and zero diagonal |
| connected | principal adjacency eigenvalue \(k\) is simple; graph distance is finite |
| 6-regular | \(\delta^*=6\), fixed radius-two ball size, trace and edge counts |
| no triangles | neighbors of one vertex are pairwise nonadjacent; \((A^2)_{uv}=0\) on an edge |
| no 4-cycles | uniqueness of two-step branches; exclusion of non-geodesic length-four edge walks |
| strict WOW violation | the nonprincipal adjacency spectrum lies in the open shifted window after the diameter-three reduction |
| diameter three | used only in the adjacency-to-distance spectral identity; supplied globally by the new reduction lemma |

## 3. Dependency graph

The audited theorem depends on:

1. the exact diameter-three identity
   \[
   D=3J+(k-3)I-2A-A^2;
   \]
2. its consequence
   \[
   \Phi(G)>0
   \iff
   |\theta+1|<\sqrt{2k-2}
   \quad(\theta\ne k);
   \]
3. the previous exact order bound \(n\le51\) for degree six;
4. the new diameter-reduction lemma;
5. elementary walk and incidence counts proved below.

The order-51 contradiction itself does not use the classification of Moore
graphs, numerical eigenvalues, or canonical generation.

## 4. Critical lemma A: the centered polynomial is positive semidefinite

Set

\[
 f_k(x)=(x+2)^2\bigl((x+1)^2-(2k-2)\bigr).
\]

On the closed shifted window

\[
 -1-\sqrt{2k-2}\le x\le-1+\sqrt{2k-2},
\]

we have \(f_k(x)\le0\).  Also

\[
 f_k(k)=(k+2)^2(k^2+3)=C_k.
\]

For a connected \(k\)-regular diameter-three graph define

\[
 M=-f_k(A)+\frac{C_k}{n}J.
\]

On the principal eigenspace, \(J\) has eigenvalue \(n\), so the eigenvalue of
\(M\) is \(-f_k(k)+C_k=0\).  On \(\mathbf1^\perp\), \(J=0\), and the eigenvalues
are \(-f_k(\theta)\ge0\).  Hence \(M\succeq0\).

**Adversarial check.**  The open spectral window is not needed to prove
positive semidefiniteness.  An interior adjacency eigenvalue \(-2\) may give a
zero eigenvalue of \(M\); none of the order-51 inequalities assumes positive
definiteness.

## 5. Critical lemma B: exact edge walk counts

Expanding gives

\[
 f_k(x)=x^4+6x^3+(15-2k)x^2+(20-8k)x+12-8k.
\]

Let \(uv\in E(G)\), and let \(\sigma_{uv}\) be the number of 5-cycles through
that edge.

### Length three

There are exactly \(2k-1\) walks of length three from \(u\) to \(v\):

- \(u,v,u,v\);
- \(u,a,u,v\) for the \(k-1\) vertices \(a\in N(u)\setminus\{v\}\);
- \(u,v,b,v\) for the \(k-1\) vertices \(b\in N(v)\setminus\{u\}\).

Any other length-three walk would be a simple path from \(u\) to \(v\), and
adding the edge \(uv\) would create a 4-cycle.  Therefore

\[
 (A^3)_{uv}=2k-1.
\]

### Length four

Every length-four walk from \(u\) to \(v\) is simple.  Indeed, an internal
repetition produces either an immediate backtrack whose remaining edge creates
a triangle, or a closed subwalk of length three or four.  These are forbidden
by simplicity and girth at least five.  Thus each such walk is the complementary
four-edge path of a unique 5-cycle through \(uv\), and conversely every such
5-cycle supplies one walk.  Hence

\[
 (A^4)_{uv}=\sigma_{uv}.
\]

Together with \((A^2)_{uv}=0\) and \(A_{uv}=1\), this gives

\[
 f_k(A)_{uv}=\sigma_{uv}+4k+14.
\]

On the diagonal,

\[
 (A^2)_{vv}=k,\qquad (A^3)_{vv}=0,\qquad
 (A^4)_{vv}=k(2k-1),
\]

so

\[
 f_k(A)_{vv}=6(k+2).
\]

## 6. Critical lemma C: the \(2\times2\) PSD bounds

The principal submatrix of \(M\) on an edge has the form

\[
 \begin{pmatrix}a&b\\b&a\end{pmatrix}
\]

with

\[
 a=\frac{C_k}{n}-6(k+2),
\]

\[
 b=\frac{C_k}{n}-(4k+14)-\sigma_{uv}.
\]

Positive semidefiniteness gives \(a\ge0\) and \(a^2-b^2\ge0\), equivalently

\[
 -a\le b\le a.
\]

The upper inequality \(b\le a\) yields

\[
 \sigma_{uv}\ge2k-2,
\]

while \(b\ge-a\) yields

\[
 \sigma_{uv}\le
 \frac{2(k+2)^2(k^2+3)}n-10k-26.
\]

**Adversarial check.**  The two inequalities have opposite algebraic origins;
reversing either sign would destroy the order-51 conclusion.  The independent
verifier checks both identities before substituting any numerical parameter.

## 7. Critical lemma D: radius-two intersection bijection

For a \(k\)-regular graph without triangles or 4-cycles,

\[
 |B_2(u)|=|B_2(v)|=k^2+1.
\]

For an edge \(uv\), the intersection \(B_2(u)\cap B_2(v)\) is the disjoint union
of:

1. \(u,v\);
2. \(N(u)\setminus\{v\}\);
3. \(N(v)\setminus\{u\}\);
4. vertices at distance two from both endpoints.

For a vertex in the fourth class, uniqueness of two-step branches gives unique
vertices \(a\in N(u)\setminus\{v\}\) and
\(b\in N(v)\setminus\{u\}\).  The cycle

\[
 u-a-z-b-v-u
\]

is a 5-cycle through \(uv\).  Conversely, the vertex opposite \(uv\) on a
5-cycle belongs to the fourth class.  This is a bijection.  Therefore

\[
 |B_2(u)\cap B_2(v)|=2k+\sigma_{uv}.
\]

Writing \(n=k^2+1+c\) and using
\(B_2(u)\cup B_2(v)\subseteq V(G)\) gives

\[
 \sigma_{uv}\ge(k-1)^2-c.
\]

## 8. Critical lemma E: order-51 integrality contradiction

For \(k=6\), \(n=51\), and \(c=14\), the two exact bounds give

\[
 11\le\sigma_{uv}\le\frac{202}{17}<12.
\]

Thus every edge lies in exactly 11 five-cycles.  There are

\[
 |E(G)|=153
\]

edges, so counting incidences between edges and 5-cycles gives

\[
 5N_5=153\cdot11=1683,
\]

which is impossible modulo five.

Each 5-cycle contributes exactly five incidences, one for each of its distinct
edges.  No orientation or multiplicity factor is missing.

## 9. Audit conclusion

After adding the degree-six diameter reduction, every dependency of the
global theorem is explicit.  The edge-local order-51 argument itself is valid,
uses exact arithmetic throughout, and has no unaccounted strictness or
multiplicity step.

The theorem remains a statement about **regular degree-six** counterexamples.
It says nothing about irregular graphs or the minimal order of an arbitrary
counterexample.