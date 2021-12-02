from collections import namedtuple

class Instruction:
    def __init__(self, instruction_str):
        instruction_parts = instruction_str.split(' ')
        self._direction = instruction_parts[0]
        self._amount = int(instruction_parts[1])

    @property
    def direction(self):
        return self._direction

    @property
    def amount(self):
        return self._amount

class Submarine:
    def __init__(self, filename):
        with open(filename,'r') as input_file:
            self._course_instructions = [Instruction(line.strip('\n')) for line in input_file]
            

    def follow_course(self):
        self._v_pos = 0
        self._h_pos = 0
        for instruction in self._course_instructions:
            if instruction.direction == 'up':
                self._v_pos -= instruction.amount
            elif instruction.direction == 'down':
                self._v_pos += instruction.amount
            else:
                self._h_pos += instruction.amount

    def follow_course2(self):
        self._v_pos = 0
        self._h_pos = 0
        self._aim = 0
        for instruction in self._course_instructions:
            if instruction.direction == 'up':
                self._aim -= instruction.amount
            elif instruction.direction == 'down':
                self._aim += instruction.amount
            else:
                self._h_pos += instruction.amount
                self._v_pos += self._aim * instruction.amount

    @property 
    def h_pos(self):
        return self._h_pos

    @property 
    def v_pos(self):
        return self._v_pos

    