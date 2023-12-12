import re
from dataclasses import dataclass, field
import itertools

@dataclass
class Record:
    org_springs: str
    damage_report: list[int]
    curr_springs: str = field(init=False)

    def __post_init__(self)->None:
        self.curr_springs = [s for s in self.org_springs]

    def is_compliant(self) -> bool:
        result = True
        matches = list(re.finditer(r'#+', ''.join(self.curr_springs)))
        if len(matches) == len(self.damage_report):
            for i, m in enumerate(matches):
                if len(m.group()) != self.damage_report[i]:
                    result = False
        else:
            result = False
        
        return result

    def combinations(self) -> int:
        '''
        Calculates number of possible combinations of springs
        '''
        
        '''
        Replace each ? with either a . or a # and determine whether it is compliant (meets damage report) 
        '''
        result = 0
        q_mark_indexes = [e[0] for e in enumerate(self.org_springs) if e[1] == '?']
        for s in itertools.product("#.", repeat=len(q_mark_indexes)):
            for i, c in enumerate(s):
                self.curr_springs[q_mark_indexes[i]] = c
            # check if curr_springs compliant
            if self.is_compliant():
                result += 1
        return result

class Springs:
    def __init__(self,file_name):
        self.records: list[Record] = []
        with open(file_name,'r') as input_file:
            for line in input_file:
                line_parts = line.strip().split()
                springs = [*line_parts[0]]
                damage_report = [int(num) for num in re.findall(r'\d+',line_parts[1])]
                self.records.append(Record(springs, damage_report))
            
    def condition_count_sum(self) -> int:
        #self.records[0].combinations()
        return sum([record.combinations() for record in self.records])
