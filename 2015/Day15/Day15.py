'''
David Hanley, November 2024
'''
from dataclasses import dataclass
import re
from itertools import product

@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavour: int
    texture: int
    calories: int
    

class Day15:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            recipe_lines: list[str] = [line.strip('\n') for line in input_file]
        
        self.ingredients: list[Ingredient] = list()
        find_words: re.Pattern = re.compile(r'\w+')
        find_nums: re.Pattern = re.compile(r'-?\d+')
        for recipe_line in recipe_lines:
            name:str = find_words.match(recipe_line).group(0)
            quantities: list[str] = find_nums.findall(recipe_line)
            capacity:int = int(quantities[0])
            durability:int = int(quantities[1])
            flavour:int = int(quantities[2])
            texture:int = int(quantities[3])
            calories:int = int(quantities[4])
            self.ingredients.append(Ingredient(name,capacity,durability, flavour, texture, calories))
            
    def solution(self) -> tuple[int,int]:
        result_part1: int = 0
        result_part2: int = 0
        for c in product(range(0,101),repeat=len(self.ingredients)):
            if sum(c) == 100:                   # only interested in those that add up to exactly 100
                capacity: int = 0 
                durability: int = 0
                flavour: int = 0
                texture: int = 0
                calories: int = 0
                for i in range(0,len(self.ingredients)):
                    capacity += self.ingredients[i].capacity * c[i]
                    durability += self.ingredients[i].durability * c[i]
                    flavour += self.ingredients[i].flavour * c[i]
                    texture += self.ingredients[i].texture * c[i]
                    calories += self.ingredients[i].calories * c[i]
                
                new_result: int = (capacity if capacity >= 0 else 0) * (durability if durability >= 0 else 0) * (flavour if flavour >= 0 else 0) * (texture if texture >= 0 else 0)
                result_part1 = new_result if new_result > result_part1 else result_part1
                result_part2 = new_result if calories == 500 and new_result > result_part2 else result_part2
              
        return (result_part1, result_part2)      
                
                        
