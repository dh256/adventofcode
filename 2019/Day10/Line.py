from Point2D import Point2D
from enum import Enum,auto
import math

class Slope(Enum):
    UP=auto(),
    DOWN=auto(),
    VERTICAL=auto(),
    HORIZONTAL=auto()

class Line:
    def __init__(self,start,end):
        '''
        Straight line between two points start and end
        delta_x = differnce between x-coords of start and end
        delta_y = diffetence between y-coords of start and end
        Work out the gcd (greatest common divisor) of delta_x and delta_y and integer divide delta_x and delta_x 
        '''
        # line always starts with point with lowest x value, swap if start.x > end.x
        if start.x > end.x:
            temp = Point2D(end.x,end.y)
            end = Point2D(start.x,start.y)
            start = temp

        self.start = start
        self.end = end
        self.delta_x = self.end.x - self.start.x 
        self.delta_y = abs(self.end.y - self.start.y)
        self.gcd = math.gcd(self.delta_x,self.delta_y)
        self.delta_x_g = self.delta_x // self.gcd
        self.delta_y_g = self.delta_y // self.gcd
        
        # work out slope
        if self.start.x == self.end.x:
            self.slope = Slope.VERTICAL
        else:
            if self.start.y == self.end.y:
                self.slope = Slope.HORIZONTAL
            elif self.start.y < self.end.y:
                self.slope = Slope.DOWN
            elif self.start.y > self.end.y:
                self.slope = Slope.UP

    def point_on_line(self,point):
        '''
        Returns True if point is on line, i.e. lies between start and end point, False otherwise
        '''
        # point must lie between min_x and max_x and min_y and max_y
        if self.start.y < self.end.y:
            min_y = self.start.y
            max_y = self.end.y
        else:
            min_y = self.end.y
            max_y = self.start.y

        if self.start.x < self.end.x:
            min_x = self.start.x
            max_x = self.end.x
        else:
            min_x = self.end.x
            max_x = self.start.x

        if (point.x >= min_x and point.x <= max_x) and (point.y >= min_y and point.y <= max_y):
            if self.slope == Slope.HORIZONTAL:
                return point.y == self.start.y
            elif self.slope == Slope.VERTICAL:
                return point.x == self.start.x
            elif self.slope == Slope.UP:
                next_point = self.start
                for _ in range(1,self.gcd):
                    next_point = Point2D(next_point.x + self.delta_x_g, next_point.y-self.delta_y_g)
                    if next_point == point:
                        return True
                return False
            elif self.slope == Slope.DOWN:
                next_point = Point2D(self.start.x,self.start.y)
                for _ in range(1,self.gcd):
                    next_point = Point2D(next_point.x + self.delta_x_g, next_point.y+self.delta_y_g)
                    if next_point == point:
                        return True
                return False
        else:
            return False

