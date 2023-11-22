from gates.NotGate import NotGate
from gates.Mux16Gate import Mux16Gate
from gates.RegisterGate import RegisterGate
from gates.AluGate import AluGate
from gates.AndGate import AndGate
from gates.OrGate import OrGate
from gates.AluGate import AluGate
from gates.PcGate import PcGate
class CPU:
    def __init__(self,rom):
        self.rom = rom
        
        self.or_gate = OrGate()
        self.not_gate = NotGate()
        self.mux16_gate = Mux16Gate()
        self.alu_gate = AluGate()
        self.and_gate = AndGate()
        
        self.alu_gate = AluGate()

        self.register_a = RegisterGate()
        self.register_d = RegisterGate()
        self.pc_gate = PcGate()
    
    def __call__(self,inM,instruction,reset):
        isCInstruction = self.or_gate(instruction[15],False)
        isAinstruction = self.not_gate(instruction[15])
        
        isCWriteA= self.and_gate(isCInstruction,instruction[5])
        loadA= self.or_gate(isAinstruction,isCWriteA)
        inAReg= self.mux16_gate(instruction, outALU, isCWriteA)
        outAreg = self.register_a(inAReg, loadA)
        addressM = outAreg[:14]
        
        loadD= self.and_gate(isCInstruction, instruction[4])
        outDReg = self.register_d(outALU, loadD)
        
        outAorM = self.mux16_gate(outAreg, inM, outAorM)
        
        outALU, isZeroOut, isNegOut= self.alu_gate(outDReg, outAorM)
        
        isNonNeg = self.not_gate(isNegOut)
        isNonZero = self.not_gate(isZeroOut)
        isPositive = self.and_gate(isNonNeg, isNonZero)
        
        writeM = self.and_gate(isCInstruction, instruction[3])
        
        jumpGT = self.and_gate(isPositive, instruction[0])
        jumpEQ = self.and_gate(isZeroOut, instruction[1])
        jumpLT = self.and_gate(isNegOut, instruction[2])
        
        jumpLE = self.or_gate(jumpEQ, jumpLT)
        jummpToA = self.or_gate(jumpLE, jumpGT)
        loadPC = self.and_gate(isCInstruction, jummpToA)
        PCinc = self.not_gate(loadPC)
        pc1 = self.pc_gate(outAreg, PCinc, loadPC, reset)
        pc = pc1[:14]
        
        return outM , writeM , addressM, pc
        
        
