from enum import StrEnum
from collections import deque

class MoveType(StrEnum):
    SPIN = 's'
    EXCHANGE = 'x'
    PARTNER = 'p'

class Move:
    def __init__(self, raw_move: str) -> None:
        self.a: str | int = 0
        self.b: str | int | None = None
        self.type: MoveType = MoveType(raw_move[0])
        if self.type == MoveType.SPIN:
            self.a = int(raw_move[1:])
        elif self.type == MoveType.EXCHANGE:
            positions: list[str] = raw_move[1:].split('/')
            self.a = int(positions[0])
            self.b = int(positions[1])
        else:
            self.a = raw_move[1]
            self.b = raw_move[3]
            
class Day16:
    def __init__(self,filename: str,programs: int=16) -> None:
        self._num_programs = programs
        self._programs: deque[str] = deque()
        with open(filename, 'r') as input_file:
            self._moves: list[Move] = [Move(m) for m in input_file.readline().strip('\n').split(',')]
            self.reset()
            self._original = ''.join(self._programs)
    
    def reset(self):
        self._programs = deque([chr(ord('a') + offset) for offset in range(self._num_programs)])
     
    def part1(self) -> str:
        '''
        Do all the moves and return program order when done
        '''
        for move in self._moves:
            if move.type == MoveType.SPIN:
                for _ in range(move.a):
                    self._programs.appendleft(self._programs.pop())    
            elif move.type == MoveType.EXCHANGE:
                temp = self._programs[move.a]
                self._programs[move.a] = self._programs[move.b] 
                self._programs[move.b] = temp
            else:
                posa = self._programs.index(move.a)
                posb = self._programs.index(move.b)
                temp = self._programs[posa]
                self._programs[posa] = self._programs[posb]
                self._programs[posb] = temp
                   
        return ''.join(self._programs)
    
    def part2(self) -> str:
        '''
        Do all moves storing state at end of set (each set indexed by a counter) until return to original program state
        Return state at index 1000000000 % counter
        '''
        self.reset()
        counter: int = 1
        results: dict[int, str] = dict()
        results[1] = self._original
        while True:
            results[counter] = self.part1()
            if results[counter] == self._original:
                return results[1000000000 % counter]
            counter += 1
            
            