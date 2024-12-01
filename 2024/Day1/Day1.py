
''' 
David Hanley, December 2024
'''
import re

class Day1:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            
        num_pairs: list[tuple[str,str]] = [re.findall(r'\d+',line) for line in lines]
        self.col1: list[int] = sorted([int(num[0]) for num in num_pairs])
        self.col2: list[int] = sorted([int(num[1]) for num in num_pairs])
            
    def part1(self) -> int:
        pairs = zip(self.col1,self.col2)
        distance = 0
        for pair in pairs:
            distance += abs(pair[0] - pair[1])
        return distance

    def part2(self) -> int:
        sim_score = 0
        for num in self.col1:
            sim_score += num * len(list(filter(lambda c2: c2 == num, self.col2)))
        return sim_score             
