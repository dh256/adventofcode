import re

class Cave:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            self.locations = []
            for line in lines:
                self.locations.append([int(loc) for loc in re.findall(r'\d',line)])
            self.max_y = len(lines)
            self.max_x = len(self.locations[0])

    def find_risk_level(self):
        low_points = []
        self.low_point_locations = []           # used in Part 2
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
                north = 10
                south = 10
                east = 10
                west = 10
                curr_val = self.locations[y][x]
                if y > 0:
                    north = self.locations[y-1][x]
                if y < self.max_y-1:
                    south = self.locations[y+1][x]
                if x < self.max_x-1:
                    east = self.locations[y][x+1]
                if x > 0:
                    west = self.locations[y][x-1]

                if (curr_val < north) and (curr_val < south) and (curr_val < east) and (curr_val < west):
                    low_points.append(curr_val)
                    self.low_point_locations.append((y,x))

        # calculate risk level
        return sum(low_points) + len(low_points)

    def find_largest_basins(self,number):
        basins = []
        num_points = 0
        for low_point_loc in self.low_point_locations:
            self.basin_low_points = 1
            self.locations_visited = []
            self.low_points(low_point_loc)
            basins.append(self.basin_low_points)

        result = 1
        for p in sorted(basins,reverse=True)[0:3]:
            result *= p

        return result

    def low_points(self,location):
        # count number of points lower than low point
        # for each point lower recurse
        self.locations_visited.append(location)
        y = location[0]
        x = location[1]
        curr_val = self.locations[y][x]
        
        # North
        if not (y-1,x) in self.locations_visited and y > 0 and curr_val < self.locations[y-1][x] and self.locations[y-1][x] != 9:
            self.basin_low_points += 1
            self.low_points((y-1,x))
        
        # South
        if not (y+1,x) in self.locations_visited and y < self.max_y-1 and curr_val < self.locations[y+1][x] and self.locations[y+1][x] != 9:
            self.basin_low_points += 1
            self.low_points((y+1,x))
        
        # East
        if not (y,x+1) in self.locations_visited and x < self.max_x-1 and curr_val < self.locations[y][x+1] and self.locations[y][x+1] != 9:
            self.basin_low_points += 1
            self.low_points((y,x+1))
        
        # West
        if not (y,x-1) in self.locations_visited and x > 0 and curr_val < self.locations[y][x-1] and self.locations[y][x-1] != 9:
            self.basin_low_points += 1
            self.low_points((y,x-1))
            
            