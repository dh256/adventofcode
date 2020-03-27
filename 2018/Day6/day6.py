# Day 6 - Manhattan Distance
# See: https://en.wikipedia.org/wiki/Taxicab_geometry for explanation of Manhattan or taxicab distance 
# Essentially for two points (p1, p2) and (q1,q2) taxicab distance is |p1 - q1| + |p2 - q2|
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.infite = False
    
    def __eq__(self,p):
        return self.x == p.x and self.y == p.y
    
    def __str__(self):
        return f"({self.x},{self.y})"

    def manhattan_distance(self, point):
        distance = abs(self.x - point.x) + abs(self.y - point.y)
        return distance

class Grid:
    def __init__(self, filename):
        with open(filename, "r") as input:
            # populate list of coords
            self.coords = []
            for line in input:
                coord = line.strip('\n').split(", ")
                x = int(coord[0])
                y = int(coord[1])
                self.points.append(Point2D(x,y))

            # get bounding rectange. Any coord that has 1 or more nearest points outside this area is infinite
            self.max_x = max(self.points, key=lambda p : p.x)
            self.max_y = max(self.points, key=lambda p : p.y)
            self.min_x = min(self.points, key=lambda p : p.x)
            self.min_y = min(self.points, key=lambda p : p.y)

    def largest_area(self):
        ref_points = {}
        for x in range(self.min_x-1, self.max_x + 2):
            for y in range (self.min_y-1, self.max_y + 2):
                ref_point = Point2D(x,y)
                distances={}
                for (i,p) in enumerate(self.points):
                    ref_point.manhattan_distance(p)   
                    distances[(i,p)] = ref_point.manhattan_distance(p)  

# solve puzzle
grid= Grid("day6.txt")
