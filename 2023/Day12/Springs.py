'''
Part 1 was brute forced
Did not work for Part 2 - way too many combinations
Got a hint to use recursion and cache decorator to improve performance
'''
import re
from functools import cache

class Record:
    def __init__(self, springs: str, damage_report: list[int]) -> None:
        self.springs: str = springs
        self.damage_report: list[int] = damage_report

    def unfold(self) -> None:
        '''
        Unfold original strings
        Required for Part 2
        '''
        self.springs = '?'.join([self.springs] * 5)
        self.damage_report = [*self.damage_report]*5

    @cache
    def get_count(self,pos,current_count,countpos):
        # pos is the next character to be processed
        # current_count is how far into the current sequence of #s we are in
        # countpos is how many sequences of #s we have already finished
        if pos == len(self.springs):
            ret = 1 if len(self.damage_report) == countpos else 0
        elif self.springs[pos] == '#':
            ret = self.get_count(pos + 1, current_count + 1, countpos)
        elif self.springs[pos] == '.' or countpos == len(self.damage_report):
            if countpos < len(self.damage_report) and current_count == self.damage_report[countpos]:
                ret = self.get_count(pos + 1, 0, countpos + 1)
            elif current_count == 0:
                ret = self.get_count(pos + 1, 0, countpos)
            else:
                ret = 0
        else:
            hash_count = self.get_count(pos + 1, current_count + 1, countpos)
            dot_count = 0
            if current_count == self.damage_report[countpos]:
                dot_count = self.get_count(pos + 1, 0, countpos + 1)
            elif current_count == 0:
                dot_count = self.get_count(pos + 1, 0, countpos)
            ret = hash_count + dot_count
        return ret

class Springs:
    def __init__(self,file_name):
        self.records: list[Record] = []
        with open(file_name,'r') as input_file:
            for line in input_file:
                line_parts = line.strip().split()
                springs = line_parts[0]
                damage_report = [int(num) for num in re.findall(r'\d+',line_parts[1])]
                self.records.append(Record(springs, damage_report))

   
    def condition_count_sum(self, part: int) -> int:
        result = 0
        for rec in self.records:
            if part == 2:
                rec.unfold()
            rec.springs += '.'
            result += rec.get_count(0,0,0)
        return result
