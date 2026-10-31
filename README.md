### Multi-Backend Quantum Circuit Benchmarking via IBM Quantum

This repository demonstrates a complete, functional workflow for configuring, executing, and benchmarking quantum circuits on actual superconducting quantum processors using **Qiskit** and the **IBM Quantum Runtime API**. 

### Features

* **Live Hardware Telemetry:** Interrogates IBM Quantum infrastructure to check backend status, operational availability, queue lengths, and qubit constraints across multiple heavy-hex architectures (ibm_marrakesh, ibm_kingston).
* **Asynchronous Execution Management:** Submits quantum workloads remotely, handles real-time job execution monitoring (Job ID tracking), and handles remote execution lifetimes.
* **State Estimation & Processing:** Retrieves and visualizes probabilistic measurement outcomes from physical quantum hardware configurations.

### Project Structure

* compare_ibm_backends.py: Script to query real-time live cluster statistics and remaining compute allocation balances.
* run_both_backends.py: Build, validate, and execute operations simultaneously across different target quantum processors.
* bloch_sphere_qiskit.py: Script to compute quantum statevectors and visualize geometric state mappings.

### Hardware Experiment Results

The execution against actual quantum processors returned the following state measurement count distributions (100 total shots per experiment): 

### 1. Execution on ibm_marrakesh (156 Qubits)

* **Job ID:** dbj1h91kdqps738vlgg0
* **Measurement Distribution:** {'00': 52, '11': 42, '10': 2, '01': 4}

### 2. Execution on ibm_kingston (156 Qubits)

* **Job ID:** dbj1hbl6p51s73cjt4b0
* **Measurement Distribution:** {'00': 50, '01': 4, '11': 46}
