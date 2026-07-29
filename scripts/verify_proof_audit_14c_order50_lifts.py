#!/usr/bin/env python3
"""Independent replay of Proof Audit 14C.

This file does not import the primary verifier.  Type A is replayed from a fixed
six-class cubic census with a separately implemented affine enumeration.  Type B
uses an independently compiled C++ pair-basis/row-recurrence census and a fresh
symbolic completion calculation.
"""
from __future__ import annotations

from fractions import Fraction
import itertools
import json
from pathlib import Path
import subprocess
import sys
import tempfile

import networkx as nx
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parents[1] if "scripts" in Path(__file__).parts else Path("/mnt/data")
CPP_SOURCE = ROOT / "scripts" / "order50_lift_independent.cpp"
FILTER_SOURCE = ROOT / "scripts" / "order50_completion_filter.cpp"
if not CPP_SOURCE.exists():
    CPP_SOURCE = Path("/mnt/data/order50_lift_independent.cpp")
if not FILTER_SOURCE.exists():
    FILTER_SOURCE = Path("/mnt/data/order50_completion_filter.cpp")

CUBIC_EDGE_LISTS = [
    [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3),(4,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
    [(0,1),(0,2),(0,3),(1,2),(1,3),(2,4),(3,5),(4,6),(4,7),(5,6),(5,7),(6,7)],
    [(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6),(5,7),(6,7)],
    [(0,1),(0,2),(0,3),(1,2),(1,4),(2,5),(3,6),(3,7),(4,6),(4,7),(5,6),(5,7)],
    [(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,6),(4,7),(5,7),(6,7)],
    [(0,1),(0,2),(0,3),(1,4),(1,5),(2,4),(2,6),(3,5),(3,7),(4,7),(5,6),(6,7)],
]


def rational_psd(matrix: np.ndarray) -> bool:
    work = [[Fraction(int(matrix[i,j])) for j in range(matrix.shape[1])]
            for i in range(matrix.shape[0])]
    while work:
        n = len(work)
        keep = []
        for i in range(n):
            if work[i][i] < 0:
                return False
            if work[i][i] == 0:
                if any(work[i][j] for j in range(n)):
                    return False
            else:
                keep.append(i)
        if not keep:
            return True
        if len(keep) < n:
            work = [[work[i][j] for j in keep] for i in keep]
            n = len(work)
        pivot = work[0][0]
        column = [work[i][0] for i in range(1,n)]
        work = [[work[i+1][j+1]-column[i]*column[j]/pivot
                 for j in range(n-1)] for i in range(n-1)]
    return True


def exact_det(matrix: np.ndarray) -> int:
    a = [[int(x) for x in row] for row in matrix.tolist()]
    n = len(a)
    if not n:
        return 1
    sign, previous = 1, 1
    for k in range(n-1):
        pivot_row = next((i for i in range(k,n) if a[i][k]), None)
        if pivot_row is None:
            return 0
        if pivot_row != k:
            a[pivot_row], a[k] = a[k], a[pivot_row]
            sign *= -1
        pivot = a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                numerator = a[i][j]*pivot-a[i][k]*a[k][j]
                if k:
                    assert numerator % previous == 0
                    numerator //= previous
                a[i][j] = numerator
        previous = pivot
    return sign*a[-1][-1]


def certified_small_minor_filter(matrices: np.ndarray, maximum: int) -> np.ndarray:
    active = np.ones(len(matrices), dtype=bool)
    n = matrices.shape[1]
    for size in range(1, min(maximum,n)+1):
        for subset in itertools.combinations(range(n),size):
            ids = np.flatnonzero(active)
            if not len(ids):
                return active
            ix = np.array(subset)
            minors = matrices[ids][:,ix[:,None],ix]
            approximate = np.linalg.det(minors.astype(float))
            for local in np.flatnonzero(approximate < -0.25):
                if exact_det(minors[local]) < 0:
                    active[ids[local]] = False
    return active


def upper_matrix(values: list[int] | np.ndarray, order: int) -> np.ndarray:
    result = np.zeros((order,order), dtype=np.int8)
    t = 0
    for i in range(order):
        for j in range(i+1,order):
            result[i,j] = result[j,i] = int(values[t]); t += 1
    return result


def affine_arrays(expressions, parameters):
    zero = {p:0 for p in parameters}
    coeff = [[sp.Rational(e.coeff(p)) for p in parameters] for e in expressions]
    const = [sp.Rational(e.subs(zero)) for e in expressions]
    denoms = [x.q for row in coeff for x in row] + [x.q for x in const]
    denominator = int(sp.ilcm(*denoms)) if denoms else 1
    return (
        np.array([[int(x*denominator) for x in row] for row in coeff], dtype=np.int64),
        np.array([int(x*denominator) for x in const], dtype=np.int64),
        denominator,
    )


def ternary_affine_matrices(order, expressions, parameters, connected=True):
    coefficient, constant, denominator = affine_arrays(expressions, parameters)
    d = len(parameters); total = 3**d; rows=[]; ternary=np.array([-1,0,1],dtype=np.int64)
    for start in range(0,total,300000):
        stop=min(total,start+300000);ids=np.arange(start,stop,dtype=np.int64)
        assignments=np.empty((stop-start,d),dtype=np.int64);work=ids.copy()
        for column in range(d):assignments[:,column]=ternary[work%3];work//=3
        values=assignments@coefficient.T+constant
        ok=np.all((values==-denominator)|(values==0)|(values==denominator),axis=1)
        if np.any(ok):rows.append(values[ok])
    if not rows:return []
    rows=np.concatenate(rows)
    signed=np.stack([upper_matrix((row//denominator).astype(int),order).astype(int) for row in rows])
    grams=signed+2*np.eye(order,dtype=int)[None,:,:]
    active=certified_small_minor_filter(grams,4)
    output=[]
    for s,g in zip(signed[active],grams[active]):
        if connected and not nx.is_connected(nx.from_numpy_array((s!=0).astype(int))):continue
        if rational_psd(g):output.append(s.astype(np.int8))
    return output


def commutant_affine(adjacency: np.ndarray):
    n=len(adjacency);variables=[];S=sp.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            x=sp.symbols(f'a_{i}_{j}');variables.append(x);S[i,j]=S[j,i]=x
    A=sp.Matrix(adjacency.tolist())
    equations=list(S*A-A*S)+[sum(S[i,j] for j in range(n))-2 for i in range(n)]
    matrix,target=sp.linear_eq_to_matrix(equations,variables)
    solution=next(iter(sp.linsolve((matrix,target),variables)))
    parameters=sorted(set().union(*(e.free_symbols for e in solution)),key=str)
    return list(solution),parameters


def edge_affine(incidence: np.ndarray, signed_vertices: np.ndarray):
    n=incidence.shape[1];variables=[];T=sp.zeros(n)
    for i in range(n):
        for j in range(i+1,n):
            x=sp.symbols(f'b_{i}_{j}');variables.append(x);T[i,j]=T[j,i]=x
    C=sp.Matrix(incidence.tolist())
    equations=list(C*T-sp.Matrix(signed_vertices.tolist())*C)+[sum(T[i,j] for j in range(n))-2 for i in range(n)]
    matrix,target=sp.linear_eq_to_matrix(equations,variables)
    solution=next(iter(sp.linsolve((matrix,target),variables)))
    parameters=sorted(set().union(*(e.free_symbols for e in solution)),key=str)
    return list(solution),parameters


def graph_automorphisms(graph):
    matcher=nx.algorithms.isomorphism.GraphMatcher(graph,graph)
    return [tuple(m[i] for i in range(8)) for m in matcher.isomorphisms_iter()]


def matrix_key(matrix, permutation):
    return tuple(int(matrix[permutation[i],permutation[j]]) for i in range(len(permutation)) for j in range(i+1,len(permutation)))


def canonical_representatives(matrices, permutations):
    reps={}
    for matrix in matrices:
        keys=[matrix_key(matrix,p) for p in permutations];key=min(keys)
        if key not in reps:
            p=permutations[keys.index(key)];reps[key]=matrix[np.ix_(p,p)].copy()
    return list(reps.values())


def incidence(graph):
    edges=sorted(tuple(sorted(e)) for e in graph.edges());C=np.zeros((8,12),dtype=int)
    for j,(u,v) in enumerate(edges):C[u,j]=C[v,j]=1
    return C,edges


def edge_permutation(edges,p):
    lookup={edge:i for i,edge in enumerate(edges)}
    return tuple(lookup[tuple(sorted((p[u],p[v])))] for u,v in edges)


def audit_type_a_independent():
    graphs=[]
    for edges in CUBIC_EDGE_LISTS:
        graph=nx.Graph();graph.add_nodes_from(range(8));graph.add_edges_from(edges)
        assert all(graph.degree(v)==3 for v in graph)
        graphs.append(graph)
    assert all(not nx.is_isomorphic(graphs[i],graphs[j]) for i in range(6) for j in range(i+1,6))
    orbit_counts=[];pair_counts=[];survivors=[]
    for graph in graphs:
        adjacency=nx.to_numpy_array(graph,dtype=int)
        expressions,parameters=commutant_affine(adjacency)
        signed8=ternary_affine_matrices(8,expressions,parameters)
        permutations=graph_automorphisms(graph)
        reps=canonical_representatives(signed8,permutations);orbit_counts.append(len(reps))
        C,edges=incidence(graph);pairs={}
        for S2 in reps:
            expressions3,parameters3=edge_affine(C,S2)
            for S3 in ternary_affine_matrices(12,expressions3,parameters3):
                keys=[]
                for p in permutations:
                    ep=edge_permutation(edges,p);keys.append((matrix_key(S2,p),matrix_key(S3,ep)))
                pairs.setdefault(min(keys),(S2,S3))
        pair_counts.append(len(pairs));survivors.extend((graph,*pair) for pair in pairs.values())
    assert sorted(orbit_counts)==[0,2,7,15,18,31]
    assert pair_counts==[1,0,0,0,0,0]
    graph,S2,S3=survivors[0]
    assert sorted(len(c) for c in nx.connected_components(graph))==[4,4]
    # Re-solve final 6x12 binary intertwiner.
    cycle=np.zeros((6,6),dtype=int)
    for i in range(6):cycle[i,(i+1)%6]=cycle[(i+1)%6,i]=1
    variables=sp.symbols('m0:72');M=sp.Matrix(6,12,variables)
    equations=list(sp.Matrix(cycle.tolist())*M-M*sp.Matrix(S3.tolist()))
    equations += [sum(M[i,j] for j in range(12))-8 for i in range(6)]
    equations += [sum(M[i,j] for i in range(6))-4 for j in range(12)]
    matrix,target=sp.linear_eq_to_matrix(equations,variables);solution=next(iter(sp.linsolve((matrix,target),variables)))
    parameters=sorted(set().union(*(e.free_symbols for e in solution)),key=str);assert len(parameters)==6
    binary=0
    for values in itertools.product((0,1),repeat=6):
        sub=dict(zip(parameters,values));entries=[e.subs(sub) for e in solution]
        binary += all(e in (0,1) for e in entries)
    assert binary==0
    return {'signed_orbits':orbit_counts,'pair_orbits':pair_counts,'binary_solutions':binary}


def compile_cpp_backends(directory: Path) -> tuple[Path, Path]:
    census = directory / "independent_census"
    completion_filter = directory / "completion_filter"
    for source, executable in (
        (CPP_SOURCE, census),
        (FILTER_SOURCE, completion_filter),
    ):
        completed = subprocess.run(
            ["g++", "-O3", "-std=c++17", str(source), "-o", str(executable)],
            text=True,
            capture_output=True,
        )
        if completed.returncode:
            print(completed.stdout)
            print(completed.stderr, file=sys.stderr)
            raise SystemExit(completed.returncode)
    return census, completion_filter


def run_cpp_backend(executable: Path):
    completed = subprocess.run([str(executable)], check=True, text=True, capture_output=True)
    lines = completed.stdout.splitlines()
    assert lines[0] == "SIGNED10 57464 632 1152 192 960"
    assert lines[-2] == "LCOUNT 140 6 2 2 2"
    assert lines[-1] == "INDEPENDENT_CPP_PASS"
    reps = [line.removeprefix("LREP ") for line in lines if line.startswith("LREP ")]
    assert len(reps) == 6 and all(len(key) == 100 for key in reps)
    return reps

def cycle10():
    A=np.zeros((10,10),dtype=int)
    for i in range(10):A[i,(i+1)%10]=A[(i+1)%10,i]=1
    return A


def completion_space(L):
    edges=[(i,j) for i in range(10) for j in range(10) if L[i,j]];assert len(edges)==20
    X1=np.zeros((10,20),dtype=int);X3=np.zeros((10,20),dtype=int)
    for column,(i,j) in enumerate(edges):X1[i,column]=1;X3[j,column]=1
    variables=[];T=sp.zeros(20)
    for i in range(20):
        for j in range(i+1,20):
            x=sp.symbols(f't_{i}_{j}');variables.append(x);T[i,j]=T[j,i]=x
    C=sp.Matrix(cycle10().tolist())
    equations=list(sp.Matrix(X1.tolist())*T-C*sp.Matrix(X1.tolist()))
    equations += list(sp.Matrix(X3.tolist())*T-C*sp.Matrix(X3.tolist()))
    equations += [sum(T[i,j] for j in range(20))-2 for i in range(20)]
    matrix,target=sp.linear_eq_to_matrix(equations,variables);solution=next(iter(sp.linsolve((matrix,target),variables)))
    parameters=sorted(set().union(*(e.free_symbols for e in solution)),key=str)
    return list(solution),parameters


def audit_type_b_completions(keys, filter_executable: Path):
    records = []
    for key in keys:
        L = np.array([int(character) for character in key], dtype=np.int8).reshape(10,10)
        expressions, parameters = completion_space(L)
        coefficient, constant, denominator = affine_arrays(expressions, parameters)
        total = 3 ** len(parameters)
        ids = np.arange(total, dtype=np.int64)
        assignments = np.empty((total, len(parameters)), dtype=np.int64)
        work = ids.copy()
        ternary = np.array([-1,0,1], dtype=np.int64)
        for column in range(len(parameters)):
            assignments[:,column] = ternary[work % 3]
            work //= 3
        numerators = assignments @ coefficient.T + constant
        admissible = np.all(
            (numerators == -denominator)
            | (numerators == 0)
            | (numerators == denominator),
            axis=1,
        )
        rows = numerators[admissible]
        payload = [f"{len(rows)} 20"]
        payload.extend(
            " ".join(map(str, (row // denominator).astype(int))) for row in rows
        )
        completed = subprocess.run(
            [str(filter_executable)],
            input="\n".join(payload) + "\n",
            text=True,
            capture_output=True,
            check=True,
        )
        fields = completed.stdout.strip().split()
        assert fields[0] == "FILTER"
        candidate_count, rejected_count, survivor_count = map(int, fields[1:])
        assert candidate_count == len(rows)
        assert rejected_count + survivor_count == candidate_count
        assert survivor_count == 1

        bipartite = nx.Graph()
        bipartite.add_nodes_from(range(20))
        bipartite.add_edges_from(
            (left, 10 + right)
            for left in range(10)
            for right in range(10)
            if L[left,right]
        )
        records.append(
            (
                nx.number_connected_components(bipartite),
                len(parameters),
                candidate_count,
                survivor_count,
            )
        )
    from collections import Counter
    assert Counter(record[0] for record in records) == {1:2, 2:2, 5:2}
    assert sorted(record[1] for record in records) == [0,0,1,1,10,10]
    return records

def main():
    report = {"Type_A": audit_type_a_independent()}
    with tempfile.TemporaryDirectory(prefix="wow284-lift-independent-") as directory:
        census, completion_filter = compile_cpp_backends(Path(directory))
        keys = run_cpp_backend(census)
        report["Type_B_completions"] = audit_type_b_completions(
            keys, completion_filter
        )
    report["conclusion"] = "independent replay excludes both order-50 lifts"
    print("independent Proof Audit 14C: PASS")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
