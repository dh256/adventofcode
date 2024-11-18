'''
David Hanley, November 2024
'''
import pytest
from Day15 import Day15

test_data=[('tests/test1.txt',(62842880,57600000))]
                  
@pytest.mark.parametrize('file_name,result',test_data)
def test_solution(file_name: str,result: tuple[int, int]):
    d = Day15(file_name)
    assert(d.solution() == result)

