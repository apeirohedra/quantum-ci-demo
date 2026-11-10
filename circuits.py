"""Example circuits checked by Quantum CI/CD in pull requests."""

from qiskit import QuantumCircuit


def bell() -> QuantumCircuit:
    """Bell pair on two qubits, measured."""
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(0, 1)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])
    return circuit


def ghz() -> QuantumCircuit:
    """Three-qubit GHZ state, measured."""
    circuit = QuantumCircuit(3, 3)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.cx(1, 2)
    circuit.measure(range(3), range(3))
    return circuit
