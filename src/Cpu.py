from gates.NotGate import NotGate
from gates.Mux16Gate import Mux16Gate
from gates.RegisterGate import RegisterGate
from gates.AluGate import AluGate
from gates.AndGate import AndGate
from gates.PcGate import PcGate
from gates.OrGate import OrGate

class CPU:
    def __init__(self):
        self.not_gate = NotGate()
        self.mux16_gate = Mux16Gate()
        self.alu_gate = AluGate()
        self.and_gate = AndGate()
        self.or_gate = OrGate()

        self.register_a = RegisterGate()
        self.register_d = RegisterGate()

        self.pc_gate = PcGate()
    
    def __call__(self,inM,instruction,reset):
        # instruction a
        if(instruction[0] == 0):
          a = self.register_a(instruction,1)
          addressM = a.copy()
          addressM[0] = 0

          out_pc = self.pc_gate(a,0,1,reset)
          out_pc[0] = 0

          out = [0]*16

          return out,0,addressM,out_pc
        # instruction c
        else:
          a = self.register_a(instruction,instruction[10])
          addressM = a.copy()
          addressM[0] = 0
          d = self.register_d(instruction,0)
          a_or_d = self.mux16_gate(a, inM, instruction[3])

          out, zr, ng = self.alu_gate(d, a_or_d, instruction[4], instruction[5], instruction[6], instruction[7], instruction[8], instruction[9])

          self.register_d(out,instruction[11])
          writeM = instruction[12]

          not_ng = self.not_gate(ng)
          not_zr = self.not_gate(zr)
          jgt = instruction[15]
          posnzr = self.and_gate(not_ng, not_zr)
          ld1 = self.and_gate(jgt, posnzr)

          jeq = instruction[14]
          ld2 = self.and_gate(jeq,not_zr)

          jlt = instruction[13]
          ld3 = self.and_gate(jlt,ng)

          ldt = self.or_gate(ld1,ld2)
          ld = self.or_gate(ld3,ldt)

          out_pc = self.pc_gate(a,ld,1,reset)
          out_pc[0] = 0

          return out,writeM,addressM,out_pc




          

            