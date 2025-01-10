''' 
David Hanley, December 2024
'''
from collections import defaultdict, deque

class Day23:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]

        self.network: dict[str, list[str]] = defaultdict(list)
        for line in lines:
            computer_from,computer_to = line.split('-')
            self.network[computer_from].append(computer_to)
            self.network[computer_to].append(computer_from)
            
    def part1(self) -> int:
        '''
        Start at each computer (start_computer).
        Use DFS to find all computers max_distance-1 distance from start_computer
        For each one, does computer have a link back to start computer?
            Yes - sort and add to valid_inter_connects (if not already found)
            No - ignore
        '''
        valid_inter_connects: list[list[str]] = list()
        max_distance = 3
        for start_computer in self.network.keys():
            visited: set[str] = set()
            stack: deque[tuple[str,int,list[str]]] = deque()
            stack.appendleft((start_computer,0,[start_computer]))
            while stack:
                computer, distance, computers = stack.popleft()
                if distance == max_distance - 1:
                    # candidate, check if this computer connects back to cu 
                    if start_computer in self.network[computer]:
                        computers = sorted(computers)
                        if computers not in valid_inter_connects:
                            valid_inter_connects.append(computers)   
                    continue
            
                visited.add(computer)

                for connected_computer in self.network[computer]:
                    if connected_computer not in visited:
                        stack.appendleft((connected_computer,distance+1,[*computers,connected_computer]))
        
            
        # count the inter connects containing at least one computer that begins with t 
        count_ts: int = 0
        for inter_connect in valid_inter_connects:
            for computer in inter_connect: 
                if computer[0] == 't':
                    count_ts += 1
                    break
        return count_ts
    
        

    def part2(self) -> int:
        return 0
                        
