
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
from collections import deque, defaultdict
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
    
    def in_range(self,x: int,y: int) -> bool:
        '''
        True if point lies in range (0,0) to (x,y) - exclusive
        False, otherwise
        '''
        return (self.x >= 0 and self.x < x) and (self.y >= 0 and self.y < y)
class Day20:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.offsets: list[Offset] = [Offset(1,0),Offset(-1,0),Offset(0,1),Offset(0,-1)]
        self.map_width = len(lines[0])
        self.map_height = len(lines)
        self.walls: set[Point] = set()
        for y in range(self.map_height):
            for x in range(self.map_width):
                if lines[y][x] == '#':
                    self.walls.add(Point(x,y))
                elif lines[y][x] == 'S':
                    self.start: Point = Point(x,y)
                elif lines[y][x] == 'E':
                    self.end: Point = Point(x,y)
                        
    def shortest_path(self) -> dict[Point,int]:
        '''
        Perform a BFS from start_pos to end_pos across map using given set of walls
        For each point visited will need to track point came from and steps (time) to get there. Needed to retrace shortest path.
        
        Then backtrack through visited nodes from end back to start to create shortest path. For each point on path stores distance (steps) from start 
        Return the full path
        '''
        visited: dict[Point,tuple[int,Point]] = dict()
        q: deque[tuple[Point,int]] = deque()
        q.append((self.start,0, None))
        while len(q) > 0:
            curr_point, time, point_from = q.popleft()
            if curr_point in visited:
                continue
            
            if curr_point == self.end:
                # need to retrace. For each point encountered record steps from start
                path: dict[Point,int] = dict()
                path[curr_point] = time
                curr_point = point_from
                while curr_point is not None:
                    path[curr_point] = visited[curr_point][1]
                    curr_point = visited[curr_point][0]
                return path
        
            visited[curr_point] = (point_from,time)
            for i in self.offsets:
                next_point = curr_point.increment(i)
                if next_point.in_range(self.map_width,self.map_height) and next_point not in self.walls:
                    q.append((next_point,time+1,curr_point))                     
    
    def possible_cheat_points(self,start_point:Point,shortest_path: dict[Point,int], cheats: int) -> dict[Point,int]:
        '''
        Starting at curr_point, find all possible points "cheats" steps from curr_point
        A possible point must be on the existing shortest_path and can only be considered once
        Return possible point with steps to get to that point
        Uses BFS
        '''
        q: deque[tuple[Point,int]] = deque()
        visited: set[Point] = set()
        q.append((start_point,0))
        possible_points: dict[Point,int] = dict()
        while len(q) > 0:
            curr_point, steps = q.popleft()
            
            if curr_point in visited:
                continue
            
            visited.add(curr_point)
            
            # is it a possible point
            if curr_point != start_point and curr_point in shortest_path and curr_point not in possible_points.keys():
                possible_points[curr_point] = steps
                
            if steps == cheats:
                continue
                
            # move to next point
            for offset in self.offsets:
                next_point = curr_point.increment(offset)
                if next_point.in_range(self.map_width,self.map_height):
                    q.append((next_point,steps+1)) 
        
        return possible_points
    
    def valid_cheats(self, start_point: Point, shortest_path: dict[Point,int], cheats: int) -> list[tuple[int,int]]:
        possible_points: dict[Point,int] = self.possible_cheat_points(start_point,shortest_path,cheats) 
        
        # process possible points from BFS above 
        cheats: list[tuple[int,int]] = list()
        for possible_point,steps in possible_points.items():
            time_saved: int = shortest_path[possible_point] - shortest_path[start_point] - steps
            if time_saved > 0:
                cheats.append(time_saved)
        return cheats
     
    def solution(self,save_at_least: int) -> list[int]:
        shortest_path: dict[Point,int] = self.shortest_path()
        
        solutions: list[int] = list() 
        for cheat_length in [2,20]: 
            times_saved: dict[int,int] = defaultdict(int)
            for curr_point in list(shortest_path.keys())[::-1]:
                for cheat in self.valid_cheats(curr_point,shortest_path,cheat_length):
                    times_saved[cheat] += 1
            solutions.append(sum([v for k, v in times_saved.items() if k >= save_at_least]))
        return solutions    
                        
