
''' 
David Hanley, December 2024
'''
import pytest
from Day10 import Day10

test_data=[('tests/test1.txt',1,1)]
test_data=[('tests/test2.txt',36,81)]
                  
@pytest.mark.parametrize('file_name,result_p1,result_p2',test_data)
def test_solution(file_name: str,result_p1: int, result_p2: int):
    d = Day10(file_name)
    assert(d.solution() == (result_p1,result_p2))

'''
@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day10(file_name)
    assert(d.part2() == result)
'''

