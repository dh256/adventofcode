from Game import Game

game = Game("input.txt")
#print(game.show_decks())
score = game.play()
print(f'Score: {score}')