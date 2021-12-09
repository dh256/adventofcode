from cave import Cave

cave = Cave('input.txt')
print(f'Part 1: {cave.find_risk_level()}')
print(f'Part 2: {cave.find_largest_basins(3)}')