from dataclasses import dataclass
from itertools import combinations
from scipy.optimize import linprog

@dataclass
class Machine:
    indicator_lights: list[bool]
    button_presses: list[tuple[int]]
    joltages: tuple[int]
     

class Day10:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        self._manual: list[Machine] = list()
        for line in lines:    
            parts: list[str] = line.split(' ')
            indicator_lights: list[bool] = list(map(lambda l: l == '#',parts[0][1:-1]))
            button_presses: list[tuple[int]] = list()
            for buttons in parts[1:-1]:
                 button_presses.append(tuple(map(lambda b: int(b),buttons[1:-1].split(','))))
            joltages: tuple[int]=tuple(map(lambda j: int(j), parts[-1][1:-1].split(',')))
            self._manual.append(Machine(indicator_lights,button_presses,joltages))
    
    def _min_presses(self, machine: Machine) -> int:
        for num_combs in range(len(machine.button_presses)+1):
            for presses in combinations(machine.button_presses,num_combs):
                lights: list[bool] = [False] * len(machine.indicator_lights)
                for press in presses:
                    for button in press:
                        lights[button] = not lights[button]
                
                # if lights match indicator lights - done
                if lights == machine.indicator_lights:
                    return num_combs
           
    def part1(self) -> int:
        result: int = 0
        for machine in self._manual:
            result += self._min_presses(machine)
        return result

    def part2(self) -> int:
        '''
        Took a hint from reddit for this
        Uses scipy linear programming to solve a system of linear equations
        '''
        result: float = 0
        for machine in self._manual:
            costs = [1 for b in machine.button_presses] 
            eqs = [[i in b for b in machine.button_presses] for i in range(len(machine.joltages))]
            result += linprog(costs, A_eq=eqs, b_eq=machine.joltages, integrality=1).fun
        return int(result)                       
