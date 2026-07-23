#!/usr/bin/env python3
"""Render bounded finite structural and semantic-distance certificates."""
from __future__ import annotations
from pathlib import Path
from lean3942_common import Spec, distance_matrix, lean_int_matrix

def finite_outputs(spec: Spec) -> dict[str,str]:
    ns=spec.namespace; d=distance_matrix(spec.graph)
    degrees=tuple(len(row) for row in spec.graph)
    neighbor_degree_sums=tuple(
        sum(degrees[u] for u in spec.graph[v]) for v in range(spec.order)
    )
    attained_degree=degrees[spec.attained_vertex]
    attained_sum=neighbor_degree_sums[spec.attained_vertex]
    out={f"lean/Wow284/{ns}/CertificateDefinitions.lean": f'''import Wow284.{ns}.Basic
/-! BFS-generated exact distance matrix for the order-{spec.order} graph. -/
namespace Wow284.{ns}
open Matrix
{lean_int_matrix("Dcert",d)}
end Wow284.{ns}
'''}
    degprop=' ∨ '.join(f'degree (coordVertex {{r}} c) = {x}' for x in spec.degree_values)
    dual=f'({spec.dual_p} : ℚ) / {spec.dual_q}'
    for r in range(spec.row_count):
        parts=[f'import Wow284.{ns}.CertificateDefinitions\n',
          f'/-! Generated finite certificate shard {r+1}/{spec.row_count}. -/\nnamespace Wow284.{ns}\n',
          f'''set_option maxRecDepth 15000 in
lemma degree_range_row_{r} : ∀ c : Fin {spec.col_count}, {degprop.format(r=r)} := by decide
set_option maxRecDepth 15000 in
lemma dual_bound_nat_row_{r} : ∀ c : Fin {spec.col_count},
    {spec.dual_p} * degree (coordVertex {r} c) ≤
      {spec.dual_q} * neighborDegreeSum (coordVertex {r} c) := by decide
''']
        for s in range(spec.row_count):
            parts.append(f'''set_option maxRecDepth 15000 in
lemma diameter_rows_{r}_{s} : ∀ c d : Fin {spec.col_count},
    HasPathAtMostThree (coordVertex {r} c) (coordVertex {s} d) := by decide
set_option maxRecDepth 15000 in
lemma semantic_distance_rows_{r}_{s} : ∀ c d : Fin {spec.col_count},
    D (coordVertex {r} c) (coordVertex {s} d) =
      Dcert (coordVertex {r} c) (coordVertex {s} d) := by decide
''')
        parts.append(f'end Wow284.{ns}\n')
        out[f'lean/Wow284/{ns}/Finite{r}.lean']='\n'.join(parts)

    imports='\n'.join(f'import Wow284.{ns}.Finite{r}' for r in range(spec.row_count))
    degcases='\n'.join(f'  · exact degree_range_row_{r} c' for r in range(spec.row_count))
    dualcases='\n'.join(f'  · exact dual_bound_nat_row_{r} c' for r in range(spec.row_count))
    rows=[]
    for r in range(spec.row_count):
        rows.append(f'''private lemma diameter_row_{r} (s : Fin {spec.row_count}) (c d : Fin {spec.col_count}) :
    HasPathAtMostThree (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''+'\n'.join(f'  · exact diameter_rows_{r}_{s} c d' for s in range(spec.row_count)))
        rows.append(f'''private lemma semantic_distance_row_{r} (s : Fin {spec.row_count}) (c d : Fin {spec.col_count}) :
    D (coordVertex {r} c) (coordVertex s d) = Dcert (coordVertex {r} c) (coordVertex s d) := by
  fin_cases s
'''+'\n'.join(f'  · exact semantic_distance_rows_{r}_{s} c d' for s in range(spec.row_count)))
    if len(spec.degree_values)==1:
        degree=f'''private lemma degree_coord (r : Fin {spec.row_count}) (c : Fin {spec.col_count}) :
    degree (coordVertex r c) = {spec.degree_values[0]} := by
  fin_cases r
{degcases}
theorem degree_six (v : Vertex) : degree v = 6 := by
  rw [← coordVertex_surj v]; exact degree_coord _ _
theorem degree_positive (v : Vertex) : 0 < degree v := by
  rw [degree_six v]
  omega
'''
    else:
        disj=' ∨ '.join(f'degree v = {x}' for x in spec.degree_values)
        cdisj=' ∨ '.join(f'degree (coordVertex r c) = {x}' for x in spec.degree_values)
        degree=f'''private lemma degree_range_coord (r : Fin {spec.row_count}) (c : Fin {spec.col_count}) : {cdisj} := by
  fin_cases r
{degcases}
theorem degree_range (v : Vertex) : {disj} := by
  rw [← coordVertex_surj v]; exact degree_range_coord _ _
theorem degree_positive (v : Vertex) : 0 < degree v := by
  rcases degree_range v with h | h <;> omega
'''
    profile=' ∧\n    '.join(f'(Finset.univ.filter fun v : Vertex => degree v = {d}).card = {n}' for d,n in spec.degree_profile)
    dcases='\n'.join(f'  · exact diameter_row_{r} s c d' for r in range(spec.row_count))
    scases='\n'.join(f'  · exact semantic_distance_row_{r} s c d' for r in range(spec.row_count))
    u,v=spec.dist3_pair
    out[f'lean/Wow284/{ns}/FiniteCertificates.lean']=f'''{imports}
/-! Assembly of exact degree, dual-degree, diameter, and distance certificates. -/
namespace Wow284.{ns}
{degree}
theorem degree_profile : {profile} := by decide
private lemma dual_bound_nat_coord (r : Fin {spec.row_count}) (c : Fin {spec.col_count}) :
    {spec.dual_p} * degree (coordVertex r c) ≤
      {spec.dual_q} * neighborDegreeSum (coordVertex r c) := by
  fin_cases r
{dualcases}
private theorem dual_bound_nat (v : Vertex) :
    {spec.dual_p} * degree v ≤ {spec.dual_q} * neighborDegreeSum v := by
  rw [← coordVertex_surj v]
  exact dual_bound_nat_coord _ _
theorem dual_degree_lower_bound (v : Vertex) : {dual} ≤ dualDegree v := by
  unfold dualDegree
  have hdegree : (0 : ℚ) < (degree v : ℚ) := by
    exact_mod_cast degree_positive v
  apply (div_le_div_iff₀ (by norm_num : (0 : ℚ) < {spec.dual_q}) hdegree).2
  have hbound := dual_bound_nat v
  have hbound' :
      {spec.dual_p} * degree v ≤ neighborDegreeSum v * {spec.dual_q} := by
    simpa [mul_comm] using hbound
  exact_mod_cast hbound'
private lemma dual_degree_attained_data :
    degree ({spec.attained_vertex} : Vertex) = {attained_degree} ∧
      neighborDegreeSum ({spec.attained_vertex} : Vertex) = {attained_sum} := by decide
theorem dual_degree_attained : ∃ v : Vertex, dualDegree v = {dual} := by
  refine ⟨{spec.attained_vertex}, ?_⟩
  rcases dual_degree_attained_data with ⟨hdegree, hsum⟩
  norm_num [dualDegree, hdegree, hsum]

{chr(10).join(rows)}
private lemma diameter_coord (r s : Fin {spec.row_count}) (c d : Fin {spec.col_count}) :
    HasPathAtMostThree (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{dcases}
theorem diameter_at_most_three : ∀ u v : Vertex, HasPathAtMostThree u v := by
  intro u v; rw [← coordVertex_surj u, ← coordVertex_surj v]; exact diameter_coord _ _ _ _
set_option maxRecDepth 15000 in
theorem explicit_distance_three :
    ¬ HasPathAtMostTwo ({u} : Vertex) {v} ∧ HasPathAtMostThree ({u} : Vertex) {v} := by decide
private lemma semantic_distance_coord (r s : Fin {spec.row_count}) (c d : Fin {spec.col_count}) :
    D (coordVertex r c) (coordVertex s d) = Dcert (coordVertex r c) (coordVertex s d) := by
  fin_cases r
{scases}
theorem semantic_distance_eq_Dcert : D = Dcert := by
  ext i j; rw [← coordVertex_surj i, ← coordVertex_surj j]; exact semantic_distance_coord _ _ _ _
end Wow284.{ns}
'''
    return out
