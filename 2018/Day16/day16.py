import ast   # using ast.literal_eval here for speed. In reality this is dangerous because it could result in execution of arbitrary code (injection)
from collections import namedtuple
from types import FunctionType

Instruction = namedtuple('Instruction','opcode inA inB inC')
PuzzleInput = namedtuple('PuzzleInput','samples test_program')

class Sample():
    def __init__(self,before,instruction,after):
        self.before = before
        self.after = after
        self.instruction = instruction
        self.opCodes = OpCodes()
        self.possible_operands = []

    def perform(self):
        # need to repeat this for each of the 16 operations
        for operand in OpCodes.operands():
            self.opCodes.registers = self.before.copy()
            eval(f'self.opCodes.{operand}(self.instruction.inA,self.instruction.inB,self.instruction.inC)')        
            if self.after == self.opCodes.registers:
                self.possible_operands.append(operand)

    def __repr__(self):
        repr = f'Registers Before: {self.before};'
        repr += f'Instruction: {self.instruction};'
        repr += f'Registers After: {self.before};'
        repr += f'Possible Operands: {self.possible_operands};'
        return repr

class OpCodes():
    registers = [0] * 4

    @staticmethod
    def operands():
        ''' 
        return a list of OpCodes operands. To do this use __dict__ method and only include FunctionTypes excluding this method and anything starting __
        '''
        return [x for x,y in OpCodes.__dict__.items() if type(y) == FunctionType and x != 'operands' and not x.startswith('__')]

    def __init__(self,registers=None):
        if registers != None:
            registers = registers

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


def process_file(filename):
    with open(filename, "r") as fileinput:
        lineNo = 1
        samples = []
        test_program = []
        for line in fileinput:
            if lineNo < 3109: 
                line = line.strip('\n')
                if lineNo % 4 == 1:
                    before = ast.literal_eval(line.split(': ')[1])

                elif lineNo % 4 == 3:
                    after = ast.literal_eval(line.split(':  ')[1])
                    samples.append(Sample(before,instruction,after))

                elif lineNo % 4 == 2:
                    instruction_args = line.split()
                    instruction = Instruction(int(instruction_args[0]),int(instruction_args[1]),int(instruction_args[2]),int(instruction_args[3]))

                elif lineNo % 4 == 0:
                    pass
            elif lineNo > 3110:
                instruction_args = line.split()
                instruction = Instruction(int(instruction_args[0]),int(instruction_args[1]),int(instruction_args[2]),int(instruction_args[3]))
                test_program.append(instruction)

            lineNo += 1

        return PuzzleInput(samples,test_program)


# run puzzle
puzzle_input = process_file("day16.txt")

# PART 1
for sample in puzzle_input.samples:
    sample.perform()
p1_result = list(filter(lambda x:len(x.possible_operands) >= 3,puzzle_input.samples))
print(f'Samples with 3 or more possible operands: {len(p1_result)}')

# PART 2 - Figure out each operand number
'''
From Part 1 above look at all samples possible operands
If any have 1, sample.instruction.opcode: sample.possible_operands[0] to op_mapping then discard
If more than 1, remove any that match an existing entry in op_mapping
Repeat until 16 op_mappings found
'''
op_mapping = {}
while len(op_mapping) < 16:
    for sample in puzzle_input.samples:
        if len(sample.possible_operands) == 0:
            pass
        elif len(sample.possible_operands) == 1:
            # have a valid mapping
            # if opcode not already mapped, add to op_mapping
            # discard
            if not sample.instruction.opcode in op_mapping: 
                op_mapping.update({sample.instruction.opcode: sample.possible_operands[0]}) 
            sample.possible_operands = []
        else:
            # remove any already mapped
            for p_op in sample.possible_operands:
                if p_op in op_mapping.values():
                    sample.possible_operands.remove(p_op)

'''
Now that we have op_mapping run the puzzle_input.test_program using the appropriate instructions
'''
operations = OpCodes()
for instruction in puzzle_input.test_program:
    operator = op_mapping[instruction.opcode]
    eval(f'operations.{operator}(instruction.inA,instruction.inB,instruction.inC)')
print(f'Reg 0 value: {operations.registers[0]}')



