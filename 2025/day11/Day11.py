from collections import deque
from functools import cache

class Day11:
    def __init__(self,file_name:str) -> None:
        with open(file_name, 'r') as input_file:
            lines: str = [line.strip('\n') for line in input_file]
        
        self._graph: dict[str, list[str]] = dict()
        for line in lines:    
            parts: list[str] = line.split(' ')
            self._graph[parts[0][0:-1]] = [id for id in parts[1:]]
        self._graph["out"] = []
            
    
    def paths_dfs(self, start: str, destination: str) -> int:
        '''
        Use DFS to find all possible paths between start and destination nodes
        
        Note:
        Only worked for Part 1; too many paths for Part 2. 
        Needed to use a recursive approach with memoisation
        See "paths" function
        '''
        paths: int = 0
        stack: deque[str] = deque()
        stack.appendleft(start)
        while len(stack) > 0:
            curr_node = stack.popleft()
            for edge in self._graph[curr_node]:
                if edge == destination:
                    paths += 1
                else:
                    stack.appendleft(edge)
        return paths        
                
    @cache
    def num_paths(self, start: str, destination: str) -> int:
        # if destination is connected to start, path found
        if destination in self._graph[start]:
            return 1 
        else:
            # otherwise find num paths from all nodes connected to start to destination 
            path_count: int = 0
            
            # recurse - count paths from all connected nodes to destination
            for edge in self._graph[start]:    
                path_count += self.num_paths(edge,destination)
            return path_count

    def part1(self) -> int:
        #return self.paths_dfs("you","out")
        return self.num_paths("you","out")
    
    def part2(self) -> int:
        # only need to count paths
        paths_svr_to_fft = self.num_paths("svr", "fft")
        paths_fft_to_dac = self.num_paths("fft", "dac")
        paths_dac_to_out = self.num_paths("dac", "out")
        
        paths_svr_to_dac = self.num_paths("svr", "dac")
        paths_dac_to_fft = self.num_paths("dac", "fft")
        paths_fft_to_out = self.num_paths("fft", "out")
                
        # return paths found          
        return (paths_svr_to_fft * paths_fft_to_dac * paths_dac_to_out) + (paths_svr_to_dac * paths_dac_to_fft * paths_fft_to_out)
                        
