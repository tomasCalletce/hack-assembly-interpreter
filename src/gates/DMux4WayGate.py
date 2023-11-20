from .DMuxGate import DMuxGate

class DMux4WayGate:
    def __init__(self):
        self.dmux_gate = DMuxGate()

    def __call__(self, input, select):
        
        out_a, out_b = self.dmux_gate(input, select[0])
        a,b = self.dmux_gate(out_a, select[1])
        c,d = self.dmux_gate(out_b, select[1])
        return a,b,c,d
