from dataclasses import dataclass
import re

@dataclass
class Point3D:
    x: int
    y: int
    z: int
    
    def distance_from_origin(self) -> int:
        return abs(self.x) + abs(self.y) + abs(self.z)

    def __add__(self,p:Point3D) -> Point3D:
        return Point3D(self.x+p.x,self.y+p.y,self.z+p.z)
    
    def __str__(self) -> str:
        return f'({self.x},{self.y},{self.z}'
    
    def __hash__(self) -> int:
        return hash((self.x,self.y,self.z))

@dataclass
class Particle:
    position: Point3D
    velocity: Point3D
    acceleration: Point3D

class Day20:
    def __init__(self, file_name: str) -> None:
        with open(file_name,'r') as input_file:
            lines: list[str] = [line.strip('\n') for line in input_file]
            
        # create particles
        self._particles: dict[int, Particle] = dict()
        for particle_index, line in enumerate(lines):
            nums: list[int] = [int(num) for num in re.findall('-*\d+',line)]
            position = Point3D(nums[0],nums[1],nums[2])
            velocity = Point3D(nums[3],nums[4],nums[5])
            acceleration = Point3D(nums[6],nums[7],nums[8])
            self._particles[particle_index] = Particle(position,velocity,acceleration)
    
    def part1(self) -> int:
        # figure out which Particle is closest to origin over long term
        # Brute force, move particles 5000 times, sort by distance from origin and pick closest
        # Crude guess based but returns correct answer
        for _ in range(5000):
            for particle in self._particles.keys():
                self._particles[particle].velocity += self._particles[particle].acceleration
                self._particles[particle].position += self._particles[particle].velocity

        return next(iter(dict(sorted(self._particles.items(),key=lambda i: i[1].position.distance_from_origin())).keys()))
    
    def part2(self) -> int:
        # figure out which Particles are left after all possible collisions have occurred
        # Brute force, move particles x times removing collisions and see how many are left. 
        # Crude guesswork but gets right answer
        for _ in range(5000):
            new_positions: dict[Point3D, int] = dict()
            for particle in self._particles.keys():
                self._particles[particle].velocity += self._particles[particle].acceleration
                self._particles[particle].position += self._particles[particle].velocity
                try:
                    new_positions[self._particles[particle].position] += 1
                except KeyError:
                    new_positions[self._particles[particle].position] = 1
            
            collisions: set[Point3D] = {i[0] for i in new_positions.items() if i[1] > 1} 
            if len(collisions) > 0:
                self._particles = dict(filter(lambda i: i[1].position not in collisions, self._particles.items()))
                
        return len(self._particles)