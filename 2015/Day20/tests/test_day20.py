'''
David Hanley, November 2024
'''
import pytest
from Day20 import Day20

test_data1=[(10,1),(70,4),(120,6),(130,8)]
                  
@pytest.mark.parametrize('min_presents,result',test_data1)
def test_solution_part1(min_presents:int ,result: int):
    d = Day20()
    assert(d.solution(min_presents)[0] == result)

