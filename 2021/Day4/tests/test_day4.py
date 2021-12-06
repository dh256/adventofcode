import pytest
from bingo import Bingo

test_data_first = [('tests/test1.txt',4512),('tests/test2.txt',8140)]
test_data_last = [('tests/test1.txt',1924)]

@pytest.mark.parametrize('filename,result', test_data_first)
def test_play_first(filename,result):
    bingo = Bingo(filename)
    assert(bingo.play() == result)

@pytest.mark.parametrize('filename,result', test_data_last)
def test_play_last(filename,result):
    bingo = Bingo(filename)
    assert(bingo.play(True) == result)