import pytest
from Day14 import Day14

test_data=[('flqrgnkx',8108,1242)]

@pytest.mark.parametrize('key,result1,result2',test_data)
def tests_parts_1and2(key,result1,result2):
    day14 = Day14(key)
    assert(day14.part1() == result1)
    assert(day14.part2() == result2)
    
    
