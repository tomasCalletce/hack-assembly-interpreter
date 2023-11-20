from .Inc16Gate import Inc16Gate
from .RegisterGate import RegisterGate
from .Mux16Gate import Mux16Gate

class PcGate:
    def __init__(self):
        self.inc16_gate = Inc16Gate()
        self.register_gate = RegisterGate()
        self.mux16_gate = Mux16Gate()

    def __call__(self, a,load , inc, reset):
        value = self.register_gate(a,0)

        inc_out = self.inc16_gate(value)
        print("inc_out", inc_out)
        inc_or_no_inc = self.mux16_gate(value, inc_out, inc)
        inc_or_no_inc_or_in = self.mux16_gate(inc_or_no_inc, a, load)
        inc_or_no_inc_or_in_or_reset = self.mux16_gate(inc_or_no_inc_or_in, [0]*16, reset)
        
        return self.register_gate(inc_or_no_inc_or_in_or_reset, 1)
        


 