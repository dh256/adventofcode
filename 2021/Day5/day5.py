from vents import Vents

filename = 'input.txt'
vents = Vents(filename,1)
result = vents.dangerous_areas
print(f'Part 1: {result}')

vents2 = Vents(filename,2)
result2 = vents2.dangerous_areas
print(f'Part 2: {result2}')