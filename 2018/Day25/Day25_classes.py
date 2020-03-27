class Point4D():
    def __init__(self, line):
        parts = line.split(',')
        self.x = int(parts[0])
        self.y = int(parts[1])
        self.z = int(parts[2])
        self.a = int(parts[3])

    def manhattan_distance(self, p):
        return abs(p.x-self.x) + abs(p.y-self.y) + abs(p.z-self.z) + abs(p.a-self.a)

    def __str__(self):
        return f'({self.x},{self.y},{self.z},{self.a})' 

    def __eq__(self,p):
        return p.x == self.x and p.y == self.y and p.z == self.z and p.a == self.a

class Sky():
    def __init__(self,filename):
        with open(filename, 'r') as in_file:
            self.stars = [Point4D(line.strip('\n')) for line in in_file]
                
    def constellations(self):
        '''
        Calculate the number of constellations in the sky
        Take a point and goto every point that is within 3 
        Recurse until you can't go to anymore - that's a single constellationm
        Find next point with no edges and continue
        Continue until no points left unvisited
        '''
        constellations = 0
        visited = [] 
        while len(visited) < len(self.stars):
            for star in self.stars:
                 if star not in visited:
                    visited.append(star)
                    self.__constellation(star, visited)
                    constellations += 1
        return constellations
    
    def __constellation(self, start_star, visited):
        for star in self.stars:
            if star not in visited and start_star.manhattan_distance(star) <= 3:
                visited.append(star)
                self.__constellation(star, visited)
