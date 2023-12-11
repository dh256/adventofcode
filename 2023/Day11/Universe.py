from itertools import permutations

class Universe:
    def __init__(self, file_name) -> None:
        self.grid: list[list[str]] = []
        with open(file_name,'r') as input_file:
            for line in input_file:
                self.grid.append([*line.strip()])

        self.height = len(self.grid)
        self.width = len(self.grid[0])

        # expand grid
        # find all rows that have only .
        empty_rows: list[int] = []
        for y in range(self.height):
            if len(list(filter(lambda i: i == '.', self.grid[y]))) == self.width:
                empty_rows.append(y)

        # find all columns that have only .
        empty_cols: list[int] = []        
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] != '.':
                    break
            else:
                empty_cols.append(x)

        # expand rows
        for y in empty_rows[::-1]:
            new_row = ['.'] * self.width
            self.grid.insert(y+1,new_row)
        self.height += len(empty_rows)

        # expand cols
        for x in empty_cols[::-1]:
            for y in range(self.height):
                self.grid[y].insert(x+1, '.')
        self.width += len(empty_cols)


    def sum_shortest_paths(self) -> int:
        galaxies: list[tuple[int, int]] = []
        # get all pairs of galaxies
        for x in range(self.width):
            for y in range(self.height):
                if self.grid[y][x] == '#':
                    galaxies.append((x,y))
        
        result = 0
        for gp in permutations(galaxies,2):          # includes (x1,y1) -> (x2,y2) and (x2,y2) -> (x1,y1)
            result += abs(gp[0][0] - gp[1][0]) + abs(gp[0][1] - gp[1][1])

        return result // 2
