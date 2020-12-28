import re
from os import makedirs, read
from enum import Enum
from Binary import Binary

class InstructionType(Enum):
    MASK = 0
    MEM = 1

class Instruction():
    def __init__(self,instruction_str):
        # mask instructions starts with mask = 
        mask = re.match(r'mask = (\w+)',instruction_str)
        if mask is not None:
            self._type = InstructionType.MASK
            self._value = mask.group(1)
            return

        # mem has the form mem[address] = value
        mem = re.match(r'mem\[(\d+)\] = (\d+)',instruction_str)
        if mem is not None:
            self._type = InstructionType.MEM
            self._address = int(mem.group(1))
            self._value = int(mem.group(2))
            return
        
        raise(f'Unexpected instruction {instruction_str}')

    @property
    def type(self):
        return self._type

    @property
    def value(self):
        return self._value
    
    @property
    def address(self):
        return self._address
    
    def __str__(self):
        if self.type == InstructionType.MASK:
            output = f'mask = {self._value}'
        else:
            output = f'mem[{self._address}] = {self._value}'
        return output

class Computer():

    def __init__(self,input_file):
        with open(input_file,'r') as program_data:
            self._mask_bits = 36
            self._mask = None
            self._memory = {}
            self._instructions = [Instruction(line.strip('\n')) for line in program_data]

    def mask2(self,address):
        # Part 2 mask rules
        # If mask bit b contains X replace address bit b with a 'X'
        # If mask bit b contains 1 replace address bit b with a '1'
        # Keep a note of the number of floating bits (X) and their bit positions
        b_address = Binary(address,self._mask_bits)
        floating_bits = 0
        floating_indexes = []
        for b in range(self._mask_bits,0,-1):
            if self._mask[b-1] == 'X':
                b_address.bin[b] = 'X'
                floating_bits += 1
                floating_indexes.append(b)
            elif self._mask[b-1] == '1':
                b_address.bin[b] = '1'

        # Now calculate all possible address values by replacing each X with 0 and/or 1
        # For example if there are 4 floating_bits then replace XXXX with 0000, 0001, 0010 .. 1111
        # Return the list of all possible address values
        address_vals = []
        for num in range(0,pow(2,floating_bits)):
            b_fb = Binary(num,floating_bits)
            b_next_address = Binary(address,self._mask_bits)
            b_next_address._bin = b_address.bin.copy()
            for i in range(floating_bits,0,-1):
                b_next_address.bin[floating_indexes[i-1]] = b_fb.bin[i]      
            address_vals.append(b_next_address)

        return address_vals

    def mask(self,value):
        # mask the given value
        # If mask bit b contains 0 replace value bit b with a '0'
        # If mask bit b contains 1 replace value bit b with a '1'
        b_value = Binary(value,self._mask_bits)
        for b in range(self._mask_bits,0,-1):
            if self._mask[b-1] == '1':
                # set corresponding bit in value to 1, if not already set to 1
                b_value.bin[b] = '1'
            elif self._mask[b-1] == '0':  
                # set corresponding bit in value to 0, if not already set to 0
                b_value.bin[b] = '0'
                
        # return masked value
        return b_value.num

    def reset(self):
        self._mask = None
        self._memory = {}

    def run(self):
        for instruction in self._instructions:
            if instruction.type == InstructionType.MASK:
                self._mask = instruction.value
            elif instruction.type == InstructionType.MEM:
                value = self.mask(instruction.value)
                self._memory[instruction.address] = value

        # return sum of all values in memory
        return sum(self._memory.values())

    def run2(self):
        for instruction in self._instructions:
            if instruction.type == InstructionType.MASK:
                self._mask = instruction.value
            elif instruction.type == InstructionType.MEM:
                addresses = self.mask2(instruction.address)
                for address in addresses:
                    self._memory[address.num] = instruction.value

        # return sum of all values in memory
        return sum(self._memory.values())
