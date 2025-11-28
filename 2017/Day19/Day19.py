from dataclasses import dataclass
from enum import StrEnum

@dataclass
class Point:
    x: int
    y: int
    
    def __eq__(self,p: Point) -> bool:
        return self.x == p.x and self.y == p.y
    
    def __add__(self, p: Point) -> Point:
        return Point(self.x + p.x, self.y + p.y)
    
    def __hash__(self):
        return hash((self.x,self.y))

class Directions(StrEnum):
    UP = 'Up'
    DOWN = 'Down'
    LEFT = 'Left'
    RIGHT = 'Right'

class Day19:
    def __init__(self, file_name):
        self._grid: dict[Point, str] = dict()
        with open(file_name, 'r') as input_file:
            rows: list[str] = [row.strip('\n') for row in input_file]
        
        # fill grid
        self._grid = {Point(x,y): rows[y][x] for x in range(len(rows[0])) for y in range(len(rows))}
        self._start: Point = list(filter(lambda v: v[1] == '|' and v[0].y == 0, self._grid.items()))[0][0]
            
    def part1and2(self) -> tuple[str,int]:
        steps: int = 0
        direction_offsets: list[Directions, Point] = {Directions.LEFT: Point(-1,0),
                                   Directions.RIGHT: Point(1,0),
                                   Directions.DOWN: Point(0,1),
                                   Directions.UP: Point(0,-1)}
        curr_pos: Point = self._start
        curr_direction: Directions = Directions.DOWN
        letters_found: str = str()
        letters: set[str] = {chr(ord('A') + offset) for offset in range(26)}
        
        while True:
            try:
                # check if curr_pos is last
                if curr_pos not in self._grid.keys() or self._grid[curr_pos] == ' ':
                    return (letters_found,steps)
                
                if self._grid[curr_pos] in letters:
                    letters_found += self._grid[curr_pos]
                elif self._grid[curr_pos] == '+':
                    # change direction
                    if curr_direction in (Directions.UP, Directions.DOWN):
                        # next direction can only be left or right
                        # look left or right and if - or letter then good (can only be one)
                        if self._grid[curr_pos + direction_offsets[Directions.LEFT]] == '-' or self._grid[curr_pos + direction_offsets[Directions.LEFT]] in letters:
                            curr_direction = Directions.LEFT
                        else:
                            curr_direction = Directions.RIGHT
                    else:
                        # next direction can only be up or down
                        # look up or down and if | then good (can only be one)
                        if self._grid[curr_pos + direction_offsets[Directions.UP]] == '|' or self._grid[curr_pos + direction_offsets[Directions.UP]] in letters:
                            curr_direction = Directions.UP
                        else:
                            curr_direction = Directions.DOWN
                
                # move to next pos
                curr_pos += direction_offsets[curr_direction]
                steps += 1
                
            except KeyError:
                print(curr_pos, letters_found) 
                break
            
    
    def part2(self):
        pass