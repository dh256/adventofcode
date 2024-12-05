
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
        Find correctly ordered page updates
        Calculate a running sum of the middle page numbers for all correctly ordered page updates
        To help with Part 2 return a list of indices of all incorrectly updates 
        '''
        sum_middles: int = 0
        invalid_indices: list[int] = list()
        for pu_index, page_update in enumerate(self.page_updates):
            valid_order: bool = True
            index: int = 0
            while index < len(page_update)-1:
                # check that every page num after curr page corresponds to a page ordering rule
                curr_page: int = page_update[index]
                remaining_pages: list[int] = page_update[index+1:]
                for remaining_page in remaining_pages:
                    if remaining_page not in self.page_orders[curr_page]:
                        # invalid
                        valid_order = False
                        break 
                
                # if not valid - move to next page update 
                # otherwise, move to next page number and check again
                if not valid_order:
                    invalid_indices.append(pu_index)
                    break
                else:
                    index += 1
            
            # if valid increment sum_middles by middle page number 
            if valid_order:
                sum_middles += page_update[len(page_update) // 2]
            
        return sum_middles, invalid_indices

    def part2(self, invalid_indices: list[int]) -> int:
        # find incorrectly ordered reorder them until ok and sum middles once in correct order
        sum_middles = 0
        for invalid_pu in invalid_indices:
            page_update = self.page_updates[invalid_pu]
            order_changed: bool = False
            index = 0
            while index < len(page_update)-1:
                # check that every page num after curr page corresponds to a page ordering rule
                curr_page = page_update[index]
                remaining_pages = page_update[index+1:]
                for remaining_page in remaining_pages:
                    if remaining_page not in self.page_orders[curr_page]:
                        # invalid
                        # swap numbers and continue from same index
                        remain_index = page_update.index(remaining_page)
                        page_update[index] = remaining_page
                        page_update[remain_index] = curr_page
                        order_changed = True
                        break 
                
                if order_changed:
                    order_changed = False
                else:
                    index += 1
            
            sum_middles += page_update[len(page_update) // 2]
            
        return sum_middles
                        
