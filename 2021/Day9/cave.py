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

    def _find_low_points(self):
        self.low_point_locations = []           # used in Part 2
        for y in range(0,self.max_y):
            for x in range(0,self.max_x):
                north = 9
                south = 9
                east = 9
                west = 9
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
                    self.low_point_locations.append((y,x))

    def find_risk_level(self):
        # find low points
        self._find_low_points()
        
        # calculate risk level
        return sum([self.locations[loc[0]][loc[1]] for loc in self.low_point_locations]) + len(self.low_point_locations)

    def find_largest_basins(self,number):
        # find low points
        self._find_low_points()
        
        basin_counts = []
        num_points = 0
        for low_point_loc in self.low_point_locations:
            self.basin_points_count = 1             # reset basin point count
            self.locations_visited = []             # reset list of locations already visited
            self._higher_points(low_point_loc)      # find all the higher points for this low point
            basin_counts.append(self.basin_points_count)    

        result = 1
        for p in sorted(basin_counts,reverse=True)[0:number]:
            result *= p

        return result

    def _higher_points(self,location):
        # for each adjacent point (North, South, East, West 
        # check if higher (unless 9) and recurse if not already visited
        self.locations_visited.append(location)
        y = location[0]
        x = location[1]
        curr_val = self.locations[y][x]
        
        # North
        if not (y-1,x) in self.locations_visited and y > 0 and curr_val < self.locations[y-1][x] and self.locations[y-1][x] != 9:
            self.basin_points_count += 1
            self._higher_points((y-1,x))
        
        # South
        if not (y+1,x) in self.locations_visited and y < self.max_y-1 and curr_val < self.locations[y+1][x] and self.locations[y+1][x] != 9:
            self.basin_points_count += 1
            self._higher_points((y+1,x))
        
        # East
        if not (y,x+1) in self.locations_visited and x < self.max_x-1 and curr_val < self.locations[y][x+1] and self.locations[y][x+1] != 9:
            self.basin_points_count += 1
            self._higher_points((y,x+1))
        
        # West
        if not (y,x-1) in self.locations_visited and x > 0 and curr_val < self.locations[y][x-1] and self.locations[y][x-1] != 9:
            self.basin_points_count += 1
            self._higher_points((y,x-1))
            
            