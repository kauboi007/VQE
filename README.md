# ⚛️ VQE — Variational Quantum Eigensolver

<div align="center">

### Hybrid Quantum-Classical Ground State Solver built from scratch using Q# + Python

<img src="https://img.shields.io/badge/Q%23-Microsoft%20Quantum-blueviolet?style=for-the-badge" />
<img src="https://img.shields.io/badge/Python-Scientific%20Computing-yellow?style=for-the-badge&logo=python" />
<img src="https://img.shields.io/badge/OpenFermion-Quantum%20Chemistry-blue?style=for-the-badge" />
<img src="https://img.shields.io/badge/PySCF-Hartree--Fock-orange?style=for-the-badge" />
<img src="https://img.shields.io/badge/Status-Working-success?style=for-the-badge" />

<br/>

</div>

---

# 🧠 Overview

This project implements a **general-purpose Variational Quantum Eigensolver (VQE)** completely from scratch using **Q#** and **Python**.

Given any molecule, the pipeline:

- Generates its molecular Hamiltonian using quantum chemistry libraries
- Converts it into Pauli operators using the Jordan-Wigner transform
- Constructs a parameterized quantum circuit in Q#
- Uses a hybrid classical-quantum optimization loop to estimate the ground state energy

Unlike tutorial-style toy VQEs, this implementation is fully modular and molecule-agnostic.

> **This project is not vibecoded**

---

# ✨ Features

## ⚛️ Quantum Circuit (Q#)

- 4-qubit hardware-efficient ansatz
- 2 entangling layers
- 16 trainable variational parameters
- Runtime-generated Pauli measurements
- Automatic basis rotation:
  - `H` for X-basis
  - `S†H` for Y-basis
  - Identity for Z-basis
- Efficient parity-based multi-qubit measurements
- No hardcoded Hamiltonians or observables

---

## 🧪 Hamiltonian Generation (PySCF + OpenFermion)

- Accepts arbitrary molecular geometries
- Hartree-Fock electronic structure calculation via PySCF
- Jordan-Wigner transformation using OpenFermion
- Converts fermionic operators → qubit Pauli strings
- Supports:
  - Custom basis sets
  - Molecular charge
  - Spin multiplicity

---

## 📈 Classical Optimization (SciPy)

- COBYLA optimizer
- Multi-start optimization strategy
- Random parameter initialization
- Shot-count configurable
- Tracks best converged energy

---

## 🚀 General VQE Runner

Single call:

```python
run_vqe(...)
```

handles:

```text
Geometry → Hamiltonian → Ansatz → Expectation Values → Optimization → Ground State Energy
```

Outputs:
- Ground state energy (Hartree)
- Energy in kJ/mol
- Optimal variational parameters

---

# 🧬 Tested Molecules

| Molecule | Formula | Status |
|---|---|---|
| Hydrogen | H₂ | ✅ |
| Lithium Hydride | LiH | ✅ |
| Helium Hydride | HeH⁺ | ✅ |
| Water | H₂O | ✅ |
| Beryllium Hydride | BeH₂ | ✅ |

---

# 🏗️ Project Structure

```text
VQE/
├── src/
│   └── quantum.qs        # Q# ansatz + expectation value operations
│
├── hamiltonian.py        # PySCF/OpenFermion Hamiltonian generation
├── interface.py          # Optimizer + VQE driver
├── qsharp.json
└── README.md
```

---

# ⚙️ How It Works

```text
          Molecular Geometry
                   │
                   ▼
        PySCF Hartree-Fock Solver
                   │
                   ▼
        Molecular Integrals
                   │
                   ▼
   OpenFermion Jordan-Wigner Transform
                   │
                   ▼
        Qubit Hamiltonian (Pauli Terms)
                   │
                   ▼
      Q# Parameterized Ansatz |ψ(θ)⟩
                   │
                   ▼
   Expectation Values ⟨ψ(θ)|H|ψ(θ)⟩
                   │
                   ▼
        COBYLA Classical Optimizer
                   │
                   ▼
          Ground State Energy
```

---

# 📦 Installation

## Create Virtual Environment

```bash
python3 -m venv vqe-env
source vqe-env/bin/activate
```

---

## Install Dependencies

```bash
pip install qsharp pyscf openfermion openfermionpyscf numpy scipy
```

> Linux / WSL recommended for PySCF compatibility.

---

# ▶️ Example Usage

```python
from interface import run_vqe

geometry = [
    ("H", (0.0, 0.0, 0.0)),
    ("H", (0.0, 0.0, 0.74))
]

run_vqe(
    geometry=geometry,
    basis="sto-3g",
    charge=0,
    multiplicity=1,
    shots=2000
)
```

---

# 📊 Results

## Hydrogen Molecule (H₂)

| Method | Energy (Hartree) |
|---|---|
| Exact Hartree-Fock | -1.1175 |
| This VQE | -1.1077 |

### Error

```text
≈ 0.01 Hartree
```

Primarily limited by:
- finite sampling shots
- ansatz expressibility
- optimizer convergence

---

# 🔬 Example Hamiltonian

```text
-0.8126 I
+0.1712 Z0
-0.2228 Z1
+0.1686 Z0Z1
+0.1205 X0X1
```

Generated automatically from molecular integrals.

---

# 🧠 Technical Highlights

✅ Runtime-generated Pauli measurements  
✅ Molecule-agnostic architecture  
✅ General expectation value engine  
✅ Hybrid quantum-classical workflow  
✅ Multi-start optimization  
✅ Quantum chemistry integration  
✅ Fully extensible ansatz design  

---

# ⚠️ Known Limitations

- Simulator-only implementation
- Runtime increases rapidly with molecule size
- Larger systems require deeper ansatz layers
- Shot noise affects precision
- No error mitigation yet
- No hardware backend integration currently

---

# 🔮 Future Improvements

- UCCSD ansatz support
- Adaptive VQE (ADAPT-VQE)
- Error mitigation
- GPU acceleration
- Hardware execution support
- Parallel expectation evaluation
- Better optimizers (SPSA, CMA-ES, gradient-based methods)

---

# 🛠️ Built With

- Q#
- Python
- PySCF
- OpenFermion
- NumPy
- SciPy

---
