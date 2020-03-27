from Point2D import Point2D
from enum import Enum

class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Rotate(Enum):
    LEFT = 0
    RIGHT = 1

class Colour(Enum):
    BLACK = 0
    WHITE = 1

class Robot:

    def __init__(self,program):
        self.program = program
        self.direction = UP
        self.grid = dict()

    def turn(self,rotate):
        new_direction = self.direction + rotate
        if new_direction == -1:
            new_direction = 3
        elif new_direction == 4:
            new_direction = 0
        self.direction = new_direction 
    
    def paint(self,colour):
        

    def run(self,input)