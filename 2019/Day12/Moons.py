import re
from Point3D import Point3D

class Moon():
    def __init__(self,name,coords):
        self.name = name
        coord=re.findall(r'[-0-9]+',coords)
        self.position = Point3D(int(coord[0]),int(coord[1]),int(coord[2]))
        self.velocity = Point3D(0,0,0)

    '''
    Apply gravity to update velocity
    '''
    def apply_gravity(self,value):
        if self.position.x > value.position.x:
            self.velocity.x -= 1
            value.velocity.x += 1
        elif self.position.x < value.position.x:
            self.velocity.x += 1
            value.velocity.x -= 1

        if self.position.y > value.position.y:
            self.velocity.y -= 1
            value.velocity.y += 1
        elif self.position.y < value.position.y:
            self.velocity.y += 1
            value.velocity.y -= 1

        if self.position.z > value.position.z:
            self.velocity.z -= 1
            value.velocity.z += 1
        elif self.position.z < value.position.z:
            self.velocity.z += 1
            value.velocity.z -= 1

    '''
    Apply velocity
    '''
    def apply_velocity(self):
        self.position += self.velocity

    def kinetic_energy(self):
        return abs(self.velocity.x) + abs(self.velocity.y) + abs(self.velocity.z)

    def potential_energy(self):
        return abs(self.position.x) + abs(self.position.y) + abs(self.position.z)

    def energy(self):
        return self.kinetic_energy() * self.potential_energy()

class Moons():
    def __init__(self,filename):  
        moon_names = ["Io","Europa","Ganymede","Callisto"]
        with open(filename,"r") as input_file:
            iter_moons = iter(moon_names)
            self.moons = [Moon(next(iter_moons),line.strip('\n')) for line in input_file]
                
    def move_moons(self, time):
        for t in range(0,time):
            # apply gravity to every pair of moons
            for m in range(0,4):
                for n in range(m+1,4):
                    self.moons[m].apply_gravity(self.moons[n])
            
            # apply velocity to each moon
            for moon in self.moons:
                moon.apply_velocity() 

        return self.total_energy()

    def total_energy(self):
        total = 0
        for m in self.moons:
            total += m.energy()
        return total 
