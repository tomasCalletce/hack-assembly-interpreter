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
from gates.Mux4Way16Gate import Mux4Way16Gate
from gates.Mux8Way16Gate import Mux8Way16Gate
from gates.DMuxGate import DMuxGate
from gates.DMux4WayGate import DMux4WayGate
from gates.DMux8WayGate import DMux8WayGate
from gates.Ram8Gate import Ram8Gate
from gates.Ram64Gate import Ram64Gate
from Loader import Loader
from Cpu import CPU

load = Loader('programs/one.dhl')
ram = load.get_ram64()
res = ram([0]*16, 0, [0,0,0,0,0,0])
print(*(int(bit) for bit in res))

# inM = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# instruction = [1,1,1,0,0,0,1,1,0,0,0,0,1,0,0,0]
# reset = 0

# cpu = CPU()
# out,writeM,addressM,out_pc=cpu(inM,instruction,reset)

# print(*(int(bit) for bit in out))

# addres = [0,0,0]
# load = 1
# input_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

# ram64_gate = Ram64Gate()
# ram64_gate(input_a, 1, [0,0,0,0,0,0])
# res = ram64_gate(input_a, 0, [0,0,0,0,0,1])
# print(*(int(bit) for bit in res))

# ram8_gate = Ram8Gate()
# ram8_gate(input_a, 0, [0,0,1])
# res = ram8_gate(input_a, 0, [0,0,1])
# print(*(int(bit) for bit in res))

#nand = NandGate()
#print(nand(True, True))

#not_gate = NotGate()
#print(not_gate(True))

# and_gate = AndGate()
# print(and_gate(True, True))

# or_gate = OrGate()
# print(or_gate(False, False))

# xor_gate = XorGate()
# print(xor_gate(True, True))

#mux_gate = MuxGate()
#print(mux_gate(True, False, False))

#mux16_gate = Mux16Gate()
# input_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# input_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# input_c = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# input_d = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
# input_e = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1] 
# input_f = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  
# input_g = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1] 
# input_h = [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1]
#print (mux16_gate(input_a, input_b, False))

# mux4way16_gate = Mux4Way16Gate()
# res = mux4way16_gate(input_a,  input_b, input_c, input_d, [1,0])

# mux8way16_gate = Mux8Way16Gate()
# res = mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [1,1,1])
# print(*(int(bit) for bit in res))
#Mux8way16
'''
mux8way16_gate = Mux8Way16Gate()
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [False, False, False]))  # Debería seleccionar 'a'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [False, False, True]))   # Debería seleccionar 'b'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [False, True, False]))   # Debería seleccionar 'c'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [False, True, True]))    # Debería seleccionar 'd'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [True, False, False]))   # Debería seleccionar 'e'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [True, False, True]))    # Debería seleccionar 'f'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [True, True, False]))    # Debería seleccionar 'g'
print(mux8way16_gate(input_a, input_b, input_c, input_d, input_e, input_f, input_g, input_h, [True, True, True]))     # Debería seleccionar 'h'
'''
#dmux_gate= DMuxGate()
#print(dmux_gate(1, 1))

#dmux4way
'''
def test_dmux4way_gate():
    dmux4way_gate = DMux4WayGate()
    
    test_cases = [(0, (0, 0)), (0, (0, 1)), (0, (1, 0)), (0, (1, 1)),
                  (1, (0, 0)), (1, (0, 1)), (1, (1, 0)), (1, (1, 1))]

    for input, select in test_cases:
        a, b, c, d = dmux4way_gate(input, select)
        print(f"input: {input}, select: {select} -> a: {a}, b: {b}, c: {c}, d: {d}")
test_dmux4way_gate()
'''
#DMux8Way
'''
def test_dmux8way_gate():
    dmux8way_gate = DMux8WayGate()

    test_cases = [(input, (sel0, sel1, sel2))
                  for input in [0, 1]
                  for sel0 in [False, True]
                  for sel1 in [False, True]
                  for sel2 in [False, True]]

    for input, select in test_cases:
        outputs = dmux8way_gate(input, select)
        print(f"input: {input}, select: {select} -> outputs: {outputs}")
test_dmux8way_gate()
'''

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

#input_one = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
#input_two = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]

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

# mux_grande = Mux4Way16Gate()
# res = mux_grande(1,1,1,0,[0,0])

# print(int(res))