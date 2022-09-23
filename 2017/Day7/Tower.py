from dataclasses import dataclass, field
import re
from collections import Counter

@dataclass
class Node:
    id: str
    weight: int                                         # weight
    weight_sum: int = 0                                 # weight_sum
    parent: str = None                                  # id of parent node 
    children: list[str] = field(default_factory=list)   # ids of child nodes

    def __eq__(self, __o: object) -> bool:
        __o.id == self.id
    
class Tower:
    def __init__(self, filename) -> None:
        self._nodes = list()
        with open(filename, 'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        # process input
        for line in lines:
            matches=re.findall(r'\w{1,}',line)
            node_id = matches[0]
            weight = int(matches[1])
            children = []
            for idx in range(2,len(matches)):
                children.append(matches[idx])
            self._nodes.append(Node(node_id,weight,children=children))

        # get parents
        for node in self._nodes:
            f = list(filter(lambda n: node.id in n.children, self._nodes))
            if len(f) > 0:
                node.parent = f[0].id

        # calc node weights
        # start with all the children i.e. nodes that have no children
        self.root.weight_sum = self.children_weight(self.root)

         
    def children_weight(self, node: Node) -> int:
        weight_sum = 0
        if len(node.children) == 0:
            node.weight_sum = node.weight
        else:
            for c in node.children:
                curr_node = self.find(c)
                weight_sum += self.children_weight(curr_node)
            node.weight_sum = weight_sum + node.weight
        return node.weight_sum
                
    
    @property
    def root(self) -> str:
        # find node with no parent and return node
        return list(filter(lambda n: n.parent is None, self._nodes))[0]

    def find(self, node_id: str) -> Node:
        return list(filter(lambda n: n.id == node_id, self._nodes))[0]

    def correct_weight_to_balance(self):
        curr_node = self.root
        while True:
            cb = self.children_balanced(curr_node)
            if cb[0]:                   # children_balanced, then parent needs to be balanced
                return curr_node.weight - correction
            else:
                ''' 
                children not balanced and unbalanced node returned 
                now check unbalanced nodes children
                '''
                correction = cb[1]
                curr_node = cb[2]

            
    def children_balanced(self, node: Node) -> bool:
        child_weights = Counter()
        child_nodes = [self.find(c) for c in node.children]
        for n in child_nodes:
            child_weights[n.weight_sum] += 1
        
        if len(child_weights) == 1:
            return (True,None)
        elif len(child_weights) == 2:
            mc = child_weights.most_common(2)
            unbalanced_weight = mc[1][0]
            balanced_weight = mc[0][0]
            unbalanced_node = list(filter(lambda i: i.weight_sum == unbalanced_weight, child_nodes))[0]
            correction = unbalanced_weight - balanced_weight
            return (False, correction, unbalanced_node)
        else:
            print('Program failure .. only 1 node can have an incorrecy weight exiting ...')
            exit(-1)