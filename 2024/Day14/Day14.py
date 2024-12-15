
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
import re


@dataclass 
class Offset:
    x: int
    y: int

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, offset: Offset, max_x: int, max_y: int) -> Self: 
        return Point((self.x+offset.x) % max_x, (self.y+offset.y) % max_y)

    def __hash__(self) -> int:
        return hash((self.x,self.y)) 

@dataclass 
class Robot:
    id: int
    position: Point
    velocity: Offset
    
    def move(self, moves:int, max_x: int, max_y: int):
        if moves > 1:
            self.velocity = Offset(self.velocity.x * moves,self.velocity.y * moves )
        self.position = self.position.increment(self.velocity,max_x,max_y)

class Day14:
    def __init__(self,file_name:str,width: int, height: int) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            
        # populate robots
        num_re = re.compile(r'-*\d+')
        self.robots: list[Robot] = list()
        for idx, line in enumerate(lines):
            n0,n1,n2,n3 = num_re.findall(line)
            robot = Robot(idx, Point(int(n0),int(n1)),Offset(int(n2),int(n3)))
            self.robots.append(robot)
        
        # width, height
        self.width: int = width
        self.height: int = height
        
        # quadrants for part 1
        x_split = self.width // 2        
        y_split = self.height // 2
        quad_1 = (Point(0,0),Point(x_split-1,y_split-1))
        quad_2 = (Point(x_split+1,0),Point(self.width-1,y_split-1))
        quad_3 = (Point(0,y_split+1),Point(x_split-1,self.height-1))
        quad_4 = (Point(x_split+1,y_split+1),Point(self.width-1,self.height-1))
        self.quads = [quad_1,quad_2,quad_3,quad_4]
    
    def draw_grid(self):
        grid_str: str = str()
        for y in range(self.height):
            for x in range(self.width):
                robots_at = len(list(filter(lambda r: r.position == Point(x,y), self.robots)))
                if robots_at == 0:
                    grid_str += '.'
                else:
                    grid_str += f'{robots_at}'
            grid_str += '\n'
        print(grid_str)
    
    def quad_counts(self) -> list[int]:
        return [len(list(filter(lambda r: (r.position.x >= quad[0].x and r.position.x <= quad[1].x) and (r.position.y >= quad[0].y and r.position.y <= quad[1].y), self.robots))) for quad in self.quads]
                 
    def part1(self) -> int:
        '''
        Calculate safety factor
        Move each robot 100 times
        Split grid into quadrants, count number in each quadrant, multiply together 
        '''
        for robot in self.robots:
            robot.move(100,self.width,self.height)
    
        total_count = 1
        quad_counts: list[int] = self.quad_counts()
        for quad_count in quad_counts:
            total_count *= quad_count
        
        return total_count

    
    def part2(self) -> int:
        move = 1
        increments = [Offset(1,0),Offset(-1,0),Offset(0,1),Offset(1,0),Offset(0,0)]         # may need to consider (0,0) too 
        start_pos = Point(self.width // 2, self.height // 2)
        while True:
            for robot in self.robots:
                robot.move(1,self.width,self.height)
                    
            # Start in middle of grid if there's a significant number of adjacent points in middle column candidate
            # draw grid and return moves - was a good guess 
            l = len(list(filter(lambda r: r.position.x == start_pos.x and (r.position.y >= start_pos.y-5 and r.position.y <= start_pos.y+5),self.robots)))
            if l > 10:
                self.draw_grid()
                return move  
            
            move += 1 
            
            
            
                        
