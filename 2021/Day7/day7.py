from crabs import Crabs

filename = 'input.txt'

crabs = Crabs(filename)
result = crabs.align()
print(f'Part 1: Pos - {result[0]}; Fuel Used - {result[1]}')

result = crabs.align2()
print(f'Part 2: Pos - {result[0]}; Fuel Used - {result[1]}')