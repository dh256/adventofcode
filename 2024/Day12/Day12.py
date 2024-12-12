
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass, field
from typing import Self
from collections import deque, defaultdict
from itertools import product

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, increment: tuple[int,int]) -> Self: 
        return Point(self.x+increment[0],self.y+increment[1])

    def __eq__(self,p2) -> bool:
        return self.x == p2.x and self.y == p2.y

    def __hash__(self) -> int:
        return hash((self.x,self.y))  

@dataclass
class Region:
    plot: str
    area: int = 0
    perimeter_points: list[tuple[Point,tuple[int,int]]] = field(default_factory=list)

class Day12:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.increments: list[tuple[int,int]] = [(1,0),(-1,0),(0,1),(0,-1)]
        
        # create map of garden plots
        self.max_x = len(lines[0])
        self.max_y = len(lines)
        self.map: dict[Point,str] = dict()
        for x in range(self.max_x):
            for y in range(self.max_y):
                self.map[Point(x,y)] = lines[y][x]
    
    def remove_next_points(self, p: Point, inc: tuple[int,int], direction: tuple[int,int],points: list[Point]) -> Point | None:
        ''' 
        Removes next point in given direction until no more exists
        '''
        while True:
            p = p.increment(direction)
            try:
                points.remove((p,inc))      
            except ValueError:
                return
    
    def number_of_sides(self, r: Region) -> int:
        '''
        Calculate numner of sides
        Take any remaining perimeter point:
            A side exists if 0 or more adjacent points (either, Left/Right/Up or Down) with same direction_from are found
            Delete all perimeter points on the side (including point itself) and increment side count by 1
        '''
        sides: int = 0
        while len(r.perimeter_points) > 0:
            p, direction_from = r.perimeter_points[0]
            for inc in self.increments:
                self.remove_next_points(p,direction_from,inc,r.perimeter_points)
            r.perimeter_points.remove((p,direction_from))
            sides += 1
        return sides
            
    def create_regions(self) -> list[Region]:
        '''
        Find region perimeter and area, using BFS (making sure to never visit same point twice)
        Region perimeter found whenever a new plot is found (e.g. in A and find B) or go off map
        Capture perimter points and direcion coming from (inc) for each perimter point; direction_from needed for identifying sides in Part 2 
        '''
        points_visited: set[Point] = set()
        regions: list[Region] = list()       # plot, area, list of perimeter points (and direction from)
        
        for x in range(0,self.max_x):
            for y in range(0,self.max_y):
                start_point: Point = Point(x,y)
                if start_point not in points_visited:
                    q: deque[Point] = deque()
                    region = Region(self.map[start_point])
                    q.append(start_point)
                    while len(q) > 0:
                        curr_point = q.popleft()
                        for next_point, direction_from in ((curr_point.increment(inc), inc) for inc in self.increments):
                            try:
                                # check if still in same region (i.e. plot has not changed)
                                if self.map[next_point] == region.plot:
                                    # if next point not already visited or not already in Q, append to Q
                                    if next_point not in points_visited and next_point not in q: 
                                        q.append(next_point)
                                else:
                                    # otherwise at perimeter
                                    region.perimeter_points.append((next_point,direction_from))                 
                            except KeyError:
                                # off map, at perimeter
                                region.perimeter_points.append((next_point,direction_from))
                        
                        points_visited.add(curr_point)
                        region.area += 1 
                    
                    # region complete
                    regions.append(region) 
        
        return regions
    
    def solution(self) -> tuple[int,int]:
        '''
        Create regions (including area and perimeter points)
        For Part 1 calculate sum of perimter length * area for all region
        For Part 2 calculate number of sides for each region and calculate sum of sides * area for all regions
        '''
        regions = self.create_regions()        
        perims_cost = sum([r.area * len(r.perimeter_points) for r in regions])
        sides_cost = sum([self.number_of_sides(r) * r.area for r in regions])
            
        # return results
        return perims_cost, sides_cost
    
   
                        

                        
