from collections import namedtuple
from types import FunctionType

class Instruction(namedtuple('Instruction','opcode inA inB inC')):
    def __str__(self):
        return f'{self.opcode} {self.inA} {self.inB} {self.inC}'

Program = namedtuple('Program','ip instructions')

class CPU():

    @staticmethod
    def operands():
        ''' 
        return a list of CPU operands. To do this use __dict__ method and only include FunctionTypes excluding this method and anything starting __
        '''
        return [x for x,y in CPU.__dict__.items() if type(y) == FunctionType and x != 'operands' and not x.startswith('__')]

    def __init__(self,registers,program):
        self.registers = registers
        self.instructions = program.instructions
        self.ip = 0
        self.bound_register = program.ip

    def addi(self,regA,valB,regC):
        self.registers[regC] = self.registers[regA] + valB

    def addr(self,regA,regB,regC):
        self.registers[regC] = self.registers[regA] + self.registers[regB]

    def muli(self,regA,valB,regC):
        self.registers[regC] = self.registers[regA] * valB

    def mulr(self,regA,regB,regC):
        self.registers[regC] = self.registers[regA] * self.registers[regB]

    def bani(self,regA,valB,regC):
        self.registers[regC] = self.registers[regA] & valB

    def banr(self,regA,regB,regC):
        self.registers[regC] = self.registers[regA] & self.registers[regB]

    def bori(self,regA,valB,regC):
        self.registers[regC] = self.registers[regA] | valB

    def borr(self,regA,regB,regC):
        self.registers[regC] = self.registers[regA] | self.registers[regB]

    def setr(self,regA,inB,regC):
        self.registers[regC] = self.registers[regA]

    def seti(self,valA,inB,regC):
        self.registers[regC] = valA

    def gtir(self,valA,regB,regC):
        self.registers[regC] = 1 if valA > self.registers[regB] else 0

    def gtri(self,regA,valB,regC):
        self.registers[regC] = 1 if self.registers[regA] > valB else 0

    def gtrr(self,regA,regB,regC):
        self.registers[regC] = 1 if self.registers[regA] > self.registers[regB] else 0

    def eqir(self,valA,regB,regC):
        self.registers[regC] = 1 if valA == self.registers[regB] else 0

    def eqri(self,regA,valB,regC):
        self.registers[regC] = 1 if self.registers[regA] == valB else 0

    def eqrr(self,regA,regB,regC):
        self.registers[regC] = 1 if self.registers[regA] == self.registers[regB] else 0

    def run_program(self):
        while self.ip < len(self.instructions):
            instruction = self.instructions[self.ip]
            self.registers[self.bound_register] = self.ip
            instruction_str = f'self.{instruction.opcode}({instruction.inA},{instruction.inB},{instruction.inC})'
            eval(instruction_str)
            self.ip = self.registers[self.bound_register]
            self.ip += 1
        return self.registers[0]

def processInput(filename):
    with open(filename, "r") as input:
        lines = [line.strip('\n') for line in input]
        return lines

def create_program(lines):
    ip_parts = lines[0].split(' ')
    ip = int(ip_parts[1])

    instructions=[]
    for line in lines[1:]:
        instr_parts = line.split(' ')
        instruction = Instruction(instr_parts[0],instr_parts[1],instr_parts[2],instr_parts[3])
        instructions.append(instruction)

    return Program(ip,instructions)

# PART 1
lines = processInput('day19.txt')
program = create_program(lines)
registers = [0] * 6
cpu = CPU(registers, program)
result = cpu.run_program()
print(f'Part 1 Result: {result}')

'''
PART 2
The code takes too long using same method as 1
Through reverse engineerimg the assembly code inout figured out that what it's actually doing is calculating the 
sum of the multiples of a number num (Instructions 2-16). num is calculated using formula in cal2_part2_num (instruction 17-35)
'''

def calc_part2_num():
    r2 = 0
    r4 = 17
    r0 = 1
    r1 = 0
    
    r2 += 2
    r4 += 1
    r2 = r2 * r2
    r4 += 1
    r2 = r2 * r4
    r4 += 1
    r2 *= 11
    r4 += 1
    r1 += 6
    r4 += 1
    r1 = r1 * r4
    r4 += 1
    r1 += 18
    r4 += 1
    r2 = r2 + r1
    r4 += 1
    r4 = r4 + r0
    r4 += 1
    r1 = r4
    r4 += 1
    r1 = r4 * r1
    r4 += 1
    r1 = r4 + r1
    r4 += 1
    r1 = r4 * r1
    r4 += 1
    r1 = r1 * 14
    r4 += 1
    r1 = r1 * r4
    r4 += 1
    r2 = r1 + r2
    r4 += 1
    r0 = 0
    r4 += 1
    r4 = 0 
    r4 += 1   
    return r2

num = calc_part2_num() #10551386  
result = 0
for x in range(1,num+1):
    if num % x == 0:
        result += x

print(f'Part 2 Result: {result}')


