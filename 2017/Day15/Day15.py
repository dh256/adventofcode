class Day15:

    def __init__(self, genA: int, genB: int) -> None:
        self._genA_start: int = genA
        self._genB_start: int = genB
        self._divisor: int = 2147483647
        self._genA_factor: int = 16807
        self._genB_factor: int = 48271
        self._bits_16: int = pow(2,16)
    
    def part1(self) -> int:
        judge_count: int = 0
        genA_next: int = self._genA_start
        genB_next: int = self._genB_start
        for _ in range(0,40000000):
            genA_next = (genA_next * self._genA_factor) % self._divisor
            genB_next = (genB_next * self._genB_factor) % self._divisor
            if genA_next % self._bits_16 == genB_next % self._bits_16:
                judge_count += 1  
        return judge_count    
    
    def part2(self) -> int:
        '''
        Solution works but is quite slow
        Need to look for a more efficient algorithm
        '''
        
        # do genA - generate 5000000 candidates and store 
        genA_next: int = self._genA_start
        genA: dict[int, int] = dict()
        i: int = 0
        while i < 50000000:
            genA_next = (genA_next * self._genA_factor) % self._divisor
            if genA_next % 4 == 0:
                genA[i] = genA_next
                i += 1
        
        # do genB - generate 5000000 candidates and store 
        genB_next: int = self._genB_start
        genB: dict[int, int] = dict()
        i: int = 0
        while i < 50000000:
            genB_next = (genB_next * self._genB_factor) % self._divisor
            if genB_next % 8 == 0:
                genB[i] = genB_next
                i += 1
        
        # count matches
        judge_count: int = 0
        for i in range(0,5000000):
            if genA[i] % self._bits_16 == genB[i] % self._bits_16:
                judge_count += 1
                
        return judge_count