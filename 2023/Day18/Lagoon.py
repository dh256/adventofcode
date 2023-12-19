from dataclasses import dataclass
from Point import Point

@dataclass
class Instruction:
    direction: str
    cubes: int
    colour: str

class Lagoon:
    offsets = {'L': (-1,0), 'R': (1,0), 'D': (0,1), 'U': (0,-1)}
    
    def __init__(self,file_name) -> None:
        with open(file_name, 'r') as input_file:
            instruction_parts = [line.strip().split() for line in input_file]
            self.instructions: list[Instruction] = [Instruction(instruction_part[0], int(instruction_part[1]), instruction_part[2][2:-1]) for instruction_part in instruction_parts]

    def part1(self) -> int:
        '''
        Return cubes dug
        '''
        
        '''
        Get points of polygon
        '''
        points: list[Point] = []
        point = Point(0,0)
        for i in self.instructions:
            point = point.offset((Lagoon.offsets[i.direction][0]*i.cubes, Lagoon.offsets[i.direction][1]*i.cubes)) 
            points.append(point)

        '''
        Use Shoelace Formula and Picks Theorem to calculate total area of polygon
        Interestingly, for Picks Theorem need to add 1 rather substract 1, not clear why but it works
        '''
        pair1_sum: int = 0
        pair2_sum: int = 0
        for idx in range(len(points)):
            p1 = points[idx]
            p2 = points[(idx+1)%len(points)] 
            pair1_sum += p1.x * p2.y 
            pair2_sum += p2.x * p1.y
        area = abs((pair1_sum-pair2_sum) // 2)
        return area+(sum([instruction.cubes for instruction in self.instructions]) // 2)+1
    
    def part2(self) -> int:
        # remap instructions based 
        direction_map = {'0': 'R', '1': 'D', '2': 'L', '3': 'U'}
        for instruction in self.instructions:
            instruction.cubes = int(instruction.colour[0:5],16)
            instruction.direction = direction_map[instruction.colour[-1]]
        
        # run part 1
        return self.part1()
        