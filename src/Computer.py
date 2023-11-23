from gates.Ram64Gate import Ram64Gate
from Loader import Loader
from Cpu import CPU

class Computer:
    def __init__(self,file_path):
        load = Loader(file_path)
        self.rom = load.get_ram64()
        self.ram = Ram64Gate()
        self.cpu = CPU()
        

