class Day1:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self._moves = map(lambda l: int(l[1:]) if l[0] == 'R' else int(l[1:])*-1,lines)
        self._dial_size: int = 100

    def part1and2(self) -> int:
        dial_pos: int = 50
        at_zero_count: int = 0
        through_zero_count: int = 0
        started_at_zero: bool = False
        
        for move in self._moves:
            dial_pos = (dial_pos + move)
            
            # figure out how many times went through zero
            if dial_pos < 0:
                # went through zero at least once
                through_zero_count += (abs(dial_pos) // self._dial_size) + 1
                
                # started at zero then decrement by 1
                if started_at_zero:
                    through_zero_count -= 1
                    
                # ended at zero then decremenrt by 1
                if dial_pos % self._dial_size == 0:
                    through_zero_count -= 1   
            
            elif dial_pos > self._dial_size:
                through_zero_count += abs(dial_pos // self._dial_size)
                
                # ended at zero then decrement by 1
                if dial_pos % self._dial_size == 0:
                    through_zero_count -= 1
            
            dial_pos = dial_pos % self._dial_size
            if dial_pos == 0:
                at_zero_count += 1
                started_at_zero = True
            else:
                started_at_zero = False
        
        return (at_zero_count, through_zero_count + at_zero_count)
                        
