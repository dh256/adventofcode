import re
from functools import reduce

class Day6:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines: list[str] = [line.strip('\n') for line in input_file]
        
        # build the columns
        # will store op, nums (as raw strings including leading and trailing spaces) and width of column
        self._cols: list[(str,list[str]),int] = list()
        matches = [m for m in re.finditer(r'\*|\+',lines[-1])]
        for match_index in range(len(matches)):
            op: str = matches[match_index].group()
            col_start: int = matches[match_index].start()
            col_end: int = matches[match_index+1].start()-1 if match_index != len(matches)-1 else len(lines[-1])
            nums: list[str] = list()
            for num_line in lines[0:-1]:
                nums.append(num_line[col_start:col_end])
            self._cols.append((op,nums,col_end-col_start))
    
    def _perform_op(self, op, nums) -> int:
        # perform operation on nums and return result
        if op == '+':
            return sum(nums)
        else:
            return reduce(lambda x, y: x * y, nums, 1)
        
    def part1(self) -> int:
        total: int = 0
        for op, nums, _ in self._cols:
            # get nums in column x
            nums = list(map(lambda n: int(n), nums))
            total += self._perform_op(op, nums)
        return total

    def part2(self) -> int:
        total: int = 0
        for op, nums, col_size in self._cols:
            col_nums: list[int] = list()
            for num_index in range(col_size-1,-1,-1):
                next_num: str = ""
                for num in nums:
                    if num[num_index].isdigit():
                        next_num += num[num_index]
                col_nums.append(int(next_num))
            total += self._perform_op(op, col_nums) 
        return total   
