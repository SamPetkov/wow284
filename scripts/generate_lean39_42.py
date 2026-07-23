#!/usr/bin/env python3
"""Generate and exactly validate the Lean certificates for orders 39 and 42."""
from __future__ import annotations
import argparse
from pathlib import Path
from lean3942_common import ROOT, spec39, spec42, verify_spec, basic, bridge, counterexample
from lean3942_finite import finite_outputs
from lean3942_ldl import ldl_outputs

def render() -> dict[Path,str]:
    outputs={}
    for spec in (spec39(),spec42()):
        verify_spec(spec)
        relative={f'lean/Wow284/{spec.namespace}/Basic.lean':basic(spec),
          f'lean/Wow284/{spec.namespace}/SpectralBridge.lean':bridge(spec),
          f'lean/Wow284/{spec.namespace}/Counterexample.lean':counterexample(spec)}
        relative.update(finite_outputs(spec)); relative.update(ldl_outputs(spec))
        outputs.update({ROOT/path:text for path,text in relative.items()})
    outputs[ROOT/'lean/Wow284Generated3942.lean']='''import Wow284.Induced39.Counterexample
import Wow284.Induced42.Counterexample
/-! Generated compilation target for the explicit order-39 and order-42 certificates. -/
'''
    outputs[ROOT/'lean/Wow284Generated3942Audit.lean']='''import Wow284Generated3942
/-! Generated axiom report for the order-39 and order-42 public endpoints. -/
#print axioms Wow284.Induced39.degree_profile
#print axioms Wow284.Induced39.semantic_distance_eq_Dcert
#print axioms Wow284.Induced39.ldl_identity
#print axioms Wow284.Induced39.lpad_left_inverse
#print axioms Wow284.Induced39.shifted_distance_real_posDef
#print axioms Wow284.Induced39.counterexample_endpoint
#print axioms Wow284.Induced42.degree_six
#print axioms Wow284.Induced42.semantic_distance_eq_Dcert
#print axioms Wow284.Induced42.ldl_identity
#print axioms Wow284.Induced42.lpad_left_inverse
#print axioms Wow284.Induced42.shifted_distance_real_posDef
#print axioms Wow284.Induced42.counterexample_endpoint
'''
    return outputs

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true'); p.add_argument('--verify-only',action='store_true')
    args=p.parse_args(); outputs=render()
    if args.verify_only:
        print('39/42 exact generator calculations: PASS'); return
    if args.check:
        stale=[x.relative_to(ROOT) for x,c in outputs.items() if not x.exists() or x.read_text()!=c]
        if stale: raise SystemExit('stale generated 39/42 Lean files: '+', '.join(map(str,stale)))
        print(f'39/42 Lean certificates: PASS ({len(outputs)} files)'); return
    for path,text in outputs.items():
        path.parent.mkdir(parents=True,exist_ok=True); path.write_text(text,encoding='utf-8',newline='\n')
        print(path.relative_to(ROOT))
if __name__=='__main__': main()
