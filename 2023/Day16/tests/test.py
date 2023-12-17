from Grid import Grid
import pytest

test_data=[('tests/input.txt',46)]
test_data2=[('tests/input.txt',51)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name,result):
    grid = Grid(file_name)
    assert(grid.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    grid = Grid(file_name)
    assert(grid.part2() == result)

