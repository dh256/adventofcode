import re
from enum import Enum, auto
from Stack import Stack
from collections import namedtuple
from copy import deepcopy

Move = namedtuple('Move', 'num_crates from_stack to_stack')

class ImportMode(Enum):
    STACKS=auto()
    MOVES=auto()

class CraneType(Enum):
    CRATE_MOVER_9000=auto()
    CRATE_MOVER_9001=auto()

class CrateStacks:
    def __init__(self, file_name) -> None:
        self.stacks = list()
        self.moves = list()
        with open(file_name, 'r') as input_file:
            mode = ImportMode.STACKS
            moves_regex = re.compile('\d+')
            stack_input = list()
            for line in input_file:
                line = line.strip('\n')
                if mode == ImportMode.STACKS:
                    if len(line) == 0:
                        # process stack input by creating stacks and change mode to MOVES
                        num_stacks = int(re.findall(r'\d',stack_input[-1])[-1])
                        self.stacks = [Stack() for _ in range(0,num_stacks)]
                        for stack_line in reversed(stack_input[0:-1]):
                            for stack_index in range(0,num_stacks):
                                if stack_index == 0:
                                    curr_crate = stack_line[1]
                                else:
                                    curr_crate = stack_line[stack_index * 4 + 1] 
                                if curr_crate != ' ':
                                    self.stacks[stack_index].push(curr_crate)
                        mode = ImportMode.MOVES
                    else:
                        # read in stack input, will process once we have all stack data
                        stack_input.append(line)
                else:
                    # process moves
                    move_parts = moves_regex.findall(line)
                    self.moves.append(Move(int(move_parts[0]),int(move_parts[1]),int(move_parts[2])))
        
        self.original = deepcopy(self.stacks)


    def perform_moves(self,crane_type):
        '''
        Move crates according to move instructions
        '''
        for move in self.moves:
            if crane_type == CraneType.CRATE_MOVER_9000:
                for _ in range(0,move.num_crates):
                    crate_to_move = self.stacks[move.from_stack-1].pop()
                    self.stacks[move.to_stack-1].push(crate_to_move)
            else:
                crates_to_move = Stack()
                for _ in range(0,move.num_crates):
                    crates_to_move.push(self.stacks[move.from_stack-1].pop()) 
                
                while True:
                    crate = crates_to_move.pop()
                    if not crate is None:
                        self.stacks[move.to_stack-1].push(crate)
                    else:
                        break

    @property
    def top(self) -> str:
        '''
        Return a string showing the crates at top of each stack
        '''
        return ''.join([stack.peek() for stack in self.stacks])
    
    def reset(self) -> None:
        '''
        Resets crate stack arrangement to original
        '''
        self.stacks = deepcopy(self.original)