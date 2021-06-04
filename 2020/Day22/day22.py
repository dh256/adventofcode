from Game import Game

game = Game("input.txt")
winner = game.play_game(game.player_deck(1),game.player_deck(2))
score = game.calculate_score(winner[1])
print(f'Winner player {winner[0]}; score: {score}')