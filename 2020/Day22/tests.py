import pytest
from Game import Game

test_data = [("test1.txt",306)]

@pytest.mark.parametrize('filename,result',test_data)
def test_play_game(filename,result):
    game = Game(filename)
    game_score = game.play()
    assert game_score == result

