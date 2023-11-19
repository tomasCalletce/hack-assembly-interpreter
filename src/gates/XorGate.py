from gates.NandGate import NandGate
from gates.OrGate import OrGate
from gates.AndGate import AndGate

class XorGate:
    def __init__(self):
        self.nand = NandGate()
        self.or_gate = OrGate()
        self.and_gate = AndGate()

    def __call__(self, a, b):
        return self.and_gate(self.nand(a, b), self.or_gate(a, b))