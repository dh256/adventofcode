
''' 
David Hanley, December 2024
'''
import pytest
from Day12 import Day12

test_data=[('tests/test4.txt',692,236),('tests/test1.txt',140,80),('tests/test2.txt',772,436),
            ('tests/test3.txt',1930,1206),('tests/test5.txt',1184,368)]
                  
@pytest.mark.parametrize('file_name,p1_result,p2_result',test_data)
def test_solution(file_name: str,p1_result: int,p2_result: int):
    d = Day12(file_name)
    assert(d.solution() == (p1_result,p2_result))


