from enum import IntEnum, auto
from collections import deque
from dataclasses import dataclass

@dataclass(frozen=True, eq=True)
class Point:
    x: int
    y: int

@dataclass 
class QueueNode:
    point: Point
    distance: int

class Move(IntEnum):
    Up = auto()
    Down = auto()
    Left = auto()
    Right = auto()

class Hills:
    def __init__(self,file_name: str) -> None:
        self.hills = {}
        x = 0
        y = 0
        with open(file_name,'r') as in_file:
            for line in in_file:
                line = line.strip('\n')
                x = 0
                for c in line:
                    if c == 'S':
                        self.start_pos = Point(x, y)
                        c = 'a'
                    elif c == 'E':
                        self.end_pos = Point(x, y)
                        c = 'z'
                    self.hills[Point(x,y)] = ord(c)
                    x += 1
                y += 1
        
        # set max_x and max_y
        self.max_x = x
        self.max_y = y
        
    def adjacent_valid(self, curr_point, adjacent_point) -> bool:
        # valid if not over edge of grid and adjacent cell is equal to or 1 more than this current cell
        new_range = range(self.hills[curr_point],self.hills[curr_point]+2)
        if not (adjacent_point.y >= 0 and adjacent_point.y < self.max_y and adjacent_point.x >= 0 and adjacent_point.x < self.max_x):
            return False
        
        if self.hills[adjacent_point] - self.hills[curr_point] > 1:
            return False

        return True

    def find_shortest_path(self, start_point=None) -> int:
        '''
        Moves from start position to final location using Breadth First Search
        Based on: https://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/
        '''
        if start_point is None:
            start_point = self.start_pos
        q = deque()
        q.append(QueueNode(start_point, 0))
        visited = {self.start_pos}

        while q:
            curr_node = q.popleft()
            if curr_node.point == self.end_pos:
                return curr_node.distance
            
            # check each direction
            for move_direction in Move:
                if move_direction == Move.Up:
                    x_inc, y_inc = 0, -1
                elif move_direction == Move.Down:
                    x_inc, y_inc = 0, 1
                elif move_direction == Move.Left:
                    x_inc, y_inc = -1, 0
                elif move_direction == Move.Right:
                    x_inc, y_inc = 1, 0

                adjacent_point = Point(curr_node.point.x+x_inc, curr_node.point.y+y_inc)
                if self.adjacent_valid(curr_node.point, adjacent_point) and not adjacent_point in visited:
                    visited.add(adjacent_point)
                    q.append(QueueNode(adjacent_point,curr_node.distance+1))

        return -1
                
                
    def find_shortest_path2(self) -> int:
        '''
        Find shortest path for all possible starting points (i.e. cells with height ord('a'))
        Brute force approach, there is probably a quicker way
        '''
        candidates = set()
        all_start_points = dict(filter(lambda item: item[1] == ord('a'), self.hills.items()))
        for start_point in all_start_points:
            result = self.find_shortest_path(start_point)
            if result != -1:
                candidates.add(result)
        return min(candidates)