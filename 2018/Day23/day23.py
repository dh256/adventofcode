class Point3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f'({self.x},{self.y},{self.z})'
    
    def __eq__(self, p):
        return self.x == p.x and self.y == p.y and self.z == p.z

    def manhattan_distance(self,p):
        return abs(self.x - p.x) + abs(self.y - p.y) + abs(self.z - p.z)

class Manbot:
    def __init__(self, pos, sig_radius):
        self.pos = pos
        self.sig_radius = sig_radius
        self.max_x = self.pos.x + self.sig_radius 
        self.min_x = self.pos.x - self.sig_radius 
        self.max_y = self.pos.y + self.sig_radius 
        self.min_y = self.pos.y - self.sig_radius 
        self.max_z = self.pos.z + self.sig_radius 
        self.min_z = self.pos.z - self.sig_radius 
        self.intersects_with = []
    
    def __str__(self):
        return f'{self.pos},{self.sig_radius},{len(self.intersects_with)}'

    def __eq__(self, m):
        return self.pos == m.pos

    def intersects(self,m2):
        return not (self.max_x > m2.min_x and
            self.min_x < m2.min_x and
            self.max_y > m2.min_y and
            self.min_y < m2.min_y and
            self.max_z > m2.min_z and
            self.min_z < m2.min_z)

class Manbots:
    def __init__(self,filename):
        self.manbots = []
        self.strongest_manbot = None
        with open(filename, 'r') as input:
            for line in input:
                self._add(line)

    def _add(self, line):
        line = line.strip('\n')
        sig_radius = int(line[line.find('r=') + 2:])
        coords_start = line.find('<')+1
        coords_end = line.find('>')
        coords = line[coords_start:coords_end].split(',')
        pos_x = int(coords[0])
        pos_y = int(coords[1])
        pos_z = int(coords[2])
        manbot = Manbot(Point3D(pos_x,pos_y,pos_z),sig_radius)
        self.manbots.append(manbot)
        if self.strongest_manbot is None or manbot.sig_radius > self.strongest_manbot.sig_radius:
            self.strongest_manbot = manbot

    def number_in_range(self):
        in_range = 0
        for m in self.manbots:
            if m.pos.manhattan_distance(self.strongest_manbot.pos) <= self.strongest_manbot.sig_radius:
                in_range += 1
        return in_range

    def intersects(self):
        for m1 in self.manbots:
            for m2 in self.manbots:
                if m1 != m2 and m1.intersects(m2):
                    m1.intersects_with.append(m2)

# run it
manbots = Manbots("test-input2.txt")
print(f'Part 1 Result: {manbots.number_in_range()}')


# PART2:
'''
Possible solution:
A Manbot can tra
For each cuboid how many other cuboids does it intersect with?
For cuboid(s) with maximum number of intersects what are the co-ords in this area?
For each coord which is furthest from 0,0,0 (manhattan distance)
'''
min_x = min(manbots.manbots, key=lambda x : x.min_x).min_x
max_x = max(manbots.manbots, key=lambda x : x.max_x).max_x
min_y = min(manbots.manbots, key=lambda x : x.min_y).min_y
max_y = max(manbots.manbots, key=lambda x : x.max_y).max_y
min_z = min(manbots.manbots, key=lambda x : x.min_z).min_z
max_z = max(manbots.manbots, key=lambda x : x.max_z).max_z
print(min_x,min_y,min_z)
print(max_x,max_y,max_z)