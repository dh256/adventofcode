class Day5:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self._ranges: list[range] = list()
        self._ingredients: list[int] = list()
        
        ranges: bool = True
        for line in lines:
            if len(line) == 0:
                ranges = False
                continue
            
            if ranges:
                start, end = map(lambda p: int(p),line.split('-'))
                self._ranges.append(range(start,end))
            else:
                self._ingredients.append(int(line))
        
        # sort ranges by start value (needed for Part 2)
        self._ranges = sorted(self._ranges, key=lambda r: r.start)
            
    def part1(self) -> int:
        # count fresh ingredients
        fresh: int = 0
        for ingredient in self._ingredients:
            for curr_range in self._ranges:
                if ingredient >= curr_range.start and ingredient <= curr_range.stop:
                   fresh += 1 
                   break
        return fresh

    def part2(self) -> int:
        # create a list of all valid non-overlapping ranges and populate with initial range
        valid_ranges: list[range] = [self._ranges[0]]
        for curr_range in self._ranges[1:]:
            # curr_range is wholly contained within last valid range continue
            if curr_range.start >= valid_ranges[-1].start and curr_range.stop <= valid_ranges[-1].stop:
                continue
            
            # curr_range start is after last valid range
            if curr_range.start > valid_ranges[-1].stop:
                # add curr_range to valid range
                valid_ranges.append(curr_range)
            # curr range starts in last valid range but stops beyond it
            else:
                # extend last valid range
                valid_ranges[-1] = range(valid_ranges[-1].start,curr_range.stop)
                
        # once we have all valid ranges, sum the size of all the ranges
        return sum(map(lambda r: (r.stop - r.start) + 1, valid_ranges))
        
                  
                        
