from collections import deque
from Point import Point
from itertools import permutations,combinations,combinations_with_replacement,product

class Garden:
    offsets = {'N': (0,-1), 'S': (0,1), 'E': (1,0), 'W': (-1,0)}
    
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            rows = [line.strip('\n') for line in input_file]
        
        # create grid
        self.grid: list[list[str]] = [[*row] for row in rows]

        # set height and  width
        self.height: int = len(self.grid)
        self.width: int = len(self.grid[0])

        # find start
        for y in range(self.height):
            try:
                idx = self.grid[y].index('S')
                self.start: Point = Point(idx, y)
                self.grid[y][idx] = '.'
            except ValueError:
                continue

    def get_next_point(self, point: Point,offset: tuple[int,int]) -> Point:
        ''' 
        Returns a point. 
        If off grid or a # returns None
        '''
        next_point = point.offset(offset)
        if 0 <= next_point.x <= self.width-1 and 0 <= next_point.y <= self.height-1:
            if self.grid[next_point.y][next_point.x] == '.':
                return next_point

        next_point = None

    def part1(self, steps: int) -> int:
        '''
        Calculate the number of garden plots reached after given number steps
        '''
        q = deque()         # stack for Depth First Search

        # initial set up
        visited = dict()    # Key-point, Value-number of steps
        get_to = set()

        # if even number of steps start at start_point
        # if odd number of steps start at any valid point within one step of start point
        if steps % 2 == 0:
            q.append((self.start,0))
        elif steps % 2 == 1:
            visited[self.start] = 0
            for offset in Garden.offsets.values():
                point = self.start.offset(offset)
                if self.grid[point.y][point.x] == '.':
                    q.append((point,1))
        
        # process points on stack
        while len(q) > 0:
            curr_point, curr_steps = q.pop()
            visited[curr_point] = curr_steps
            if curr_steps == steps:
                get_to.add(curr_point)
            else:
                # can get to every second point, evens or odds depending on number of steps
                if (steps % 2 == 0 and curr_steps % 2 == 0) or (steps % 2 == 1 and curr_steps % 2 == 1):
                    get_to.add(curr_point)
                
                # where can you move to
                # Check every second point in any combination of directions
                for p in product(self.offsets.keys(),self.offsets.keys()):
                    next_point1 = self.get_next_point(curr_point, self.offsets[p[0]])
                    if next_point1 is None:
                        continue

                    next_point2 = self.get_next_point(next_point1, self.offsets[p[1]])
                    if next_point2 is None:
                        continue
                    
                    if next_point2 in visited.keys() and curr_steps+2 >= visited[next_point2]:
                        continue
    
                    # keep going - add next point to q (stack)
                    q.append((next_point2,curr_steps+2))
        
        return len(get_to)