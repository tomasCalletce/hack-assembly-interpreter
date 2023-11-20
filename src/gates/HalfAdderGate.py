from .XorGate import XorGate
from .AndGate import AndGate

class HalfAdderGate:
    def __init__(self):
        self.xor_gate = XorGate()
        self.and_gate = AndGate()
        
    def __call__(self, a, b):
        sum_result = self.xor_gate(a, b)
        carry_result = self.and_gate(a, b)
        return sum_result, carry_result
  