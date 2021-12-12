import math

# Based on code taken from Day 6 - 2019
class Vertex:
    def __init__(self,id,alt_label=None):
        self.id = id
        self.alt_label = alt_label
        self.edges = {}

class Edge:
    def __init__(self,dest,weight=1):
        self.dest = dest
        self.weight = weight

class SimpleGraph:
    def __init__(self,directed=False):  
        self.vertices = {}
        self.directed = directed
        self.shortest_path_source = ""
        self.shortest_path_table = ""

    def add_vertex(self,id,alt_label=None):
        '''
        Add new vertex
        '''
        if id not in self.vertices:
            self.vertices[id] = Vertex(id,alt_label)

    def add_edge(self,source,dest,weight=1):
        '''
        Add edge. If not directed also add edge in opposite direction
        '''
        if source not in self.vertices:
            self.add_vertex(source)
        
        if dest not in self.vertices:
            self.add_vertex(dest)
        
        if dest not in self.vertices[source].edges:
            self.vertices[source].edges[dest] = weight

        if not self.directed:
            if dest not in self.vertices[dest].edges:
                self.vertices[dest].edges[source] = weight
    
    def all_paths(self,next_vertex_id='start',path=None,visit_twice=None):
        # returns all paths through graph that start at start and end at end
        # vertices with a lower case can only be visited 
        if path is None:
            path = []
            self.paths = []
        
        # get each edge
        path.append(next_vertex_id)
        curr_vertex = self.vertices[next_vertex_id]
        for e in curr_vertex.edges.keys():
            if e == 'start':
                pass            # do not go back to start   
            elif e == 'end':
                final_path = path.copy()
                final_path.append('end')
                self.paths.append(final_path)
            elif e.islower():
                # if visit_twice is not specified check already in path, if so pass
                # if visit_twice is specified, check whether already appears in path twice
                if visit_twice is None: 
                    if e in path:
                        pass
                    else:
                        self.all_paths(e,path.copy(),visit_twice)
                else:
                    if e == visit_twice and len(list(filter(lambda x : x == visit_twice, path))) == 2:
                        pass
                    elif e != visit_twice and e in path:
                        pass
                    else:
                        self.all_paths(e,path.copy(),visit_twice)

            else:
                self.all_paths(e,path.copy(),visit_twice)

        return

    