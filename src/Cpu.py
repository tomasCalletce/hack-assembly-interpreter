from gates.NotGate import NotGate
from gates.Mux16Gate import Mux16Gate
from gates.RegisterGate import RegisterGate
from gates.AluGate import AluGate
from gates.AndGate import AndGate

class CPU:
    def __init__(self,rom):
        self.rom = rom
        
        self.not_gate = NotGate()
        self.mux16_gate = Mux16Gate()
        self.alu_gate = AluGate()
        self.and_gate = AndGate()

        self.register_a = RegisterGate()
        self.register_d = RegisterGate()
    
    def __call__(self,inM,instruction,reset):
        # instruction a
        if(instruction[0] == 0):
          a = self.register_a(instruction,1)
        
        # instruction c
        else:
          a = self.register_a(instruction,instruction[10])
          d = self.register_d(instruction,0)
          a_or_d = self.mux16_gate(a, inM, instruction[3])

          out = self.alu_gate(d, a_or_d, instruction[4], instruction[5], instruction[6], instruction[7], instruction[8], instruction[9])

          self.register_d(out,instruction[11])
          writeM = instruction[12]
          

            