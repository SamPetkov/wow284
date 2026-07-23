#!/usr/bin/env python3
"""Render padded exact rational LDL certificates."""
from __future__ import annotations
import sympy as sp
from lean3942_common import Spec, distance_matrix, lean_rat, lean_rat_matrix

def pad(matrix: sp.Matrix, n: int) -> sp.Matrix:
    result=sp.eye(n); result[:matrix.rows,:matrix.cols]=matrix; return result

def shard(name,lhs,rhs,r,rows):
    lines=[]
    for s in range(rows):
        lines += ['set_option maxRecDepth 25000 in',f'lemma {name}_rows_{r}_{s} : ∀ c d : Fin 5,',
          f'    ({lhs}) (coordPad {r} c) (coordPad {s} d) =',
          f'      ({rhs}) (coordPad {r} c) (coordPad {s} d) := by',
          '  intro c d','  fin_cases c <;> fin_cases d <;> decide','']
    lines += [f'lemma {name}_row_{r} (s : Fin {rows}) (c d : Fin 5) :',
      f'    ({lhs}) (coordPad {r} c) (coordPad s d) =',
      f'      ({rhs}) (coordPad {r} c) (coordPad s d) := by','  fin_cases s']
    lines += [f'  · exact {name}_rows_{r}_{s} c d' for s in range(rows)]
    return '\n'.join(lines)+'\n'

def assembly(name,lhs,rhs,rows):
    return f'''private lemma {name}_coord (r s : Fin {rows}) (c d : Fin 5) :
    ({lhs}) (coordPad r c) (coordPad s d) = ({rhs}) (coordPad r c) (coordPad s d) := by
  fin_cases r
'''+'\n'.join(f'  · exact {name}_row_{r} s c d' for r in range(rows))+f'''
theorem {name} : {lhs} = {rhs} := by
  ext i j; rw [← coordPad_surj i, ← coordPad_surj j]; exact {name}_coord _ _ _ _
'''

def ldl_outputs(spec: Spec) -> dict[str,str]:
    ns=spec.namespace; distance=distance_matrix(spec.graph)
    core=spec.shift_scale*distance+spec.shift_diag*sp.eye(spec.order)
    lower,delta=core.LDLdecomposition(hermitian=True); inverse=lower.inv()
    assert lower*delta*lower.T==core and inverse*lower==sp.eye(spec.order)
    pivots=[sp.factor(delta[i,i]) for i in range(spec.order)]
    assert all(x>0 for x in pivots)
    mpad,lpad,dpad,ipad=map(lambda m:pad(m,spec.pad_order),(core,lower,delta,inverse))
    assert lpad*dpad*lpad.T==mpad and ipad*lpad==sp.eye(spec.pad_order)
    pivec=pivots+[sp.Integer(1)]*(spec.pad_order-spec.order)
    out={f'lean/Wow284/{ns}/LDLDefinitions.lean':f'''import Wow284.{ns}.Basic
import Mathlib.Analysis.Matrix.PosDef
/-! Generated exact `{spec.shift_scale}D+{spec.shift_diag}I` LDL data; padding is an identity block. -/
namespace Wow284.{ns}
open Matrix
abbrev PadVertex := Fin {spec.pad_order}
def coordPad (r : Fin {spec.pad_rows}) (c : Fin 5) : PadVertex := ⟨5*r.val+c.val, by omega⟩
lemma coordPad_surj (v : PadVertex) :
    coordPad ⟨v.val/5, by omega⟩ ⟨v.val%5, Nat.mod_lt _ (by omega)⟩ = v := by
  apply Fin.ext; simp [coordPad]; omega
{lean_rat_matrix('Mcore',core,'Vertex')}
{lean_rat_matrix('Mpad',mpad,'PadVertex')}
{lean_rat_matrix('Lpad',lpad,'PadVertex')}
{lean_rat_matrix('LpadInv',ipad,'PadVertex')}
def pivotPad : PadVertex → ℚ := ![{', '.join(lean_rat(x) for x in pivec)}]
def DeltaPad : Matrix PadVertex PadVertex ℚ := diagonal pivotPad
end Wow284.{ns}
'''}
    for kind,name,lhs,rhs in [('Identity','ldl_identity','Lpad * DeltaPad * Lpad.transpose','Mpad'),
                              ('Left','lpad_left_inverse','LpadInv * Lpad','(1 : Matrix PadVertex PadVertex ℚ)')]:
        for r in range(spec.pad_rows):
            out[f'lean/Wow284/{ns}/LDL{kind}{r}.lean']=f'''import Wow284.{ns}.LDLDefinitions
/-! Generated rational identity shard {r+1}/{spec.pad_rows}. -/
namespace Wow284.{ns}
{shard(name,lhs,rhs,r,spec.pad_rows)}end Wow284.{ns}
'''
        imports='\n'.join(f'import Wow284.{ns}.LDL{kind}{r}' for r in range(spec.pad_rows))
        out[f'lean/Wow284/{ns}/LDL{kind}.lean']=f'''{imports}
namespace Wow284.{ns}
{assembly(name,lhs,rhs,spec.pad_rows)}end Wow284.{ns}
'''
    out[f'lean/Wow284/{ns}/LDLData.lean']=f'''import Wow284.{ns}.LDLIdentity
import Wow284.{ns}.LDLLeft
namespace Wow284.{ns}
open Matrix
theorem pivotPad_positive : ∀ i : PadVertex, 0 < pivotPad i := by decide
def embedPad (v : Vertex) : PadVertex := ⟨v.val, by omega⟩
lemma embedPad_injective : Function.Injective embedPad := by
  intro u v h; apply Fin.ext; simpa [embedPad] using congrArg Fin.val h
lemma Mpad_submatrix : Mpad.submatrix embedPad embedPad = Mcore := by ext i j; decide
end Wow284.{ns}
'''
    return out
