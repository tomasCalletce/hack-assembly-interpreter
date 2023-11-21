from .Ram8Gate import Ram8Gate
from .DMux8WayGate import DMux8WayGate
from .Mux8Way16Gate import Mux8Way16Gate

class Ram64Gate:
    def __init__(self):
        self.dmux = DMux8WayGate()
        self.mux = Mux8Way16Gate()
        self.ram8s = [Ram8Gate() for _ in range(16)]
    
    def __call__(self, input, load, address):
        assert len(address) == 6, "Address must be a list of six bits."

        out_a, out_b, out_c, out_d, out_e, out_f, out_g, out_h = self.dmux(load, address[3:6])

        ram0 = self.ram8s[0](input,out_a,address[0:3])
        ram1 = self.ram8s[1](input,out_b,address[0:3])
        ram2 = self.ram8s[2](input,out_c,address[0:3])
        ram3 = self.ram8s[3](input,out_d,address[0:3])
        ram4 = self.ram8s[4](input,out_e,address[0:3])
        ram5 = self.ram8s[5](input,out_f,address[0:3])
        ram6 = self.ram8s[6](input,out_g,address[0:3])
        ram7 = self.ram8s[7](input,out_h,address[0:3])

        return self.mux(ram0,ram1,ram2,ram3,ram4,ram5,ram6,ram7,address[3:6])
        





