
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
                        
    def bfs(self) -> dict[Point,int]:
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
    
    def valid_cheats(self, curr_point: Point, shortest_path: dict[Point,int], walls_walked: set[Point]) -> list[tuple[int,int]]:
        '''
        Are there walls worth walking through:
        Yes, if one (or more) of following patterns met and wall not already walked through: 
            
            .#.
            
        or 
        
            .
            #
            .
            
        where # is a wall and . is a point on shortest path
                
        '''
        cheats: list[tuple[int,int]] = list()
        for offset in self.offsets:
            poss_wall_point: Point = curr_point.increment(offset)
            poss_path_point: Point = curr_point.increment(Offset(offset.x*2,offset.y*2))
            if poss_wall_point in self.walls and poss_path_point in shortest_path.keys():
                if poss_wall_point not in walls_walked:
                    time_saved: int = shortest_path[poss_path_point] - shortest_path[curr_point] - 2
                    if time_saved > 0:
                        cheats.append((time_saved,poss_wall_point))
        return cheats
            
    def part1(self) -> int:
        reduced_time_count: int = 0
        shortest_path: dict[Point,int] = self.bfs()
        
        # debugging
        times_saved: dict[int,int] = defaultdict(int)
        
        # Holds walls already walked through
        walls_walked: set[Point] = set()
        for curr_point in list(shortest_path.keys())[::-1]:
            for cheat in self.valid_cheats(curr_point,shortest_path, walls_walked):
                time_saved, wall_walked = cheat
                walls_walked.add(wall_walked)
                
                # debugging
                times_saved[time_saved] += 1
                
                if time_saved >= 100:           # need to change this for actual input
                    reduced_time_count += 1
    
        for k,v in sorted(times_saved.items(), key=lambda i: i[0]):
            print(f'There are {v} cheats that save {k} picseconds')
            
        return reduced_time_count
        
    def part2(self) -> int:
        return 0
                        
