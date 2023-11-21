from .DMux8WayGate import DMux8WayGate
from .Mux8Way16Gate import Mux8Way16Gate
from .RegisterGate import RegisterGate

class Ram8Gate:
    def __init__(self):
        self.dmux = DMux8WayGate()
        self.mux = Mux8Way16Gate()
        self.registers = [RegisterGate() for _ in range(16)]

    def __call__(self, input, load, address):
        assert len(address) == 3, "Address must be a list of three bits."

        out_a, out_b, out_c, out_d, out_e, out_f, out_g, out_h = self.dmux(load, address)

        reg0 = self.registers[0](input,out_a)
        reg1 = self.registers[1](input,out_b)
        reg2 = self.registers[2](input,out_c)
        reg3 = self.registers[3](input,out_d)
        reg4 = self.registers[4](input,out_e)
        reg5 = self.registers[5](input,out_f)
        reg6 = self.registers[6](input,out_g)
        reg7 = self.registers[7](input,out_h)
    
        return self.mux(reg0,reg1,reg2,reg3,reg4,reg5,reg6,reg7,address)

