from game import Game
import pytest

test_data = [(4,8,739785)]
@pytest.mark.parametrize('player1_start,player2_start,result', test_data)
def test_play(player1_start,player2_start,result):
    game = Game(player1_start,player2_start)
    assert(game.play() == result)

test_data2 = [(4,8,444356092776315)]
@pytest.mark.parametrize('player1_start,player2_start,result', test_data2)
def test_play(player1_start,player2_start,result):
    game = Game(player1_start,player2_start)
    assert(game.play2() == result)