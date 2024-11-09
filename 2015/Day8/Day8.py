import re

class Day8:
    def __init__(self, filename: str) -> None: 
        with open(filename,'r') as input_file:
            self.literals: list[str] = [line.strip('\n') for line in input_file]   
    
    def calculate(self) -> tuple[int,int]:
        escape_rx = re.compile(r'(\\\\)|(\\x[0-9a-f]{2})|(\\")')
        memory_chars: int = 0
        string_code_chars: int = 0
        total_chars: int = 0
        for literal in self.literals:
            string_code_chars += len(literal)
            
            '''
            Part 1
            '''
            counts: list[int] = [0,0,0]   # holds counts of items found in each regex group found
            escape_matches = escape_rx.finditer(literal)
            # count number of matches in each group
            for m in escape_matches:
                for e, g in enumerate(m.groups()):
                    counts[e] = counts[e]+ (1 if g is not None else 0)           
            
            # subtract out number of characters from literal length
            # 2 for each double quote (start and end of literal)
            # 1 for each double slash or double quotes 
            # 3 for each hex code
            memory_chars += (len(literal) - (2 + counts[0] + counts[1]*3 + counts[2]))         
        
            '''
            Part 2
            '''
            encode_counts: list[int] = [0,0]
            encode_rx = re.compile(r'(")|(\\)')
            encode_rx_matches = encode_rx.finditer(literal)
            for m in encode_rx_matches:
                for e, g in enumerate(m.groups()):
                    encode_counts[e] = encode_counts[e]+ (1 if g is not None else 0)
            
            # add in additional characters
            # two for start and end quotes
            # one for each " and \ character found         
            total_chars += len(literal) + 2 + encode_counts[0] + encode_counts[1]
            
        return ((string_code_chars - memory_chars),(total_chars-string_code_chars))
            