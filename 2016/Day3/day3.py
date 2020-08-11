from Triangles import Triangles

triangles = Triangles("input.txt")
print(f'Part 1 Possible Triangles = {triangles.possible(columns=False)}')
print(f'Part 2 Possible Triangles = {triangles.possible(columns=True)}')


