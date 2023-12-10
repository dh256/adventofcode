from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Point():
    x: int
    y: int

    def distance(self, p2) -> int:
        return abs((self.x - p2.x)) + abs((self.y - p2.y))
    
    def offset(self, offset: tuple):
        '''
        Offset point by (x+a,y+b) where (a,b) is offset tuple
        '''
        return Point(self.x + offset[0], self.y + offset[1])
