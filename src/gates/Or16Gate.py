from .OrGate import OrGate

class Or16Gate:
    def __init__(self):
      self.or_gate = OrGate()

    def __call__(self, a, b):
        output = [self.or_gate(a[i],b[i]) for i in range(16)]
        return output