from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int
    
    def neighbours(self) -> list[Point]:
        return [self.add(o) for o in [Point(0,1),Point(0,-1),Point(1,0),Point(-1,0)]]
                
    def add(self,p2: Point) -> Point:
        return Point(self.x+p2.x,self.y+p2.y)
    
    def __hash__(self):
        return hash((self.x,self.y))