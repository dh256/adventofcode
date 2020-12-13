class InfiniteLoopDetectedError(Exception):
    pass

class Instruction():
    def __init__(self,code):
        instruction_parts = code.split(' ')
        self._instruction = instruction_parts[0]
        self._arguement = int(instruction_parts[1])
        self._times_run = 0

    @property
    def instruction(self):
        return self._instruction

    @property
    def arguement(self):
        return self._arguement

    def swap(self):
        if self._instruction == "nop":
            self._instruction = "jmp"
        elif self._instruction == "jmp":
            self._instruction = "nop"

    def reset(self):
        self._times_run = 0

    def inc_times_run(self):
        self._times_run += 1
        if self._times_run == 2:
            raise InfiniteLoopDetectedError

class Console():

    def __init__(self,file_name):
        with open(file_name, 'r') as instruction_data:
            self._accumulator = 0
            self._ip = 0
            self._instructions = [Instruction(line.strip('\n')) for line in instruction_data]

    @property
    def accumulator(self):
        return self._accumulator

    def reset(self):
        # set ip and accumulator to 0
        # set times run of all instructions to 0
        self._ip = 0
        self._accumulator = 0
        for instruction in self._instructions:
            instruction.reset()

    def run(self):
        self.reset()
        while self._ip < len(self._instructions):
            try:
                next_instruction = self._instructions[self._ip]
                next_instruction.inc_times_run()
                if next_instruction.instruction == "nop":
                    self._ip += 1
                elif next_instruction.instruction == "acc":
                    self._accumulator += next_instruction.arguement
                    self._ip += 1
                elif next_instruction.instruction == "jmp":
                    self._ip += next_instruction.arguement
            except InfiniteLoopDetectedError:
                raise InfiniteLoopDetectedError

    def run2(self):
        # Need to run console numerous times switching nop to a jmp and a jmp to a nop and
        # determing whether console code runs to completion i.e. does not enter an infinite loop
        for instruction_no in range(len(self._instructions)):
            if self._instructions[instruction_no].instruction in ('jmp','nop'):
                # swap instruction
                self._instructions[instruction_no].swap()
                try:
                    self.run()
                    break
                except InfiniteLoopDetectedError:
                    pass
                # swap back
                self._instructions[instruction_no].swap()
                