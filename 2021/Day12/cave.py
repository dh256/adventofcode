from graph import SimpleGraph

class Cave:
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.graph = SimpleGraph()
            self.map = [line.strip('\n') for line in input_file]
            for m in self.map:
                vertices = m.split('-')
                self.graph.add_edge(vertices[0],vertices[1])

    def calc_num_paths(self):
        # traverse all paths and return number that reached end
        self.graph.all_paths()
        return len(self.graph.paths)

    def calc_num_paths2(self):
        # traverse all paths and return number that reached end
        all_paths = []
        self.graph.all_paths()
        all_paths.extend(self.graph.paths)
        for v in self.graph.vertices.keys():
            if v not in ('start','end') and v.islower():    
                self.graph.all_paths(visit_twice=v)
                all_paths.extend(self.graph.paths)

        # de-dupe
        return len({','.join(ap) for ap in all_paths})
        


