from MemoryGame import MemoryGame

input = (6,13,1,15,2,0)
game = MemoryGame(input)
result = game.play(2020)
print(result)

game2 = MemoryGame(input)
result2 = game2.play(30000000)
print(result2)
