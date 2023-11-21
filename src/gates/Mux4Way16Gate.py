from .Mux16Gate import Mux16Gate

class Mux4Way16Gate:
    def __init__(self):
        self.Mux16_gate = Mux16Gate()

    def __call__(self, a, b, c, d, select):
        assert len(select) == 2, "Selector must be a list or tuple of two bits."
        output_cd = self.Mux16_gate(c, d, select[1])  # Selecciona entre 'c' y 'd' con el primer bit.
        output_ab = self.Mux16_gate(a, b, select[1])  # Selecciona entre 'a' y 'b' con el primer bit.
        return self.Mux16_gate(output_ab, output_cd, select[0])
