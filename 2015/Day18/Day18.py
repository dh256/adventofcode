'''
David Hanley, November 2024
'''
class Day18:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self.grid: list[str] = [line.strip('\n') for line in input_file]
        self.width: int = len(self.grid[0])
        self.height: int = len(self.grid)
    
    def count_neighbours_on(self, x: int, y: int) -> int:
        lights_on = 0
        for x_offset in range(-1,2):
            for y_offset in range(-1,2):
                if x_offset == 0 and y_offset == 0:
                    continue
                
                if x+x_offset < 0 or x+x_offset >= self.width:
                    continue
                
                if y+y_offset < 0 or y+y_offset >= self.height:
                    continue
                
                if self.grid[y+y_offset][x+x_offset] == '#':
                    lights_on += 1
        
        return lights_on
                       
            
    def solution(self,steps: int,part: int) -> int:
        if part == 2:
            self.grid[0] = '#' + self.grid[0][1:-1] + '#'
            self.grid[self.height-1] = '#' + self.grid[self.height-1][1:-1] + '#'
        for _ in range(0,steps):
            # process lights
            next_grid: list[str] = list()
            for y in range(0,self.height):
                new_row = ""
                for x in range(0,self.width):    
                    if part == 2 and ((x == 0 and y == 0) or (x == 0 and y == self.height-1) or (x == self.width-1 and y == 0) or (x == self.width-1 and y == self.height-1)):
                        new_row += '#'
                        continue
                    
                    # count neighbouring lights and apply transformation
                    neighbour_lights_on: int = self.count_neighbours_on(x,y)
                    if self.grid[y][x] == '#': 
                        if neighbour_lights_on in (2,3):
                            new_row += '#'
                        else:
                            new_row += '.'
                    else:
                        if neighbour_lights_on == 3:
                            new_row += '#'
                        else:
                            new_row += '.'
                next_grid.append(new_row)
            self.grid = next_grid 
        
        # count lights that are on in grid     
        return sum([len(list(filter(lambda c: c == '#', row))) for row in self.grid])
        
                        
