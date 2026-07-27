#!/usr/bin/env python3
"""Third fail-closed proof-completeness pass for the expanded manuscript."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "v22" / "main.tex"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise AssertionError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def main() -> None:
    text = TEX.read_text(encoding="utf-8")
    replacements: list[tuple[str, str, str]] = [
        (
            "publication-email",
            r"\email{samuil.petkov@phys.ens.psl.eu}",
            r"\email{samuil.petkov@ens.psl.eu}",
        ),
        (
            "forward-dependency",
            "\\begin{proof}\n"
            "Let the degree be \\(k\\).  Lemma~\\ref{lem:diam-rayleigh} and strictness give\n"
            "\\(\\diam(G)<k\\).",
            "\\begin{proof}\n"
            "We use the LP ceiling proved independently in\n"
            "Theorem~\\ref{thm:lp-ceiling}; that theorem does not depend on the present\n"
            "degree reduction.  Let the degree be \\(k\\).\n"
            "Lemma~\\ref{lem:diam-rayleigh} and strictness give \\(\\diam(G)<k\\).",
        ),
        (
            "second-subconstituent-diameter",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  The remaining vertices sharing\n"
            "the unique neighbour of a chosen vertex are at distance three, so\n"
            "Theorem~\\ref{thm:diameter-three-score} applies.",
            "Thus \\(B\\) has principal eigenvalue \\(K-1\\), eigenvalue \\(-1\\) on\n"
            "\\(C^{\\mathsf T}(\\one^\\perp)\\), and the two Moore roots\n"
            "\\((-1\\pm\\sqrt{4K-3})/2\\) on \\(\\ker C\\).  It remains to identify the\n"
            "diameter of \\(X\\).  If the unique common neighbour in \\(M\\) of two\n"
            "nonadjacent vertices \\(x,y\\in X\\) lies in \\(X\\), their distance in \\(X\\)\n"
            "is two.  Otherwise it is their common parent in \\(N(v)\\).  Choose\n"
            "\\(b\\in N_X(x)\\).  Then \\(b\\not\\sim y\\), and the unique common neighbour\n"
            "\\(c\\) of \\(b,y\\) belongs to \\(X\\): it cannot be \\(v\\), and it cannot\n"
            "lie in \\(N(v)\\), since \\(b\\) and \\(y\\) have different parents there.\n"
            "Thus \\(x-b-c-y\\) is a path in \\(X\\).  Pairs with a common parent have no\n"
            "length-two path in \\(X\\), so \\(X\\) has diameter three and\n"
            "Theorem~\\ref{thm:diameter-three-score} applies.",
        ),
        (
            "one-puncture-path-location",
            "For distinct \\(a,a'\\in A\\), choose a neighbour \\(b\\in B\\) of \\(a\\).  The\n"
            "unique common neighbour \\(c\\) of \\(b,a'\\) lies in \\(B\\), giving the\n"
            "surviving path \\(a-b-c-a'\\).",
            "For distinct \\(a,a'\\in A\\), choose a neighbour \\(b\\in B\\) of \\(a\\).  The\n"
            "vertices \\(b,a'\\) are nonadjacent, and their unique common neighbour \\(c\\)\n"
            "lies in \\(B\\): it is not \\(v\\), since \\(b\\not\\sim v\\), and it is not in\n"
            "\\(A\\), since an edge inside \\(A\\) would form a triangle through \\(v\\).\n"
            "Hence \\(a-b-c-a'\\) is a surviving path.",
        ),
        (
            "edge-puncture-path-location",
            "Only pairs inside \\(A\\) or inside \\(B\\) lose a\n"
            "length-two path; the same unique-common-neighbour construction supplies a\n"
            "surviving length-three path.",
            "Only pairs inside \\(A\\) or inside \\(B\\) lose a length-two path.  For\n"
            "distinct \\(a,a'\\in A\\), choose a residual neighbour \\(c\\) of \\(a\\).  The\n"
            "vertices \\(c,a'\\) are nonadjacent, and their unique common neighbour is also\n"
            "residual: it cannot be one of the deleted endpoints, cannot lie in \\(A\\) by\n"
            "triangle-freeness, and cannot lie in \\(B\\) because no edge joins \\(A\\) to\n"
            "\\(B\\).  This gives a surviving length-three path; the argument for \\(B\\) is\n"
            "symmetric.",
        ),
        (
            "nonadjacent-score-bound",
            "Proposition~\\ref{prop:deletion-stability} gives a positive lower bound for\n"
            "the child score for every \\(k\\ge6\\).  After the sign-preserving squarings,\n"
            "the remaining condition is \\(P(k)>0\\), where\n",
            "Since the parent Moore graph has score\n"
            "\\(k-(3+\\Delta)/2\\) and \\(a-b=2/k\\),\n"
            "Proposition~\\ref{prop:deletion-stability} gives\n"
            "\\[\n"
            " \\Phi(H)\\ge\n"
            " \\frac{3k-5-\\Delta-\\sqrt{k^2+4k-4}}2-\\frac2k.\n"
            "\\]\n"
            "For \\(k\\ge6\\), the sign-preserving squarings reduce positivity of this\n"
            "lower bound to \\(P(k)>0\\), where\n",
        ),
        (
            "small-puncture-grammar",
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x.\n"
            "\\]\n"
            "and\n"
            "\\[\n"
            " d_H^*(x)\n"
            " \\ge k-\\frac{s-t_x}{k-t_x}\n"
            " \\ge k-\\frac{s}{k}.\n"
            "\\]\n",
            "\\[\n"
            " \\sum_{y\\in N_H(x)}t_y\\le s-t_x.\n"
            "\\]\n"
            "Consequently,\n"
            "\\[\n"
            " d_H^*(x)\n"
            " \\ge k-\\frac{s-t_x}{k-t_x}\n"
            " \\ge k-\\frac{s}{k},\n"
            "\\]\n"
            "where the last inequality follows from\n"
            "\\[\n"
            " \\left(k-\\frac{s-t}{k-t}\\right)-\\left(k-\\frac{s}{k}\\right)\n"
            " =\\frac{t(k-s)}{k(k-t)}\\ge0.\n"
            "\\]\n",
        ),
        (
            "nonadjacent-linebreak",
            "The direct sum,\n"
            "injectivity, orthogonality, all recomputed distances, and the polynomial sign\n",
            "The direct-sum decomposition, injectivity, orthogonality, all recomputed\n"
            "distances, and the polynomial sign\n",
        ),
    ]

    for label, old, new in replacements:
        text = replace_once(text, old, new, label)

    if any(ord(char) < 32 and char not in "\t\n" for char in text):
        raise AssertionError("control byte introduced in third pass")
    TEX.write_text(text, encoding="utf-8", newline="\n")
    print("v2.2 third proof-completeness pass: PASS")


if __name__ == "__main__":
    main()
