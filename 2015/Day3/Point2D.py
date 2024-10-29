from dataclasses import dataclass
@dataclass
class Point2D:
    x: int
    y: int
    
    def move(self, direction:str):
        if direction == '^':
            new_pos = Point2D(self.x, self.y+1)
        elif direction == 'v':
            new_pos = Point2D(self.x, self.y-1)
        elif direction == '>':
            new_pos = Point2D(self.x+1, self.y)
        elif direction == '<':
            new_pos = Point2D(self.x-1, self.y)
        return new_pos
    
    def __hash__(self) -> int:
        return hash((self.x,self.y))