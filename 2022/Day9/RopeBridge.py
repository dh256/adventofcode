from dataclasses import dataclass, field
from enum import Enum

class Direction(Enum):
    RIGHT='R'
    LEFT='L'
    UP='U'
    DOWN='D'

@dataclass(eq=True, frozen=True)        # Point is immutable, is hashable and can be used in a set
class Point:
    x: int
    y: int

    def adjacent(self, p2) -> bool:
        '''
        Return True if this point is adjacent (in any direction) to other point
        '''
        return abs(self.x - p2.x) <= 1 and abs(self.y - p2.y) <= 1

@dataclass
class Move:
    move_parts: list = field(kw_only=True)
    direction: Direction = field(init=False)
    steps: int = field(init=False)
    x_inc: int = field(init=False,default=0)
    y_inc: int = field(init=False,default=0)

    def __post_init__(self):
        self.direction = Direction(self.move_parts[0])
        self.steps = int(self.move_parts[1])
        if self.direction == Direction.RIGHT:
            self.x_inc = 1
        elif self.direction == Direction.LEFT:
            self.x_inc = -1
        elif self.direction == Direction.UP:
            self.y_inc = 1
        elif self.direction == Direction.DOWN:
            self.y_inc = -1

class Rope:
    def __init__(self,file_name):
        with open(file_name,'r') as input_file:
            self.moves = [Move(move_parts=line.strip('\n').split(' ')) for line in input_file]

        # mark the start position of head and tail
        self.head_curr_pos = Point(0,0)
        self.tail_curr_pos = Point(0,0)

    
    def move(self) -> int():
        '''
        Move rope according to move instructions
        Record the points that tail visits (once) along the way
        '''
        self.tail_visited_once = {Point(0,0)}        # Use a set. Only need to know if visited once
        for move in self.moves:
            for _ in range(0,move.steps):
                # head moves
                self.head_curr_pos = Point(self.head_curr_pos.x + move.x_inc, self.head_curr_pos.y + move.y_inc)

                # tail moves only if its not adjacent to head
                if not self.head_curr_pos.adjacent(self.tail_curr_pos):
                    # move tail
                    if move.direction == Direction.RIGHT:
                        self.tail_curr_pos = Point(self.head_curr_pos.x-1, self.head_curr_pos.y)
                    elif move.direction == Direction.LEFT:
                        self.tail_curr_pos = Point(self.head_curr_pos.x+1, self.head_curr_pos.y)
                    elif move.direction == Direction.UP:
                        self.tail_curr_pos = Point(self.head_curr_pos.x, self.head_curr_pos.y-1)
                    elif move.direction == Direction.DOWN:
                        self.tail_curr_pos = Point(self.head_curr_pos.x, self.head_curr_pos.y+1)

                    self.tail_visited_once.add(self.tail_curr_pos)
    
    @property
    def tail_visit_at_least_once(self) -> int:
        '''
        Number of points visited at least once during last set of moves
        '''
        return len(self.tail_visited_once)