import re

class Day8:
    def __init__(self, filename: str) -> None: 
        with open(filename,'r') as input_file:
            self.literals: list[str] = [line.strip('\n') for line in input_file]   
    
    def part1(self) -> int:
        all = re.compile(r'(\\\\)|(\\x[0-9a-f]{2})|(\\")')
        memory_chars: int = 0
        string_code_chars: int = 0
        for literal in self.literals:
            counts: list[int] = [0,0,0]   # holds counts of items found in each regex group found
            string_code_chars += len(literal)
            all_matches = all.finditer(literal)
            # count number of matches in each group
            for m in all_matches:
                for e, g in enumerate(m.groups()):
                    counts[e] = counts[e]+ (1 if g is not None else 0)           
            
            # subtract out number of characters from literal length
            # 1 for each double slash or double quotes 
            # 3 for each hex code
            memory_chars += (len(literal) - (2 + counts[0] + counts[1]*3 + counts[2]))         
        
        return string_code_chars - memory_chars
            
    def part2(self) -> int:
        pass