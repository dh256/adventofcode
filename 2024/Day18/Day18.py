
''' 
David Hanley, December 2024
'''
import re
from dataclasses import dataclass
from typing import Self
from collections import deque

@dataclass 
class Offset:
    x: int
    y: int

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, offset: Offset) -> Self: 
        return Point(self.x+offset.x, self.y+offset.y)        

    def __hash__(self) -> int:
        return hash((self.x,self.y)) 

class Day18:
    def __init__(self,file_name:str,grid_width: int, grid_height: int,num_bytes: int) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.grid: dict[Point,str] = dict()
        self.grid_width: int = grid_width
        self.grid_height: int = grid_height
        self.byte_coords: list[Point] = [Point(int(byte_strs[0]),int(byte_strs[1])) for byte_strs in [re.findall(r'\d+',line) for line in lines]]
        for x in range(0,self.grid_width):
            for y in range(self.grid_height):
                curr_point = Point(x,y)
                if curr_point in self.byte_coords[0:num_bytes]:
                    self.grid[Point(x,y)] = '#'
                else:
                    self.grid[Point(x,y)] = '.'
    
    def draw_grid(self) -> None:
        out_str: str = str()
        for y in range(self.grid_height):
            for x in range(0,self.grid_width):
                out_str += self.grid[Point(x,y)]
            out_str += '\n'
        print(out_str)
           
    def part1(self) -> int:
        visited: set[Point] = set()
        q: deque[tuple[Point,int]] = deque()
        q.append((Point(0,0),0))
        while len(q) > 0:
            curr_pos, steps = q.popleft()
            if curr_pos in visited:
                continue
            
            if curr_pos == Point(self.grid_width-1,self.grid_height-1):
                return steps
        
            visited.add(curr_pos)            
            for i in [Offset(0,1),Offset(0,-1),Offset(1,0),Offset(-1,0)]:
                next_pos = curr_pos.increment(i)
                try:
                    if self.grid[next_pos] != '#':
                        q.append((next_pos,steps+1))
                except KeyError:
                    pass
                
    def part2(self) -> int:
        return 0
                        
