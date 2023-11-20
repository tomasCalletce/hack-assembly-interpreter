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
from gates.Not16Gate import Not16Gate
from gates.And16Gate import And16Gate
from gates.Or16Gate import Or16Gate
from gates.Or8WayGate import Or8WayGate
from gates.AluGate import AluGate
from gates.BitGate import BitGate
from gates.RegisterGate import RegisterGate
from gates.PcGate import PcGate


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

# half_adder_gate = HalfAdderGate()
# sum_result, carry_out = half_adder_gate(1, 1)
# print((int(sum_result), int(carry_out)))

# full_adder_gate = FullAdderGate()
# sum_result, carry_out = full_adder_gate(0, 1, 1)
# print((int(sum_result), int(carry_out)))




# not16_gate = Not16Gate()
# res = not16_gate(input_one)



# or16_gate = Or16Gate()
# res = or16_gate(input_one, input_two)
# print(*(int(bit) for bit in res))

# input_one = [0, 0, 0, 1, 0, 0, 1, 0]

# or8way_gate = Or8WayGate()
# res = or8way_gate(input_one)
# print(res)

input_one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
input_two = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

# alu_out, zr_out, ng_out = AluGate()(input_one, input_two, 0, 1, 0, 0, 1, 1)

# print(*(int(bit) for bit in alu_out))
# print('isnegative', ng_out)

# add16_gate = Add16Gate()
# res = add16_gate(input_one, input_two)

# print(*(int(bit) for bit in res))

# zx = 1
# nx = 0

# zx_out = Mux16Gate()(input_one, [0]*16, zx)
# not_x = Not16Gate()(zx_out)
# nx_out = Mux16Gate()(zx_out, not_x, nx)

# print(*(int(bit) for bit in nx_out))

# bit_gate = BitGate()
# bit_gate(1,0)
# print(bit_gate(0,0))

# register_gate = RegisterGate()
# res = register_gate(input_one,1)
# res = register_gate(input_two,1)

# print(*(int(bit) for bit in res))

# pc_gate = PcGate()
# pc_gate(input_one,0,1,0)
# pc_gate(input_one,0,1,0)
# res = pc_gate(input_one,0,0,1)
# print(*(int(bit) for bit in res))



# inc16_gate = Inc16Gate()
# res = inc16_gate(input_one)

# print(*(int(bit) for bit in res))