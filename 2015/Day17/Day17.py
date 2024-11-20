'''
David Hanley, November 2024
'''
from itertools import combinations

class Day17:
    def __init__(self,file_name:str,qty: int) -> None:
        self.qty = qty
        with open(file_name, 'r') as input_file:
            self.containers = [int(line.strip('\n')) for line in input_file]
            
    def solution(self) -> int:
        containers_distr: dict[int, int] = {}
        count: int = 0
        for i in range(0, len(self.containers)):
            for p in combinations(self.containers, i):
                if sum(p) == self.qty:
                    count += 1
                    if containers_distr.get(i) is None:
                        containers_distr[i] = 1
                    else:
                        containers_distr[i] += 1
                        
        return (count, min(containers_distr.items(),key=lambda i: i[0])[1])
                        
