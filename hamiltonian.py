from openfermionpyscf import run_pyscf
from openfermion import jordan_wigner, MolecularData

def getpaulicoeffs(atoms,basis='sto-3g'):
    molecule=MolecularData(atoms,basis,1,0)
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

#test
atoms = [('H', (0, 0, 0)), ('H', (0, 0, 0.74))]
op = getpaulicoeffs(atoms)
print(parser(op))