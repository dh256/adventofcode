import math

class Vertex:
    def __init__(self,id,alt_label=None):
        self.id = id
        self.alt_label = alt_label
        self.edges = {}

class DijkstraRecord:
    def __init__(self):
        self.distance_from_source = math.inf
        self.adjacent_vertex = None

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

    def _create_dijkstra_table(self,source_vertex):
        '''
        Dijkstra's algorithm involves calculating the minimum distance of all vertices in graph (and closest adjacent vertex) from source_vertex
        See: https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e for full details
        '''
        
        ''''
        Create initial table
        Initially contains an entry for every vertex in graph; 
        distance from source is initially infinite except source itself which is zero
        adjancenet_vertex initially None

        Need a visited and unvisted list to track vertices already visited and not visited
        Initally visited is empty and unvisited is all vertices in graph
        '''
        if self.shortest_path_source != source_vertex:   # only generate table if not already done
            self.shortest_path_source = source_vertex
            unvisited = []
            visited = []
            self.shortest_path_table = {}
            for v in self.vertices.keys():
                self.shortest_path_table[v] = DijkstraRecord()
                unvisited.append(v)
            self.shortest_path_table[source_vertex].distance_from_source = 0

            '''
            Populate table:
            Find unvisited vertex closest to source
            For each edged in this vertex:
                check not already visited (prevents going back in undirected graph)
                distance from source is the distance of closest node from source + weight of edge
                If this new distance is less than current distance from source of vertex, update distance and adjacent vertex
            Update visited and unvisited lists 
            Continue until next_vertex is None (i.e. all nodes visited)
            '''
            next_vertex = self._closest_vertex_unvisited(unvisited,visited)
            while next_vertex[0] is not None:
                for dest,weight in self.vertices[next_vertex[0]].edges.items():
                    if dest not in visited:
                        distance = next_vertex[1] + weight
                        if distance < self.shortest_path_table[dest].distance_from_source:
                            self.shortest_path_table[dest].distance_from_source = distance
                            self.shortest_path_table[dest].adjacent_vertex = next_vertex[0]
                
                unvisited.remove(next_vertex[0])
                visited.append(next_vertex[0])
                next_vertex = self._closest_vertex_unvisited(unvisited,visited)

    def _closest_vertex_unvisited(self, unvisited, visited):
        min_dist = math.inf
        closest_vertex = None
        for vertex in unvisited:
            if vertex not in visited and self.shortest_path_table[vertex].distance_from_source < min_dist:
                min_dist = self.shortest_path_table[vertex].distance_from_source
                closest_vertex = vertex
        return(closest_vertex,min_dist)

    def shortest_distance(self,source_vertex,dest_vertex):
        '''
        Look up destination vertex in Dijkstra's table and return distance from source
        '''
        self._create_dijkstra_table(source_vertex)
        return self.shortest_path_table[dest_vertex].distance_from_source

    def shortest_path(self,source_vertex,dest_vertex):
        '''
        Return list of path - first entry 
        Work backwards through Dijkstra table going to each adjacent node until back at source
        adding each vertext to shortest path list
        Finally add source_vertext to list
        '''
        self._create_dijkstra_table(source_vertex)
        shortest_path = [dest_vertex]
        next_vertex = self.shortest_path_table[dest_vertex].adjacent_vertex
        while next_vertex != source_vertex:
            shortest_path.append(next_vertex)
            next_vertex = self.shortest_path_table[next_vertex].adjacent_vertex
        shortest_path.append[source_vertex]
        return shortest_path

    def total_min_path_distances(self,source_vertex):
        '''
        Return the total distance to all vertices in Dijkstra table
        ''' 
        self._create_dijkstra_table(source_vertex)
        distance = 0
        for vertex,dijkstra_record in self.shortest_path_table.items():
            distance += dijkstra_record.distance_from_source
        return distance