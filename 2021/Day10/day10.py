from nav import Nav

nav = Nav('input.txt')
scores = nav.calc_scores()
print(f'Part 1: {scores[0]}')
print(f'Part 2: {scores[1]}')

