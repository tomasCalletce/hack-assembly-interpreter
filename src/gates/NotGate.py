from .NandGate import NandGate

class NotGate:
    def __init__(self):
        self.nand = NandGate()

    def __call__(self, a):
        return self.nand(a, a)
