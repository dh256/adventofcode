from enum import IntEnum

class Instruction:
    def __init__(self,opcode,params):
        self.opcode = opcode

class ParameterMode(IntEnum):
    POSITION = 0,
    IMMEDIATE = 1,
    RELATIVE = 2 

class StopReason(IntEnum):
    NONE = 0,
    STOP = 1,
    INPUT_REQUIRED = 2

class Computer:
    def __init__(self,program,input_vals=[]):
        program_values = program.split(',')
        self.input_vals = input_vals
        self.output_vals = []
        self.instruct_pointer = 0
        self._memory = {}
        self.relative_base = 0

        # write program to memory
        address = 0
        for value in program_values:
            self._memory_write(address,int(value))
            address += 1

    def _memory_read(self,address):
        if address < 0:
            SystemExit(f"Invalid address {address}")
        try:
            return self._memory[address]
        except KeyError:                     # KeyError indicates memory does not yet exist. Write 0 to memory and return 0
            self._memory_write(address,0)
            return self._memory[address]

    def _memory_write(self,address,value):
        if address < 0:
            SystemExit(f"Invalid address {address}")
        self._memory[address] = value
    
    def process_instruction(self):
        stop_reason = StopReason.NONE
        
        # get opcode
        instruction = self._memory_read(self.instruct_pointer)
        opcode = instruction % 100

        # execute instruction

        # addition
        if opcode == 1:
            value = self.get_parameter(instruction,1) + self.get_parameter(instruction,2)
            self.set_parameter(instruction,3,value) 
            self.instruct_pointer += 4

        # multiply
        elif opcode == 2:
            value = self.get_parameter(instruction,1) * self.get_parameter(instruction,2)
            self.set_parameter(instruction,3,value) 
            self.instruct_pointer += 4

        # input
        elif opcode == 3:
            if len(self.input_vals) == 0:
                stop_reason = StopReason.INPUT_REQUIRED
            else:
                value = self.input_vals.pop(0)
                self.set_parameter(instruction,1,value)
                self.instruct_pointer += 2

        # output
        elif opcode == 4:
            out_val = self.get_parameter(instruction,1)
            self.output_vals.append(out_val)
            self.instruct_pointer += 2
            
        # jump if true
        elif opcode == 5:
            if self.get_parameter(instruction,1) != 0:
                self.instruct_pointer = self.get_parameter(instruction,2)
            else:
                self.instruct_pointer += 3

        # jump if false
        elif opcode == 6:
            if self.get_parameter(instruction,1) == 0:
                self.instruct_pointer = self.get_parameter(instruction,2)
            else:
                self.instruct_pointer += 3

        # less than
        elif opcode == 7:
            if self.get_parameter(instruction,1) < self.get_parameter(instruction,2):
                self.set_parameter(instruction,3,1)
            else:
                self.set_parameter(instruction,3,0)
            self.instruct_pointer += 4  

        # equals
        elif opcode == 8:
            if self.get_parameter(instruction,1) == self.get_parameter(instruction,2):
                self.set_parameter(instruction,3,1)
            else:
                self.set_parameter(instruction,3,0)
            self.instruct_pointer += 4

        # Set Relative Base
        elif opcode == 9:
            self.relative_base += self.get_parameter(instruction,1)
            self.instruct_pointer += 2

        elif opcode == 99:
            stop_reason = StopReason.STOP

        else:
            raise Exception(f"Fatal error occurred. Unexpected opcode {opcode} found at address {self.instruct_pointer}")

        return stop_reason

    def _get_parameter_mode(self,instruction,offset):
        param_modes= instruction // 100
        param_mode = (param_modes % (10 ** offset)) // (10 ** (offset-1)) 
        return param_mode

    def set_parameter(self,instruction,offset,value):
        '''
        Sets memory at address specified by POSITION or RELATIVE arguement to value 
        '''
        param_mode = self._get_parameter_mode(instruction,offset) 
        if param_mode == ParameterMode.POSITION:
            self._memory_write(self._memory_read(self.instruct_pointer+offset),value)
        elif param_mode == ParameterMode.RELATIVE:
            self._memory_write(self._memory_read(self.instruct_pointer+offset) + self.relative_base,value)
        else:
            SystemExit('Invalid param mode for setting a parameter')

    def get_parameter(self,instruction,offset):
        '''
        Return parameter value for instruction and arguement (offset)
        '''
        param_mode = self._get_parameter_mode(instruction,offset) 
        
        # get value - either from:
        #  immediate location 
        #  memory location reference by position
        #  memory location + relative_base
        if param_mode == ParameterMode.IMMEDIATE:
            param_value = self._memory_read(self.instruct_pointer+offset)
        elif param_mode == ParameterMode.POSITION:
            param_value = self._memory_read(self._memory_read(self.instruct_pointer+offset))
        elif param_mode == ParameterMode.RELATIVE:
            param_value = self._memory_read(self._memory_read(self.instruct_pointer+offset) + self.relative_base)
        return param_value

    def run_program(self, start_at_zero=True):
        stop_reason = StopReason.NONE
        if start_at_zero:
            self.instruct_pointer = 0
        while stop_reason is StopReason.NONE:
            stop_reason = self.process_instruction()
        return (self.output_vals,stop_reason)