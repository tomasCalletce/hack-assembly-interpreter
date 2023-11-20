from .AndGate import AndGate
from .OrGate import OrGate
from .NotGate import NotGate

class MuxGate:
    def __init__(self):
        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.not_gate = NotGate()

    def __call__(self, a, b, select):
        # if select is 0 return a otherwise return b
        not_select = self.not_gate(select)
        output_a = self.and_gate(a, not_select)
        output_b = self.and_gate(b, select)
        return self.or_gate(output_a, output_b)