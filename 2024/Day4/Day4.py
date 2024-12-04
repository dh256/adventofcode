
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
from itertools import product

@dataclass 
class Point:
    x: int
    y: int
    
    def increment(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])
    
    def __hash__(self) -> int:
        return hash((self.x,self.y))
    
class Day4:
    def __init__(self,file_name:str) -> None:
        
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # increments used in finding XMAS words
        self.increments = [p for p in product(range(-1,2),range(-1,2)) if p != (0,0)]
        
        # populate grid
        self.max_x = len(lines[0])
        self.max_y = len(lines)
        self.grid: dict[Point,str] = dict()    
        for x in range(0,self.max_x):
            for y in range(0,self.max_y):
                self.grid[Point(x,y)] = lines[y][x]
        
    def xmas_found(self: Self, p: Point) -> int:
        found = 0
        for increment in self.increments:
            next_point = p
            for c in 'MAS':
                next_point = next_point.increment(increment)
                try:
                    if self.grid[next_point] != c:
                        break
                except KeyError:    # off grid
                    break
            else:
                found += 1
        return found
    
    def mas_exists(self: Self, p: Point) -> bool:
        try:
            # vertical
            first_word = self.grid[p.increment((-1,1))] + 'A' + self.grid[p.increment((1,1))]
            second_word = self.grid[p.increment((-1,-1))] + 'A' + self.grid[p.increment((1,-1))]
            if first_word in ('SAM','MAS') and first_word == second_word:
                return True
            
            # horizontal    
            first_word = self.grid[p.increment((-1,-1))] + 'A' + self.grid[p.increment((-1,1))]
            second_word = self.grid[p.increment((1,-1))] + 'A' + self.grid[p.increment((1,1))]
            if first_word in ('SAM','MAS') and first_word == second_word:
                return True
                
            return False
                
        except KeyError:    # off grid
            return False
        
        
    def solution(self) -> tuple[int,int]:
        count_xmas: int = 0
        count_mas: int = 0
        for x in range(0,self.max_x):
            for y in range(0,self.max_y):
                p: Point = Point(x,y)
                if self.grid[p] == 'X':
                    count_xmas += self.xmas_found(p)
                elif self.grid[p] == 'A':
                    if self.mas_exists(p):
                        count_mas += 1 
                    
        return (count_xmas,count_mas)
     
                        
