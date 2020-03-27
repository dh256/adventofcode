'''
David Hanley, Dec 2019
See: https://adventofcode.com/2019/day/6
'''
from Orbits import Orbits

print('Building Orbits ...')
orbits = Orbits("input.txt")
print('Calculating Total Orbits ...')
print(f'Part 1 Total Orbits: {orbits.total_orbits()}')
print('Calculating Shortest Distance ...')
print(f'Part 2 Shortest Distance: {orbits.shortest_distance()}')
