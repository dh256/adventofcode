'''
David Hanley, November 2024
'''
import re

class Day16:
    things: list[str] = [
        "children",
        "cats",
        "samoyeds",
        "pomeranians",
        "akitas",
        "vizslas",
        "goldfish",
        "trees",
        "cars",
        "perfumes"
        ]

    gift: dict = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1
        }

    
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self.sues: list[dict] = list()
        for line in lines:
            curr_sue: dict = dict()
            for thing in Day16.things:
                thing_match = re.search(rf'{thing}: (\d+)',line)
                if thing_match:
                    curr_sue[thing] = int(thing_match.group(1))
            self.sues.append(curr_sue)     
                    
    def solution(self, part: int) -> int:
            for sue_num, sue in enumerate(self.sues, start=1):
                for thing, thing_num in sue.items():
                    if part == 2 and thing in ('cats','trees'):
                        if Day16.gift[thing] >= thing_num:
                            break
                    elif part == 2 and thing in ('pomeranians','goldfish'):
                        if Day16.gift[thing] <= thing_num:
                            break
                    else: 
                        if Day16.gift[thing] != thing_num:
                            break
                else:
                    return sue_num

                        
