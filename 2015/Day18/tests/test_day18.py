'''
David Hanley, November 2024
'''
import pytest
from Day18 import Day18

test_data1=[('tests/test1.txt',1,4,4),('tests/test1.txt',2,5,17)]
               
@pytest.mark.parametrize('file_name,part,steps,result',test_data1)
def test_solution(file_name: str,part: int,steps: int, result: int):
    d = Day18(file_name)
    assert(d.solution(steps,part) == result)

