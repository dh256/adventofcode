
''' 
David Hanley, December 2024
'''
import re

class Day3:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self.lines: list[str] = [line.strip('\n') for line in input_file]
                    
    def part1(self) -> int:
        result: int = 0
        regex = re.compile('mul\((\d+),(\d+)\)')
        for line in self.lines:
            result += sum([int(match[0]) * int(match[1]) for match in regex.findall(line)])
        return result

    def part2(self) -> int:
        result: int = 0
        regex = re.compile(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))")
        do: bool = True
        for line in self.lines:
            for match in re.findall(r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))", line):
                if match[3]:
                    do = False
                    continue
                
                if match[2]:
                    do = True
                    continue
                
                if do:
                    result += int(match[0]) * int(match[1])
        
        return result
                     


