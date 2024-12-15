
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
import re
from colorama import Fore

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

class Day15:
    def __init__(self,file_name:str,part: int) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.part = part
        self.increments: dict[str, Offset] = {'>': Offset(1,0), '<': Offset(-1,0), 'v': Offset(0,1), '^': Offset(0,-1)}
        self.map: dict[Point, str] = dict()
        self.moves: str = str()
        mode='map'
        for y, line in enumerate(lines):
            if len(line) == 0:
                self.map_width = x
                self.map_height = y
                mode = 'moves'
            
            if mode == 'map':
                x = 0
                for c in line:
                    if c == '@':
                        self.start_pos: Point = Point(x,y)
                        c = '.'
                    self.map[Point(x,y)] = c
                    x += 1
            
            if mode == 'moves':
                self.moves += line
    
    def draw_grid(self,robot_pos: Point):
        output_str: str = ''
        for y in range(self.map_width):
            for x in range(self.map_width):
                if Point(x,y) == robot_pos:
                    output_str += f'{Fore.GREEN}@{Fore.RESET}'
                else:
                    output_str += self.map[Point(x,y)]
            output_str += '\n'
        output_str += '\n'
        print(output_str)
    
    def move_boxes(self,robot_pos: Point,next_robot_pos: Point,direction: Offset) -> Point:
        '''
        Move boxes in direction 
        '''
        next_box_pos = next_robot_pos
        boxes_to_move: int = 0
        while self.map[next_box_pos] == 'O':
            next_box_pos = next_box_pos.increment(direction)
            boxes_to_move += 1
        
        if self.map[next_box_pos] == '.':
            self.map[next_robot_pos] = '.'
            next_box_pos = next_robot_pos.increment(direction)
            for _ in range(boxes_to_move):
                self.map[next_box_pos] = 'O'
                next_box_pos = next_box_pos.increment(direction)
            return next_robot_pos
        else:
            # can't move boxes
            return robot_pos
    
    def part1(self) -> int:
        # move boxes
        robot_pos: Point = self.start_pos
        for move in self.moves:
            next_pos: Point = robot_pos.increment(self.increments[move])
            if self.map[next_pos] == '.':
                robot_pos = next_pos
            elif self.map[next_pos] == 'O':
                # move box(es)
                robot_pos = self.move_boxes(robot_pos,next_pos,self.increments[move])
            
        # sum of box postions
        return sum([i[0].x + 100 * i[0].y for i in self.map.items() if i[1] == 'O'])

    def part2(self) -> int:
        return 0
         
    def solution(self) -> int:
        if self.part == 1:
            return self.part1()               
        else:
            return self.part2()
