
''' 
David Hanley, December 2024
'''
import pytest
from Day20 import Day20

test_data=[('tests/test1.txt',50,1,285)]
                  
@pytest.mark.parametrize('file_name,save_at_least,p1_result,p2_result',test_data)
def test_solution(file_name: str,save_at_least: int,p1_result: int,p2_result: int):
    d = Day20(file_name)
    assert(d.solution(save_at_least) == [p1_result,p2_result])


