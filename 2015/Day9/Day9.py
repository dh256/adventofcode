'''
David Hanley, November 2024
'''
import re
from dataclasses import dataclass 
from collections import deque

@dataclass
class Edge:
    dest: int
    distance: int
    
    def __hash__(self) -> int:
        return hash((self.dest, self.distance))

class Day9:
    def __init__(self, filename: str) -> None: 
        self._nodes: dict[str, set[Edge]] = dict()
        reg_ex = re.compile(r'([A-Z][A-Za-z]+)|(\d+)')
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
        
        for line in lines:
            matches = reg_ex.finditer(line)
            values = []
            for m in matches:
                values.append(m.group())
            
            # from -> to
            try:
                self._nodes[values[0]].add(Edge(values[1],int(values[2]))) 
            except KeyError:
                self._nodes[values[0]] = {Edge(values[1],int(values[2]))}  

            # to -> from
            try:
                self._nodes[values[1]].add(Edge(values[0],int(values[2]))) 
            except KeyError:
                self._nodes[values[1]] = {Edge(values[0],int(values[2]))}  
        
    def _path_length(self, longest: bool = True) -> int:
        # shortest or longest path to visit all nodes:
        # must start and end at different locations
        # must visit a location exactly once  
        # BFS, maintaining accumulated distance and path. Any path that contains all nodes becomes a candidate path.
        all_paths: dict[str, int] = dict()
        for node in self._nodes.keys():
            candidate_path_lengths: list[int] = list()
            q: deque[tuple[str,int,list[str]]] = deque()
            q.append((node,0,[node]))
            while q:
                curr_node, curr_dist, curr_path = q.popleft()
                for e in self._nodes[curr_node]:
                    if e.dest not in curr_path:
                        new_path = curr_path + [e.dest]
                        new_dist = curr_dist+e.distance
                        if len(new_path) == len(self._nodes):
                            # all nodes visited once - potential path - done
                            candidate_path_lengths.append(new_dist)
                        else:
                            # add next node to Q for processing
                            q.append((e.dest,new_dist,new_path))
            
            all_paths[node] = sorted(candidate_path_lengths,reverse=longest)[0]
            
        return sorted(all_paths.values(), key=lambda v: v, reverse=longest)[0]
    
    def part1(self) -> int:
        return self._path_length(False)
    
    def part2(self) -> int:
        return self._path_length(True)