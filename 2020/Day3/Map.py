import collections
from collections import namedtuple

Slope = namedtuple("Slope","right,down")

class Map:
    def __init__(self,input_file):
        with open(input_file,"r") as map_file:
            self.map = [line.strip('\n') for line in map_file]
        self.height = len(self.map)
        self.width = len(self.map[0])

    def traverse(self,slopes):
        '''
        Return number of trees encountered traversing map with each given slope multiplied together
        '''
        multiple = 1
        for slope in slopes:
            trees_encountered = 0
            curr_x = slope.right
            curr_y = slope.down
            while curr_y < self.height:
                if self.map[curr_y][curr_x] == '#':
                    trees_encountered += 1
                curr_x = (curr_x + slope.right) % self.width  # wraps round if goes off end
                curr_y += slope.down
            multiple *= trees_encountered
        return multiple