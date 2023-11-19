from gates.NandGate import NandGate
from gates.NotGate import NotGate
from gates.AndGate import AndGate
from gates.OrGate import OrGate
from gates.XorGate import XorGate

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