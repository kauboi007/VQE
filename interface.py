# H2 PAULI STRING -> E = -0.8105 + 0.1721⟨IZ⟩ - 0.1721⟨ZI⟩ - 0.2227⟨ZZ⟩ + 0.1209⟨XX⟩ + 0.1209⟨YY⟩

import qsharp as qs
import numpy as np
from scipy.optimize import minimize
qs.init(project_root='.')
coeff=[-0.8105,0.1721,-0.1721,- 0.2227,0.1209,0.1209]#pauli coeff as an array

#cost function to get the expectation values from the qsharp code and substitute into the pauli string
def costfn(t):
    res = qs.eval(f"mkvqe.measureall({[float(x) for x in t]}, 1000)")
    return coeff[0]+res[0]*coeff[1]+res[1]*coeff[2]+res[2]*coeff[3]+res[3]*coeff[4]+res[4]*coeff[5]
best=None;
for i in range(5):
    t0 = np.random.uniform(0, 2*np.pi, 4)
    res = minimize(costfn, t0, method='COBYLA')
    if best is None or res.fun<best.fun:
        best=res
    
print(f"Ground state energy in Hatrees:{best.fun}")
print(f"Ground state energy in KJ/mol:{best.fun*2625.4996}")
fp=best.x # final parameters array
print(f"Final parameters: t1={fp[0]} t2={fp[1]} t3={fp[2]} t4={fp[3]}")
