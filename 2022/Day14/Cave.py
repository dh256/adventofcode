from dataclasses import dataclass
from enum import Enum, auto
from copy import deepcopy

class TileMaterial(Enum):
    Air = auto()
    Rock = auto()
    Sand = auto()
    

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def next(self, offsets: tuple):
        return Point(self.x + offsets[0], self.y + offsets[1])

    @classmethod
    def convert_to_point(cls, point_coords: str):
        '''
        Converts a x,y coord string into a Point
        '''
        start_point_coords = point_coords.split(',')
        return Point(int(start_point_coords[0]), int(start_point_coords[1]))


class Cave:
    sand_move_offsets = [(0,1),(-1,1),(1,1)]            # allowable moves for a grain of sand - offsets from current point
    sand_start_point = Point(500,0)                     # point that sand first enters grid
    def __init__(self, file_name: str) -> None:
        '''
        Constructor
        '''
        self.grid = dict()
        with open(file_name, 'r') as input_file:
            for line in input_file:
                line = line.strip('\n')
                self.rock_line_coords = line.split(' -> ')
                start_point = Point.convert_to_point(self.rock_line_coords[0])
                for curr_index in range(1, len(self.rock_line_coords)):
                    end_point = Point.convert_to_point(self.rock_line_coords[curr_index])
                    
                    # lines can be drawn either up or down
                    if start_point.y > end_point.y:
                        start_y = end_point.y
                        end_y = start_point.y
                    else:
                        start_y = start_point.y
                        end_y = end_point.y

                    # lines can be drawn either left or right
                    if start_point.x > end_point.x:
                        start_x = end_point.x
                        end_x = start_point.x
                    else:
                        start_x = start_point.x
                        end_x = end_point.x
                    
                    for x in range(start_x, end_x+1):
                        for y in range(start_y, end_y+1):
                            self.grid[Point(x,y)] = TileMaterial.Rock
                    start_point = end_point

        # find last row that has rock on it
        self.last_rock_row = max([key.y for key in self.grid.keys()])
        self.original = deepcopy(self.grid)
        
    def reset(self) -> None:
        '''
        Resets cave to original state - useful for Part 2
        '''
        self.grid = deepcopy(self.original) 
         

    def falling_sand(self) -> int:
        '''
        Simulate falling sand and return number of units of sand come to rest
        '''
        fallen_sand = 0
        curr_point = Cave.sand_start_point
        while curr_point.y <= self.last_rock_row:
            for move_offset in Cave.sand_move_offsets:
                next_point = curr_point.next(move_offset)
                
                # build grid dynamically - all new points must be air
                if next_point not in self.grid:
                    self.grid[next_point] = TileMaterial.Air

                # if next point is air, move is allowed and can keep falling
                if self.grid[next_point] == TileMaterial.Air:
                    curr_point = next_point
                    break
            else:
                # all moves blocked
                # sand comes to rest at current point
                self.grid[curr_point] = TileMaterial.Sand
                fallen_sand += 1
                
                # go to next grain of sand
                curr_point = Cave.sand_start_point

        return fallen_sand

    def falling_sand2(self) -> int:
        '''
        Assume a floor row (made of rock) two below lowest row infinitely wide now exists with rock on it, 
        Run si
        mulation until no more sand can fall i.e. sand is now blocking Point 500,0
        Return number of grains of sand that have fallen
        '''
        floor_row = self.last_rock_row+2
        fallen_sand = 0
        curr_point = Cave.sand_start_point
        while True:
            # check next available cell (in order down, diagonally left, diagonnaly right)
            for move_offset in Cave.sand_move_offsets:
                next_point = curr_point.next(move_offset)
                
                # build grid dynamically 
                # If on floor row all new points are rock, otherwise air
                if next_point not in self.grid:
                    if next_point.y < floor_row:
                        self.grid[next_point] = TileMaterial.Air
                    else:
                        # floor row is all rock
                        self.grid[next_point] = TileMaterial.Rock
                
                # if next point is air, move is allowed and can keep falling
                if self.grid[next_point] == TileMaterial.Air:
                    curr_point = next_point
                    break
            else:
                # all moves blocked
                # sand comes to rest at current point
                self.grid[curr_point] = TileMaterial.Sand
                fallen_sand += 1
                if curr_point == Cave.sand_start_point:
                    # done, no more sand can fall
                    return fallen_sand
                else:
                    curr_point = Cave.sand_start_point
        