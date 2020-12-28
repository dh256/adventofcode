from MemoryGame import MemoryGame
import pytest

test_data = [((0,3,6),436),((1,3,2),1),((2,1,3),10),((1,2,3),27),((2,3,1),78),((3,2,1),438),((3,1,2),1836)]
test_data2 = [((0,3,6),175594),((1,3,2),2578),((2,1,3),3544142),((1,2,3),261214),((2,3,1),6895259),((3,2,1),18),((3,1,2),362)]


@pytest.mark.parametrize("input,result",test_data)
def test_play(input,result):
    game = MemoryGame(input)
    assert game.play(2020) == result

@pytest.mark.parametrize("input,result",test_data2)
def test_play2(input,result):
    game = MemoryGame(input)
    assert game.play(30000000) == result

