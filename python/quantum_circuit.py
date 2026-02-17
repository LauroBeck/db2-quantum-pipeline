from qiskit import QuantumCircuit
import math

def squash(x, scale=3.0):
    return 2 * math.atan(scale * x)

def build_circuit(ret, trend, vol):
    qc = QuantumCircuit(3, 3)

    qc.ry(squash(ret), 0)
    qc.ry(squash(trend), 1)
    qc.ry(squash(vol), 2)

    qc.cx(0, 1)
    qc.cx(1, 2)

    qc.measure([0,1,2], [0,1,2])
    return qc
