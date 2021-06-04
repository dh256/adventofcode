import pytest
from Game import Game

#test_data = [("test1.txt",306)]   # Part 1
test_data = [("test1.txt",291)]    # Part 2

@pytest.mark.parametrize('filename,result',test_data)
def test_play_game(filename,result):
    game = Game(filename)
    winner = game.play_game(game.player_deck(1),game.player_deck(2))
    assert game.calculate_score(winner[1]) == result

