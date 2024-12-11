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
    
    # functools cache method makes this insanely fast as it caches results from calls with same inputs
    # dynamic programming
    @functools.cache
    def generate_stone_nums(self,num,blinks):
        # reached blink 75, return single number
        if blinks == self.max_blinks:
            return 1
        
        # recursively, work out next numbers (according to rules) and count number generated
        nums_generated = 0
        if num == 0:
            nums_generated += self.generate_stone_nums(1,blinks+1)
        elif len(str(num)) % 2 == 0:
            pow10 = pow(10, len(f'{num}') // 2)         # would be great if there was an easy way to do this with maths
            left_num = num // pow10
            right_num = num % pow10
            nums_generated += self.generate_stone_nums(left_num,blinks+1)
            nums_generated += self.generate_stone_nums(right_num,blinks+1)
        else:
            nums_generated += self.generate_stone_nums(num * 2024, blinks+1)
        return nums_generated
    
    
   