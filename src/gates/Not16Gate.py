from .NotGate import NotGate

class Not16Gate:
    def __init__(self):
        self.not_gate = NotGate()

    def __call__(self, a):
        output = [self.not_gate(a[i]) for i in range(16)]
        return output
