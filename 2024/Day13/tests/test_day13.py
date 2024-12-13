''' 
David Hanley, December 2024
'''
import pytest
from Day13 import Day13

test_data1=[('tests/test1.txt',1,480)]
                  
@pytest.mark.parametrize('file_name,part,result',test_data1)
def test_solution(file_name: str,part: int,result: int):
    d = Day13(file_name)
    assert(d.solution(part) == result)

