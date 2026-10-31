
from qiskit import QuantumCircuit
from qiskit.transpiler import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2

# Connect to IBM Quantum
service = QiskitRuntimeService()

# Create a two-qubit Bell State circuit
qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)
qc.measure_all()

# Run on both real quantum computers
backend_names = ["ibm_marrakesh", "ibm_kingston"]

for name in backend_names:

    print("\n================================")
    print("Running on:", name)
    print("================================")

    backend = service.backend(name)

    # Check whether the backend is operational
    status = backend.status()

    if not status.operational:
        print("Backend is not operational. Skipping.")
        continue

    # Compile circuit for this particular hardware
    pm = generate_preset_pass_manager(
        optimization_level=1,
        backend=backend
    )

    isa_circuit = pm.run(qc)

    # Create sampler
    sampler = SamplerV2(mode=backend)

    # Submit 100 shots
    job = sampler.run([isa_circuit], shots=100)

    print("Job ID:", job.job_id())
    print("Waiting for results...")

    # Wait for execution to finish
    result = job.result()

    # Display measurement counts
    counts = result[0].data.meas.get_counts()

    print("Backend:", name)
    print("Measurement results:", counts)

print("\nBoth backend experiments completed!")
