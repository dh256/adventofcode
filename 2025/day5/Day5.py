from dataclasses import dataclass

@dataclass
class InclusiveRange:
    start: int
    stop: int
    
    def includes_value(self, value: int) -> bool:
        return value >= self.start and value <= self.stop
    
    def contains(self, r: InclusiveRange) -> bool:
        return r.start >= self.start and r.stop <= self.stop
    
    def supercedes(self, r: InclusiveRange) -> bool:
        return self.start > r.stop
    
    def overlaps_end(self, r: InclusiveRange) -> bool:
        return self.start >= r.start and self.start <= r.stop and self.stop > r.stop
    
    @property
    def size(self) -> int:
        return (self.stop-self.start)+1

class Day5:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self._ranges: list[InclusiveRange] = list()
        self._ingredients: list[int] = list()
        
        ranges: bool = True
        for line in lines:
            if len(line) == 0:
                ranges = False
                continue
            
            if ranges:
                start, end = map(lambda p: int(p),line.split('-'))
                self._ranges.append(InclusiveRange(start,end))
            else:
                self._ingredients.append(int(line))
            
    def part1(self) -> int:
        # count fresh ingredients
        fresh: int = 0
        for ingredient in self._ingredients:
            for curr_range in self._ranges:
                if curr_range.includes_value(ingredient):
                   fresh += 1 
                   break
        return fresh

    def part2(self) -> int:
        # method requires that ranges are sorted by start value in ascending order
        self._ranges = sorted(self._ranges, key=lambda r: r.start)
        total_fresh: int = 0
        curr_range: InclusiveRange = self._ranges[0]
        for next_range in self._ranges[1:]:
            # next_range supercedes curr_range
            if next_range.supercedes(curr_range):
                total_fresh += curr_range.size
                curr_range = next_range
            
            # next_range overlaps end of curr_range
            elif next_range.overlaps_end(curr_range):
                # extend curr_range
                curr_range.stop = next_range.stop
                    
        # finally add curr_range size and return result
        return total_fresh + curr_range.size
    