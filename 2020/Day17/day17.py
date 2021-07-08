from Cubes import Cubes, Cubes2

# Part 1
cube = Cubes('input.txt')
result = cube.cycle(6)
print(f'Part 1: {result}')

# Part 2
cube2 = Cubes2('input.txt')
result = cube2.cycle(6)
print(f'Part 2: {result}')
