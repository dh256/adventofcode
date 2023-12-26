'''
Part 1 solution: quite slow but gets right answer
'''
from collections import deque
from Point import Point

class Hike:
    offsets={'N': (0,-1), 'S': (0,1), 'E': (1,0), 'W': (-1,0)}
    slopes={'>': 'E', '<': 'W', 'v': 'S','^': 'N'}
             
    def on_grid(self,p: Point) -> bool:
        '''
        returns True if given point p in on grides
        '''
        return 0 <= p.x < self.width and 0 <= p.y < self.height

    def __init__(self,file_name) -> None:
        self.grid: list[list] = list()
        with open(file_name, 'r') as input_file:
            for line in [line.strip() for line in input_file]:
                self.grid.append([*line])

        self.width = len(self.grid[0])
        self.height = len(self.grid)
        self.start = Point(self.grid[0].index('.'),0)
        self.end = Point(self.grid[-1].index('.'),self.height-1)

    def part1(self) -> int:
        '''
        Calculate longest hike you can take
        '''
        path_lengths: list[int] = list()
        q = deque()
        q.appendleft((self.start,0,set()))      # point, direction, steps, visited
        while len(q) > 0:
            curr_point, steps, visited = q.pop()
            
            # if a slope can only move in direction of that slope
            if self.grid[curr_point.y][curr_point.x] in Hike.slopes.keys():
                offset_range = [Hike.offsets[self.slopes[self.grid[curr_point.y][curr_point.x]]]]
            else:
                # otherwise check all directions
                offset_range = Hike.offsets.values()

            # check all possible next points
            for offset in offset_range:
                next_point = curr_point.offset(offset)

                # is on grid
                if not self.on_grid(next_point):
                    continue

                # already visited
                if next_point in visited:
                    continue

                # reached the end
                if next_point == self.end:
                    # reached end, append to path lengths
                    path_lengths.append(steps+1)
                    continue

                # if a path or a slope - add next point to Q
                if self.grid[next_point.y][next_point.x] == '.' or self.grid[next_point.y][next_point.x] in Hike.slopes.keys():
                    new_visited = {v for v in visited}
                    new_visited.add(curr_point)
                    q.appendleft((next_point,steps+1,new_visited))  
                    continue 

        return max(path_lengths)