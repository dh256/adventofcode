
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self

@dataclass 
class Point:
    x: int
    y: int
    
    def add(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])
    
    def __hash__(self):
        return hash((self.x,self.y))
    
class Day4:
    def __init__(self,file_name:str) -> None:
        
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.min_y = 0
        self.min_x = 0
        self.max_x = len(lines[0])
        self.max_y = len(lines)
        
        self.grid: dict[Point,str] = dict()    
        for x in range(self.min_x,self.max_x):
            for y in range(self.min_y,self.max_y):
                self.grid[Point(x,y)] = lines[y][x]
        
    def xmas_exists(self: Self, p: Point, increment: tuple[int,int]) -> bool:
        next_point = p
        for c in 'MAS':
            next_point = next_point.add(increment)
            try:
                if self.grid[next_point] != c:
                    return False
            except KeyError:
                return False
        return True
            
    def part1(self) -> int:
        increments = [(0,-1),(0,1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        count_xmas: int = 0
        for x in range(self.min_x,self.max_x):
            for y in range(self.min_y,self.max_y):
                p: Point = Point(x,y)
                if self.grid[p] == 'X':
                    # look to see whether word XMAS exists in any possible direction
                    for increment in increments:
                        if self.xmas_exists(p,increment):
                            count_xmas += 1   
        return count_xmas    
  

    def part2(self) -> int:
        return 0
                        
