class Eris:
    grid_size = 5
    def __init__(self, filename):
        # populate grid
        self.layout = {}
        with open(filename, 'r') as grid_input:
            rows = [line.strip('\n') for line in grid_input]
            y = 0
            for row in rows:
                x = 0
                for cell in row:
                    if cell == '.': 
                        self.layout[(x,y)] = 0
                    else:
                        self.layout[(x,y)] = 1
                    x += 1
                y += 1

    def __repr__(self):
        out_str = ''
        for y in range(0,Eris.grid_size):
            for x in range(0,Eris.grid_size):
                if self.layout[(x,y)] == 1:
                    out_str += '#'
                else:
                    out_str += '.'
            out_str += '\n'
        return out_str
    
    '''
    Hash Eris by creating a 25 bit number where each bit position represents value of point in grid
    Highest bit represents point 4,4 -> 2nd highest point (3,4) .. Lowest bit point (0,0)
    '''
    def __hash__(self):
        num = 0
        for y in range(Eris.grid_size-1,-1,-1):
            for x in range(Eris.grid_size-1,-1,-1):
                num = (num | self.layout[(x,y)]) << 1
        return num >> 1   # reverse final bit shift
    
    def _count_adjacent_bugs(self,x,y):
        adj_bugs = 0
        # up 1
        if y > 0: 
            adj_bugs += self.layout[(x,y-1)]

        # down 1
        if y < Eris.grid_size-1:
            adj_bugs += self.layout[(x,y+1)]

        # left 1
        if x > 0:
            adj_bugs += self.layout[(x-1,y)]

        # right 1
        if x < Eris.grid_size-1:
            adj_bugs += self.layout[(x+1,y)]

        return adj_bugs

    '''
    Calculate Biodiversity by moving bugs until the same pattern of bugs appears twice
    '''
    def biodiversity(self):
        hashed_layouts = {self.__hash__(): 0}
        while True: 
            # first of all populate adjacent bugs
            adj_bugs = {}
            for y in range(0,Eris.grid_size):
                for x in range(0,Eris.grid_size):
                    adj_bugs[(x,y)] = self._count_adjacent_bugs(x,y)

            # now update grid
            for y in range(0,Eris.grid_size):
                for x in range(0,Eris.grid_size):
                    if self.layout[(x,y)] == 1 and adj_bugs[(x,y)] != 1:
                        self.layout[(x,y)] = 0
                    elif self.layout[(x,y)] == 0 and adj_bugs[(x,y)] in (1,2):
                        self.layout[(x,y)] = 1

            # get hash, and add to hashed_layouts - if exception, already exists return hash
            hash_layout = self.__hash__()
            if hash_layout in hashed_layouts:
                return hash_layout
            else:
                hashed_layouts[hash_layout] = 0
            
                
                
        