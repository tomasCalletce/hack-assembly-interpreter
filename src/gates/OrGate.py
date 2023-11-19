from .NandGate import NandGate
from .NotGate import NotGate

class OrGate:
    def __init__(self):
        self.nand = NandGate()
        self.not_gate = NotGate()

    def __call__(self, a, b):
        return self.nand(self.not_gate(a), self.not_gate(b))