import pytest
from Game import Game

test_data = [("389125467",10,"92658374"),("389125467",100,"67384529")]
test_data2 = [("389125467",10000000,149245887792)]

@pytest.mark.parametrize('input,moves,result',test_data)
def test_play_part1(input,moves,result):
    labels = [int(c) for c in input]
    game = Game(labels)
    assert game.play_part1(moves) == result

@pytest.mark.parametrize('input,moves,result',test_data2)
def test_play_part2(input,moves,result):
    labels = [int(c) for c in input]
    labels.extend(range(10,1000001))
    game = Game(labels)
    assert game.play_part2(moves) == result