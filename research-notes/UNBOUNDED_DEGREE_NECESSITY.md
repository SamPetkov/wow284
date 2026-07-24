# Why an infinite regular counterexample family must have unbounded degree

Let \(G\) be a connected \(k\)-regular strict counterexample to WOW-284.
Regularity gives
\[
  \delta^*(G)=k.
\]
Choose vertices \(u,v\) at distance \(\operatorname{diam}(G)\).  The Rayleigh
quotient of the distance matrix at \(e_u-e_v\) is
\[
  rac{(e_u-e_v)^{\mathsf T}D(G)(e_u-e_v)}
       {\lVert e_u-e_v\rVert^2}
  =-d_G(u,v)
  =-\operatorname{diam}(G).
\]
Hence
\[
  \lambda_{\min}(D(G))\le-\operatorname{diam}(G).
\]
Strict violation means
\[
  0<\delta^*(G)+\lambda_{\min}(D(G))
   \le k-\operatorname{diam}(G),
\]
so
\[
  \operatorname{diam}(G)<k.
\]

Fix \(k\ge2\).  Every such graph has diameter at most \(k-1\).  The Moore
bound therefore gives
\[
  |V(G)|
  \le
  1+k\sum_{i=0}^{k-2}(k-1)^i.
\]
The right-hand side depends only on \(k\).  There are only finitely many
simple graphs on at most that many vertices, and therefore only finitely many
connected \(k\)-regular strict counterexamples.

Consequently, any infinite family of regular strict counterexamples must have
unbounded degree.

This argument is elementary and does not assert that an infinite family
exists.  It only supplies a necessary condition for one.
