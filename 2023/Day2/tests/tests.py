
import pytest
from Game import Games

test_data=[('tests/input.txt',8)]
test_data2=[('tests/input.txt',2286)]

@pytest.mark.parametrize('input_file,result',test_data)
def test_sum_of_impossible_ids(input_file,result):
    games = Games(input_file)
    assert(games.sum_of_impossible_ids() == result)

@pytest.mark.parametrize('input_file,result',test_data2)
def test_sum_of_powers(input_file,result):
    games = Games(input_file)
    assert(games.sum_of_powers() == result)

