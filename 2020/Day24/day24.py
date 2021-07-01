from HexGrid import HexGrid

grid=HexGrid("input.txt")
black_tiles=grid.process()
print(f'Black tiles: {black_tiles}')
