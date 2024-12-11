''' 
David Hanley, December 2024
'''
import functools

class Day11:
    def __init__(self,stones:str) -> None:
        self.stone_nums: list[int] = [int(stone) for stone in stones.split(' ')]
            
    def solution(self, blinks: int) -> int:
        nums_generated = 0
        self.max_blinks = blinks
        for num in self.stone_nums:
            nums_generated += self.generate_stone_nums(num,0)
        return nums_generated
    
    # dynamic programming
    # functools cache method makes this insanely fast as it caches results from calls with same inputs
    @functools.cache
    def generate_stone_nums(self,num,blinks):
        
        # reached required number of blinks, no need to recurse any further. Return count of 1 (this num)
        if blinks == self.max_blinks:
            return 1
        
        # Work out next numbers (according to rules) and add the count of this to number generated
        nums_generated = 0
        if num == 0:
            nums_generated += self.generate_stone_nums(1,blinks+1)
        elif len(str(num)) % 2 == 0:
            pow10 = pow(10, len(f'{num}') // 2)         # would be great if there was an easy way to do this with maths
            nums_generated += self.generate_stone_nums(num // pow10,blinks+1)
            nums_generated += self.generate_stone_nums(num % pow10,blinks+1)
        else:
            nums_generated += self.generate_stone_nums(num * 2024, blinks+1)
        
        # return count of numbers generated
        return nums_generated
    
    
   