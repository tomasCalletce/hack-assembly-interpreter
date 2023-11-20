from .Add16Gate import Add16Gate

class Inc16Gate:
    def __init__(self):
        self.add_16_gate = Add16Gate()

    def __call__(self, a):
        one = [0] * 16
        one[15] = 1
        return self.add_16_gate(a,one)
        
