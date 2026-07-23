from __future__ import annotations
import importlib.util, random, math, time
from collections import deque
from fractions import Fraction
import numpy as np

spec=importlib.util.spec_from_file_location('v','/mnt/data/verify_wow284_38_40_42.py')
v=importlib.util.module_from_spec(spec);spec.loader.exec_module(v)
full,l=v.hoffman_singleton(); del0={('P',0,j) for j in range(5)}|{('Q',0,j) for j in range(5)}
g40,l40=v.induced(full,l,del0);g38,l38=v.induced(g40,l40,{('P',1,0),('P',1,1)})

def induced(g, delete):
 keep=[i for i in range(len(g)) if i not in delete]; mp={u:i for i,u in enumerate(keep)}
 return [set(mp[w] for w in g[u] if w in mp) for u in keep]

def valid(g):
 n=len(g)
 # symmetric and no loop assumed
 for i in range(n):
  for j in range(i+1,n):
   c=len(g[i]&g[j])
   if j in g[i]:
    if c: return False
   elif c>1:return False
 # connected
 seen={0};q=[0]
 for u in q:
  for w in g[u]:
   if w not in seen:seen.add(w);q.append(w)
 return len(seen)==n

def score(g):
 n=len(g);deg=[len(x) for x in g]
 dual=min(Fraction(sum(deg[w] for w in g[u]),deg[u]) for u in range(n))
 D=np.empty((n,n),dtype=float)
 for s in range(n):
  d=[-1]*n;d[s]=0;q=deque([s])
  while q:
   u=q.popleft()
   for w in g[u]:
    if d[w]<0:d[w]=d[u]+1;q.append(w)
  if -1 in d:return -1e9,dual,-1e9
  D[s]=d
 least=float(np.linalg.eigvalsh(D)[0])
 return float(dual)+least,dual,least

def edges(g):return [(u,v) for u in range(len(g)) for v in g[u] if u<v]

# choose best vertex-deletion start
starts=[]
for a in range(38):
 h=induced(g38,{a});s=score(h);starts.append((s[0],a,h,s))
starts.sort(reverse=True,key=lambda z:z[0])
print('start best',starts[0][0:2],starts[0][3])

rng=random.Random(284)
global_best=starts[0]
start_time=time.time()
for restart in range(12):
 base=starts[restart%min(len(starts),10)]
 cur=[set(x) for x in base[2]]; cur_s=base[3]; best=(cur_s[0],None,[set(x) for x in cur],cur_s)
 T0=0.08
 for it in range(4000):
  es=edges(cur)
  (a,b),(c,d)=rng.sample(es,2)
  if len({a,b,c,d})<4:continue
  if rng.random()<.5: x,y=a,c; z,w=b,d
  else: x,y=a,d; z,w=b,c
  if y in cur[x] or w in cur[z] or x==y or z==w:continue
  # remove old edges, add new
  cur[a].remove(b);cur[b].remove(a);cur[c].remove(d);cur[d].remove(c)
  cur[x].add(y);cur[y].add(x);cur[z].add(w);cur[w].add(z)
  if not valid(cur):
   cur[x].remove(y);cur[y].remove(x);cur[z].remove(w);cur[w].remove(z)
   cur[a].add(b);cur[b].add(a);cur[c].add(d);cur[d].add(c)
   continue
  new_s=score(cur)
  temp=T0*(1-it/4000)
  accept=new_s[0]>=cur_s[0] or rng.random()<math.exp((new_s[0]-cur_s[0])/max(temp,1e-6))
  if accept:
   cur_s=new_s
   if new_s[0]>best[0]:
    best=(new_s[0],(restart,it),[set(q) for q in cur],new_s)
    if new_s[0]>global_best[0]:
     global_best=(new_s[0],base[1],best[2],new_s)
     print('NEW GLOBAL',global_best[0], 'restart/it',restart,it,'dual/least',new_s[1:],'elapsed',time.time()-start_time,flush=True)
     if new_s[0]>1e-7:
      break
  else:
   cur[x].remove(y);cur[y].remove(x);cur[z].remove(w);cur[w].remove(z)
   cur[a].add(b);cur[b].add(a);cur[c].add(d);cur[d].add(c)
 if global_best[0]>1e-7:break
 print('restart',restart,'best',best[0],best[3])
print('FINAL',global_best[0],global_best[1],global_best[3])
if global_best[0]>-1e8:
 print('edges')
 print([(u,w) for u in range(37) for w in global_best[2][u] if u<w])
