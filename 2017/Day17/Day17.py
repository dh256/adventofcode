            
class Day17:
    def __init__(self,steps: int) -> None:
        self._steps = steps
        self._buffer: list[int] = [0]
     
    def part1(self) -> int:
        # fill buffer
        curr_pos: int = 0
        for i in range(1,2018):
            curr_pos = ((curr_pos + self._steps) % len(self._buffer)) + 1
            self._buffer = self._buffer[0:curr_pos] + [i] + self._buffer[curr_pos:]
        return self._buffer[curr_pos+1]     
            
    def part2(self) -> int:
        '''
        zero will always be at index 0 (cannot insert at position 0)
        Therefore, only need to track what values are inserted at position 1 
        All other values are irrelevant as they only ever get pushed up and we do not need to track these
        '''
        result: int | None = None
        curr_pos: int = 0
        for i in range(1,50000000):
            curr_pos = ((curr_pos + self._steps) % i) + 1
            if curr_pos == 1:
                result = i
        return result
        
        