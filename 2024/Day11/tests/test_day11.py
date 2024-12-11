
''' 
David Hanley, December 2024
'''
import pytest
from Day11 import Day11

test_data1=[('0 1 10 99 999',1,7),('125 17',1,3),('125 17',5,13),('125 17',25,55312)]
                  
@pytest.mark.parametrize('stones,blinks,result',test_data1)
def test_part1(stones: str,blinks: int,result: int):
    d = Day11(stones)
    assert(d.solution(blinks) == result)


