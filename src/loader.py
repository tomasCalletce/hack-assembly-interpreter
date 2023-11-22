from gates.Ram64Gate import Ram64Gate

class Loader:
    def __init__(self,file_path):
        self.lines = []
        self.file_path = file_path
        self.ram64_gate = Ram64Gate()
        self.read_file()
        self.load()

    def read_file(self):
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    self.lines.append([int(bit) for bit in line])
        except Exception as e:
            print(f"An error occurred: {e}")

    def load(self):
        address = [0,0,0,0,0,0]  
        for line in self.lines:
            self.ram64_gate(line, 1, address)
            self.increment_address(address)  

    def increment_address(self, address):
        carry = 1
        for i in range(len(address) - 1, -1, -1):
            if address[i] == 0 and carry == 1:
                address[i] = 1
                carry = 0
            elif address[i] == 1 and carry == 1:
                address[i] = 0
                carry = 1
            else:
                break
    
    def get_ram64(self):
        return self.ram64_gate
    
            