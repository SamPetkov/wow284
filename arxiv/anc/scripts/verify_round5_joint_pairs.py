"""Exact receiving check, independently regenerating the degree moments."""
from pathlib import Path
import json, hashlib
R=Path(__file__).resolve().parent
raw=(R/'WOW_JOINT_PILOT.json').read_bytes()
data=json.loads(raw)
def choose2(n): return n*(n-1)//2
def moments(b,cap):
    states={(0,0)}
    for _ in range(b):
        states={(s+t,w+choose2(t)) for s,w in states for t in range(cap+1)}
    return states
cache={}
old=kept=0
removed=[]
witnesses=[]
for profile in data['kept']:
    a,b=profile['n2'],profile['n4']
    # The original filter's radius-two caps, recomputed from its definition.
    h=a+b
    D4=min(4,b-1,(h-9)//2) if b else 0
    D2=min(2,b,(h-5)//2) if a else 0
    if b:
        assert D4>=0
    if a:
        assert D2>=0
    states=cache.setdefault((b,D4),moments(b,D4))
    bysum={}
    for s,w in states: bysum.setdefault(s,[]).append(w)
    surviving=[]
    for x in profile['e44_candidates']:
        old+=1
        y,z=4*b-2*x,a-2*b+x
        found=None
        for W in sorted(bysum.get(2*x,[])):
            for a2 in range(a+1):
                a0,a1=a-y+a2,y-2*a2
                if min(a0,a1)<0 or a1+2*a2!=y: continue
                if D2<2 and a2: continue
                if D2<1 and a1: continue
                counts=(x+W+a2,z+W-6*x+6*b+a0,y+6*x-2*W+a1)
                assert min(counts)>=0
                assert sum(counts)==2*a+8*b
                if all(v<=cap for v,cap in zip(counts,(choose2(b),choose2(a),a*b))):
                    found=(W,a2);break
            if found is not None:break
        if found is None:
            removed.append((a,b,x))
        else:
            kept+=1;surviving.append(x)
            witnesses.append(dict(a=a,b=b,x=x,W=found[0],a2=found[1]))
    assert surviving,profile
    assert surviving==[v['x'] for v in profile['joint_candidates']],(a,b,surviving)
assert old==2540 and kept==2515
assert len(removed)==25 and all(1<=a<=4 and x==2*b for a,b,x in removed)
# Independent direct binomial identities at all permitted vertex degrees.
for t in range(5):
    assert choose2(4-t)==choose2(t)-3*t+6
    assert t*(4-t)==3*t-2*choose2(t)
out=dict(status='EXACT_FINITE_CHECK_PASS_NOT_GRAPH_EXISTENCE',
    input_sha256=hashlib.sha256(raw).hexdigest(),profiles=len(data['kept']),
    baseline_pairs=old,joint_pairs=kept,removed=removed,witnesses=witnesses)
(R/'WOW_JOINT_RECEIVING_CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='witnesses'},indent=2))
