'''
For Part 2 knew I had to use modulo to stop worry levels getting too high but wasn't sure how to calculate it
Used a hint from here: https://www.youtube.com/watch?v=W9vVJ8gDxj4
Other than that all code is my own
'''
from dataclasses import dataclass, field
import re
import math

@dataclass
class Monkey:
    '''
    Holds monkey details
    '''
    desc: list[str] = field(kw_only=True)
    items: list[int]= field(init=False)
    op: str = field(init=False)
    test_divisor: int = field(init=False)
    throw_to_false: int = field(init=False)
    throw_to_true: int = field(init=False)

    def __post_init__(self):
        '''
        Set monkey properties using the info passed in monkey desc
        '''
        int_regex = re.compile(r'\d+')

        self.items = [int(i) for i in int_regex.findall(self.desc[0])]
        self.op = self.desc[1][len('  Operation: new = '):]
        self.test_divisor = [int(i) for i in int_regex.findall(self.desc[2])][0]
        self.throw_to_true = [int(i) for i in int_regex.findall(self.desc[3])][0]
        self.throw_to_false = [int(i) for i in int_regex.findall(self.desc[4])][0]


class Monkeys:
    '''
    Collection of monkeys and associate methods 
    '''
    def __init__(self,file_name):
        self.monkeys = dict()
        with open(file_name, 'r') as input_file:
            for line in input_file:
                line = line.strip('\n')
                if line.startswith('Monkey'):
                    # set next monkey and start a new monkey desc
                    next_monkey_id = int(line[len('Monkey: ')-1:-1])
                    monkey_desc = []
                elif len(line) == 0:
                    self.monkeys[next_monkey_id] = Monkey(desc=monkey_desc)
                else:
                    monkey_desc.append(line)
            
            # add last monkey
            self.monkeys[next_monkey_id] = Monkey(desc=monkey_desc)

        # calculate lcm of all the divisors - needed for Part 2
        self.lcm = 1
        for monkey in self.monkeys.values():
            self.lcm *= (self.lcm*monkey.test_divisor)//math.gcd(self.lcm,monkey.test_divisor)

    def perform_round(self,monkey_inspections,part: int) -> None:
        '''
        Performs round using either part 1 or part 
        '''
        for curr_monkey_id, curr_monkey in self.monkeys.items():
            old_worry_levels = [i for i in curr_monkey.items]
            for old in old_worry_levels:
                new_worry_level = eval(curr_monkey.op)
                if part == 1:
                    # Part 1
                    new_worry_level = new_worry_level // 3
                else:
                    # Part 2
                    new_worry_level = new_worry_level % self.lcm

                if new_worry_level % curr_monkey.test_divisor == 0:
                    self.monkeys[curr_monkey.throw_to_true].items.append(new_worry_level)
                else:
                    self.monkeys[curr_monkey.throw_to_false].items.append(new_worry_level)
                
                # remove old worry level from current monkey
                self.monkeys[curr_monkey_id].items.remove(old) 
                monkey_inspections[curr_monkey_id] += 1
    
    def calc_monkey_business(self, rounds: int, part: int) -> int:
        '''
        Performs a number of rounds using eithee Part 1 or Part 2 rules
        Returns product of two highest number of inspections carried out by monkeys
        '''
        monkey_inspections = {i: 0 for i in self.monkeys.keys()}
        
        # perform rounds
        for r in range(0,rounds):
            self.perform_round(monkey_inspections,part)

        # calculate and return result
        results = sorted(monkey_inspections.values(), key=lambda v: v, reverse=True)
        return results[0] * results[1]