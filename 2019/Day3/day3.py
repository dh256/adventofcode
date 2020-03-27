from Grid import Grid
from Lines import Lines

lines = Lines("input.txt")
grid = Grid(lines)
grid.populate()
closest_point = grid.closest_intersect()
shortest_path = grid.shortest_intersect_path()
print(f'Part 1: {closest_point}')
print(f'Part 2: {shortest_path}')