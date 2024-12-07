
''' 
David Hanley, December 2024
'''
import pytest
from Day7 import Day7

test_data=[('tests/test1.txt',3749,11387)]
                  
@pytest.mark.parametrize('file_name,result_p1,result_p2',test_data)
def test_part1(file_name: str,result_p1: int,result_p2: int):
    d = Day7(file_name)
    result = d.solution()
    assert(result[0] == result_p1)
    assert(result[1] == result_p2)

