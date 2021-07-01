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

    def process(self):
        # if coord not found then create new entry and set color to 0
        # if coord found set colour to !colour (i.e. 0 becomes 1 and 1 becomes 0)
        # after all instructions, count all entries where colour == 1 and return value
        for instructions in self.instructions:
            # reset curr_coord to origin hexagon
            x = 0
            y = 0
            z = 0
            for instruction in instructions.instructions:
                
                if instruction == "e":
                    # move east  inc x, dec y
                    x += 1
                    y -= 1
                elif instruction == "w":
                    # move west: dec x, inc y, 
                    x -= 1
                    y += 1 
                elif instruction == "nw":
                    # move north west: inc y, dec z, 
                    #x -= 1
                    y += 1
                    z -= 1
                elif instruction == "ne":
                    # move north east: inc x, dec z
                    x += 1
                    z -= 1
                elif instruction == "sw":
                    # move south west: dec x, inc z
                    x -= 1
                    z += 1
                elif instruction == "se":
                    # move south east: dec y, inc z
                    y -= 1
                    z += 1
                else:
                    print('Unexpected instruction. Terminating.')
                    exit()

                # check that x + y + z == 0, if not terminate program
                if x + y + z != 0:
                    print(f"Violation of coorodinate system detected: ({x,y,z}) is invalid")
                else:
                    pass
                    # set colour 
                    '''
                    try:
                        self.grid[(x,y,z)] = not self.grid[(x,y,z)]
                    except KeyError:
                        # first time, grid space visited, set to black
                        self.grid[(x,y,z)] = 1
            
                    '''
            # set colour
            try:
                self.grid[(x,y,z)] = not self.grid[(x,y,z)] 
                print('Visited > 1 times')
            except KeyError:
                # first time, grid space visited, set to black
                self.grid[(x,y,z)] = 1
            print(f'{(x,y,z)} set {self.grid[(x,y,z)]}')   

        # calculate number of black hexagons
        return len(list(filter(lambda i: i[1] == 1,self.grid.items())))
