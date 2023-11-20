from .NotGate import NotGate
from .BitGate import BitGate

class RegisterGate:
    def __init__(self):
        self.bits = [BitGate() for _ in range(16)]

    def __call__(self, a, load):
        if(load == 1):
            for i in range(16):
                self.bits[i](a[i], 1)
        return [self.bits[i](a[i],0) for i in range(16)]
