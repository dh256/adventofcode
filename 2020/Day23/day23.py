from Game import Game

input_val =  "962713854"

labels = [int(c) for c in input_val]
game = Game(labels)
result = game.play_part1(100)
print(f'Part 1: {result}')

labels.extend(range(10,1000001))
game = Game(labels)
result = game.play_part2(10000000)
print(f'Part 2: {result}')
