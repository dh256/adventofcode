class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self, value):
        '''
        Returns Manhattan distance between 2 points
        '''
        return abs(self.x - value.x) + abs(self.y - value.y)

    def __eq__(self, value):
        return self.x == value.x and self.y == value.y

    def __hash__(self):
        return hash((self.x,self.y))

    def __repr__(self):
        return f'({self.x},{self.y})'
