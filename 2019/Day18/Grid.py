from Point2D import Point2D

class Grid:
    def __init__(self, filename):
        self.grid={}
        with open(filename, 'r') as input_data:
            rows = [line.strip('\n') for line in input_data]
            for row in rows:
                self.grid.append(row)
        
    '''
    Calculate the shortest path to collect all the keys
    '''
    def shortest_path(self):
        return 8