from .HalfAdderGate import HalfAdderGate
from .OrGate import OrGate

class FullAdderGate:
    def __init__(self):
        self.half_adder_gate = HalfAdderGate()
        self.or_gate = OrGate()
        
    def __call__(self, a, b, c):
        sum_result, carry_result = self.half_adder_gate(a, b)
        sum_result, carry_result = self.half_adder_gate(sum_result, c)
        carry_result = self.or_gate(carry_result, self.half_adder_gate(a, b)[1])
        return sum_result, carry_result

  