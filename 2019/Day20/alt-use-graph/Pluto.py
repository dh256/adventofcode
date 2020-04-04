from Graph import SimpleGraph
import uuid

class Pluto:
    def __init__(self,filename):
        self.graph = SimpleGraph()
        self.added_ids = []
        self.start_vertex = None    # holds id of start node (AA)
        self.end_vertex = None      # holds id of end node (ZZ)
        with open(filename,"r") as file_input:
            '''
            Add any . to graph as a vertex
            Vertices are labelled with a guid unless its a teleport node
            A teleport node is any node along the edge of grid or internal "hole"
            Telport vertices have alt_label set to with the associated label 
            '''
            self.rows = [line.strip('\n') for line in file_input]
            
            # get grid edges
            self.first_col = 2
            self.first_row = 2
            self.last_col = len(max(self.rows, key=len))-3
            self.last_row = len(self.rows)-3

            # get doughnut edges
            y=0
            edge_found = False
            for row in self.rows:
                if y in range(self.first_row,self.last_row):
                    if " " in row[self.first_col:self.last_col+1] and not edge_found:
                        edge_found = True
                        self.doughnut_first_row = y
                        self.doughnut_first_col = row.find(' ',self.first_col)   # find position of first space    
                        self.doughnut_last_col = row.rfind(' ',self.doughnut_first_col,self.last_col+1)    # find position of last space
                    elif " " not in row[self.first_col:self.last_col] and edge_found:
                        self.doughnut_last_row = y-1
                        break
                y += 1
            
            # build graph
            print('Building graph ...')
            for y in range(self.first_row,self.last_row+1):
                for x in range (self.first_col,self.last_col+1):
                    vertex = self._add_vertex(x,y)        
                    if not vertex is None:
                        self._add_neighbours(x,y,vertex)

            # add egdes between teleport nodes
            self._add_teleport_edges()
            print('Graph built')


    '''
    Is point on edge of grid
    '''
    def _on_grid_edge(self,x,y):
        return y == self.first_row or y == self.last_row or x == self.first_col or x == self.last_col

    ''' 
    is point on edge of doughnut
    '''
    def _on_doughnut_edge(self,x,y):
        if y == self.doughnut_first_row-1 or y == self.doughnut_last_row + 1:
            return x in range(self.doughnut_first_col-1,self.doughnut_last_col+2)    
        elif y in range(self.doughnut_first_row, self.doughnut_last_row+1):
            return x == self.doughnut_first_col - 1 or x == self.doughnut_last_col + 1
        else:
            return False

    def _add_teleport_edges(self):
        # teleport vertices all those with an alt_label
        teleport_vertices = list(filter(lambda e : not e[1].alt_label is None, self.graph.vertices.items()))
        for v in teleport_vertices:
            if not v[1].alt_label in ('AA','ZZ'):  # AA and ZZ are not teleports
                # find other vertex with same alt_label but different id and add edge between them
                for v2 in teleport_vertices:
                    if v[1].alt_label == v2[1].alt_label and v[0] != v2[0]:
                        self.graph.add_edge(v[0],v2[0])
                        break

    def _add_vertex(self,x,y):
        if self.rows[y][x] == '.':    # a node
            # is a teleport vertex if on edge of grid or doughnut
            # if so get label
            # add vertex to graph
            id = (x,y)
            label = None
            if self._on_grid_edge(x,y):
                if y == self.first_row:
                    label = f'{self.rows[y-2][x]}{self.rows[y-1][x]}'
                elif x == self.first_col:
                    label = f'{self.rows[y][x-2]}{self.rows[y][x-1]}'
                elif y == self.last_row:
                    label = f'{self.rows[y+1][x]}{self.rows[y+2][x]}'
                elif x == self.last_col:
                    label = f'{self.rows[y][x+1]}{self.rows[y][x+2]}'
            elif self._on_doughnut_edge(x,y):
                if y == self.doughnut_first_row - 1:
                    label = f'{self.rows[y+1][x]}{self.rows[y+2][x]}'
                elif x == self.doughnut_first_col - 1:
                    label = f'{self.rows[y][x+1]}{self.rows[y][x+2]}'
                elif y == self.doughnut_last_row + 1:
                    label = f'{self.rows[y-2][x]}{self.rows[y-1][x]}'
                elif x == self.doughnut_last_col + 1:
                    label = f'{self.rows[y][x-2]}{self.rows[y][x-1]}'
            
            self._add_graph_vertex(id,label)    # add vertex   
            return id     
        else:
            return None
    
    def _add_graph_vertex(self,id,alt_label):
        if not id in self.added_ids:
            self.added_ids.append(id)
            self.graph.add_vertex(id,alt_label)
            if alt_label == 'AA':
                self.start_vertex = id
            if alt_label == 'ZZ':
                self.end_vertex = id

    def _add_edge(self,x,y,source):
        dest_vertex = self._add_vertex(x,y)
        if not dest_vertex is None:
            self.graph.add_edge(source,dest_vertex)

    def _add_neighbours(self,x,y,source):
        '''
        Look up, down, left, right for possible neighbouring vertices
        '''
        self._add_edge(x,y-1,source)
        self._add_edge(x,y+1,source)
        self._add_edge(x-1,y,source)
        self._add_edge(x+1,y,source)
        
    def find_shortest_distance(self):
        print('Calculating shortest distance ...')
        return self.graph.shortest_distance(self.start_vertex,self.end_vertex)

    def __repr__(self):
        out_str = ""
        for row in self.rows:
            for c in row:
                out_str += c
            out_str += '\n'
        return out_str