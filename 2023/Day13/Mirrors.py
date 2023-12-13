from dataclasses import dataclass, field

@dataclass
class ReflectionLine:
    type: str = 'N'
    num: int = 0

    @property
    def score(self) -> int:
        if self.type == 'H':
            return (100 * (self.num+1))
        elif self.type == 'V':        
            return self.num+1
        else:
            return 0


@dataclass
class Pattern:
    grid: list[str]
    width: int
    height: int
    reflection_line: ReflectionLine = field(default_factory=ReflectionLine)
    
    def transpose_grid(self):
        self.grid = list(map(list, zip(*self.grid)))
        self.width = len(self.grid[0])
        self.height = len(self.grid)
        return    

    def calc_reflection_line(self, mode: str) -> bool:
        '''
        Calculate where the reflection line is
        '''        
        if mode == 'V':
            # transpose grid
            self.transpose_grid()
        
        for i in range(0,self.height-1):
            # check whether rows either side of imaginary line match
            # make sure not to go over edge of grid
            match = False
            for offset in range(i+1):
                up_offset = i+offset+1
                down_offset = i-offset

                if up_offset < self.height and down_offset >= 0:
                    if self.grid[up_offset] == self.grid[down_offset]:
                        match = True
                    else:
                        match = False
                        break
            
            if match:
                # found reflection line
                self.reflection_line = ReflectionLine(mode,i)
                return True
            
        return False

class Mirrors:

    def __init__(self, filename) -> None:
        with open(filename, 'r') as input_file:
            self.patterns: list[Pattern] = []
            for raw_grid in input_file.read().split('\n\n'): 
                grid = raw_grid.split('\n')
                width = len(grid[0])
                height = len(grid)
                self.patterns.append(Pattern(grid,width,height))
        
    def part1(self) -> int:
        '''
        Returns number after summarizing all notes
        '''
        for pattern in self.patterns:
            # if there is not a HORIZONTAL reflection line check vertical
            if not pattern.calc_reflection_line('H'):
                pattern.calc_reflection_line('V')

        # calculate totals
        return sum([pattern.reflection_line.score for pattern in self.patterns])
       
