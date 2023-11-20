from .AndGate import AndGate

class And16Gate:
    def __init__(self):
        self.and_gate = AndGate()

    def __call__(self, a, b):
        output = [self.and_gate(a[i],b[i]) for i in range(16)]
        return output