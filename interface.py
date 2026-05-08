# H2 PAULI STRING -> E = -0.8105 + 0.1721⟨IZ⟩ - 0.1721⟨ZI⟩ - 0.2227⟨ZZ⟩ + 0.1209⟨XX⟩ + 0.1209⟨YY⟩

import qsharp as qs
import numpy as np
from scipy.optimize import minimize
from hamiltonian import parsepauli,getpaulicoeffs,parser
qs.init(project_root='.')

atoms = [('H', (0,0,0)), ('H', (0,0,0.74))]
pd=parser(getpaulicoeffs(atoms))
def costfn(t):
    energy=0
    for term,coeff in pd.items():
        if term=="I":
            energy+=coeff
        else:
            gates,qubits=parsepauli(term)
            gatesstr = "[" + ",".join(f'"{g}"' for g in gates) + "]"
            energy+=coeff*qs.eval(f"mkvqe.expval({gatesstr},{qubits},{[float(x) for x in t]},1000)")

    return energy

best=None;
for i in range(5):
    t0 = np.random.uniform(0, 2*np.pi, 8)
    res = minimize(costfn, t0, method='COBYLA')
    if best is None or res.fun<best.fun:
        best=res
    
print(f"Ground state energy in Hatrees:{best.fun}")
print(f"Ground state energy in KJ/mol:{best.fun*2625.4996}")
fp=best.x # final parameters array
print(f"Final parameters: t1={fp[0]} t2={fp[1]} t3={fp[2]} t4={fp[3]}")
