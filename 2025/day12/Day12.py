import re
from dataclasses import dataclass, field, Field

@dataclass
class Region:
    width: int
    height: int
    indexes: list[int] = field(default_factory=list)

@dataclass
class Point:
    x: int
    y: int
    
    def __hash__(self) -> int:
        return hash((self.x,self.y))
    
    def __eq__(self,p2) -> int:
        return self.x == p2.x and self.y == p2.y

class Day12:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            parts = input_file.read().split('\n\n')
         
        # shapes
        self.shapes: dict[int,int] = dict()
        for s, part in enumerate(parts[0:6]):
            area: int = 0
            shape = dict()
            for line in part.split('\n')[1:]:
                for c in line:
                    if c == '#':
                        area += 1
            self.shapes[s] = area
        
        # regions
        self.regions: list[Region] = list()
        for line in parts[6].split('\n'):
            width, height, *indexes = map(lambda n: int(n), re.findall('\\d+',line))
            self.regions.append(Region(width,height,indexes)) 
            
    def part1(self) -> int:
        result: int = 0
        for region in self.regions:  
            total_area: int = 0
            for index, num_shapes in enumerate(region.indexes):
                total_area += self.shapes[index] * num_shapes
        
            if total_area <= region.width * region.height:
                result += 1   
          
        return result  
                    
