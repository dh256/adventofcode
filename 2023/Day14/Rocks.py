from Point import Point
from collections import defaultdict

class Rocks:
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            grid = [line.strip('\n') for line in input_file]
        
        self.cube_rocks_col = defaultdict(list)
        self.cube_rocks_row = defaultdict(list)
        self.round_rocks = dict()
        self.width = len(grid[0])
        self.height = len(grid)
        rock_idx = 0
        for y in range(self.height):
            for x in range(self.width):
                if grid[y][x] == 'O':
                    self.round_rocks[rock_idx] = (Point(x,y))
                elif grid[y][x] == '#':
                    self.cube_rocks_col[x].append(y)
                    self.cube_rocks_row[y].append(x)
                rock_idx+=1
            
    def __str__(self) -> str:
        disp = ''
        for y in range(self.height):
            for x in range(self.width):
                if Point(x,y) in self.round_rocks.values():
                    disp += 'O'
                elif y in self.cube_rocks_col[x]:
                    disp += '#'
                else:
                    disp += '.'

            disp += '\n'

        return disp

    def move_rocks_N(self, col, start_row, end_row, round_rocks) -> int:
        # There must be at least two spaces between cube rocks
        if end_row-start_row >= 2:
            # move rocks
            rocks_to_move = list(filter(lambda r: start_row <= r[1] <= end_row, round_rocks))
            round_offset = 0
            for r in rocks_to_move:
                self.round_rocks[r[0]] = Point(col,start_row+round_offset)
                round_offset += 1
            

    def tilt(self, direction: str) -> None:
        ''' 
        Tilt North and calculate total load on North beams
        '''
        if direction == 'N':    

            for col in range(self.width):
                round_rocks = [(i[0], i[1].y) for i in filter(lambda r: r[1].x == col, self.round_rocks.items())]
                start_row = 0
                end_row = None
                for end_row in self.cube_rocks_col[col]:
                    self.move_rocks_N(col,start_row,end_row,round_rocks)             
                    start_row = end_row + 1

                # move everything else up:
                if end_row is None or end_row < self.height:
                    self.move_rocks_N(col,start_row,self.height,round_rocks)


    def total_positions(self) -> int:
        total = 0
        for x in range(self.width):
            for r in filter(lambda r: r.x == x, self.round_rocks.values()):
                total += self.height - r.y
        return total

    def part1(self) -> int:
        self.tilt('N')
        total = self.total_positions()
        return total       
