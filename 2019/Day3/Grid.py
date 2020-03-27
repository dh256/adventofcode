from Lines import Lines
from Point2D import Point2D
import copy

        
class Grid:
    def __init__(self,lines):
        self.centre_point = Point2D(0,0)
        self.lines = lines
        self.grid = {}
        
    def add_line(self,x,y,lineno,steps):
        point = Point2D(x,y)
        if point in self.grid:
            if not lineno in self.grid.get(point)[0]:
                lines = copy.copy(self.grid.get(point))
                lines.append((lineno,steps))
                self.grid[point] = lines
        else:
            self.grid[point] = [(lineno,steps)]
    
    def populate(self):
        lineno = 1
        for line in self.lines.lines:
            steps = 0
            curr_x = self.centre_point.x
            curr_y = self.centre_point.y
            for instruction in line.instructions:
                if instruction.direction == "U":
                    for y in range(instruction.points):
                        steps += 1
                        curr_y += 1
                        self.add_line(curr_x,curr_y,lineno,steps)

                elif instruction.direction == "D":
                    for y in range(instruction.points):
                        steps += 1
                        curr_y -= 1
                        self.add_line(curr_x,curr_y,lineno,steps)

                elif instruction.direction == "R":
                    for x in range(instruction.points):
                        steps += 1
                        curr_x += 1
                        self.add_line(curr_x,curr_y,lineno,steps)

                elif instruction.direction == "L":
                    for x in range(instruction.points):
                        steps += 1
                        curr_x -= 1
                        self.add_line(curr_x,curr_y,lineno,steps)
        
            lineno += 1

    def closest_intersect(self):
        # closest intersect is min distance of any point with 2 line nos from centre point
        intersect_points = [key for key,val in self.grid.items() if len(val) == 2]
        nearest_point = min(intersect_points, key=lambda i : i.distance(self.centre_point))
        return nearest_point.distance(self.centre_point)

    def shortest_intersect_path(self):
        # shortest intersect path is shortest combined path for 2 wires
        intersect_points = [val for key,val in self.grid.items() if len(val) == 2]
        shortest_path = min(intersect_points, key=lambda v : v[0][1] + v[1][1])
        return shortest_path[0][1] + shortest_path[1][1]
