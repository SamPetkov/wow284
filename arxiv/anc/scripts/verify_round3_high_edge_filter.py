"""Exact necessary-profile enumeration for WOW-284, 1 November 2026.
Standard library only. No graph-realizability assertion or Lean replay.
Run: python scripts/verify_round3_high_edge_filter.py [output.json]
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json
import sys

def ceil_fraction(t):
    return -((-t.numerator)//t.denominator)

def enumerate_profiles():
    baseline=[]
    survivors=[]
    for b in range(51):
        for a in range(51-b):
            m=a+2*b
            if m%5:
                continue
            S2=4*a+16*b
            low=max(1950-m,ceil_fraction(Fraction(43*m*m-70200*m+119632500,58500)))
            high=min((Fraction(2200)-Fraction(5*m,6)-Fraction(S2,12)).__floor__(),
                     ceil_fraction(Fraction(4220000-2200*m-7*m*m,2000))-1)
            if low>high:
                continue
            row=dict(n0=50-a-b,n2=a,n4=b,m=m,N6_min=low,N6_max=high)
            baseline.append(row)
            h=a+b
            if (h and h<5) or (b and h<9) or h*(h-1)<4*a+16*b:
                continue
            B=comb(b,2)
            D4=min(4,b-1,(h-9)//2) if b else 0
            D2=min(2,b,(h-5)//2) if a else 0
            xs=[]
            for x in range(2*b+1):
                y=4*b-2*x
                z=a-2*b+x
                if x>B or y<0 or z<0 or 2*x>b*D4 or y>a*D2:
                    continue
                q,r=divmod(2*x,b) if b else (0,0)
                Wmin=b*q*(q-1)//2+r*q
                if max(0,y-a)+x+Wmin<=B:
                    xs.append(x)
            if xs:
                survivors.append(dict(row,e44_candidates=xs))
    assert len(baseline)==266
    assert len(survivors)==246
    ids={(r["n0"],r["n2"],r["n4"]) for r in survivors}
    removed=[r for r in baseline if (r["n0"],r["n2"],r["n4"]) not in ids]
    assert len(removed)==20
    return dict(status="NECESSARY_INTEGER_PROFILES_ONLY",baseline_count=266,
                surviving_count=246,removed_count=20,survivors=survivors,removed=removed)

if __name__=="__main__":
    result=enumerate_profiles()
    if len(sys.argv)>1:
        Path(sys.argv[1]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8",newline="\n")
    print(json.dumps({k:v for k,v in result.items() if not isinstance(v,list)},indent=2))
