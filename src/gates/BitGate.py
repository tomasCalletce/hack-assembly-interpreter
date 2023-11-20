class BitGate:
    def __init__(self):
        self.state = 0

    def __call__(self, a, load):
        if load == 1:
            self.state = a
        return self.state
     