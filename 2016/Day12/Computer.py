class UnexpectedInstruction(Exception):
    pass

# Holds an instruction
class Instruction():
    def __init__(self,instruction_txt):
        instruction_parts = instruction_txt.split(" ")
        self.instruction_type = instruction_parts[0]
        self.args = []
        for arg in instruction_parts[1:]:
            self.args.append(arg)

    def __str__(self):
        output = f'{self.instruction_type}'
        for arg in self.args:
            output += f' {arg}'
        return output

# The Computer. Holds a set of instructions and registery values
class Computer:
    def __init__(self, filename):
        self.registers = {"a":0, "b": 0, "c": 0, "d": 0}
        with open(filename, 'r') as input_file:
            self.instructions = [Instruction(line.strip('\n')) for line in input_file]
        self.num_instructions = len(self.instructions)

    def reset(self):
        self.registers = {"a":0, "b": 0, "c": 0, "d": 0}

    def set_register(self,reg,value):
        self.registers[reg] = value

    def execute(self):
        instruction_pointer = 0
        while instruction_pointer < self.num_instructions:
            i = self.instructions[instruction_pointer]
            if i.instruction_type == "cpy":
                try:
                    new_value = int(i.args[0])
                except ValueError as ve:
                    new_value = self.registers[i.args[0]]
                self.registers[i.args[1]] = new_value
                instruction_pointer += 1
            elif i.instruction_type == "dec":
                self.registers[i.args[0]] = self.registers[i.args[0]] - 1
                instruction_pointer += 1
            elif i.instruction_type == "inc":
                self.registers[i.args[0]] = self.registers[i.args[0]] + 1
                instruction_pointer += 1
            elif i.instruction_type == "jnz":
                try:
                    jump_value = int(i.args[0])
                except ValueError:
                    jump_value = self.registers[i.args[0]]
                if jump_value == 0:
                    instruction_pointer += 1
                else:
                    instruction_pointer += int(i.args[1])
            else:
                # unexpected input instructions
                raise UnexpectedInstruction(f'Unexpected instruction type {i.instruction_type}')
        return self.registers["a"]