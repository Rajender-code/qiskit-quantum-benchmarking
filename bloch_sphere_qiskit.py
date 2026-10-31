from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector

# Create one-qubit circuit
qc = QuantumCircuit(1)

# Apply Hadamard gate
qc.h(0)

# Calculate state vector
state = Statevector.from_instruction(qc)

print("QUANTUM STATE:")
print(state)

# Display Bloch sphere
figure = plot_bloch_multivector(state)

figure.show()

