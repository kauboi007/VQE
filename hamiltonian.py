#finished coding on 8/5/26 - 5:11PM
from openfermionpyscf import run_pyscf
from openfermion import jordan_wigner, MolecularData

def getpaulicoeffs(atoms,basis='sto-3g',multiplicity=1,charge=0):
    molecule=MolecularData(atoms,basis,multiplicity,charge)
    molecule=run_pyscf(molecule)
    hamiltonian=molecule.get_molecular_hamiltonian()
    qubitop=jordan_wigner(hamiltonian)
    return qubitop

def parser(qubitop):
    paulidic={}
    for key, coeff in qubitop.terms.items():
        pauli_str = ''.join(gate + str(idx) for idx, gate in key)
        if pauli_str == '':
            pauli_str = 'I'
        paulidic[pauli_str] = float(coeff)
    return paulidic

def parsepauli(paulistring):
    n=len(paulistring)
    gates=[]
    qubits=[]
    for i in range(0,n,2):
        gates.append(paulistring[i])
        qubits.append(int(paulistring[i+1]))
    return gates,qubits






