
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
        ''' 
        Find correctly ordered page updates.
        '''
        sum_middles = 0
        for page_update in self.page_updates:
            valid_order = True
            index = 0
            while index < len(page_update)-1:
                # check that every page num after curr page corresponds to a page ordering rule
                curr_page = page_update[index]
                remaining_pages = page_update[index+1:]
                for remaining_page in remaining_pages:
                    if remaining_page not in self.page_orders[curr_page]:
                        # invalid
                        valid_order = False
                        break 
                
                # if not valid - move to next page update 
                # otherwise, move to next page number and check again
                if not valid_order:
                    break
                else:
                    index += 1
            
            # if valid increment sum_middles by middle page number 
            if valid_order:
                sum_middles += page_update[len(page_update) // 2]
            
        return sum_middles

    def part2(self) -> int:
        # find incorrectly ordered reorder them until ok and sum middles once in correct order
        sum_middles = 0
        for page_update in self.page_updates:
            valid_order: bool = True
            order_changed: bool = False
            index = 0
            while index < len(page_update)-1:
                # check that every page num after curr page corresponds to a page ordering rule
                curr_page = page_update[index]
                remaining_pages = page_update[index+1:]
                for remaining_page in remaining_pages:
                    if remaining_page not in self.page_orders[curr_page]:
                        # invalid
                        # swap numbers and continie from same index
                        remain_index = page_update.index(remaining_page)
                        page_update[index] = remaining_page
                        page_update[remain_index] = curr_page
                        valid_order = False
                        order_changed = True
                        break 
                
                if not valid_order:
                    valid_order = True
                else:
                    index += 1
            
            if order_changed:
                sum_middles += page_update[len(page_update) // 2]
            
        return sum_middles
                        
