import re
from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Point():
    x: int
    y: int


class Engine:
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            self.schematic = [line.strip('\n') for line in input_file]
        self.rows = len(self.schematic)
        self.cols = len(self.schematic[0])
        self.numbers: list[tuple] = []
        self.symbols: list[Point] = []

        # process schematic
        re_nums = re.compile(r'\d+')
        re_symbols = re.compile(r'[^0-9\.]')
        y = 0
        for x in range(self.rows):
            curr_schematic_row = self.schematic[x]
            for num in re.finditer(re_nums, curr_schematic_row):
                start_pos = num.start()
                end_pos = num.end()-1
                value = int(num.group(0))
                self.numbers.append((Point(start_pos,y),Point(end_pos,y),value))

            for symbol in re.finditer(re_symbols, curr_schematic_row):
                self.symbols.append(Point(symbol.start(),y))

            y += 1

    def _is_part_number(self, num: tuple) -> bool:
        start_row = 0 if num[0].y == 0 else num[0].y - 1
        start_col = 0 if num[0].x == 0 else num[0].x - 1
        end_row = self.rows-1 if num[1].y == self.rows-1 else num[1].y + 1
        end_col = self.cols-1 if num[1].x == self.cols-1 else num[1].x + 1

        for y in range(start_row, end_row+1):
            for x in range(start_col, end_col+1):
                if Point(x,y) in self.symbols:
                    return True
        return False
            


    def sum_of_part_numbers(self) -> int:
        result = 0
        for num in self.numbers:
            if self._is_part_number(num):
                result += num[2]
        return result
    
