
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from collections import deque
from typing import Self

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])

    def __hash__(self) -> int:
        return hash((self.x,self.y))    
    
class Day10:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # create map and trailheads
        self.map: dict[int,int] = dict()
        self.trailheads: list[int] = list()
        for x in range(0, len(lines[0])):
            for y in range(0, len(lines)):
                self.map[Point(x,y)] = int(lines[y][x])
                if self.map[Point(x,y)] == 0:
                    self.trailheads.append(Point(x,y))    
             
    def solution(self) -> tuple[int,int]:
        '''
        DFS (using stack) to find all possible paths from each 0 (trailhead) to 9 in map
        For Part 1 count the distinct number of time a 9 is reached
        For Part 2 count all times a 9 reached
        '''
        total_score = 0             # part 1
        total_rating = 0            # part 2
        increments: tuple[int,int] = [(1,0),(-1,0),(0,1),(0,-1)]   # right, left, down, up
        for trailhead in self.trailheads:
            nines_reachable: list[Point] = list()
            stack = deque()                
            stack.appendleft((trailhead))
            while len(stack) > 0:
                curr_position: Point = stack.popleft()
                for inc in increments:
                    try:
                        next_position: Point = curr_position.increment(inc)
                        if self.map[next_position] - self.map[curr_position] == 1:
                            if self.map[next_position] == 9:
                                nines_reachable.append(next_position)
                            else:
                                # add to stack
                                stack.appendleft(next_position)     
                    except KeyError:
                        pass    # off grid
            
            total_score += len(set(nines_reachable))
            total_rating += len(nines_reachable)
        return (total_score, total_rating)

    