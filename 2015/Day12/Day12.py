'''
David Hanley, Nov 2024
'''
import re
import json

class Day12:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self.json = json.load(input_file) 
        
    def part1(self) -> int:
        return self.walk_json(self.json,1)
        
    def part2(self) -> int:
        return self.walk_json(self.json,2)
        
    def walk_json(self,current_level, part: int) -> int:
        # walk JSON structure
        level_total = 0
        if type(current_level) == dict:
            level_values = [value for value in current_level.values()]
        else:
            level_values = [value for value in current_level]
        
        next_level = list(filter(lambda i: type(i) in (list, dict), level_values))
        ints = list(filter(lambda i: type(i) == int, level_values))
        strings = list(filter(lambda i: type(i) == str, level_values))
        
        walk_next_levels = True
        if part == 2:
            red_strings = list(filter(lambda i: i == 'red', strings))
            walk_next_levels = (type(current_level) == dict and len(red_strings) == 0) or (type(current_level) == list)
        
        if walk_next_levels:
            level_total += sum(ints)
            for next_l in next_level:
                level_total += self.walk_json(next_l,part)
        
        return level_total
             
                    
