from enum import Enum
import sys
from copy import copy

class LabelDirection(Enum):
    Up=0
    Down=1
    Left=2
    Right=3


class PortalType(Enum):
    Outer=0
    Inner=1

class Portal:
    def __init__(self,label,portal_type):
        self.label = label
        self.type = portal_type

class Pluto:
    def __init__(self,filename):
        self.portals = {}
        with open(filename,"r") as file_input:
            self.rows = [line.strip('\n') for line in file_input]
            
            # get grid outer edges
            self.first_col = 2
            self.first_row = 2
            self.last_col = len(max(self.rows, key=len))-3
            self.last_row = len(self.rows)-3

            # get doughnut edges
            y=0
            edge_found = False
            for row in self.rows:
                if y in range(self.first_row,self.last_row):
                    if " " in row[self.first_col:self.last_col+1] and not edge_found:
                        edge_found = True
                        self.doughnut_first_row = y
                        self.doughnut_first_col = row.find(' ',self.first_col)   # find position of first space    
                        self.doughnut_last_col = row.rfind(' ',self.doughnut_first_col,self.last_col+1)    # find position of last space
                    elif " " not in row[self.first_col:self.last_col] and edge_found:
                        self.doughnut_last_row = y-1
                        break
                y += 1
            
            # get a list of all the portals
            self._get_portals()
            

    '''
    Get all the portals on Pluto
    '''
    def _get_portals(self):
        '''
        go round outer edge and identify all portals
        '''
        for y in (self.first_row,self.last_row):
            for x in range(self.first_col, self.last_col+1):
                if y == self.first_row:
                    self._add_portal(x,y,LabelDirection.Up,PortalType.Outer)
                else:
                    self._add_portal(x,y,LabelDirection.Down,PortalType.Outer)
                
        for x in (self.first_col,self.last_col):
            for y in range(self.first_row+1, self.last_row):
                if x == self.first_col:
                    self._add_portal(x,y,LabelDirection.Left,PortalType.Outer)
                else:
                    self._add_portal(x,y,LabelDirection.Right,PortalType.Outer)

        '''
        go round inner edge and identify all portals
        '''
        for y in (self.doughnut_first_row - 1,self.doughnut_last_row + 1):
            for x in range(self.doughnut_first_col-1, self.doughnut_last_col+2):
                if y == self.doughnut_first_row-1:
                    self._add_portal(x,y,LabelDirection.Down,PortalType.Inner)
                else:
                    self._add_portal(x,y,LabelDirection.Up,PortalType.Inner)
                
        for x in (self.doughnut_first_col-1,self.doughnut_last_col+1):
            for y in range(self.doughnut_first_row, self.doughnut_last_row+1):
                if x == self.doughnut_first_col-1:
                    self._add_portal(x,y,LabelDirection.Right,PortalType.Inner)
                else:
                    self._add_portal(x,y,LabelDirection.Left,PortalType.Inner)

    '''
    Add a portal to self.portals.
    Note that 'AA' and 'ZZ' are entry and exit points and not portals
    '''
    def _add_portal(self,x,y,direction,portal_type):
        if self.rows[y][x] == ".":
            label = self._get_label(x,y,direction)
            if label not in ('AA','ZZ'):
                self.portals[(x,y)] = Portal(label,portal_type)
            elif label == 'AA':
                self.entry_point = (x,y)
            elif label == 'ZZ':
                self.exit_point = (x,y)

    '''
    Is x,y a portal
    '''
    def _is_portal(self,x,y):
        return (x,y) in self.portals

    '''
    Jump across a portal from portal at (x,y) to corresponding portal. Return (x,y) of new location
    Portals always go from outer->inner or inner->outer
    '''
    def _jump_portal(self,x,y):
        if self._is_portal(x,y):
            portal_from = self.portals[(x,y)]
            portal_to = list(filter(lambda e : e[1].label == portal_from.label and e[1].type != portal_from.type, self.portals.items()))[0]
            return (portal_to[0][0],portal_to[0][1])
        else:
            raise ValueError(f'({x},{y}) is not a portal')

    def _get_label(self,x,y,direction):
        if direction == LabelDirection.Up:
            label = f'{self.rows[y-2][x]}{self.rows[y-1][x]}'
        elif direction == LabelDirection.Down:
            label = f'{self.rows[y+1][x]}{self.rows[y+2][x]}'
        elif direction == LabelDirection.Left:
            label = f'{self.rows[y][x-2]}{self.rows[y][x-1]}'
        elif direction == LabelDirection.Right:
            label = f'{self.rows[y][x+1]}{self.rows[y][x+2]}'
        return label


    '''
    Is point on edge of grid
    '''
    def _on_grid_edge(self,x,y):
        return y == self.first_row or y == self.last_row or x == self.first_col or x == self.last_col

    ''' 
    is point on edge of doughnut
    '''
    def _on_doughnut_edge(self,x,y):
        if y == self.doughnut_first_row-1 or y == self.doughnut_last_row + 1:
            return x in range(self.doughnut_first_col-1,self.doughnut_last_col+2)    
        elif y in range(self.doughnut_first_row, self.doughnut_last_row+1):
            return x == self.doughnut_first_col - 1 or x == self.doughnut_last_col + 1
        else:
            return False

    def find_shortest_distance(self):
        print('Calculating shortest distance ...')
        self.already_visited = {}
        self.paths = []             # list of paths (each path is a list of points)
        path = []                   # first path currently empty
        self.build_path(path,self.entry_point)

        '''
        look at all paths
        take all paths that have last entry as ZZ (exit_point)
        find path with shortest length - length is shortest path-1
        '''
        shortest_path = sys.maxsize
        for path in self.paths:
            if path[-1] == self.exit_point:         
                if len(path) < shortest_path:
                    shortest_path = len(path)
        return shortest_path-1                      # subtract 1 don't include final point itself

    '''
    Build path: 
    starting at start point
    get neighbours
        if 0: stop (either a dead end or exit point)
        if 1: keep going to next point
        if > 1: recurse - start building next path passing in current path and neighbour as starting point
    '''
    def build_path(self,path,curr_point):    
        self.paths.append(path)
        path.append(curr_point)
        while True:
            self.already_visited[curr_point] = True
            neighbours = self._get_neighbours(curr_point,path)
            if len(neighbours) == 0:
                break
            elif len(neighbours) == 1:  
                curr_point = neighbours[0]
                path.append(curr_point)
            else:   
                # recurse for each neighbour
                for n in neighbours:
                    new_path = copy(path)
                    self.build_path(new_path,n)
                break
                    

    '''
    Get neighbouring points - check up, down, left right for "." and return all
    Don't include any points in the current path as already visited
    Also need to consider portals. If point is a portal jump to matching portal point
    '''
    def _get_neighbours(self,point,curr_path):
        x = point[0]
        y = point[1]
        neighbours = []
        
        # if point is portal, get point at other side of portal
        # if not already visited, add point to neighbours and return
        # otherwise check other possible neighbours
        if self._is_portal(x,y):
            portal_jump = self._jump_portal(x,y)
            if portal_jump not in curr_path:
                neighbours.append(portal_jump)
                return neighbours

        # up
        if self.rows[y-1][x] == "." and (x,y-1) not in curr_path:
            neighbours.append((x,y-1))

        # down
        if self.rows[y+1][x] == "." and (x,y+1) not in curr_path:
            neighbours.append((x,y+1))

        # left 
        if self.rows[y][x-1] == "." and (x-1,y) not in curr_path:
            neighbours.append((x-1,y))

        # right 
        if self.rows[y][x+1] == "." and (x+1,y) not in curr_path:
            neighbours.append((x+1,y))
        return neighbours

    def __repr__(self):
        out_str = ""
        for row in self.rows:
            for c in row:
                out_str += c
            out_str += '\n'
        return out_str