from math import sqrt, modf

class Day3:
    def __init__(self, cell: int):
        self.cell = cell
    
    def solution(self,part: int) -> int:
        # populate adjacents - offsets to find all adjacent cells
        if part == 2:
            adjacents: list[tuple[int,int]] = [(x,y) for x in range(-1,2) for y in range(-1,2) if (x,y) != (0,0)]
                
        '''
        Build each spiral (n, where n>0) as follows:
            Move up 2*n-1 rows.  (x,y+1) 
            Move left 2*n cols.  (x-1,y) 
            Move down 2*n rows.  (x,y-1)
            Move right 2*n cols. (x+1,y)
            
        Note: Spiral 0 contains single value 1
        '''
        squares: dict[tuple[int,int],int] = dict()
        squares[(0,0)] = 1
        if part == 1 and self.cell == 1:
            return 0
        if part == 2 and self.cell < 1:
            return 1
        
        spiral: int = 1
        counter: int = 2
        while True:
            curr_x: int = spiral
            curr_y: int = -spiral
            
            for side in range(0,4):
                for _ in range(0,2*spiral):
                    if side == 0:       # right
                        curr_y += 1
                    elif side == 1:     # top
                        curr_x -= 1
                    elif side == 2:     # left
                        curr_y -= 1
                    else:               # bottom
                        curr_x += 1
                    
                    if part == 1:
                        squares[(curr_x,curr_y)] = counter
                        if counter == self.cell:
                            return abs(curr_x) + abs(curr_y)
                        counter += 1
                    elif part == 2:
                        squares[(curr_x,curr_y)] = self._sum_adjacent_squares(curr_x,curr_y,squares,adjacents)
                        if squares[(curr_x,curr_y)] > self.cell:
                            return squares[(curr_x,curr_y)]
            
            spiral += 1    
    
    def _sum_adjacent_squares(self, curr_x: int, curr_y: int, cells: dict, adjacents: list) -> int:  
        new_value: int = 0
        for adjacent in adjacents:
            adjacent = (curr_x+adjacent[0],curr_y+adjacent[1])
            if adjacent in cells.keys():
                new_value += cells[adjacent]
                
        return new_value
    