from gates.NandGate import NandGate
from gates.NotGate import NotGate
from gates.AndGate import AndGate
from gates.OrGate import OrGate
from gates.XorGate import XorGate
from gates.MuxGate import MuxGate
from gates.Mux16Gate import Mux16Gate
from gates.HalfAdderGate import HalfAdderGate
from gates.FullAdderGate import FullAdderGate
from gates.Add16Gate import Add16Gate
from gates.Inc16Gate import Inc16Gate

# nand = NandGate()
# print(nand(True, True))

# not_gate = NotGate()
# print(not_gate(True))

# and_gate = AndGate()
# print(and_gate(True, True))

# or_gate = OrGate()
# print(or_gate(False, False))

# xor_gate = XorGate()
# print(xor_gate(True, True))

# mux_gate = MuxGate()
# print(mux_gate(True, False, False))

# mux16_gate = Mux16Gate()
# input_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# input_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# print (mux16_gate(input_a, input_b, True))

half_adder_gate = HalfAdderGate()
sum_result, carry_out = half_adder_gate(1, 1)
print((int(sum_result), int(carry_out)))

full_adder_gate = FullAdderGate()
sum_result, carry_out = full_adder_gate(0, 1, 1)
print((int(sum_result), int(carry_out)))

input_one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
input_two = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]



inc16_gate = Inc16Gate()
res = inc16_gate(input_one)

print(*(int(bit) for bit in res))