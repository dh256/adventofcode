
''' 
David Hanley, December 2024
'''
import pytest
from Day15 import Day15

test_data=[('tests/test1.txt',1,2028),('tests/test2.txt',1,10092)]

                  
@pytest.mark.parametrize('file_name,part,result',test_data)
def test_solution(file_name: str,part:int,result: int):
    d = Day15(file_name,part)
    assert(d.solution() == result)


