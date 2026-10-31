from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService()

backend_names = ["ibm_marrakesh", "ibm_kingston"]

for name in backend_names:
    backend = service.backend(name)
    status = backend.status()

    print("\nBackend:", backend.name)
    print("Qubits:", backend.num_qubits)
    print("Operational:", status.operational)
    print("Pending jobs:", status.pending_jobs)

print("\nYour IBM Quantum usage:")
print(service.usage())