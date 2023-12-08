from dataclasses import dataclass
import re
import math

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
            node_parts = re.findall(r'[\w\d]+', n)
            self.nodes[node_parts[0]] = Node(node_parts[1], node_parts[2])

    def steps(self,curr_node: str,end_func: callable) -> int:
        steps = 0
        while not end_func(curr_node):
            curr_direction = self.directions[steps % self.num_directions]
            if curr_direction == 'R':
                curr_node = self.nodes[curr_node].right  
            else:
                curr_node = self.nodes[curr_node].left
            steps += 1
        return steps
    
    def part_one(self) -> int:
        return self.steps('AAA', lambda x: x == 'ZZZ')

    def part_two(self) -> int:
        # start_nodes find all nodes ending in A
        curr_nodes = list(filter(lambda k: k[-1] == 'A', self.nodes.keys()))
        
        # work out number of steps for each node to get to its end node
        steps_list = []
        for curr_node in curr_nodes:
            steps_list.append(self.steps(curr_node, lambda x: x[-1] == 'Z'))
        
        # LCM (not product) is the minimum number of steps needed
        return math.lcm(*steps_list)
    