
''' 
David Hanley, December 2024
'''
from functools import cache

class Day19:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.patterns: list[str] = lines[0].split(', ')
        self.designs: list[str] = [line for line in lines[2:]]
    
    @cache
    def valid_design(self, design: str) -> bool:
        '''
        Assume that design is not valid
        Loop through all possible patterns
            If design starts with current pattern, recursively call this function on what's left of the design after removing pattern and OR result with current result
            This ensures that if a single combination matches then will get a TRUE result
            Note: Crtitical to do this for all possible combinations
        Fucntion returns True if design is completely matched
        Return result when all combinations processed
        
        Use @cache, memonization is needed for acceptable performance. 
        '''
        if len(design) == 0:
            return True
        else:
            result: bool = False
            for pattern in self.patterns:
                if design.startswith(pattern):
                    result = result or self.valid_design(design[len(pattern):])
                else:
                    continue
            return result

    @cache
    def valid_design2(self, design: str) -> int:
        '''
        Similar to valid_design above except this time
        count the number of times get a match that than just yes/no
        '''
        if len(design) == 0:
            return 1
        else:
            matches: int = 0
            for pattern in self.patterns:
                if design.startswith(pattern):
                    matches = matches + self.valid_design2(design[len(pattern):])
                else:
                    continue
            return matches
    
    def part1(self) -> int:
        good_designs: int = 0
        for design in self.designs:
            if self.valid_design(design):
                good_designs += 1   
        return good_designs
        
    def part2(self) -> int:
        good_design_combs: int = 0
        for design in self.designs:
            good_design_combs += self.valid_design2(design)
        
        return good_design_combs
                        
