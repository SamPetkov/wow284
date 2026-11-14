/*
 * small_order_g6filter.c -- proved prefilter for strict WOW-284
 * counterexamples, applied to graph6 streams (for example from nauty geng).
 *
 * Reads graph6 lines (orders up to 62) on stdin.  A graph is DISCARDED when
 * some vertex v has  s_v / d_v <= 2 + sqrt(2),  where d_v is the degree and
 * s_v the sum of the neighbour degrees (so d*(v) = s_v / d_v), or when it has
 * an isolated vertex.  The test is exact integer arithmetic:
 *     s_v / d_v <= 2 + sqrt 2   <=>   a <= 0  or  a^2 <= 2 d_v^2,
 * with a = s_v - 2 d_v (sqrt 2 is irrational, so equality cannot occur for
 * d_v > 0).
 *
 * Why discarding is sound.  Let G be connected, of girth >= 5, with fewer
 * than 50 vertices and Phi(G) > 0.  If diam(G) <= 2, then G is a star
 * (Phi < 0) or a Moore graph of diameter two (non-adjacent vertices have
 * equal degree, adjacent ones too, so G is regular), and Phi > 0 forces
 * degree 7 or 57, i.e. 50 or 3250 vertices.  Hence diam(G) >= 3, and the
 * first four vertices of a diametral geodesic span an isometric path, whose
 * distance matrix D(P_4) has least eigenvalue -(2 + sqrt 2); by Cauchy
 * interlacing lambda_min(D) <= -(2 + sqrt 2), so delta* > 2 + sqrt 2.
 * A discarded graph has delta* <= 2 + sqrt 2.
 *
 * Usage:  geng -c -t -f [-D<max>] n [res/mod] | small_order_g6filter [--all]
 * Survivors (or every graph with --all) are copied to stdout; the line
 * "TOTAL <read> KEPT <written>" goes to stderr.
 */
#include <stdio.h>
#include <stdint.h>
#include <string.h>

int main(int argc, char **argv)
{
    char line[4096];
    unsigned long long total = 0, kept = 0;
    int keep_all = (argc > 1 && strcmp(argv[1], "--all") == 0);
    uint64_t adj[64];
    long deg[64];

    while (fgets(line, sizeof line, stdin)) {
        if (line[0] == '>' || line[0] == '\n') continue;
        int n = line[0] - 63;
        if (n < 1 || n > 62) {
            fprintf(stderr, "unsupported graph6 order\n");
            return 2;
        }
        memset(adj, 0, sizeof adj);
        const char *p = line + 1;
        int bitpos = 0, cur = 0;
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (bitpos == 0) {
                    cur = (*p++) - 63;
                    if (cur < 0 || cur > 63) {
                        fprintf(stderr, "malformed graph6 line\n");
                        return 2;
                    }
                    bitpos = 6;
                }
                bitpos--;
                if ((cur >> bitpos) & 1) {
                    adj[i] |= (uint64_t)1 << j;
                    adj[j] |= (uint64_t)1 << i;
                }
            }
        }
        total++;
        for (int v = 0; v < n; v++) deg[v] = __builtin_popcountll(adj[v]);
        int pass = 1;
        for (int v = 0; v < n && pass; v++) {
            if (deg[v] == 0) { pass = 0; break; }
            long sv = 0;
            uint64_t m = adj[v];
            while (m) {
                int u = __builtin_ctzll(m);
                m &= m - 1;
                sv += deg[u];
            }
            long a = sv - 2 * deg[v];
            if (a <= 0 || a * a <= 2 * deg[v] * deg[v]) pass = 0;
        }
        if (keep_all || pass) {
            kept++;
            fputs(line, stdout);
        }
    }
    fprintf(stderr, "TOTAL %llu KEPT %llu\n", total, kept);
    return 0;
}
