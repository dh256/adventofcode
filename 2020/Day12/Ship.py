from collections import namedtuple
import dataclasses as dc
from enum import Enum

class ShipMoveMode(Enum):
    SHIP = 1
    WAYPOINT = 2

class Position(): 
    def __init__(self,x,y):
        self._x = x
        self._y = y

    @property 
    def x(self):
        return self._x

    @property 
    def y(self):
        return self._y
        
    @x.setter
    def x(self,val):
        self._x = val 

    @y.setter
    def y(self,val):
        self._y = val 

class Nav:
    def __init__(self,instruction):
        self._instruction = instruction[0]
        self._units = int(instruction[1:])

    @property
    def instruction(self):
        return self._instruction

    @property
    def units(self):
        return self._units

class Ship():
    def __init__(self,file_name):
        with open(file_name,'r') as nav_data:
            self._nav_instructs = [Nav(line.strip('\n')) for line in nav_data]
        self.reset()

    def reset(self):
        self._facing = 90     
        self._position = Position(0,0)
        self._waypoint_position = Position(10,1)
    
    def navigate(self,mode=ShipMoveMode.SHIP):
        '''
        Run navigation instructions and calculate Manhattan distance travelled
        '''
        if mode == ShipMoveMode.SHIP:
            # Ship move mode - Part 1
            for nav in self._nav_instructs:
                if nav.instruction == 'E':
                    self._position.x += nav.units 
                elif nav.instruction == 'W':
                    self._position.x -= nav.units 
                elif nav.instruction == 'N':
                    self._position.y += nav.units 
                elif nav.instruction == 'S':
                    self._position.y -= nav.units 
                elif nav.instruction == 'L':
                    self._facing = self._facing - nav.units
                    if self._facing < 0:
                        self._facing = 360 + self._facing
                elif nav.instruction == 'R':
                    self._facing = (self._facing + nav.units) % 360
                elif nav.instruction == 'F':
                    if self._facing == 0:
                        self._position.y += nav.units
                    elif self._facing == 90:
                        self._position.x += nav.units 
                    elif self._facing == 180:
                        self._position.y -= nav.units 
                    elif self._facing == 270:
                        self._position.x -= nav.units
        else: 
            # Wapoint mode - Part 2
            for nav in self._nav_instructs:
                if nav.instruction == 'E':
                    self._waypoint_position.x += nav.units 
                elif nav.instruction == 'W':
                    self._waypoint_position.x -= nav.units 
                elif nav.instruction == 'N':
                    self._waypoint_position.y += nav.units 
                elif nav.instruction == 'S':
                    self._waypoint_position.y -= nav.units 
                elif nav.instruction in ('L','R'):
                    self.rotate_waypoint(nav.instruction,nav.units)
                elif nav.instruction == 'F':
                    # move ship
                    self._position.x += nav.units * self._waypoint_position.x
                    self._position.y += nav.units * self._waypoint_position.y

        return abs(self._position.x) + abs(self._position.y)
        
                    
    def rotate_waypoint(self,direction,rotate_by):
        for r in range(0,rotate_by // 90):
            if direction == "L":    # counterclockwise
                new_x = self._waypoint_position.y * -1
                self._waypoint_position.y = self._waypoint_position.x
                self._waypoint_position.x = new_x
            else:                   # clockwise
                new_x = self._waypoint_position.y
                self._waypoint_position.y = self._waypoint_position.x * -1
                self._waypoint_position.x = new_x