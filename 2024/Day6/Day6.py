
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
from copy import copy

@dataclass 
class Point:
    x: int
    y: int
    
    def increment(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])
    
    def __hash__(self) -> int:
        return hash((self.x,self.y))
    
class Day6:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines: list[str] = [line.strip('\n') for line in input_file]
        
        # Build grid and record start position
        self.grid: dict[Point, str] = dict()
        for x in range(0,len(lines[0])):
            for y in range(0,len(lines)):
                if lines[y][x] == '^':
                    self.grid[Point(x,y)] = '.'
                    self.start_pos: Point = Point(x,y)
                else:    
                    self.grid[Point(x,y)] = lines[y][x]
        
        # increments to move North (0), East (1), South (2) and West (3)        
        self.direction_increments: list[tuple[int,int]] = [(0,-1),(1,0),(0,1),(-1,0)]
            
    def part1(self) -> set[Point]:
        '''
        Fills a set (unique) of points visited traversing grid following Day 6 P1 rules. 
        Traversal ends when next move takes you off the grid.
        Take length of set to get result.
        '''
        curr_direction: int = 0
        curr_increment: tuple[int, int] = self.direction_increments[curr_direction]
        curr_pos: Point = self.start_pos
        positions_visited: set[Point] = set()
        while True:
            positions_visited.add((curr_pos))
            try:
                next_pos = curr_pos.increment(curr_increment)
                if self.grid[next_pos] == '#':
                    # rotate 90 degrees right
                    curr_direction = (curr_direction + 1) % 4
                    curr_increment = self.direction_increments[curr_direction]
                else:
                    curr_pos = next_pos
                    
            except KeyError:      # off grid
                return positions_visited
        

    def part2(self,points: set[Point]) -> int:
        '''
        Similar to Part 1 except for each position visited in Part 1), put in an obstacle.
        Traverse grid again, from start. If the same point is visited, in the same direction twice, must have a loop. 
        If so, increment loop count.
        Return loop count
        '''
        loops: int = 0
        for point in points:
            # do not include start point
            if point != self.start_pos:
                self.grid[point] = '#'
                curr_direction: int = 0
                curr_increment: tuple[int, int] = self.direction_increments[curr_direction]
                curr_pos: Point = self.start_pos
                positions_visited: set[Point, int] = set()
                while (curr_pos, curr_direction) not in positions_visited:
                    positions_visited.add((curr_pos,curr_direction))
                    try:
                        next_pos: Point = curr_pos.increment(curr_increment)
                        if self.grid[next_pos] == '#':
                            # rotate 90 degrees right
                            curr_direction = (curr_direction + 1) % 4
                            curr_increment = self.direction_increments[curr_direction]
                        else:
                            curr_pos = next_pos
                    except KeyError:      # off grid
                        break
                else:
                    loops += 1
                self.grid[point] = '.'
        return loops