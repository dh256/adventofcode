from dataclasses import dataclass, field
from enum import Enum


@dataclass
class Instruction:
    raw: str = field(kw_only=True)
    op: str = field(init=False)
    arg: int = field(init=False, default=None)

    def __post_init__(self):
        inst_parts = self.raw.split(' ')
        self.op = inst_parts[0]
        if len(inst_parts) > 1:
            self.arg = int(inst_parts[1])
            
    @property
    def cycles(self) -> int:
        if self.op == 'noop':
            return 1
        elif self.op == 'addx':
            return 2

class CPU:

    def __init__(self,file_name) -> None:
        with open(file_name, 'r') as input_file:
            self.instructions: list[Instruction] = [Instruction(raw=line.strip('\n')) for line in input_file]
        self.registers: dict = {'x': 1}

    def run_instructions(self) -> None:
        self.cycle_values = dict()
        curr_cycle = 1
        for instruct in self.instructions:
            if instruct.op == 'noop':
                self.cycle_values[curr_cycle] = self.registers['x']
                curr_cycle += 1
            elif instruct.op == 'addx':
                self.cycle_values[curr_cycle] = self.registers['x']
                curr_cycle += 1
                self.cycle_values[curr_cycle] = self.registers['x']
                self.registers['x'] += instruct.arg
                curr_cycle += 1
    
    def sum_signal_strengths(self, cycles: list[int]) -> int:
        '''
        Returns the sum of signal_strengths after each of the cycles in given list
        '''
        candidates = dict(filter(lambda item : item[0] in cycles, self.cycle_values.items())) 
        result = sum(map(lambda item: item[0] * item[1], candidates.items()))
        return result

    def display(self):
        row = []
        for curr_cycle in range(0,240):
            if curr_cycle % 40 == 0:
                '''
                Output previous row and start a new row
                '''
                print(''.join(row))
                row = ['.'] * 40            # all pixels are darl

            # current sprite position = curr 'x' reg val
            sprite_pos = self.cycle_values[curr_cycle+1]
            
            # if pixel being drawn correponds to current pos of sprite - light it up
            if curr_cycle % 40 in range(sprite_pos-1,sprite_pos+2):
                row[(curr_cycle % 40)] = '#'
        
        # print last row
        print(''.join(row))