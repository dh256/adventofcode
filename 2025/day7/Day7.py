from dataclasses import dataclass
from collections import deque
from functools import cache

@dataclass
class Point:
    x: int
    y: int
    
    def __add__(self, p: Point):
        return Point(self.x + p.x, self.y + p.y)
    
    def __eq__(self, p: Point) -> bool:
        return self.x == p.x and self.y == p.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))

class Day7:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            rows: list[str] = [line.strip('\n') for line in input_file]
            
        # build grid
        self._grid: dict[Point, str] = {Point(x,y): rows[y][x] for x in range(len(rows[0])) for y in range(len(rows))} 
        self._start: Point = next(filter(lambda i: i[1] == 'S', self._grid.items()))[0]
    
    
    # breadth first search (Q)
    def part1(self) -> int:
        splits: int = 0
        q: deque[Point] = deque()
        q.append(self._start)
        while len(q) != 0:
            next_point: Point = q.popleft() + Point(0,1)
            if next_point in self._grid:
                if self._grid[next_point] == '^':
                    splits += 1
                    beam_left_point: Point = next_point + Point(-1,0)
                    if len(q) == 0 or q[-1] != beam_left_point:
                        q.append(beam_left_point)
                    beam_right_point: Point = next_point + Point(1,0)
                    q.append(beam_right_point)
                else:
                    if len(q) == 0 or q[-1] != next_point:
                        q.append(next_point)
        
        return splits
    
    # use recursion with memoization
    @cache         
    def _paths(self, start: Point) -> int:
        # reached end of grid, found 1 path
        if start not in self._grid:
            return 1 
        
        # if split, count number of paths in each split
        if self._grid[start] == '^':
            left_path = start + Point(1,0)
            right_path = start + Point(-1,0)
            result = self._paths(left_path) + self._paths(right_path)
        else:        
            # otherwise move down
            result = self._paths(start + Point(0,1))
        return result
    
    def part2(self) -> int:
        return self._paths(self._start)
