class CPU:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.instructions = [int(line.strip('\n')) for line in input_file]

    def process(self) -> int:
        steps = 0
        index = 0
        new_index = 0
        while True:
            try:
                new_index += self.instructions[index]
                self.instructions[index] += 1
                index = new_index
                steps += 1
            except IndexError:
                return steps

    def process2(self) -> int:
        steps = 0
        index = 0
        new_index = 0
        while True:
            try:
                new_index += self.instructions[index]
                if self.instructions[index] >= 3:
                    self.instructions[index] -= 1
                else:
                    self.instructions[index] += 1
                index = new_index
                steps += 1
            except IndexError:
                return steps