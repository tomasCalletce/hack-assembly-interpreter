from .DMuxGate import DMuxGate

class DMux8WayGate:
    def __init__(self):
        self.dmux_gate = DMuxGate()

    def __call__(self, input, select):
        
        abcd, efgh = self.dmux_gate(input, select[0])
        ab,cd = self.dmux_gate(abcd, select[1])
        ef,gh = self.dmux_gate(efgh, select[1])
        a , b = self.dmux_gate(ab, select[2])
        c , d = self.dmux_gate(cd, select[2])
        e, f = self.dmux_gate(ef, select[2])
        g, h = self.dmux_gate(gh, select[2])
        return a,b,c,d,e,f,g,h
