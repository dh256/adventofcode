from collections import namedtuple

Point = namedtuple('Point', 'x y')
Fold = namedtuple('Fold', 'direction position')

class Paper:
    def __init__(self,filename):
        self.grid = {}
        self.folds = []
        with open(filename, 'r') as input_file:
            inputs = [line.strip('\n') for line in input_file]
            
        # get co-ords
        for i in inputs:
            if len(i) == 0:
                pass
            elif i.startswith('fold'):
                fold_parts = i.split(' ')[2].split('=')
                fold = Fold(fold_parts[0], int(fold_parts[1]))
                self.folds.append(fold)
            else:
                coords = [int(c) for c in i.split(',')]
                self.grid[Point(coords[0],coords[1])] = True    

    def __str__(self):
        out_str = ''
        max_y = max(self.grid.keys(), key=lambda k: k.y).y
        max_x = max(self.grid.keys(), key=lambda k: k.x).x
        for y in range (0,max_y+1):
            for x in range(0,max_x+1):
                if Point(x,y) in self.grid:
                    out_str += '.'
                else:
                    out_str += ' '
            out_str += '\n'
        return out_str

    def do_folds(self,all=False):
        '''
        Carry out fold instructions (either all or only first) and return dots remaining
        '''
        if all:
            for curr_fold in self.folds:
                self.fold(curr_fold)
            # return a str representation of grid
            return str(self)   
        else:
            self.fold(self.folds[0])
            # return number of dots in grid 
            return str(len(self.grid))

    def fold(self,curr_fold):
        if curr_fold.direction == 'y':
            # all dots below fold line move up (x pos will not change)
            for dot in list(filter(lambda k : k.y > curr_fold.position, self.grid.keys())):
                new_y = dot.y - (2 * (dot.y - curr_fold.position))
                if new_y >= 0:
                    self.grid[Point(dot.x,new_y)] = True
                # dot below fold line disappears
                self.grid.pop(dot)
        else:
            # all dots to right of fold line move left (y pos will not change)
            for dot in list(filter(lambda k : k.x > curr_fold.position, self.grid.keys())):
                new_x = dot.x - (2 * (dot.x - curr_fold.position))
                if new_x >= 0:
                    self.grid[Point(new_x,dot.y)] = True
                # dot to right of fold line disappears
                self.grid.pop(dot)