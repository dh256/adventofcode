from enum import IntEnum

class Instruction:
    def __init__(self,opcode,params):
        self.opcode = opcode

class ParameterMode(IntEnum):
    POSITION = 0,
    IMMEDIATE = 1 

class OpType(IntEnum):
    READ = 0,
    WRITE = 1

class Computer:
    def __init__(self,program):
        # write program to memory
        memory_values = program.split(',')
        self.instruct_pointer = 0
        self.memory = []
        for value in memory_values:
            self.memory.append(int(value))

    def initialise_memory(self,values=None):
        if not values is None:
            self.memory[1] = values[0]
            self.memory[2] = values[1]

    def process_instruction(self):
        stop = False
        
        # get opcode
        instruction = self.memory[self.instruct_pointer]
        opcode = instruction % 100

        # execute instruction
        if opcode == 1:
            self.memory[self.get_parameter(instruction,3,OpType.WRITE)] = self.get_parameter(instruction,1,OpType.READ) + self.get_parameter(instruction,2,OpType.READ)
            self.instruct_pointer += 4

        elif opcode == 2:
            self.memory[self.get_parameter(instruction,3,OpType.WRITE)] = self.get_parameter(instruction,1,OpType.READ) * self.get_parameter(instruction,2,OpType.READ)
            self.instruct_pointer += 4

        elif opcode == 3:
            input_val = int(input("Input Value: "))
            self.memory[self.get_parameter(instruction,1,OpType.WRITE)] = input_val
            self.instruct_pointer += 2

        elif opcode == 4:
            output_val = self.get_parameter(instruction,1,OpType.READ)
            self.instruct_pointer += 2
            print(f"Output: {output_val}")

        # jump if true
        elif opcode == 5:
            if self.get_parameter(instruction,1,OpType.READ) != 0:
                self.instruct_pointer = self.get_parameter(instruction,2,OpType.READ)
            else:
                self.instruct_pointer += 3

        # jump if false
        elif opcode == 6:
            if self.get_parameter(instruction,1,OpType.READ) == 0:
                self.instruct_pointer = self.get_parameter(instruction,2,OpType.READ)
            else:
                self.instruct_pointer += 3

        # less than
        elif opcode == 7:
            write_pos = self.get_parameter(instruction,3,OpType.WRITE)
            if self.get_parameter(instruction,1,OpType.READ) < self.get_parameter(instruction,2,OpType.READ):
                self.memory[write_pos] = 1
            else:
                self.memory[write_pos] = 0 
            self.instruct_pointer += 4  

        # equals
        elif opcode == 8:
            write_pos = self.get_parameter(instruction,3,OpType.WRITE)
            if self.get_parameter(instruction,1,OpType.READ) == self.get_parameter(instruction,2,OpType.READ):
                self.memory[write_pos] = 1
            else:
                self.memory[write_pos] = 0
            self.instruct_pointer += 4

        elif opcode == 99:
            num_params = 0
            stop = True

        else:
            raise Exception(f"Fatal error occurred. Unexpected opcode {opcode} found at address {self.instruct_pointer}")

        return stop

    def get_parameter(self,instruction,offset,optype):
        # if read op read other rom position in memory or immediate value depending on ParameterMode
        # write ops are always immediate
        param_mode = ParameterMode.POSITION   # DEFAULT
        if optype == OpType.READ:
            # get param node for parameter
            if instruction > 100:
                param_modes= instruction // 100
                param_mode = (param_modes % (10 ** offset)) // (10 ** (offset-1)) 
        else:
            param_mode = ParameterMode.IMMEDIATE
        
        # get value - either from immediate location or from memory location reference by position
        if param_mode == ParameterMode.IMMEDIATE:
            param_value = self.memory[self.instruct_pointer+offset]
        else:
            param_value = self.memory[self.memory[self.instruct_pointer+offset]]

        return param_value

    def run_program(self):
        stop = False
        self.instruct_pointer = 0
        while not stop:
            stop = self.process_instruction()