from enum import Enum
from collections import namedtuple

# coord
class Coord(namedtuple('Coord', 'x y')):
    def __str__(self):
        return f'({self.x},{self.y})'

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.y < other.y and self.x < other.x

    def __gt__(self, other):
        return self.y > other.y and self.x > other.x
        
    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(other)

    def __hash__(self):
        return(hash(repr(self)))

'''
Grid is a dictionary of coords between (min_x,miny) and (max_x,max_y)
If a coord exists it represents either a WALL, ROOM, HORIZ_DOOR (Pass N-S), VERTICAL_DOOR (pass E-W)
If a coord does not exist it is unknown
'''
class Grid():
    def __init__(self, filename):
        self.regex = self.get_regex(filename)
        self.start_pos = Coord(0,0)
        self.grid = {self.start_pos: CellType.START}
        self.max_x = 0
        self.min_x = 0
        self.max_y = 0
        self.min_y = 0
        self.candidates = []
        self.visited = set()

    def get_regex(self, filename):
        with open(filename, 'r') as file_in:
            line = file_in.readline().strip('\n')
            return line

    def _group(self,start_index,end_index):
        ''' 
        extracts a group and all parts
        group starts at char after ( and continues to char before matching ) bracket
        '''
        group_start = start_index + 1
        group_end = end_index
        group = self.regex[group_start:group_end]
        group_parts = group.split('|')

    def _set_grid_limits(self,x,y):
        # set grid limits if changed
        self.min_x = x-1 if self.min_x > x-1 else self.min_x
        self.max_x = x+1 if self.max_x < x+1 else self.max_x
        self.min_y = y-1 if self.min_y > y-1 else self.min_y
        self.max_y = y+1 if self.max_y < y+1 else self.max_y

    def build_map(self):
        next_x = x = self.start_pos.x
        next_y = y = self.start_pos.y
        for c in self.regex:
            if c not in ('^','$'):
                # set grid limits if changed
                self._set_grid_limits(x,y)
                
                # x,y is a room
                # all surrounding cells (x-1,y); (x+1,y); (x,y+1); (x,y-1) are unknown unless already something else
                self.grid[Coord(x,y)] = CellType.ROOM

                if c == 'E':
                    # position x+1, y must be a vert door; next position x+2,y 
                    self.create_door(c,CellType.VERTICAL_DOOR,x+1,y)
                    next_x = x+2
                    next_y = y
                    
                elif c == 'W':
                    # position x-1, y must be a vert door, next position x-2, y 
                    self.create_door(c,CellType.VERTICAL_DOOR,x-1,y)
                    next_x = x-2
                    next_y = y

                elif c == 'N':
                    # position x,y+1 must be a Horiz door; next position x,y+2
                    self.create_door(c,CellType.HORIZONTAL_DOOR,x,y+1)
                    next_x = x
                    next_y = y+2

                elif c == 'S':
                    # position x,y-1 must be a horiz door; next position x,y-2
                    self.create_door(c,CellType.HORIZONTAL_DOOR,x,y-1)
                    next_x = x
                    next_y = y-2
                
                x=next_x
                y=next_y

        # last cell must be a room
        self.grid[Coord(next_x,next_y)] = CellType.ROOM 
        # set grid limits if changed
        self._set_grid_limits(next_x,next_y)

    def order(self):
        return sorted(self.grid.items(), key=lambda x:x[0])

    def __str__(self):
        out = ''
        for y in range(self.max_y,self.min_y-1,-1):
            for x in range(self.min_x,self.max_x+1):
                try:
                    if Coord(x,y) == self.start_pos:
                        out += CellType.START.value
                    else:
                        out += f'{self.grid[Coord(x,y)].value}'
                except KeyError:
                    out += f'{CellType.WALL.value}'
            out += '\n' 
        return out

    def create_door(self,direction,door_type,x,y):
        self.grid[Coord(x,y)] = door_type
        if direction == 'N' or direction == 'S':
            self.grid[Coord(x+1,y)] = CellType.WALL
            self.grid[Coord(x-1,y)] = CellType.WALL
        else:
            self.grid[Coord(x,y+1)] = CellType.WALL
            self.grid[Coord(x,y-1)] = CellType.WALL
 
    def _get_next_rooms(self,this_room,prev_room):
        '''
        Returns the doors (exits) from a given room
        '''
        rooms = []
        for x in range(this_room.x - 1, this_room.x+2):
            for y in range(this_room.y+1, this_room.y-2, -1):
                try:
                    next_room = None
                    if self.grid[Coord(x,y)] == CellType.VERTICAL_DOOR:   
                        if x > this_room.x:
                            next_room = Coord(x+1,y)
                        elif x < this_room.x:
                            next_room = Coord(x-1,y)
                    elif self.grid[Coord(x,y)] == CellType.HORIZONTAL_DOOR:
                        if y > this_room.y:
                            next_room = Coord(x,y+1)
                        elif y < this_room.y:
                            next_room = Coord(x,y-1)
                    if next_room is not None and next_room != prev_room:
                        rooms.append(next_room)
                except KeyError:
                    pass
        return rooms
    
    def _furthest_room_rec(self, this_room, prev_room=None, steps=0, doors=0):
        '''
        Find the room furthest from your starting point and the min number of doors required to reach it

        Record => (Room coord, steps, doors)

        Start (x,y) 
            Have I been here before STOP and record steps and doors passed through 
                
            if no exit door STOP and record steps and doors passed through
            if only one exit door continue through that door and loop again
            if more than one exit door: 
                Split and go through each door 
        ''' 
        if this_room in self.visited:
            candidate = [this_room,steps,doors]
            self.candidates.append(candidate)
        else:
            self.visited.add(this_room)
            next_rooms = self._get_next_rooms(this_room,prev_room)
            if len(next_rooms) == 0:
                candidate = [this_room,steps,doors]
                self.candidates.append(candidate)
            else:
                for next_room in next_rooms:
                    self._furthest_room_rec(next_room,this_room,steps+2,doors+1)

    def furthest_room(self):
        self.visited = set()
        self.candidates = []
        start_pos = self.start_pos
        self._furthest_room_rec(start_pos)

        # sort candidates by steps and then by doors
        # item at front of list is winner
        cands = sorted(self.candidates,key=lambda c:(c[1],c[2]))
        return cands[-1]

# door enum
class DoorType(Enum): 
   HORIZONTAL = '-' 
   VERTICAL = '|' 

class CellType(Enum):
    WALL = '#'
    UNKNOWN = '?'
    HORIZONTAL_DOOR = '-'
    VERTICAL_DOOR = '|'
    ROOM ='.'
    START = 'X'


# Do it
file_name = "day20_test.txt"
g = Grid(file_name)
g.build_map()
print(g)
result = g.furthest_room()
print(result)