from .MuxGate import MuxGate

class Mux16Gate:
    def __init__(self):
        self.mux_gates = MuxGate()

    def __call__(self, a, b, select):
        # a and b are 16-bit lists
        output = [self.mux_gates(a[i], b[i], select) for i in range(16)]
        return output