from dataclasses import dataclass
import re

@dataclass
class Node:
    left: str
    right: str

class Network:
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            self.directions,nodes = input_file.read().split('\n\n')
        
        self.num_directions = len(self.directions)
        self.nodes: dict[Node] = {}
        for n in nodes.split('\n'):
            node_parts = re.findall(r'[A-Z][A-Z][A-Z]', n)
            self.nodes[node_parts[0]] = Node(node_parts[1], node_parts[2])


    def steps(self) -> int:
        curr_node = 'AAA'
        steps = 0
        while curr_node != 'ZZZ':
            curr_direction = self.directions[steps % self.num_directions]
            if curr_direction == 'R':
                curr_node = self.nodes[curr_node].right  
            else:
                curr_node = self.nodes[curr_node].left
            steps += 1
        return steps