from gates.NandGate import NandGate
from gates.NotGate import NotGate
from gates.AndGate import AndGate
from gates.OrGate import OrGate
from gates.XorGate import XorGate
from gates.MuxGate import MuxGate
from gates.Mux16Gate import Mux16Gate

nand = NandGate()
print(nand(True, True))

not_gate = NotGate()
print(not_gate(True))

and_gate = AndGate()
print(and_gate(True, True))

or_gate = OrGate()
print(or_gate(False, False))

xor_gate = XorGate()
print(xor_gate(True, True))

mux_gate = MuxGate()
print(mux_gate(True, False, False))

mux16_gate = Mux16Gate()
input_a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
input_b = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print (mux16_gate(input_a, input_b, False))