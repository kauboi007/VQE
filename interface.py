import qsharp as qs
import numpy as np
from scipy.optimize import minimize
from hamiltonian import parsepauli,getpaulicoeffs,parser
qs.init(project_root='.')


def run_vqe(atoms,basis="sto-3g",charge=0,multiplicity=1,shots=1000,runs=5):
    pd=parser(getpaulicoeffs(atoms,basis,multiplicity,charge))
    def costfn(t):
        energy=0
        for term,coeff in pd.items():
            if term=="I":
                energy+=coeff
            else:
                gates,qubits=parsepauli(term)
                gatesstr = "[" + ",".join(f'"{g}"' for g in gates) + "]"
                energy+=coeff*qs.eval(f"mkvqe.expval({gatesstr},{qubits},{[float(x) for x in t]},{shots})")

        return energy
    best=None; 
    for i in range(runs):
        t0 = np.random.uniform(0, 2*np.pi, 16)
        res = minimize(costfn, t0, method='COBYLA')
        if best is None or res.fun<best.fun:
            best=res
    print(f"Ground state energy in Hatrees:{best.fun}")
    print(f"Ground state energy in KJ/mol:{best.fun*2625.4996}")
    print(f"Final parameters: {best.x}")

run_vqe([('H', (0,0,0)), ('H', (0,0,0.74))])



    

