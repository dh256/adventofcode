import pytest
from Game import Game

test_data=[('tests/test1.txt',1,15),('tests/test1.txt',2,12)]

@pytest.mark.parametrize('file_name,strategy,score',test_data)
def test_play_game(file_name,strategy,score):
    game = Game(file_name,strategy)
    assert(game.play() == score) 

