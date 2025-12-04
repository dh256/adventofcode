from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
    def __add__(self, p: Point):
        return Point(self.x + p.x, self.y + p.y)
    
    def __eq__(self, p: Point) -> bool:
        return self.x == p.x and self.y == p.y
    
    def __hash__(self) -> int:
        return hash((self.x, self.y))
        
class Day4:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            rows: list[str] = [line.strip('\n') for line in input_file]
            
        # build grid
        self._grid: dict[Point, str] = {Point(x,y): rows[y][x] for x in range(len(rows[0])) for y in range(len(rows))}    
        
        # create offsets
        self._offsets: list[Point] = [Point(x,y) for x in range(-1,2) for y in range(-1,2) if Point(x,y) != Point(0,0)]
        
    
    def get_accessible_rolls(self) -> list[Point]:
        # get location of all accessible rolls
        accessible_rolls: set[Point] = set()
        for curr_point in self._grid.keys():
            if self._grid[curr_point] == '@':
                adjacent_rolls: int = 0    
                for offset in self._offsets:
                    try:
                        if self._grid[curr_point + offset] == '@':
                            adjacent_rolls += 1
                    except KeyError:
                        # off grid, ignore
                        pass
                        
                    # more than 3, roll not accessible
                    if adjacent_rolls > 3:
                        break 
                else:
                    accessible_rolls.add(curr_point)
        
        return accessible_rolls
            
    def part1(self) -> int:
        return len(self.get_accessible_rolls())

    def part2(self) -> int:
        rolls_removed: int = 0
        while True:
            accessibe_rolls: list[Point] = self.get_accessible_rolls()
            if len(accessibe_rolls) == 0:
                return rolls_removed
            else:
                # count and remove accessible rolls
                rolls_removed += len(accessibe_rolls)
                for accessible_roll in accessibe_rolls:
                    self._grid.pop(accessible_roll)
                
    
                        
