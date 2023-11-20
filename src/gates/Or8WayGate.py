from .OrGate import OrGate

class Or8WayGate:
    def __init__(self):
        self.or_gate = OrGate()

    def __call__(self, a):
        result = False
        for i in range(8):
            result = self.or_gate(result, a[i])
            if result:
                return True
        return False