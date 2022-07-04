from enum import Enum
from shutil import move
from webbrowser import get

class Facing(Enum):
    EAST = '>'
    SOUTH = 'v'
    EMPTY = '.'
'''
class Point:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
'''


class SeaCucumbers:
    def __init__(self, filename):
        self.cucumbers = dict()         # will hold cucumbers grid
        with open(filename,'r') as input_file:
            cucumber_lines = [line.strip('\n') for line in input_file]

        self.cols = len(cucumber_lines[0])
        self.rows = len(cucumber_lines)

        # populate cucumbers dictionary 
        for y in range(0, self.rows):
            for x in range(0,self.cols):
                self.cucumbers[(x,y)] = cucumber_lines[y][x]
             
        


    '''
    Returns number of steps when cucumbers can no longer move
    '''
    def stepsNoMove(self):
        steps = 0
        no_move = False
        while not no_move:
            # move all east facing
            move_east = []
            for y in range(0,self.rows):
                for x in range(0,self.cols): 
                    if self.cucumbers[(x,y)] == Facing.EAST.value and self.cucumbers[((x+1) % self.cols,y)] == Facing.EMPTY.value:
                        # this one can move, store current and new pos
                        move_east.append(((x,y),((x+1) % self.cols,y)))
            
            for me in move_east:
                self.cucumbers[me[0]] = Facing.EMPTY.value
                self.cucumbers[me[1]] = Facing.EAST.value
                 

            # move all south facing
            move_south = []
            for y in range(0,self.rows):
                for x in range(0,self.cols): 
                    if self.cucumbers[(x,y)] == Facing.SOUTH.value and self.cucumbers[(x,(y+1) % self.rows)] == Facing.EMPTY.value:
                        # this one can move, store current and new pos
                        move_south.append(((x,y),(x,(y+1) % self.rows)))
            
            for ms in move_south:
                self.cucumbers[ms[0]] = Facing.EMPTY.value
                self.cucumbers[ms[1]] = Facing.SOUTH.value

            no_move = len(move_east) == 0 and len(move_south) == 0
            steps += 1

        return steps
    
    def show(self):
        out_str = ""
        for y in range(0, self.rows):
            row = ""
            for x in range(0, self.cols):
                row += self.cucumbers[(x,y)]
            out_str += f'\n{row}'
        return out_str