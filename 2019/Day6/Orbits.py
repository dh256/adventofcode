from Graph import SimpleGraph

class Orbits:
    def __init__(self,filename):
        # build graph
        self.orbits = SimpleGraph()
        with open(filename,'r') as orbit_data:
            orbit_data = [line.strip('\n') for line in orbit_data]
            for orbit in orbit_data:
                planets = orbit.split(')')
                self.orbits.add_edgde(planets[0],planets[1])

    def total_orbits(self):
        # The total number of direct and indirect orbits:
        # Sum of the Distance of each Planet from COM
        return self.orbits.total_min_path_distances('COM')

    def shortest_distance(self,from_planet="YOU",to_planet="SAN"):
        return self.orbits.shortest_distance(from_planet,to_planet) - 2