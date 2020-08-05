from Directions import Directions

directions = Directions("input.txt")
print(f'Part 1 distance to Easter Bunny HQ: {directions.easter_bunny_hq()}')
print(f'Part 2 distance to Easter Bunny HQ: {directions.easter_bunny_hq(part2=True)}')