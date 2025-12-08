from dataclasses import dataclass, field
from itertools import combinations
from math import sqrt
from collections import deque
from functools import reduce

@dataclass
class Point3D:
    point_str:str=field(kw_only=True,repr=False,hash=False,compare=False)
    x: int=field(init=False)
    y: int=field(init=False)
    z:int=field(init=False)
    
    def __add__(self, p: Point3D):
        return Point3D(self.x + p.x, self.y + p.y, self.z + p.z)
    
    def __eq__(self, p: Point3D) -> bool:
        return self.x == p.x and self.y == p.y and self.z == p.z
    
    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def distance(self, p: Point3D) -> int:
        return sqrt(pow(self.x-p.x,2) + pow(self.y-p.y,2) + pow(self.z-p.z,2))
    
    def __post_init__(self):
        self.x, self.y, self.z = map(lambda p: int(p), self.point_str.split(','))
        
class Day8:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            self._boxes = [Point3D(point_str=line.strip('\n')) for line in input_file]
        
         
    def _visited_nodes(self, node: Point3D, graph: dict[Point3D, list[Point3D]]) -> set[Point3D]:
        nodes_visited: set[Point3D] = set()
        stack: deque = deque()
        stack.appendleft(node)
        while len(stack) > 0:
            curr_node = stack.popleft()
            nodes_visited.add(curr_node)
            edges = graph[curr_node]
            for n in edges:
                if n not in nodes_visited:
                    stack.appendleft(n)
        return nodes_visited
        
    def parts1and2(self, pairs: int) -> tuple[int, int]:
        # junction boxes are a graph where- initally edgeless    
        graph: dict[Point3D, list[Point3D]] = {p: [] for p in self._boxes}
        
        # get all combinations of juncton boxes sorted in descending order of distance between them
        box_combinations = list(sorted(combinations(self._boxes,2), key=lambda c: c[0].distance(c[1])))
        
        pair_counter: int = 0
        
        # populate graph
        for perm in box_combinations:
            pair_counter += 1
            graph[perm[0]].append(perm[1])
            graph[perm[1]].append(perm[0])
        
            # part 1
            if pair_counter == pairs:
        
                # calculate number of nodes in each subgraph
                num_nodes: list[int] = list()
                possible_nodes = {n for n in graph.keys()}
                while len(possible_nodes) > 0:
                    nodes = self._visited_nodes(possible_nodes.pop(),graph)
                    num_nodes.append(len(nodes))
                    possible_nodes = possible_nodes.difference(nodes)
        
                # multiply lengths of three longest subgraphs
                part1: int = reduce(lambda x, y: x * y, list(sorted(num_nodes,reverse=True))[0:3], 1)
            
            # part2
            # graph is connected when every node has at least one edge
            if len(list(filter(lambda v: len(v) == 0, graph.values()))) == 0:
                part2: int = perm[0].x * perm[1].x
                break
        
        return part1, part2
            
    
    