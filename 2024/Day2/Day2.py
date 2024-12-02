
''' 
David Hanley, December 2024
'''
import re
from copy import copy

class Day2:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.reports: list[list[int]] = list()
        all_reports: list[list[str]] = [re.findall(r'\d+',line) for line in lines]
        for report in all_reports:
            self.reports.append([int(num) for num in report])
    
    def safe(self, report) -> bool:
        if len(report) > 1:
            decreasing = report[0] > report[1]
            for index in range(0,len(report)-1):
                diff = report[index] - report[index+1]
                if decreasing: 
                    if (diff < 1 or diff > 3):
                        return False
                else:
                    if (diff < -3 or diff > -1):
                        return False         
        return True      
    
    def part1(self) -> int:
        safe_count: int = 0
        for report in self.reports:
            safe_count = safe_count + 1 if self.safe(report) else safe_count
        return safe_count
                        

    def part2(self) -> int:
        safe_count: int = 0
        for report in self.reports:
            if self.safe(report):
                safe_count += 1
            else:
                # remove each level, one at a time and check if now safe
                # if so, increment safe_count and move to next report
                for level_to_remove in range(0,len(report)):
                    if level_to_remove < len(report):
                        next_report: list[int] = report[0:level_to_remove] + report[level_to_remove+1:]    
                    else:
                        next_report: list[int] = report[-1]
                    if self.safe(next_report):
                        safe_count += 1
                        break
        return safe_count
                        
