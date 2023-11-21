from .AndGate import AndGate
from .NotGate import NotGate

class DMuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

    def __call__(self, input, select):
        not_select = self.not_gate(select)
        out_a = self.and_gate(input, not_select)
        out_b = self.and_gate(select, input)
        return out_a, out_b
