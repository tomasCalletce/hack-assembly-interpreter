class Mux8Way16Gate:
    def __init__(self):
        self.Mux4Way16_gate = Mux4Way16Gate()
        self.Mux16_gate = Mux16Gate()

    def __call__(self, a, b, c, d, e, f, g, h, select):
        assert len(select) == 3, "Selector must be a list or tuple of three bits."
        
        output_abcd = self.Mux4Way16_gate(a, b, c, d, select[1:])
        output_efgh = self.Mux4Way16_gate(e, f, g, h, select[1:])
    
        output = self.Mux16_gate(output_abcd, output_efgh, select[0])    
        return output
