import re
from collections import defaultdict
from Point import Point

class Engine:
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            self.schematic = [line.strip('\n') for line in input_file]
        self.rows = len(self.schematic)
        self.cols = len(self.schematic[0])
        self.row_numbers = defaultdict(list)        
        self.symbols: dict = {}

        # process schematic
        re_nums = re.compile(r'\d+')
        re_symbols = re.compile(r'[^0-9\.]')
        y = 0
        for x in range(self.rows):
            curr_schematic_row = self.schematic[x]
            # find numbers in each row.
            # for each number store start and end points and value
            for num in re.finditer(re_nums, curr_schematic_row):
                start_pos = num.start()
                end_pos = num.end()-1
                value = int(num.group(0))
                start_pos_pt = Point(start_pos,y)
                end_pos_pt = Point(end_pos,y)
                self.row_numbers[y].append((start_pos_pt,end_pos_pt,value))

            # find symbols in each row
            # for each symbol store position and value
            for symbol in re.finditer(re_symbols, curr_schematic_row):
                self.symbols[Point(symbol.start(),y)] = symbol.group(0)

            y += 1

    def _is_part_number(self, num: tuple) -> bool:
        # get start and end rows and cols to cover all adjacent points
        start_row = 0 if num[0].y == 0 else num[0].y - 1
        start_col = 0 if num[0].x == 0 else num[0].x - 1
        end_row = self.rows-1 if num[1].y == self.rows-1 else num[1].y + 1
        end_col = self.cols-1 if num[1].x == self.cols-1 else num[1].x + 1

        # part number if any adjacent point to number is a symbol
        for y in range(start_row, end_row+1):
            for x in range(start_col, end_col+1):  
                if Point(x,y) in self.symbols.keys():
                    return True
        return False

    def _gear_nums(self, symbol_pos: Point) -> list[int]:
        # get start and end rows and cols to cover all adjacent points
        start_row = 0 if symbol_pos.y == 0 else symbol_pos.y - 1
        start_col = 0 if symbol_pos.x == 0 else symbol_pos.x - 1
        end_row = self.rows-1 if symbol_pos.y == self.rows-1 else symbol_pos.y + 1
        end_col = self.cols-1 if symbol_pos.x == self.cols-1 else symbol_pos.x + 1

        # if a part of a number found in any point adjacent to gear symbol then it may form part of gear ratio
        nums = []
        for y in range(start_row, end_row+1):
            row_nums = self.row_numbers[y]
            for x in range(start_col, end_col+1):
                for num in row_nums:
                    if x >= num[0].x and x <= num[1].x:
                        nums.append(num[2])
                        # remove to prevent number being counted more than once
                        row_nums.remove(num)
                        break
        return nums
    
    def sum_of_part_numbers(self) -> int:
        result = 0
        for y in range(self.rows+1):
            for num in self.row_numbers[y]:
                if self._is_part_number(num):
                    result += num[2]
        return result
    
    def sum_of_gear_ratios(self) -> int:
        result = 0
        for item in self.symbols.items():
            if item[1] == '*':
                nums = self._gear_nums(item[0])
                # if two numbers found, add gear ratio to total 
                if len(nums) == 2:
                    result += (nums[0] * nums[1])
        return result