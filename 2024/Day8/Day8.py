
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass, field
from collections import defaultdict
from typing import Self
from itertools import combinations

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])
    
    def xy_offset(self,p2,reversed: bool=False) -> tuple[int,int]:
        '''
        Returns x, y offset required to move from p1 (self) to p2
        e.g. -1,-1 indicates a that to move from self to p2 you need to move left 1 and up 1
        If reversed, return x_offset*-1 and y_offset*-1
        '''
        x_offset = p2.x - self.x if not reversed else (p2.x - self.x) * -1
        y_offset = p2.y - self.y if not reversed else (p2.y - self.y) * -1
        return (x_offset,y_offset)

    def __hash__(self) -> int:
        return hash((self.x,self.y))        

@dataclass
class GridItem:
    '''
    Grid point can either hold an atenna and/or set of antinodes 
    '''
    atenna: str
    antinodes: set[str] = field(default_factory=set)
    
    def __hash__(self):
        return hash((self.atenna,tuple(self.antinodes)))
    
class Day8:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # holds the grid/map
        self.grid: dict[Point, GridItem] = dict()
        
        # for speed/convenience also hold the locations of each antenna type
        self.antenna_locations: dict[str, list[Point]] = defaultdict(list)
        
        # populate above
        for x in range(0,len(lines[0])):
            for y in range(0, len(lines)):
                self.grid[Point(x,y)] = GridItem(atenna=lines[y][x])
                if lines[y][x] != '.':
                    self.antenna_locations[self.grid[Point(x,y)].atenna].append(Point(x,y))
    
    def add_antinode(self,part: int, antenna: str,p1: Point, p2: Point) -> None:
        '''
        Work out x,y offset from p1 -> p2 record an antinode at p1.increment(reversed_offset)
        where reversed_offset = x_offset * -1, y_offset * -1
        Add antinodes at each incremnent (stopping after first increment if part 1) until off grid
        '''
        if part == 2:
            self.grid[p1].antinodes.add(antenna)
        xy_offset: tuple[int,int] = p1.xy_offset(p2,reversed=True)
        while True:
            p1 = p1.increment((xy_offset[0],xy_offset[1]))   
            try:
                self.grid[p1].antinodes.add(antenna)
                if part == 1:
                    return
            except KeyError: 
                return
            
    def add_antinodes(self,part:int) -> int:
        for antenna, locations in self.antenna_locations.items():
            if len(locations) > 1:
                '''
                Get all combinations of pairs
                For each pair, add antinodes relative to p1 and p2, (ony add one for Part 1) 
                Return unique number of antinodes added
                '''
                antenna_pairs: combinations = combinations(locations,2)
                for p1,p2 in antenna_pairs:
                    self.add_antinode(part,antenna,p1,p2)
                    self.add_antinode(part,antenna,p2,p1)
        
        return sum([1 for v in self.grid.values() if len(v.antinodes) > 0])
    
    def part1(self) -> int:
        return self.add_antinodes(1)
    
    def part2(self) -> int:
        return self.add_antinodes(2)

                        
