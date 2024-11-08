from dataclasses import dataclass
from enum import StrEnum
import numpy as np
from collections import deque

class InstructionType(StrEnum):
    AND='AND'
    OR='OR'
    LSHIFT='LSHIFT'
    RSHIFT='RSHIFT'
    NOT='NOT'
    SET='SET'       # set value of output wire to value of input wire

@dataclass
class Instruction:
    type: InstructionType
    arg1: str
    arg2: str | None = None

class Day7:
    def __init__(self, filename: str) -> None: 
        self.signals: dict[str, np.uint16] = dict()
        self.instructions: dict[str, Instruction] = {}
        with open(filename,'r') as input_file:
            for raw_instruction in [line.strip('\n') for line in input_file]:
                raw_instruction_parts: list[str] = raw_instruction.split(' -> ')
                instruction_parts = raw_instruction_parts[0].split(' ')
                wire = raw_instruction_parts[1]
                
                if len(instruction_parts) == 1:
                    self.instructions[wire] = Instruction(InstructionType.SET,arg1=instruction_parts[0])
                 
                elif len(instruction_parts) == 2:
                    self.instructions[wire] = Instruction(instruction_parts[0],arg1=instruction_parts[1])
                
                elif len(instruction_parts) == 3:
                    self.instructions[wire]= Instruction(instruction_parts[1],arg1=instruction_parts[0],arg2=instruction_parts[2])
    
    def is_uint16(self, arg: str) -> bool:
        try:
            _ = np.uint16(arg)
            return True
        except ValueError:
            return False    
    
    def _current_arg_value(self, arg: str) -> np.uint16 | None:
        if self.is_uint16(arg):
            return np.uint16(arg)
        else:
            return self.wire_values.get(arg, None)
    
    def _find_wire_value(self, wire: str) -> int:
        '''
        Do a DFS through instructions set, working back from instruction that sets given wire
        Put instruction that sets required wire onto stack
        While stack is not empty:
            Look at instruction at top of stack
            Check whether all arguements have a value (either an int, or wire has a value)
            If so, compute instruction, set output wire value and remove instruction from stack
            Otherwise, get instruction that sets unknown arg and add to stack
        '''
        self.wire_values: dict[str, np.uint16] = {}
        instruction_stack: deque[(str,Instruction)] = deque()
        instruction_stack.appendleft((wire,self.instructions[wire]))
        while len(instruction_stack) > 0:
            wire, next_instruction = instruction_stack[0]
            
            arg_val1 = self._current_arg_value(next_instruction.arg1)
            arg_val2 = self._current_arg_value(next_instruction.arg2) if next_instruction.arg2 is not None else None
            
            if (arg_val1 is not None): 
                if next_instruction.type == InstructionType.SET:
                    self.wire_values[wire] = arg_val1
                    instruction_stack.popleft()
                elif next_instruction.type == InstructionType.NOT:
                    self.wire_values[wire] = np.bitwise_not(arg_val1)
                    instruction_stack.popleft()
                
                if (arg_val2 is not None):
                    if next_instruction.type == InstructionType.AND:
                        self.wire_values[wire] = np.bitwise_and(arg_val1,arg_val2)
                        instruction_stack.popleft()
                    elif next_instruction.type == InstructionType.OR:
                        self.wire_values[wire] = np.bitwise_or(arg_val1,arg_val2)
                        instruction_stack.popleft()
                    elif next_instruction.type == InstructionType.LSHIFT:
                        self.wire_values[wire] = np.bitwise_left_shift(arg_val1,arg_val2)
                        instruction_stack.popleft()
                    elif next_instruction.type == InstructionType.RSHIFT:
                        self.wire_values[wire] = np.bitwise_right_shift(arg_val1,arg_val2)
                        instruction_stack.popleft()
                else:
                    if next_instruction.arg2 is not None:
                        instruction_stack.appendleft((next_instruction.arg2,self.instructions[next_instruction.arg2]))
            else:
                instruction_stack.appendleft((next_instruction.arg1,self.instructions[next_instruction.arg1]))
                       
        return int(self.wire_values[wire])
    
    def part1(self, wire: str) -> int:
        return self._find_wire_value(wire)
            
    def part2(self, wire) -> int:
        wire_value = self._find_wire_value(wire)
        self.instructions['b'].arg1 = f'{wire_value}'
        return self._find_wire_value(wire)