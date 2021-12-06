from collections import namedtuple
import re

Point = namedtuple('Point', 'x y')

class Vents:
    def __init__(self,filename,part):
        with open(filename,'r') as input_file:
            self.grid = {}
            lines = [line.strip('\n') for line in input_file]
            for line in lines:
                draw = False
                coords = [int(c) for c in re.findall(r'\d+', line)]
                x1 = coords[0]
                x2 = coords[2]
                y1 = coords[1]
                y2 = coords[3]

                if x1 == x2:
                    draw = True
                    loops = abs(y1-y2)
                    x_inc = 0
                    x_range = None
                    if y2 < y1:
                        y_inc = -1
                    else:
                        y_inc = 1
                elif y1 == y2:
                    draw = True
                    loops = abs(x1-x2)
                    y_inc = 0
                    x_range = None
                    if x2 < x1:
                        x_inc = -1
                    else:
                        x_inc = 1
                    
                else: 
                    if part == 2:
                        # diaganol lines only
                        draw = True
                        loops = abs(x1-x2)
                        if x2 < x1:
                            x_inc = -1
                        else: 
                            x_inc = 1

                        if y2 < y1:
                            y_inc = -1
                        else: 
                            y_inc = 1

                # draw line if required
                if draw:     
                    x = x1
                    y = y1
                    for loop in range(0,loops+1):  
                        if Point(x,y) in self.grid.keys():
                            self.grid[Point(x,y)] += 1
                        else:
                            self.grid[Point(x,y)] = 1
                        x += x_inc
                        y += y_inc

                

    @property
    def dangerous_areas(self):
        return len(list(filter(lambda v : v > 1, self.grid.values())))