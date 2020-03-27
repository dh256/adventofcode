from collections import namedtuple
from enum import IntEnum,unique

@unique
class RegionType(IntEnum):
    ROCKY = 0
    WET = 1
    NARROW = 2

class Point(namedtuple('Point', 'x y')):
    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x, self.y))  

class Region():
    '''
    Has a geoligacal index
    Has an errosion level
    Has a region type
    '''
    def __init__(self, geological_index, errosion_level, reg_type):
        self.geological_index = geological_index
        self.errosion_level = errosion_level
        self.reg_type = reg_type

class Cave():
    '''
    Collection of regions each one referenced by a Point
    Has a depth, mouth and a target point 
    For Part 2 may have to go beyond X,Y of target. Need a way to add in an additional row or column of coords
    '''
    def __init__(self,target,depth):
        self.max_x = 0
        self.max_y = 0
        self.mouth = Point(0,0)
        self.depth = depth
        self.target = target
        self.grid = dict()
        self.grid[mouth] = self.create_region(mouth)

    def add_column(self):
        '''
        Adding a column means going from max_x+1,0 to max_x+1,max_y (new max_x becomes max_x + 1)
        Adding a row means going from 0, max_y+1 to max_x, max_y+1  (new max_y becomes max_y + 1)
        '''
        self.max_x += 1
        for y in range(self.max_y + 1):
            p = Point(self.max_x,y)
            self.grid[p] = self.create_region(p)
    
    def add_row(self):
        self.max_y += 1
        for x in range(self.max_x + 1):
            p = Point(x,self.max_y)
            self.grid[p] = self.create_region(p)
            
    def create_region(self, p):
        geo_index = self.calc_geo_index(p)
        errosion_level = self.calc_errosion_level(geo_index)
        reg_type = self.calc_region_type(errosion_level)
        return Region(geo_index,errosion_level,reg_type)

    def calc_geo_index(self, p):
        if p == self.mouth or p == self.target:
            geological_index = 0
        elif p.x == 0 and p.y > 0:
            geological_index = p.y * 48271
        elif p.y == 0 and p.x > 0:
            geological_index = p.x * 16807
        else:
            geological_index = self.grid[Point(p.x-1, p.y)].errosion_level * self.grid[Point(p.x, p.y-1)].errosion_level
        return geological_index

    def calc_errosion_level(self, geological_index):
        return (geological_index + self.depth) % 20183

    def calc_region_type(self, errosion_level):
        return RegionType(errosion_level % 3)

    # Part 1
    def risk_level(self):
        risk_level = 0
        for x in range(self.target.x + 1):
            if x > self.max_x:
                self.add_column()
            for y in range(self.target.y + 1):
                if y > self.max_y:
                    self.add_row()
                risk_level += int(self.grid[Point(x,y)].reg_type)
        return risk_level

    # Part 2
    def shortest_path():
        '''
        Need to calculate the shortest path to reach target 
        '''
        pass


depth=5355
target=Point(14,796)    
mouth=Point(0,0)
'''
depth=510
target = Point(10,10)
mouth=Point(0,0)
'''

cave = Cave(target,depth)
print(f'Risk Level: {cave.risk_level()}')


    

