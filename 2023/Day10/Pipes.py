from Point import Point
from collections import deque

class Pipes:
    pipes = ('|','-','L','J','7','F')       # pipes    
    connect_from_east = ('-','J','7')       # anything that can connect to something from the east
    connect_from_west = ('-','L','F')       # anything that can connect to something from the east
    connect_from_north = ('|','7','F')      # anything that can connect to something from the east
    connect_from_south = ['|','L','J']      # anything that can connect to something from the east
    direction_offsets = {'N': (0,-1), 'S': (0,1), 'W': (-1,0), 'E': (1,0)}

    def set_s_pipe(self) -> str:
        # which ways can you move
        for p in Pipes.pipes:
            valid_directions: set[str] = set()
            for direction in Pipes.direction_offsets.items():
                new_pos = self.start.offset(direction[1])
                if self.valid_move(p, new_pos, direction[0]):
                    valid_directions.add(direction[0])
                
            if valid_directions == {'N','S'}:
                return '|'
            
            if valid_directions == {'E','W'}:
                return '-'

            if valid_directions == {'N','E'}:
                return 'L'
            
            if valid_directions == {'N','W'}:
                return 'J'
            
            if valid_directions == {'S','E'}:
                return 'F'
            
            if valid_directions == {'S','W'}:
                return '7'

    def __init__(self, file_name) -> None:
        with open(file_name,'r') as input_file:
            self.grid = [line.strip() for line in input_file]

        # get grid sizes    
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        
        # find start
        for y in range(self.rows):
            try:
                x = self.grid[y].index('S')
                self.start = Point(x,y)
            except ValueError:
                continue

        #set s_pipe
        self.grid[self.start.y]=self.grid[self.start.y].replace('S', self.set_s_pipe())

    '''
    DH VALID MOVES LOGIC IS WRONG
    WORK WITH INPUT6.TXT
    WHEN GET TO (1,1) a '-' character, valid moves returns TRUE for N
    THIS IS INCORRECT, only valid moves are E or W
    NEED TO CONSIDER CURRENT CHAR FIRST
    e.g., if a - only valid moves are E or W and so 
    '''

    def valid_move(self, curr_pipe: str, new_pos: Point,direction: str) -> bool:
        '''
        Determines if a valid move
        '''
        valid_pipes = None
        
        if not (new_pos.x >= self.cols or new_pos.y >= self.rows or new_pos.x < 0 or new_pos.y < 0):

            if curr_pipe == '-':
                if direction == 'E':
                    valid_pipes = Pipes.connect_from_east
                elif direction == 'W':
                    valid_pipes = Pipes.connect_from_west

            elif curr_pipe == '|':
                if direction == 'N':
                    valid_pipes = Pipes.connect_from_north
                elif direction == 'S':
                    valid_pipes = Pipes.connect_from_south

            elif curr_pipe == 'L':
                if direction == 'N':
                    valid_pipes = Pipes.connect_from_north
                elif direction == 'E':
                    valid_pipes = Pipes.connect_from_east

            elif curr_pipe == 'F':
                if direction == 'E':
                    valid_pipes = Pipes.connect_from_east
                elif direction == 'S':
                    valid_pipes = Pipes.connect_from_south

            elif curr_pipe == 'J':
                if direction == 'W':
                    valid_pipes = Pipes.connect_from_west
                elif direction == 'N':
                    valid_pipes = Pipes.connect_from_north

            elif curr_pipe == '7':
                if direction == 'W':
                    valid_pipes = Pipes.connect_from_west
                elif direction == 'S':
                    valid_pipes = Pipes.connect_from_south

        if valid_pipes:
            return self.grid[new_pos.y][new_pos.x] in valid_pipes
        else:
            return False

    def steps_to_farthest(self) -> int:
        # use breadth first search to find steps back to S
        q = deque()
        q.appendleft((self.start,None,0))
        while True:
            try:
                curr_pos, from_pos, steps = q.pop()
                for direction in Pipes.direction_offsets.items():
                    next_pos = curr_pos.offset(direction[1])
                    if (from_pos is None) or (next_pos != from_pos):
                        if self.valid_move(self.grid[curr_pos.y][curr_pos.x], next_pos, direction[0]):
                            if next_pos == self.start:
                                return (steps+1) // 2
                            else:
                                q.appendleft((next_pos,curr_pos,steps+1))
            except IndexError:
                print('No path found!!')
                exit()
                