
''' 
David Hanley, December 2024
'''
from dataclasses import dataclass,field
from typing import ClassVar
from enum import Enum, auto

class SchematicType(Enum):
    KEY = auto()
    LOCK = auto()

@dataclass
class Schematic:
    drawing: list[str] 
    type: SchematicType = field(init=False) 
    pin_heights: list[int] = field(init=False)
    width: ClassVar[int] = 5
    height: ClassVar[int] = 6

    def __post_init__(self):
        self.type = SchematicType.LOCK if self.drawing[0] == '#' * Schematic.width else SchematicType.KEY
        
        # calculate pin heights
        self.pin_heights = list()
        for col in range(Schematic.width):
            if self.type == SchematicType.LOCK:
                row = 1
                row_increment = 1
            else:
                row = Schematic.height-1
                row_increment = -1
        
            pin_height: int = 0
            while self.drawing[row][col] == '#':
                pin_height += 1
                row += row_increment
            self.pin_heights.append(pin_height)

class Day25:
    def __init__(self,file_name:str) -> None:
        drawing: list[str] = list()
        self.schematics: list[Schematic] = list()    
        with open(file_name, 'r') as input_file:
            for line in input_file:
                if len(line.strip('\n')) == 0:
                    self.schematics.append(Schematic(drawing))
                    drawing = list()
                else:
                    drawing.append(line.strip('\n'))
            
        self.schematics.append(Schematic(drawing))
            
    def part1(self) -> int:
        # get all the keys
        result: int = 0
        keys = list(filter(lambda s: s.type == SchematicType.KEY, self.schematics))
        locks = filter(lambda s: s.type == SchematicType.LOCK, self.schematics)
        for lock in locks:
            for key in keys:
                for idx, lock_ph in enumerate(lock.pin_heights):
                    if key.pin_heights[idx] + lock_ph >= Schematic.height:
                        break
                else:
                    result += 1
        return result

                        
