from Garden import Garden
import pytest

test_data=[('tests/input.txt',1,2),('tests/input.txt',2,4),('tests/input.txt',3,6),('tests/input.txt',6,16)]

@pytest.mark.parametrize('file_name,steps,result',test_data)
def test_part1(file_name,steps,result):
    garden = Garden(file_name)
    assert(garden.part1(steps) == result)

