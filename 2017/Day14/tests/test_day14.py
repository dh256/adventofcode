import pytest
from Day14 import Day14

test_data=[('flqrgnkx',8108)]

@pytest.mark.parametrize('key,result',test_data)
def tests_part1(key,result):
    day14 = Day14(key)
    assert(day14.part1() == result)
    

    
