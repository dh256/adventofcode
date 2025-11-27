from dataclasses import dataclass,field
from collections import deque

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
            

class LastSoundPlayedInterrupt(Exception):
    pass
class ProgramExited(Exception):
    pass
class Tablet:
    def __init__(self, code: list[str]):
        # registers
        self._registers: list[dict[str, int]] = list()
        self._instructions: list[list[Instruction]] = list()
        self._instruction_pointer: list[int] = list()
        self._queues: list[deque[int]] = list()
        self._program_waiting: list[bool] = list()
        
        for _ in range(2):
            self._registers.append({chr(ord('a') + offset): 0 for offset in range(26)})
            self._instructions.append([Instruction(code_line) for code_line in code])
            self._instruction_pointer.append(0)
            self._queues.append(deque())
            self._program_waiting.append(False)
        self._registers[1]['p'] = 1
        
        # part 1 and part 2 results
        self._last_sound_played: int = 0
        self._program1_sent: int = 0

    def reg_or_val(self,arg: str | int,program: int):
        '''
        Determine whether instruction arguement refers to a registy or is a number
        If number return number
        If registry return value in registry
        '''
        if type(arg) is int:
            return arg
        else:
            return self._registers[program][arg]
    
    def execute_next_instruction(self,part: int,program: int):
        '''
        Execute next instruction for given program
        For part 1 and part 2 - snd and rcv instructions have different behaviours
        Increments instruction pointer as needed
        '''
        instruction: Instruction = self._instructions[program][self._instruction_pointer[program]]
        if instruction.name == 'set':
            arg2: int = self.reg_or_val(instruction.arg2,program)
            self._registers[program][instruction.arg1] = arg2
            self._instruction_pointer[program] += 1
        elif instruction.name == 'add':
            arg2: int = self.reg_or_val(instruction.arg2,program)
            self._registers[program][instruction.arg1] += arg2
            self._instruction_pointer[program] += 1
        elif instruction.name == 'mul':
            arg2: int = self.reg_or_val(instruction.arg2,program)
            self._registers[program][instruction.arg1] *= arg2
            self._instruction_pointer[program] += 1
        elif instruction.name == 'mod':
            arg2: int = self.reg_or_val(instruction.arg2,program)
            self._registers[program][instruction.arg1] %= arg2
            self._instruction_pointer[program] += 1
        elif instruction.name == 'snd':
            arg1: int = self.reg_or_val(instruction.arg1,program)
            if part == 1:
                self._last_sound_played = arg1
            else:
                self._queues[not program].append(arg1)
                if program == 1:
                    self._program1_sent += 1
            self._instruction_pointer[program] += 1
        elif instruction.name == 'rcv':
            if part == 1:
                arg1: int = self._registers[program][instruction.arg1]
                if arg1 > 0:
                    raise LastSoundPlayedInterrupt()
                else:
                    self._instruction_pointer[program] += 1
            else:
                if len(self._queues[program]) > 0:
                    self._program_waiting[program] = False
                    self._registers[program][instruction.arg1] = self._queues[program].popleft()
                    self._instruction_pointer[program] += 1
                else:
                    # wait and do not execute instruction pointer
                    self._program_waiting[program] = True
                
        elif instruction.name == 'jgz':
            arg1: int = self.reg_or_val(instruction.arg1,program)
            arg2: int = self.reg_or_val(instruction.arg2,program)
            if arg1 > 0:
                self._instruction_pointer[program] += arg2
            else:
                self._instruction_pointer[program] += 1
        
        if self._instruction_pointer[program] < 0 or self._instruction_pointer[program] >= len(self._instructions[program]):
            raise ProgramExited()
        
    def run(self, part: int) -> int:
        '''
        Run tablet program(s)
        Part 1 - execute instructions (program 0 only) until LastSoundPlayedInterrupt received
        Part 2 - execute instructions in program 0 and program 1 until deadlock or both programs end
        '''
        if part == 1:
            # run instructions
            while True:
                try:
                    self.execute_next_instruction(1,0)
                except LastSoundPlayedInterrupt:
                    return self._last_sound_played
                except ProgramExited:
                    print('Program Exited')
                    exit()
                    
        else:
            programs_done: list[bool] = [False, False]
            while True: 
                # keep going unti both program0 and program1 are done 
                # or both program0 and program1 waiting
                if programs_done[0] and programs_done[1]: 
                    break
                    
                if self._program_waiting[0] and self._program_waiting[1]:
                    break
                
                # execute next instruction for each program
                for program in range(2):
                    try:
                        self.execute_next_instruction(2,program)
                    except ProgramExited as pe0:
                        programs_done[program] = True
            
            return self._program1_sent    
            
class Day18:
    def __init__(self,file_name: str) -> None:
        with open(file_name, 'r') as input_file:
            self._code: list[str] = [line.strip('\n') for line in input_file]
    
    def part1(self) -> int:
        tablet = Tablet(self._code)
        return tablet.run(1)
                        
    def part2(self) -> int:
        tablet = Tablet(self._code)
        return tablet.run(2)
        
        