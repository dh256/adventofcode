'''
David Hanley, Nov 2024
'''
import re

class Day12:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self.text = input_file.read()
            
    def part1(self) -> int:
        return sum([int(result) for result in re.findall(r'-?\d+', self.text)])
        
    def part2(self) -> int:
        pass
                        
