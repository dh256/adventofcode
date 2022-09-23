from dataclasses import dataclass

@dataclass
class Instruction:
    register: str
    operation: str
    value: int
    condition_reg: str
    condition_op: str
    condition_value: int

class CPU:
    def __init__(self,filename):
        self.registers = dict()
        with open(filename,'r') as input_file:
            raw_instructions = [line.strip('\n').split(' ') for line in input_file]
            self.instructions = [Instruction(ri[0],ri[1],int(ri[2]),ri[4],ri[5],int(ri[6])) for ri in raw_instructions]
    

    def process(self) -> int:
        highest_ever = 0
        for i in self.instructions:
            # initialise registers if not seen before
            if not i.register in self.registers.keys():
                self.registers[i.register] = 0
            if not i.condition_reg in self.registers.keys():
                self.registers[i.condition_reg] = 0

            if eval(f'{self.registers[i.condition_reg]} {i.condition_op} {i.condition_value}'):
                if i.operation == 'inc':
                    self.registers[i.register] += i.value
                else:
                    self.registers[i.register] -= i.value
            
            if max(self.registers.values()) > highest_ever:
                highest_ever = max(self.registers.values())

        # get max register value at end - part 1 and higest_ever, part 2
        return (max(self.registers.values()),highest_ever)