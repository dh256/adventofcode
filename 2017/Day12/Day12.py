import re
from collections import deque

class Day12:

    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            nodes = [re.findall('[\\d]+', line.strip('\n')) for line in input_file]
            self._graph: dict[int, set[int]] = {int(node[0]): list(map(lambda n: int(n),node[1:])) for node in nodes}
    
    def part1(self) -> int:
        '''
        Do a full traversal of all nodes that can be reached from node 0
        '''
        nodes = self.nodes_in_group(0)
        return len(nodes)

    def part2(self) -> int:
        '''
        Start at lowest node in all nodes (0), find the nodes that can be visited from this node
        Remove visited nodes from all nodes and repeat until no nodes left in all nodes
        Number of groups is number of repitions
        '''
        all_nodes: set[int] = set(self._graph.keys())
        groups: int = 0
        while len(all_nodes) > 0:
            group_nodes: set[int] = self.nodes_in_group(min(all_nodes))
            all_nodes = all_nodes - group_nodes
            groups += 1
        return groups
            
    def nodes_in_group(self, start_node: int) -> set[int]:
        '''
        Find and return all nodes that can be visited from start_node
        Use Depth First Search (Stack)
        '''
        visited: set[int] = set()
        q = deque()
        q.appendleft(start_node)
        while len(q) > 0:
            curr_node: int = q.popleft()
            for e in self._graph[curr_node]:
                if not e in visited:
                    visited.add(e)
                    q.appendleft(e)
        return visited