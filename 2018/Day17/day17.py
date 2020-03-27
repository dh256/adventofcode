from collections import namedtuple
import click

Point = namedtuple('Point', 'x y')
SAND = '.'
WATERFLOW = '|'
WATERSTANDING = '~'
CLAY = '#'
SPRING = '+'

class Grid():
    def __init__(self,clay_strands):
        self.spring=Point(500,0)
        self.clay_strands = clay_strands
        # add in sand
        self.grid = []
        for y in range(0,self.clay_strands.maxY+1):
            row = [SAND] * (self.clay_strands.maxX+1)
            self.grid.append(row)
    
        #self.grid = [[SAND] * (self.clay_strands.maxX+1)] * (self.clay_strands.maxY+1)
        
        self.grid[self.spring.y][self.spring.x] = SPRING
        for strand in self.clay_strands.strands:
            if strand.start.x == strand.end.x: 
                # vertical strand
                for y in range(strand.start.y,strand.end.y+1):
                    self.grid[y][strand.start.x] = CLAY
            else:
                # horizonal strand
                for x in range(strand.start.x,strand.end.x+1):
                    self.grid[strand.start.y][x] = CLAY

    def constrained(self,point):
        '''
        determines whether at current pos is constrained
        constrained if:
            - while all entries in row y+1 are either CLAY or STANDING water and hit a CLAY at x-n (A) and x+m (B)
            -   essentially need to find position of last # to left and first # to right
                then check that all entries in row y+1 between A and B are either all CLAY or are all STANDING WATER  
        '''

        # go left
        left_point = point
        left_constrain = None
        while left_constrain is None:
            if self.grid[left_point.y][left_point.x-1] == CLAY:
                left_point = Point(left_point.x-1,left_point.y)
                left_constrain = True
            else:
                if self.grid[left_point.y+1][left_point.x-1] in (CLAY,WATERSTANDING):
                    left_point = Point(left_point.x-1,left_point.y)
                else:
                    left_constrain = False
        
         # go right
        right_point = point
        right_constrain = None
        while right_constrain is None:
            if self.grid[right_point.y][right_point.x+1] == CLAY:
                right_point = Point(right_point.x+1,right_point.y)
                right_constrain = True
            else:
                if self.grid[right_point.y+1][right_point.x+1] in (CLAY,WATERSTANDING):
                    right_point = Point(right_point.x+1,right_point.y)
                else:
                    right_constrain = False

        return (left_constrain and right_constrain,left_point.x,right_point.x)        
    
    def fill(self,pos=None):
        '''
        fill grid with water
        can ignore everything above, water will start at spring.x,minY-1
        '''
        if pos is None:
            pos = Point(self.spring.x,self.clay_strands.minY-1)
        
        '''
        can water fall - always fall if it can?
            can fall if next square down is sand or y position < maxY
            if it can fall keep going
        if it can't fall, then need to check whether constrained
            if y > maxY then stop
            constrained if a clay strand found both left and right 
                if constrained fill row with standing water and move up
            if not constrained flow left and right until can fall again or is constrained
            Note:   when working out if constrained ANCHOR point must be current x position of water
                    when move up it is essential that x stays the same
            Recursion is in here somewhere - perhaps when splitting left and right.
        '''
        while True:
            fall = self.can_fall(pos)
            if fall[0] == False:
                if fall[1] == "MAX" or fall[1] == "WATER_FLOW":
                    # stop - nothing more to do
                    break
                else:
                    '''
                    either fully constrained (left and right clay on same row) in which case fill row with standing water between left constrain + 1 and right constrain - 1
                    or constrained on one side in which case water will flow to constrained side and stop and flow to unconstrained side until can fall
                    '''
                    constrained = self.constrained(pos)
                    if constrained[0]:
                        for x in range(constrained[1]+1,constrained[2]):
                            self.grid[pos.y][x] = WATERSTANDING
                        pos=Point(pos.x,pos.y-1)
                    else:
                        '''
                        find point where either:
                        '''
                        # go left
                        new_pos=pos
                        while True:
                            if self.grid[new_pos.y][new_pos.x-1] == CLAY:
                                # stop
                                break
                            else:
                                new_pos = Point(new_pos.x-1,new_pos.y)
                                self.grid[new_pos.y][new_pos.x] = WATERFLOW
                                fall = self.can_fall(new_pos)
                                if fall[0]:
                                    # recurse
                                    self.fill(new_pos)
                                    break  

                        # go right
                        new_pos=pos
                        while True:
                            if self.grid[new_pos.y][new_pos.x+1] == CLAY:
                                # stop
                                break
                            else:
                                new_pos = Point(new_pos.x+1,new_pos.y)
                                self.grid[new_pos.y][new_pos.x] = WATERFLOW
                                fall = self.can_fall(new_pos)
                                if fall[0]:
                                    # recurse
                                    self.fill(new_pos)
                                    break  
                        break
            else:
                pos = Point(pos.x,pos.y+1)
                self.grid[pos.y][pos.x] = WATERFLOW
                

    def can_fall(self,point):
        '''
        Returns a tuple (boolean,reason)
        if boolean = FALSE, a reason is given either CLAY if encountered clay, WATER if encountered standing water or MAX if encountered MAXY
        '''
        fall = True
        reason = None
        if point.y >= self.clay_strands.maxY:
            fall = False
            reason = "MAX"
        else:
            if self.is_clay(point.x,point.y+1):
                fall = False
                reason = "CLAY"
            elif self.is_water_standing(point.x,point.y+1):
                fall = False
                reason = "WATER"
            elif self.is_water_flow(point.x,point.y+1):
                fall = False
                reason = "WATER_FLOW"
        return (fall,reason)

    def __repr__(self):
        output = ""
        for row in self.grid[self.clay_strands.minY:self.clay_strands.maxY+1]:
            for col in row[self.clay_strands.minX:self.clay_strands.maxX+1]:
                output += col
            output += '\n'
        return output

    def countwater(self):
        water = 0
        for row in self.grid[self.clay_strands.minY:self.clay_strands.maxY+1]:
            water_cells = [entry for entry in row if entry == WATERFLOW or entry == WATERSTANDING]
            water += len(water_cells)
        return water

    '''
    def is_sand(self,x,y):
        return self.grid[y][x] == SAND
    '''
    
    def is_clay(self,x,y):
        return self.grid[y][x] == CLAY

    def is_water_standing(self,x,y):
        return self.grid[y][x] == WATERSTANDING

    def is_water_flow(self,x,y):
        return self.grid[y][x] == WATERFLOW 

    '''
    def is_water(self,x,y):
        return self.is_water_flow(x,y) or self.is_water_standing(x,y)
    '''

