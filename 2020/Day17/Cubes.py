class Cubes:
    # get active cubes
    # range is the min-1 to nax-1 for each dimension
    def ranges(self):
        active_cubes = [item[0] for item in list(filter(lambda i:i[1],self.grid.items()))]
        min_x = min(active_cubes,key=lambda i:i[0])[0]
        max_x = max(active_cubes,key=lambda i:i[0])[0]
        min_y = min(active_cubes,key=lambda i:i[1])[1]
        max_y = max(active_cubes,key=lambda i:i[1])[1]
        min_z = min(active_cubes,key=lambda i:i[2])[2]
        max_z = max(active_cubes,key=lambda i:i[2])[2]
        return (min_x-1,max_x+1,min_y-1,max_y+1,min_z-1,max_z+1)
    
    def __init__(self,filename) -> None:
        self.grid = {}          # grid - key is coord of cube, value is state (False, inactive; True, active)
        with open(filename,"r") as input_file:
            initial_grid_points = [line.strip('\n') for line in input_file]
            x = 0
            y = 0
            z = 0
            for row in initial_grid_points:
                x = 0
                for c in row:
                    self.grid[(x,y,z)] = c == '#'
                    x += 1
                y += 1

    def get_neighbours(self,coord):
        neighbours = [(x,y,z) for x in range(coord[0]-1,coord[0]+2) for y in range(coord[1]-1,coord[1]+2) for z in range(coord[2]-1,coord[2]+2)]
       

        # make sure they are all in the grid
        for neighbour in neighbours:
            if neighbour not in self.grid.keys():
                self.grid[neighbour] = False

        # remove actual coord
        neighbours.remove(coord) 
        return neighbours 


    def cycle(self,cycles):
        # Go through neighbours, if active count; if inactive get all its neighbours and count active, if 3 active add to switch_list (for active cubes if active count is 2 or 3 add to switch_list)
        # Repeat cycle number of times  
        for cycle in range(0,cycles):
            # get all active cubes
            switch_list = []            # contains the co-ords of all cubes to switch
            ranges = self.ranges()

            # for each cube - get neighbours
            for x in range(ranges[0],ranges[1]+1):
                for y in range(ranges[2],ranges[3]+1):
                    for z in range(ranges[4],ranges[5]+1):
                        neighbours = self.get_neighbours((x,y,z))
                        active_neighbours = len([n for n in neighbours if self.grid[n]])
                        if (self.grid[(x,y,z)] and active_neighbours not in (2,3)) or (not self.grid[(x,y,z)] and active_neighbours == 3):
                            switch_list.append((x,y,z)) 

            for cube in switch_list:
                if not cube in self.grid.keys():
                    self.grid[cube] = False
                self.grid[cube] = not self.grid[cube] 
            
        # return number of active cubes
        return len(list(filter(lambda v:v,self.grid.values())))


class Cubes2:
    # get active cubes
    # range is the min-1 to nax-1 for each dimension
    def ranges(self):
        active_cubes = [item[0] for item in list(filter(lambda i:i[1],self.grid.items()))]
        min_x = min(active_cubes,key=lambda i:i[0])[0]
        max_x = max(active_cubes,key=lambda i:i[0])[0]
        min_y = min(active_cubes,key=lambda i:i[1])[1]
        max_y = max(active_cubes,key=lambda i:i[1])[1]
        min_z = min(active_cubes,key=lambda i:i[2])[2]
        max_z = max(active_cubes,key=lambda i:i[2])[2]
        min_w = min(active_cubes,key=lambda i:i[3])[3]
        max_w = max(active_cubes,key=lambda i:i[3])[3]
        return (min_x-1,max_x+1,min_y-1,max_y+1,min_z-1,max_z+1,min_w-1,max_w+1)
    
    def __init__(self,filename) -> None:
        self.grid = {}          # grid - key is coord of cube, value is state (False, inactive; True, active)
        with open(filename,"r") as input_file:
            initial_grid_points = [line.strip('\n') for line in input_file]
            x = 0
            y = 0
            z = 0
            w = 0
            for row in initial_grid_points:
                x = 0
                for c in row:
                    self.grid[(x,y,z,w)] = c == '#'
                    x += 1
                y += 1

    def get_neighbours(self,coord):
        neighbours = [(x,y,z,w) for x in range(coord[0]-1,coord[0]+2) for y in range(coord[1]-1,coord[1]+2) for z in range(coord[2]-1,coord[2]+2) for w in range(coord[3]-1,coord[3]+2)]
    
        # make sure they are all in the grid
        for neighbour in neighbours:
            if neighbour not in self.grid.keys():
                self.grid[neighbour] = False

        # remove actual coord
        neighbours.remove(coord) 
        return neighbours 


    def cycle(self,cycles):
        # Go through neighbours, if active count; if inactive get all its neighbours and count active, if 3 active add to switch_list (for active cubes if active count is 2 or 3 add to switch_list)
        # Repeat cycle number of times  
        for cycle in range(0,cycles):
            # get all active cubes
            switch_list = []            # contains the co-ords of all cubes to switch
            ranges = self.ranges()

            # for each cube - get neighbours
            for x in range(ranges[0],ranges[1]+1):
                for y in range(ranges[2],ranges[3]+1):
                    for z in range(ranges[4],ranges[5]+1):
                        for w in range(ranges[6],ranges[7]+1):
                            neighbours = self.get_neighbours((x,y,z,w))
                            active_neighbours = len([n for n in neighbours if self.grid[n]])
                            if (self.grid[(x,y,z,w)] and active_neighbours not in (2,3)) or (not self.grid[(x,y,z,w)] and active_neighbours == 3):
                                switch_list.append((x,y,z,w)) 

            for cube in switch_list:
                if not cube in self.grid.keys():
                    self.grid[cube] = False
                self.grid[cube] = not self.grid[cube] 
            
        # return number of active cubes
        return len(list(filter(lambda v:v,self.grid.values())))

        