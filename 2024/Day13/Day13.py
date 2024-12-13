
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass
from typing import Self
import re
from math import lcm

@dataclass 
class Offset:
    x: int
    y: int

@dataclass
class Point:
    x: int
    y: int
    
    def increment(self, offset: Offset) -> Self: 
        return Point(self.x+offset.x,self.y+offset.y)

    def __hash__(self) -> int:
        return hash((self.x,self.y))  

@dataclass 
class Machine:
    buttonA: Offset
    buttonB: Offset
    prize: Point

class Day13:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            
        # get machines
        self.machines: list[Machine] = list()
        num_regex = re.compile(r'\d+')
        for line in lines:
            if len(line) != 0:
                x, y = num_regex.findall(line)
                x, y = int(x), int(y)
                if line.startswith('Button A'):
                    buttonA = Offset(x,y)
                elif line.startswith('Button B'):
                    buttonB = Offset(x,y)
                else: 
                    prize = Point(x,y)
            else:
                machine = Machine(buttonA,buttonB,prize)
                self.machines.append(machine)
            
    def solution(self,part: int) -> int:
        # work out min tokens
        total_tokens: int = 0
        
        for machine in self.machines:
            x = machine.prize.x 
            y = machine.prize.y
            if part == 2:
                x += 10_000_000_000_000
                y += 10_000_000_000_000
                
            ax = machine.buttonA.x
            bx = machine.buttonB.x
            ay = machine.buttonA.y
            by = machine.buttonB.y
            
            '''
            need to solve equations
            pa * ax + pb * bx = x    (1)
            pa * ay + pb * by = y    (2)
            '''
            
            lcm_x = lcm(ax,ay)
            multiplier_1 = lcm_x // ax 
            multiplier_2 = lcm_x // ay

            pb_enumerator = x * multiplier_1 - y * multiplier_2
            pb_denominator = bx * multiplier_1 - by * multiplier_2
            if pb_enumerator % pb_denominator == 0:
                # solution for pb
                pb =  pb_enumerator // pb_denominator
                
                # solve for pa by substituting pb into
                # pa * ax + pb * bx = x => pa = (x - pb * bx) / ax
                # only have a solution if (x - pb * bx) % ax == 0
                pa_enumerator = (x - bx * pb)
                pa_denominator = ax
                if pa_enumerator % pa_denominator == 0:
                    # solution for pa
                    pa = pa_enumerator // pa_denominator
                    total_tokens += pa * 3 + pb
            
        return total_tokens
                        
