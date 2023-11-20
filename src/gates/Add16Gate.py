from .HalfAdderGate import HalfAdderGate
from .FullAdderGate import FullAdderGate

class Add16Gate:
    def __init__(self):
        self.half_adder_gate = HalfAdderGate()
        self.full_adder_gate = FullAdderGate()

    def __call__(self, a, b):
        result = [0] * 16
        carry = 0
        sum_result = 0

        sum_result, carry = self.half_adder_gate(a[15], b[15])
        result[0] = sum_result

        for i in range(14, -1, -1):
            sum_result, carry = self.full_adder_gate(a[i], b[i], carry)
            result[i] = sum_result
        
        return result

        


  