
''' 
David Hanley, December 2024
'''
import re
from itertools import product

class Day7:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # get equations, for each equation first member of list is test value 
        # and remaining members are the numbers to combine with operators
        num_re = re.compile(r'\d+')
        self.equations: list[list[int]] = list()
        for line in lines:
            self.equations.append([int(n) for n in num_re.findall(line)])

    def equation_solvable(self, equation: list[int], operator_combination: str) -> bool:
        '''
        Determines whether an equation can be solved.
        Can be solved if after combing all numbers (equation[1:]) with supplied operator combination, get a result 
        equal to equation[0].
        '''
        calculation = equation[1]
        for i in range(0,len(operator_combination)):
            op = operator_combination[i] 
            if op == '+':
                calculation = calculation + equation[i+2]
            elif op == '*':
                calculation = calculation * equation[i+2]
            elif op == '|':
                calculation = int(f'{calculation}' + f'{equation[i+2]}')
        return calculation == equation[0]
    
    def solution(self) -> tuple[int, int]:
        '''
        Calculates solution for Parts 1 and 2
        For Part 1: 
            - Work out all possible combination of operators *+ for equation numbers
            - For each operator combination determine if it solves equation. 
            - If equation can be solved, record index of equation (do not want to consider these in Part 2) and add equation result to p1_result
            
        For Part 2:
            - Similar to Part 1, except:
                - p2_result initialised to p1_result
                - Only consider equations not solvable in Part 1
                - Add an addtional operator and work out possible combinations of *+| for equation numbers
                - If equation can be solved add equation result to p2_result
                
        Return p1_result and p2_result
        '''
        p1_equations: list[int] = list()
        for part in [1,2]:
            if part == 1:
                p1_result: int = 0
                operators: str = '*+'
                equation_source: list[list[int]] = self.equations
            else: 
                p2_result = p1_result
                operators = '*+|'
                equation_source = [e for i,e in enumerate(self.equations) if i not in p1_equations]
            
            for equation_index, equation in enumerate(equation_source):
                operator_combinations: tuple[str] = product(operators,repeat=len(equation)-2)
                for operator_combination in operator_combinations:
                    if part == 1 or (part == 2 and '|' in operator_combination):
                        if self.equation_solvable(equation,operator_combination):
                            if part == 1:
                                p1_equations.append(equation_index)
                                p1_result += equation[0]
                                break
                            else:
                                p2_result += equation[0]
        
        return (p1_result,p2_result)