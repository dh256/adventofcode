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
            rows = [line.strip('\n') for line in input_file]
            
        # build grid
        self._max_x: int = len(rows[0])
        self._max_y: int = len(rows)
        self._grid: dict[Point, str] = {Point(x,y): rows[y][x] for x in range(self._max_x) for y in range(self._max_y)}    
        
    
    def get_accessible_rolls(self) -> list[Point]:
        # create offsets
        offsets: list[Point] = [Point(x,y) for x in range(-1,2) for y in range(-1,2) if Point(x,y) != Point(0,0)]
        
        # count accessible rolls
        accessible_rolls: list[Point] = list()
        for curr_point in self._grid.keys():
            if self._grid[curr_point] == '@':
                rolls: int = 0    
                for offset in offsets:
                    try:
                        if self._grid[curr_point + offset] == '@':
                            rolls += 1
                        
                        # more than 3, roll not accessible
                        if rolls > 3:
                            break
                    except KeyError:
                        # off grid, ignore
                        pass
                else:
                    accessible_rolls.append(curr_point)
        
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
                for accessible_roll in accessibe_rolls:
                    self._grid.pop(accessible_roll)
                rolls_removed += len(accessibe_rolls)
    
                        
