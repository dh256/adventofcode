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

    def move_rocks_S(self, col, start_row, end_row, round_rocks) -> int:
        # There must be at least two spaces between cube rocks
        if end_row-start_row >= 2:
            # move rocks
            rocks_to_move = list(filter(lambda r: start_row <= r[1] <= end_row, round_rocks))
            round_offset = 0
            for r in rocks_to_move:
                self.round_rocks[r[0]] = Point(col,(end_row-1)-round_offset)
                round_offset += 1

    def move_rocks_W(self, row, start_col, end_col, round_rocks) -> int:
        # There must be at least two spaces between cube rocks
        if end_col-start_col >= 2:
            # move rocks
            rocks_to_move = list(filter(lambda r: start_col <= r[1] <= end_col, round_rocks))
            round_offset = 0
            for r in rocks_to_move:
                self.round_rocks[r[0]] = Point(start_col+round_offset,row)
                round_offset += 1

    def move_rocks_E(self, row, start_col, end_col, round_rocks) -> int:
        # There must be at least two spaces between cube rocks
        if end_col-start_col >= 2:
            # move rocks
            rocks_to_move = list(filter(lambda r: start_col <= r[1] <= end_col, round_rocks))
            round_offset = 0
            for r in rocks_to_move:
                self.round_rocks[r[0]] = Point((end_col-1)-round_offset,row)
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

        elif direction == 'S':    
            for col in range(self.width):
                round_rocks = [(i[0], i[1].y) for i in filter(lambda r: r[1].x == col, self.round_rocks.items())]
                start_row = 0
                end_row = None
                for end_row in self.cube_rocks_col[col]:
                    self.move_rocks_S(col,start_row,end_row,round_rocks)             
                    start_row = end_row + 1

                # move everything else down:
                if end_row is None or end_row < self.height:
                    self.move_rocks_S(col,start_row,self.height,round_rocks)


        elif direction == 'W':    
            for row in range(self.height):
                round_rocks = [(i[0], i[1].x) for i in filter(lambda r: r[1].y == row, self.round_rocks.items())]
                start_col = 0
                end_col = None
                for end_col in self.cube_rocks_row[row]:
                    self.move_rocks_W(row,start_col,end_col,round_rocks)             
                    start_col = end_col + 1

                # move everything else up:
                if end_col is None or end_col < self.width:
                    self.move_rocks_W(row,start_col,self.width,round_rocks)

        elif direction == 'E':    
            for row in range(self.height):
                round_rocks = [(i[0], i[1].x) for i in filter(lambda r: r[1].y == row, self.round_rocks.items())]
                start_col = 0
                end_col = None
                for end_col in self.cube_rocks_row[row]:
                    self.move_rocks_E(row,start_col,end_col,round_rocks)             
                    start_col = end_col + 1

                # move everything else up:
                if end_col is None or end_col < self.width:
                    self.move_rocks_E(row,start_col,self.width,round_rocks)


    def total_positions(self) -> int:
        total = 0
        for x in range(self.width):
            for r in filter(lambda r: r.x == x, self.round_rocks.values()):
                total += self.height - r.y
        return total

    def part1(self) -> int:
        for x in range (200):
            self.tilt('N')
            self.tilt('W')
            self.tilt('S')
            self.tilt('E')
            print(f'{x},{self.total_positions()}')
        return 0       
