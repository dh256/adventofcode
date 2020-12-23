from collections import namedtuple
import dataclasses as dc

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
        self._facing = 90      # initially facing east 
        self._position = Position(x=0,y=0)
        with open(file_name,'r') as nav_data:
            self._nav_instructs = [Nav(line.strip('\n')) for line in nav_data]

    def navigate(self):
        '''
        Run navigation instructions and calculate Manhattan distance travelled
        '''
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
                print(f'Turn left {nav.units}: facing {self._facing}')
            elif nav.instruction == 'R':
                self._facing = (self._facing + nav.units) % 360
                print(f'Turn right {nav.units}: facing {self._facing}')
            elif nav.instruction == 'F':
                if self._facing == 0:
                    self._position.y += nav.units
                elif self._facing == 90:
                    self._position.x += nav.units 
                elif self._facing == 180:
                    self._position.y -= nav.units 
                elif self._facing == 270:
                    self._position.x -= nav.units

        # Retun manhattan distance from start
        return abs(self._position.x) + abs(self._position.y)      