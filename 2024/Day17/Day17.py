
''' 
David Hanley, December 2024
'''
import re
class Day17:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.registers: list[int] = [int(re.findall(r'\d+', line)[0]) for line in lines[0:3]]
        self.program: list[int] = [int(p) for p in re.findall(r'\d+', lines[4])]
        print(self.registers)
        print(self.program)
               
    def part1(self) -> str:
        ip: int = 0
        output: list[int] = list()
        while ip < len(self.program):
            jumped = False
            opcode: int = self.program[ip]
            literal_operand: int = self.program[ip+1]
            combo_operand: int = literal_operand
            if combo_operand in range(4,7):
                combo_operand = self.registers[combo_operand - 4]
            
            match opcode:
                case 0: 
                    self.registers[0] = self.registers[0] // pow(2,combo_operand)

                case 1: 
                    self.registers[1] = self.registers[1] ^ literal_operand
                    
                case 2: 
                    self.registers[1] = combo_operand % 8
                    
                case 3: 
                    if self.registers[0] >0: 
                        ip = literal_operand
                        jumped = True

                case 4: 
                    self.registers[1] = self.registers[1] ^ self.registers[2]
                
                case 5: 
                    output.append(combo_operand % 8)
                    
                case 6: 
                    self.registers[1] = self.registers[0] // pow(2,combo_operand)
                    
                case 7: 
                    self.registers[2] = self.registers[0] // pow(2,combo_operand)
            
            if not jumped:
                ip += 2
                
        return ','.join([f'{o}' for o in output])

    def part2(self) -> str:
        return 0
                        
