"""Independent exact algebra/profile check. No graph-existence search."""
from pathlib import Path
from fractions import Fraction as F
import json
R=Path(__file__).resolve().parent
f=[28,9,-1,-4];sizes=[1,6,30,13]
norm=sum(sizes[i]*f[i]**2 for i in range(4))
assert sum(sizes[i]*f[i] for i in range(4))==0 and norm==1508
assert all(-1+9-s-4*(5-s)==3*s-12 for s in range(6))
assert all(-4-(6-e)-4*e==-10-3*e for e in range(7))
# Each is a valid integer inequality on the entire admissible degree range.
assert all((s-2)*(s-3)>=0 for s in range(6))
assert all(e*(e-1)>=0 for e in range(7))
layer2=(9*(-180)+144*30,9*10-72*2)
layer3=(100*13-69*72,69*2)
lower=(82**2+6*32**2+layer2[0]+layer3[0],layer2[1]+layer3[1])
assert lower==(11900,84)
rayleigh=(F(10*norm-lower[0],norm),F(-lower[1],norm))
assert rayleigh==(F(795,377),F(-21,377))
assert rayleigh[0]+38*rayleigh[1]==-F(3,377)
# A separately generated three-variable form at tau=38, using minimal
# second moments only (not assuming their joint graphical realizability).
def quadratic(x,y,z):
    f0=-6*x-30*y-13*z
    ns=f0**2+6*x**2+30*y**2+13*z**2
    B0=f0+6*x;B1=f0+x+5*y
    # L2: x+y+5z+(y-z)*s, sum s=76, sum s^2=200.
    # L3: 6y+z+(z-y)*e, sum e=4, sum e^2=4.
    c2=x+y+5*z;d2=y-z;c3=6*y+z;d3=z-y
    bs=B0**2+6*B1**2+30*c2**2+2*c2*d2*76+d2**2*200+13*c3**2+2*c3*d3*4+d3**2*4
    return 10*ns-bs
basis=[(1,0,0),(0,1,0),(0,0,1)]
K=[[0]*3 for _ in range(3)]
for i in range(3):K[i][i]=quadratic(*basis[i])
for i in range(3):
    for j in range(i):
        aij=quadratic(*(basis[i][k]+basis[j][k] for k in range(3)))-K[i][i]-K[j][j]
        assert aij%2==0
        K[i][j]=K[j][i]=aij//2
assert K==[[240,944,316],[944,3844,1212],[316,1212,422]]
det=sum(K[0][j]*(K[1][(j+1)%3]*K[2][(j+2)%3]-K[1][(j+2)%3]*K[2][(j+1)%3]) for j in range(3))
assert det==-43200 and quadratic(9,-1,-4)==-12
profiles=[]
for j in range(11):
    m=5*j;S2=4*m
    lo=max(1950-m,(43*m*m-70200*m+119632500+58499)//58500)
    hi=min((26400-10*m-S2)//12,
        (4220000-2200*m-7*m*m-1)//2000)
    assert lo<=hi,(j,lo,hi)
    profiles.append(dict(n0=50-m,n2=m,n4=0,m=m,N6_min=lo,N6_max=hi,
        auxiliary_H='empty' if j==0 else f'C_{m} plus {50-m} isolated vertices'))
out=dict(status='EXACT_ARITHMETIC_PASS_NOT_GRAPH_EXISTENCE',layer_sizes=[1,6,30,13],
    vector=f,norm_squared=norm,Af_plus_f_norm_lower='11900+84*tau',
    rayleigh_bound='(795-21*tau)/377',tau38_bound='-3/377',matrix=K,
    determinant=det,profiles=profiles)
(R/'WOW_LAYER_EXACT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
