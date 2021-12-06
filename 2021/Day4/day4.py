from bingo import Bingo

filename = 'input.txt'
bingo = Bingo(filename)
result = bingo.play()
print(f'Part 1: {result}')

bingo2 = Bingo(filename)
result2 = bingo2.play(True)
print(f'Part 2: {result2}')