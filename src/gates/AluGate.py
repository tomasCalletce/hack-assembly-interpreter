from .Mux16Gate import Mux16Gate
from .Not16Gate import Not16Gate
from .Add16Gate import Add16Gate
from .And16Gate import And16Gate
from .Or8WayGate import Or8WayGate
from .NotGate import NotGate

class AluGate:
    def __init__(self):
        self.mux16_gate = Mux16Gate()
        self.not16_gate = Not16Gate()
        self.add16_gate = Add16Gate()
        self.and16_gate = And16Gate()
        self.or8way_gate = Or8WayGate()
        self.not_gate = NotGate()

    def __call__(self, a, b, zx, nx, zy, ny, f, no):
        zx_out = self.mux16_gate(a, [0]*16, zx)
        not_x = self.not16_gate(zx_out)
        nx_out = self.mux16_gate(zx_out, not_x, nx)

        zy_out = self.mux16_gate(b, [0]*16, zy)
        not_y = self.not16_gate(zy_out)
        ny_out = self.mux16_gate(zy_out, not_y, ny)

        x_plus_y = self.add16_gate(nx_out, ny_out)
        x_and_y = self.and16_gate(nx_out, ny_out)
        func_chosen = self.mux16_gate(x_and_y, x_plus_y, f)

        not_func_chosen = self.not16_gate(func_chosen)
        out = self.mux16_gate(func_chosen, not_func_chosen, no)

        zr_or = self.or8way_gate(out)
        zr_out = self.not_gate(zr_or)

        ng_out = out[0]

        return out, zr_out, ng_out