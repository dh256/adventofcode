class Computer:
    def __init__(self,program):
        # write program to memory
        memory_values = program.split(',')
        self.memory = []
        for value in memory_values:
            self.memory.append(int(value))

    def initialise_memory(self,values=None):
        if not values is None:
            self.memory[1] = values[0]
            self.memory[2] = values[1]

    def run_program(self):
        instruct_pointer = 0
        while True:
            # get opcode
            opcode = self.memory[instruct_pointer]
            if opcode in (1,2):
                # get paramaters
                num_params = 3
                params = []
                params.append(self.memory[self.memory[instruct_pointer+1]])
                params.append(self.memory[self.memory[instruct_pointer+2]])
                params.append(self.memory[instruct_pointer+3])
                
                # exectute instruction
                if opcode == 1:
                    self.memory[params[2]] = params[0] + params[1]
                elif opcode == 2:
                    self.memory[params[2]] = params[0] * params[1]
            elif opcode == 99:
                break
            else:
                raise Exception("Unexpected instruction found")
                break

            # next instruction
            instruct_pointer = instruct_pointer + 4  