class ClayStrand(namedtuple('ClayStrand', 'start end')):
    def __repr__(self):
        return f'({self.start.x},{self.start.y})-({self.end.x},{self.end.y})'

class ClayStrands():
    def __init__(self,filename):
        with open(filename,"r") as fileinput:
            self.strands = [self._getStrand(line) for line in fileinput]
            self.minY = min(self.strands, key=lambda s:s.start.y).start.y
            self.maxY = max(self.strands, key=lambda s:s.end.y).end.y
            self.minX = min(self.strands, key=lambda s:s.start.x).start.x - 1
            self.maxX = max(self.strands, key=lambda s:s.end.x).end.x + 1
        
    def _getStrand(self,line):
        # want to turn puzzle input into two (x,y) coords marking start and end point of a clay strand
        # if first coord label is x then (x,coord2_start) to (x,coord2_end)
        # if first coord label is y then (coord2_start,y) to (coord2_end,y)
        startPoint = None
        endPoint = None
        line = line.strip('\n')
        coords = line.split(', ')
        coord_1_label = coords[0][0]
        coord_1_value = int(coords[0][2:])
        
        coord2_start_end = coords[1][2:].split('..')
        coord2_start = int(coord2_start_end[0])
        coord2_end = int(coord2_start_end[1])
        if coord_1_label == "x":
            startPoint = Point(coord_1_value,coord2_start)
            endPoint = Point(coord_1_value,coord2_end)
        else:
            startPoint = Point(coord2_start,coord_1_value)
            endPoint = Point(coord2_end,coord_1_value)
        return(ClayStrand(startPoint,endPoint))

@click.command()
@click.option(
    '--file',
    '-f',
    help='Input file'
)
def run(file):
    strands = ClayStrands(file)
    grid = Grid(strands)
    grid.fill()
    print(f'Water can reach {grid.countwater()} tiles')
    # first guess of 533 was too low
    # need to look at stopping if water found - did this
    # second guess of 36799 was too high

if __name__ == "__main__":
    run()
    