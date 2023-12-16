from Rocks import Rocks
import pytest

test_data=[('tests/input.txt',136)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_part1(file_name, result):
    rocks = Rocks(file_name)
    assert(rocks.part1() == result)

