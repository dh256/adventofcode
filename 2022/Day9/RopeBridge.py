from dataclasses import dataclass, field
from enum import Enum
from itertools import pairwise

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
    def __init__(self,file_name,length=2):
        with open(file_name,'r') as input_file:
            self.moves = [Move(move_parts=line.strip('\n').split(' ')) for line in input_file]

        self.knots = [Point(0,0)] * length      # create a list holding current position of each knot. Head knot is index 0; 
        self.tail_knot = length - 1             # index of tail knot
    
    def move_knot(self,successor_index: int) -> None:
        # only move predecessor if is no longer adjacent to successor
        successor = self.knots[successor_index]
        predecessor = self.knots[successor_index+1]
        if not successor.adjacent(predecessor):
            # move predecessor
            if successor.x > predecessor.x and successor.y == predecessor.y:
                # move one to the right
                predecessor = Point(predecessor.x+1,predecessor.y)
            elif successor.x < predecessor.x and successor.y == predecessor.y:
                # move one to the left
                predecessor = Point(predecessor.x-1,predecessor.y)
            elif successor.y > predecessor.y and successor.x == predecessor.x:
                # move one up
                predecessor = Point(predecessor.x,predecessor.y+1)
            elif successor.y < predecessor.y and successor.x == predecessor.x:
                # move one down
                predecessor = Point(predecessor.x,predecessor.y-1)
            elif successor.x > predecessor.x and successor.y > predecessor.y:
                # move up one and right one
                predecessor = Point(predecessor.x+1,predecessor.y+1)
            elif successor.x > predecessor.x and successor.y < predecessor.y:
                # move down one and right one
                predecessor = Point(predecessor.x+1,predecessor.y-1)
            elif successor.x < predecessor.x and successor.y < predecessor.y:
                # move left one and down one
                predecessor = Point(predecessor.x-1,predecessor.y-1)
            elif successor.x < predecessor.x and successor.y > predecessor.y:
                # move up one and left one
                predecessor = Point(predecessor.x-1,predecessor.y+1)

            # update predecessors new point
            self.knots[successor_index+1] = predecessor

    def move(self) -> None:
        '''
        Move rope according to move instructions
        Record the points that tail knot visits (once) along the way
        '''
        self.tail_visited_once = {Point(0,0)}        # Use a set. Only need to know if visited once
        for move in self.moves:
            for _ in range(0,move.steps):
                # head moves
                self.knots[0] = Point(self.knots[0].x + move.x_inc, self.knots[0].y + move.y_inc)

                # move all other knots (will only move if not adjacent to its successor)
                for knot_index in range(0,self.tail_knot):
                    self.move_knot(knot_index)

                # add tail to tail_visited_set (duplicates ignored)
                self.tail_visited_once.add(self.knots[self.tail_knot])
    
    @property
    def tail_visit_at_least_once(self) -> int:
        '''
        Number of points visited at least once during last set of moves
        '''
        return len(self.tail_visited_once)