# Need to figure out why 8,9 is 7 when it should be 6 after second go around of step 2

from collections import namedtuple
from colorama import Style, Fore

Point = namedtuple('Point', 'x y')

directions = ['y-1,x', 'y+1,x', 'y,x+1', 'y,x-1', 'y-1.x+1', 'y+1,x+1', 'y+1,x-1', 'y-1,x-1']

class Octopus:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            rows = [line.strip('\n') for line in input_file]
            self.max_y = len(rows)
            self.grid = []
            for r in rows:
                cols = [int(c) for c in r]
                self.grid.append(cols)
            self.max_x = len(self.grid[0])

    def calc_all_flash(self):
        '''
        Returns the step when all octopus have a value of 0
        '''
        step = 1
        while True:
            self.perform_step()
            if self.all_zeros():
                break    
            step += 1
        return step

    def all_zeros(self):
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
                if self.grid[y][x] != 0:
                    return False
        return True

    def calc_flashes(self,steps):
        total_flashes = 0
        for step in range(0,steps):
            total_flashes += self.perform_step()
        return total_flashes

    def perform_step(self):
        # increase energy level of all octopuses by 1
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
                self.grid[y][x] += 1

        # now for each octopus at level 10 - increase energy of all octopuses around this one
        self.flashed = set()
        round = 1
        while True:
            keep_going = False
            for y in range(0,self.max_y):
                for x in range(0,self.max_x):
                    if self.grid[y][x] > 9 and not (y,x) in self.flashed:
                        keep_going = True
                        self.power_up_adjacent(y,x)
            if not keep_going:
                break
            round += 1

        # now set all flashed to zero
        for (y,x) in self.flashed:
            self.grid[y][x] = 0

        return len(self.flashed)

    def power_up_adjacent(self,y,x):
        self.flashed.add((y,x))
        for y_diff in range(-1,2):
            for x_diff in range(-1,2):
                if y_diff == 0 and x_diff == 0:
                    # don't increment yourself
                    pass
                else:                    
                    if x+x_diff < 0 or x+x_diff > self.max_x-1 or y+y_diff < 0 or y+y_diff > self.max_y-1:
                        pass
                    else:
                        self.grid[y+y_diff][x+x_diff] += 1

    
    def __str__(self):
        out_str = f'{Fore.WHITE}'
        for row in self.grid:
            for c in row:
                if c != 0:
                    out_str += f'{c} '
                else:
                    out_str += f'{Style.BRIGHT}{c}{Style.NORMAL} '
            out_str += '\n'
        return out_str