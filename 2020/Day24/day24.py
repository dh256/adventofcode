from HexGrid import HexGrid

# Part 1
grid = HexGrid("input.txt")
grid.process_instructions()
black_tiles = grid.black_tiles
print(f'Part 1: Black tiles: {black_tiles}')

# Part 2
black_tiles=grid.flip_tiles(100)
black_tiles = grid.black_tiles
print(f'Part 2: Black tiles: {black_tiles}')
