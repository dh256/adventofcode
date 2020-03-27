# Day 18 2018 Advent of Code
# (c) David Hanley 2019. All rights reserved. 
import itertools
from collections import Counter

PART1_MINUTES = 10
PART2_MINUTES = 1000000000

GROUND = '.'
YARD = '#'
TREES = '|'

class LumberArea():
    def __init__(self, fillename):
        with open(fillename,'r') as input:
            self.area = [[c for c in line.strip()] for line in input]
            self.width = len(self.area[0])
            self.height = len(self.area)

    def part1(self,minutes):
        for _ in range(minutes):
            self.iterate()
        return self.value()

    def iterate(self):
        new_area = [['.' for x in range(self.width)] for y in range(self.height)]
        for y in range(0,self.height):
            for x in range(0,self.width):
                new_acre = None
                distr = self.surrounding_acres_distr(x,y)
                if self.area[y][x] == GROUND:
                    '''
                    An open acre will become filled with trees if three or more adjacent acres contained trees. 
                    Otherwise, nothing happens.
                    '''
                    if distr[TREES] >= 3:
                        new_acre = TREES
                    else:
                        new_acre = GROUND
                elif self.area[y][x] == TREES:
                    '''
                    An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. 
                    Otherwise, nothing happens.
                    '''
                    if distr[YARD] >= 3:
                        new_acre = YARD
                    else:
                        new_acre = TREES
                elif self.area[y][x] == YARD:
                    '''
                    An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre containing trees. 
                    Otherwise, it becomes open.
                    '''
                    if distr[YARD] >= 1 and distr[TREES] >= 1:
                        new_acre = YARD
                    else:
                        new_acre = GROUND
                new_area[y][x] = new_acre
        self.area = [*new_area]

    def part2(self,minutes):
        '''
        Calculating 1000000000 iterations will take too long (days)
        Assume: At some point going to get a repeating cycle
        Loop through iterations until repeat of area representation found
        Mark number of minutes as an offset
        At this point, start calculating values after each iteration until repeat found again
        Period (length of repeating cycle) is length of values list
        Calculate value after x minutes:
            index = (x - offset) % period 
        Look up values[index] - this is the answer
        Note: GOT A HINT FOR THIS FROM REDDIT BUT CODE IS MINE
        '''
        offset = 0
        period = 0
        results={}
        values=[]
        first_repeat = True
        calc_value = False
        for minute in range(minutes):    
            hash = repr(self)
            if hash in results: 
                if first_repeat:
                    first_repeat = False
                    results={}
                    calc_value = True
                    offset = minute
                else:
                    period = len(values)
                    return values[(minutes - offset) % period]

            results[hash] = None 
            if calc_value:
                values.append(self.value())
            self.iterate()

    def surrounding_acres_distr(self,x,y):
        '''
        return the acres surrounding given point
        surrounding acres: 
                start_x = x-1
                start_y = y-1 
                end_x = x+1
                end_y = y+1 
            unless y == self.height - 1 (last row) in which case:
                end_y = y 
            unless y == 0 (first row) in which case: 
                start_y = 0
            unless x == 0 (firs col) in which case:
                start_x = 0
            unless x == self.width -1 (last col) in which case: 
                end_x = x
            in call cases excluding (x,y) itself
        '''
        curr_acre = self.area[y][x]
        start_x = x-1 if x > 0 else 0
        start_y = y-1 if y > 0 else 0
        end_x = x+1 if x < self.width - 1 else x
        end_y = y+1 if y < self.height - 1 else y
        
        distr = {YARD: 0, TREES: 0, GROUND: 0}
        for row in self.area[start_y:end_y+1]:
            for acre in row[start_x:end_x+1]:
                distr[acre] = distr[acre] + 1 
        # remove curr_acre from distr
        distr[curr_acre] = distr[curr_acre] - 1          

        # return a count of each type
        return distr

    def acre_distr(self):
        '''
        # use itertools to chain together all values in 2D self.area into one list
        # loop through and store acre distribution in a dictionary
        distr = {YARD: 0, TREES: 0, GROUND: 0}
        for acre in list(itertools.chain.from_iterable(self.area)):
            distr[acre] = distr[acre] + 1 
        return distr
        '''
        '''
        Alternative: 
        Use Counter from collections package
        Use itertools to chain together all values in 2D self.area into a single iterable
        '''
        c = Counter(itertools.chain.from_iterable(self.area))
        return c

    def value(self):
        distr = self.acre_distr()
        return distr[TREES] * distr[YARD]

    def __repr__(self):
        output = ""
        for line in self.area:
            output += ''.join(line)
        return output

    def __str__(self):
        output = ""
        for line in self.area:
            output += ''.join(line)
            output += '\n'
        return output

# solve puzzle
lumber_area = LumberArea('day18.txt')
value1 = lumber_area.part1(PART1_MINUTES)
print(f'lumber area value after {PART1_MINUTES}: {value1}')

lumber_area = LumberArea('day18.txt')
value2 = lumber_area.part2(PART2_MINUTES)
print(f'lumber area value after {PART2_MINUTES}: {value2}')



