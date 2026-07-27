# Edge-walk microlemma for girth at least five

This note isolates the walk-count step used in Proof Audit 01.

## Lemma

Let \(G\) be a finite simple graph with no triangle or 4-cycle, and let
\(uv\in E(G)\).  If both endpoints have degree \(k\), then

\[
 (A^3)_{uv}=2k-1,
\]

and

\[
 (A^4)_{uv}=\sigma_{uv},
\]

where \(\sigma_{uv}\) is the number of 5-cycles containing the edge \(uv\).

## Length-three walks

The following walks always occur:

- \(u,v,u,v\);
- \(u,a,u,v\), one for each \(a\in N(u)\setminus\{v\}\);
- \(u,v,b,v\), one for each \(b\in N(v)\setminus\{u\}\).

They give \(1+(k-1)+(k-1)=2k-1\) walks.

Any remaining length-three walk would have the form

\[
 u-a-b-v
\]

with four distinct vertices.  Together with the edge \(vu\), this would be a
4-cycle.  Hence no further walk exists.

## Length-four walks

Consider a length-four walk

\[
 u=x_0,x_1,x_2,x_3,x_4=v.
\]

Consecutive vertices are distinct because the graph is simple.  We show that
all five vertices are distinct.

- If \(x_1=v\), then \(v,x_2,x_3,v\) is a triangle; loops are unavailable to
  degenerate this closed 3-walk.
- If \(x_3=u\), the symmetric triangle occurs.
- If \(x_2=u\), then \(x_3\) is adjacent to both \(u\) and \(v\), giving a
  triangle.
- If \(x_2=v\), then \(x_1\) is adjacent to both \(u\) and \(v\), giving a
  triangle.
- If \(x_1=x_3\), that common vertex is adjacent to both \(u\) and \(v\), again
  giving a triangle.
- The identities \(x_1=u\), \(x_2=x_1\), \(x_3=x_2\), and \(x_3=v\) would be
  loops and are impossible.

These cases exhaust every possible repetition.  Thus the walk is a simple
four-edge path from \(u\) to \(v\).  Adding the edge \(vu\) produces a 5-cycle.
Conversely, every 5-cycle containing \(uv\) has a unique complementary
four-edge path from \(u\) to \(v\).  The correspondence is bijective, proving

\[
 (A^4)_{uv}=\sigma_{uv}.
\]

The proof uses no regularity away from the two endpoints and no spectral
information.