from Hailstones import Hailstones
import pytest

test_data=[('tests/input.txt',7,27,2)]

@pytest.mark.parametrize('file_name,min_xy,max_xy,result',test_data)
def test_part1(file_name,min_xy,max_xy,result):
    hailstones = Hailstones(file_name)
    assert(hailstones.part1(min_xy,max_xy) == result)

