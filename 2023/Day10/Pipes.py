from Point import Point
from collections import deque

class Pipes:
    pipes = ('|','-','L','J','7','F')       # pipes    
    connect_from_east = ('-','J','7')       # pipes that can connect to another pipe from the east
    connect_from_west = ('-','L','F')       # pipes that can connect to another pipe from the west
    connect_from_north = ('|','7','F')      # pipes that can connect to another pipe from the north
    connect_from_south = ['|','L','J']      # pipes that can connect to another from the south
    direction_offsets = {'N': (0,-1), 'S': (0,1), 'W': (-1,0), 'E': (1,0)}      # point offsets for each direction that you can move

    def set_s_pipe(self) -> str:
        '''
        Figure out what the S pipe actually is
        Determine the only two valid pairs and then set to correct pipe
        '''
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

        # replace S pipe with correct pipe
        self.grid[self.start.y]=self.grid[self.start.y].replace('S', self.set_s_pipe())

    def valid_move(self, curr_pipe: str, new_pos: Point, direction: str) -> bool:
        '''
        Determine if given move direction is valid
        '''
        valid_pipes = None
        
        # make sure still on grid
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

    def get_path(self) -> list[Point]:
        # use breadth first search to find path back to S
        q = deque()
        q.appendleft((self.start,None,[self.start]))
        while True:
            curr_pos, from_pos, path = q.pop()
            for direction in Pipes.direction_offsets.items():
                next_pos = curr_pos.offset(direction[1])
                if from_pos != next_pos:            # prevent move backwards
                    if self.valid_move(self.grid[curr_pos.y][curr_pos.x], next_pos, direction[0]):
                        if next_pos == self.start:
                            return path
                        else:
                            q.appendleft((next_pos,curr_pos,[*path,next_pos]))

    def steps_to_farthest(self) -> int:
        return len(self.get_path()) // 2

    def enclosed_by_loop(self) -> int:
        path = self.get_path()

        ''' 
        Find enclosed loops in path using Pick's Theorem and the Shoelace Formula
        
        A = i + b / 2 - 1

        where A is Area
        i is internal area  (calculated using Shoelace formula)
        b is number of points (length of path)
        
        i = (sum of (Point 1.x * Point 2.y - Point 1.y * Point 2.x)) / 2

        I did need a hint for the maths of this but then easy to implement
        Points must be in an ordered list, which you get from getting path in Part 1
        '''
        sum = 0
        
        # showlace formula
        for idx in range(len(path)):
            p1 = path[idx]
            p2 = path[(idx+1)%len(path)]      # need to loop back first cooord
            sum += p1.x * p2.y - p1.y * p2.x        
            i = abs(sum//2)

        # Pick's Theorem
        return(i-len(path)//2+1)