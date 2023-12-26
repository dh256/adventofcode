import re
from dataclasses import dataclass, field
from itertools import permutations

@dataclass
class Hailstone:
    x: int
    y: int
    z: int
    vx: int
    vy: int
    vz: int
    m: float = field(init=False)        # gradient
    c: float = field(init=False)        # where line intercepts y axis

    def __post_init__(self) -> None:
        '''
        Calculate m and c
        '''
        self.m = self.vy / self.vx                  
        self.c = self.y - (self.m * self.x)

    def intersection(self, h2) -> tuple[float,float]:
        '''
        Calculate where two lines intersect
        i.e. solve for x and y - if no intersection return None
        '''
        # need to check lines not parallel (same gradient)
        if not self.m == h2.m:
            # find intersection
            xi = (h2.c - self.c) / (self.m - h2.m)
            yi = self.m * xi + self.c
            return (xi,yi)
        else:
            return None
    
    

class Hailstones:
    def __init__(self, file_name: str) -> None:
        self.hailstones: list[Hailstone] = []
        with open(file_name,'r') as input_file:
            hailstones_raw = [re.findall(r'-?\d+', line.strip()) for line in input_file]
            for hailstone in hailstones_raw:
                self.hailstones.append(Hailstone(int(hailstone[0]),int(hailstone[1]),int(hailstone[2]),int(hailstone[3]),int(hailstone[4]),int(hailstone[5])))

    def in_past(self,h: Hailstone, i: tuple[float, float]) -> bool:
        if h.vx > 0 and i[0] < h.x:
            return True

        if h.vx < 0 and i[0] > h.x:
            return True

        if h.vy > 0 and i[1] < h.y:
            return True

        if h.vy < 0 and i[1] > h.y:
            return True

        return False

    def part1(self,min_xy: int, max_xy: int) -> int:
        '''
        Return the number of hailstones who paths will intersect inside a bounding rectangle
        (min_x,min_y),(max_x,max_y)
        '''
        intersects = 0
        for p in permutations(self.hailstones,2):
            h1, h2 = p
            if i:=h1.intersection(h2):
                # do lines interesect in give region
                if (min_xy <= i[0] <= max_xy) and (min_xy <= i[1] <= max_xy):
                    # is intersection in the past for either hailstone? 
                    # If so do not count intersection
                    
                    # check h1
                    if not (self.in_past(h1,i) or self.in_past(h2,i)):
                        intersects += 1

        return intersects // 2
    
