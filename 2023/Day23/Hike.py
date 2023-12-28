'''
Part 1 solution: a little slow (few secons)
Part 2 solution: simple mod to part 1 but incredibly slow (at least 24 hours)
Both parts use recursion (whenever two or more possible paths are found) to consider all possible paths from start to end and return longest

Will come back to this to make it more efficient.
Secret is to visit each node once and hold max steps to each node.
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

    def path(self,curr_point: Point,steps: int, visited: set[int], ignore_paths: bool) -> None:
        while True:
            if curr_point == self.end:
                self.path_lengths.add(steps)
                return
            
            if not ignore_paths:
                if self.grid[curr_point.y][curr_point.x] in Hike.slopes.keys():
                    offset_range = [Hike.offsets[self.slopes[self.grid[curr_point.y][curr_point.x]]]]
                else:
                    # otherwise check all directions
                    offset_range = Hike.offsets.values()
            else:
                offset_range = Hike.offsets.values()

            possible_points = []
            for offset in offset_range:
                next_point = curr_point.offset(offset)
                
                # off grid
                if not self.on_grid(next_point):
                    continue
                
                # already visited
                if next_point in visited:
                    continue

                # is a path or a slope
                if self.grid[next_point.y][next_point.x] == '.' or self.grid[next_point.y][next_point.x] in Hike.slopes.keys():
                    possible_points.append(next_point)

            if len(possible_points) == 0:
                return
            elif len(possible_points) == 1:
                visited.add(curr_point)
                steps += 1
                curr_point = possible_points[0]
            else:
                visited.add(curr_point)
                for p in possible_points:
                    next_visited = {v for v in visited}
                    self.path(p, steps+1, next_visited,ignore_paths)
                return  

    def part1_alt(self) -> int:
        self.path_lengths = set()
        self.path(self.start, 0, set(), False)
        return max(self.path_lengths)
    
    def part2_alt(self) -> int:
        self.path_lengths = set()
        self.path(self.start, 0, set(), True)
        return max(self.path_lengths)

    def part1(self, ignore_slopes: bool = False) -> int:
        '''
        Calculate longest hike you can take
        If ignore_slopes is True treat all slopes as normal paths
        '''
        path_lengths: list[int] = list()
        q = deque()
        q.append((self.start,0,set()))      # point, direction, steps, visited
        while len(q) > 0:
            curr_point, steps, visited = q.pop()
            
            # if a slope can only move in direction of that slope
            if not ignore_slopes:
                if self.grid[curr_point.y][curr_point.x] in Hike.slopes.keys():
                    offset_range = [Hike.offsets[self.slopes[self.grid[curr_point.y][curr_point.x]]]]
                else:
                    # otherwise check all directions
                    offset_range = Hike.offsets.values()
            else:
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
                    print(f'End Reached: Path length {steps+1}')
                    path_lengths.append(steps+1)
                    continue

                # if a path or a slope - add next point to Q
                if self.grid[next_point.y][next_point.x] == '.' or self.grid[next_point.y][next_point.x] in Hike.slopes.keys():
                    new_visited = {v for v in visited}
                    new_visited.add(curr_point)
                    q.append((next_point,steps+1,new_visited))  
                    continue 

        return max(path_lengths)
    
    def part2(self) -> int:
        '''
        Calculate longest hike you can take
        This time treat all slopes as normal paths
        '''
        return self.part1(True)
