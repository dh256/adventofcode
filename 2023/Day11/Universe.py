from itertools import permutations

class Universe:
    def __init__(self, file_name:str, e: int) -> None:
        grid: list[list[str]] = []
        with open(file_name,'r') as input_file:
            for line in input_file:
                grid.append([*line.strip()])

        height: int = len(grid)
        width: int = len(grid[0])

        # get the galaxies
        self.galaxies: dict = {}
        galaxy_id: int = 1
        for x in range(width):
            for y in range(height):
                if grid[y][x] == '#':
                    self.galaxies[galaxy_id] = (x,y)
                    galaxy_id += 1

        # get empty rows and cols
        empty_rows = sorted(list({r for r in range(height)}.difference({v[1] for v in self.galaxies.values()})))
        empty_cols = sorted(list({r for r in range(width)}.difference({v[0] for v in self.galaxies.values()})))

        '''
        Expands universe e times
        e.g. if e = 2 then, each intitial empty row and column are replaced by 2 rows and columns
        e.g. if e = 10 then, each intitial empty row and column are expanded by 9
        Only care about galaxies. Only need to move position of galaxies right or down by number expanded rows and columns 
        Must do in reverse order starting from highest rows and columns first
        '''
        for y in empty_rows[::-1]:
            # find all galaxies after y and move these down by e
            for g in filter(lambda i: i[1][1] > y, self.galaxies.items()):
                self.galaxies[g[0]] = (self.galaxies[g[0]][0],self.galaxies[g[0]][1]+e-1)

        for x in empty_cols[::-1]:
            # find all galaxies after x and move these right by e
            for g in filter(lambda i: i[1][0] > x, self.galaxies.items()):
                self.galaxies[g[0]] = (self.galaxies[g[0]][0]+e-1,self.galaxies[g[0]][1])         

    def sum_shortest_paths(self) -> int:
        result = 0
        for gp in permutations(self.galaxies.values(),2):          # permutations includes (x1,y1) -> (x2,y2) and (x2,y2) -> (x1,y1)
            result += abs(gp[0][0] - gp[1][0]) + abs(gp[0][1] - gp[1][1])

        return result // 2
