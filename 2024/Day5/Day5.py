
''' 
David Hanley, December 2024
'''
import re
from collections import defaultdict

class Day5:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        num_re = re.compile(r'\d+')
        page_order = True
        self.page_orders: dict[int,list[int]] = defaultdict(list)
        self.page_updates: list[list[int]] = list()
        for line in lines:
            if len(line) == 0:
                page_order = False
                continue
            
            page_nums = [int(p) for p in num_re.findall(line)]
            if page_order:
                self.page_orders[page_nums[0]].append(page_nums[1])
            else:
                self.page_updates.append(page_nums)
                
            
    def part1(self) -> int:
        # find correctly ordered updates
        sum_middles = 0
        for page_update in self.page_updates:
            valid_order = True
            index = 0
            while index < len(page_update)-1:
                # check that every page after it corresponds to a page ordering rule
                curr_page = page_update[index]
                remaining_pages = page_update[index+1:]
                for remaining_page in remaining_pages:
                    if remaining_page not in self.page_orders[curr_page]:
                        # invalid
                        valid_order = False
                        break 
                
                if not valid_order:
                    break
                else:
                    index += 1
            
            if valid_order:
                sum_middles += page_update[len(page_update) // 2]
            
        return sum_middles

    def part2(self) -> int:
        return 0
                        
