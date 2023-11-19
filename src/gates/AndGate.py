from .NandGate import NandGate
from .NotGate import NotGate

class AndGate:
    def __init__(self):
        self.nand = NandGate()
        self.not_gate = NotGate()

    def __call__(self, a, b):
        return self.not_gate(self.nand(a, b))