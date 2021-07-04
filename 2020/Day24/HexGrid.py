from enum import Enum

class Directions(Enum):
    NE="ne"
    E="e"
    SE="se"
    SW="sw"
    W="w"
    NW="nw"
class Colour(Enum):
    WHITE=0
    BLACK=1
class Hexagon():

    @staticmethod
    def all_adjacent(x,y,z):
        '''
        Returns a list of all the coords of all hexagons adjacent to given coords
        '''
        hexagons = []

        # ne: inc x, dec z
        hexagons.append((x+1,y,z-1))
        # e: inc x, dec y
        hexagons.append((x+1,y-1,z))
        # se: dec y, inc z
        hexagons.append((x,y-1,z+1))
        # sw: dec x, inc z
        hexagons.append((x-1,y,z+1))
        # w: dec x, inc y
        hexagons.append((x-1,y+1,z))
        # nw: inc y, dec z
        hexagons.append((x,y+1,z-1))

        return hexagons

    @staticmethod
    def adjacent(x,y,z,direction):
        if direction == "e":
            # move east  inc x, dec y
            x += 1
            y -= 1
        elif direction == "w":
            # move west: dec x, inc y, 
            x -= 1
            y += 1 
        elif direction == "nw":
            # move north west: inc y, dec z, 
            y += 1
            z -= 1
        elif direction == "ne":
            # move north east: inc x, dec z
            x += 1
            z -= 1
        elif direction == "sw":
            # move south west: dec x, inc z
            x -= 1
            z += 1
        elif direction == "se":
            # move south east: dec y, inc z
            y -= 1
            z += 1
        return (x,y,z)

    

class Instructions:
    def __init__(self,instructions_str):
        # break instructions string into a set of individual instructions
        self.instructions = []
        curr_index = 0
        while curr_index < len(instructions_str):
            if instructions_str[curr_index] == 'e' or instructions_str[curr_index] == 'w':
                self.instructions.append(instructions_str[curr_index:curr_index+1])
                curr_index += 1
            else:
                self.instructions.append(instructions_str[curr_index:curr_index+2])
                curr_index += 2

class HexGrid:
    # need a coordinate system for HexGrid
    # See: https://www.redblobgames.com/grids/hexagons/ 
    # grid will be a dictionary where key is coord and value is current colour 0 - white; 1 - black
    
    def __init__(self,file_name):
        self.grid = {}
        with open(file_name,"r") as input_file:
            self.instructions = [Instructions(line.strip('\n')) for line in input_file]

    def process_instructions(self):
        # if coord not found then create new entry and set color to 0
        # if coord found set colour to !colour (i.e. 0 becomes 1 and 1 becomes 0)
        # after all instructions, count all entries where colour == 1 and return value
        for instructions in self.instructions:
            # reset curr_coord to origin hexagon
            x = 0
            y = 0
            z = 0
            for instruction in instructions.instructions:
                (x,y,z) = Hexagon.adjacent(x,y,z,instruction)
                
            # set colour
            if (x,y,z) in self.grid.keys():
                # invert colour
                self.flip((x,y,z)) 
            else:
                # first time, grid space visited, set to black
                self.grid[(x,y,z)] = Colour.BLACK
   
    def get_colour(self,key):
        # check if tile exists in grid - if not create a new white one
        if not key in self.grid.keys():
            self.grid[key] = Colour.WHITE

        # return colour
        return self.grid[key]

    @property
    def black_tiles(self):
        # return number of black tiles
        return len(list(filter(lambda v: v == Colour.BLACK, self.grid.values())))

    def flip(self,key):
        if self.grid[key] == Colour.BLACK:
            self.grid[key] = Colour.WHITE
        else:
            self.grid[key] = Colour.BLACK
    
    def flip_tiles(self,days):
        # now do daily transformation
        # get all the black tiles and count number of black adjacent tiles, if number is 0 or > 2, then add tile to flip list
        # for each white tile adjacent to one of the black tiles, count number of adjacent black tiles; if number is 2 then add to flip list (if not already added)
        # When complete, flip all tiles in flip list and repeat for given number of days 
        for day in range(1,days+1):
            tiles_to_flip = []
            
            # get every black tile
            black_tiles = [item[0] for item in list(filter(lambda i: i[1] == Colour.BLACK, self.grid.items()))]
            for black_tile in black_tiles:
                # get all tiles adjacent to black_tile
                adjacent_tiles_b = Hexagon.all_adjacent(black_tile[0],black_tile[1],black_tile[2])
                num_black_tiles1 = 0
                for tile in adjacent_tiles_b:
                    if self.get_colour(tile) == Colour.BLACK:
                        # if black, count 
                        num_black_tiles1 += 1
                    else:
                        # if white, get all adjacent tiles to white tile and count number that are black
                        adjacent_tiles_w = Hexagon.all_adjacent(tile[0],tile[1],tile[2])
                        num_black_tiles2 = 0
                        for tile_w in adjacent_tiles_w:
                            if self.get_colour(tile_w) == Colour.BLACK:
                                num_black_tiles2 += 1
                        
                        # should white tile be flipped
                        if num_black_tiles2 == 2 and tile not in tiles_to_flip:
                            tiles_to_flip.append(tile) 
                                             

                # should black tile be flipped
                if (num_black_tiles1 == 0 or num_black_tiles1 > 2) and black_tile not in tiles_to_flip:
                    tiles_to_flip.append(black_tile) 

            # flip tiles
            for tile in tiles_to_flip:
                self.flip(tile)

            


        
