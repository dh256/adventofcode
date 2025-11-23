from dataclasses import dataclass,field

@dataclass
class Instruction:
    raw: str
    name: str = field(init=False)
    arg1: str | int = field(init=False)
    arg2: str | int | None = field(init=False)
    
    def __post_init__(self):
        instruction_parts = self.raw.split(' ')
        self.name = instruction_parts[0]
        try:
            self.arg1 = int(instruction_parts[1])
        except ValueError:
            self.arg1 = instruction_parts[1]
        
        try:
            self.arg2 = int(instruction_parts[2])
        except IndexError:
            self.arg2 = None
        except ValueError:
            self.arg2 = instruction_parts[2]
            
class Day18:
    def __init__(self,file_name: str) -> None:
        self._registers: dict[str, int] = {chr(ord('a') + offset): 0 for offset in range(26)}
        with open(file_name, 'r') as input_file:
            self._instructions: list[Instruction] = [Instruction(line.strip('\n')) for line in input_file]
    
    def reg_or_val(self,arg: str | int):
        if type(arg) is int:
            return arg
        else:
            return self._registers[arg]
    
    def part1(self) -> int:
        # run instructions
        curr_instruction: int = 0
        last_sound_played: int | None = None
        while True:
            instruction = self._instructions[curr_instruction]
            if instruction.name == 'set':
                arg2: int = self.reg_or_val(instruction.arg2)
                self._registers[instruction.arg1] = arg2
            elif instruction.name == 'add':
                arg2: int = self.reg_or_val(instruction.arg2)
                self._registers[instruction.arg1] += arg2
            elif instruction.name == 'mul':
                arg2: int = self.reg_or_val(instruction.arg2)
                self._registers[instruction.arg1] *= arg2
            elif instruction.name == 'mod':
                arg2: int = self.reg_or_val(instruction.arg2)
                self._registers[instruction.arg1] %= arg2
            elif instruction.name == 'snd':
                arg1: int = self.reg_or_val(instruction.arg1)
                last_sound_played = arg1
            elif instruction.name == 'rcv':
                arg1: int = self.reg_or_val(instruction.arg1)
                if arg1 > 0:
                    return last_sound_played
            elif instruction.name == 'jgz':
                arg1: int = self.reg_or_val(instruction.arg1)
                arg2: int = self.reg_or_val(instruction.arg2)
                if arg1 > 0:
                    curr_instruction += arg2
                    continue
            
            curr_instruction += 1
            
    def part2(self) -> int:
        pass
        
        