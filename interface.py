#finished coding on 8/5/26 - 5:11PM
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

#Example molecules - uncomment and run 
#due to the limitation of VQE itself , anything beyond LiH will take long time to finish
#feel free to play with , change the shots , change the amount of times you wanna run the optimization loop
#make a absolutely destructive molecule by changning the charge and multiplicity in the function call
#and most importantly have fun!

# Hydrogen molecule H2
# run_vqe([('H', (0,0,0)), ('H', (0,0,0.74))])

# Lithium Hydride LiH
# run_vqe([('Li', (0,0,0)), ('H', (0,0,1.6))])

# Helium Hydride HeH+ (charged)
# run_vqe([('He', (0,0,0)), ('H', (0,0,0.77))], charge=1)

# Water H2O - shots changed for better accuracy
# run_vqe([('O', (0,0,0)), ('H', (0,0.76,-0.48)), ('H', (0,-0.76,-0.48))], shots=2000)

# Beryllium Hydride BeH2 - shots changed for better accuracy
# run_vqe([('Be', (0,0,0)), ('H', (0,0,1.33)), ('H', (0,0,-1.33))], shots=2000)



    

