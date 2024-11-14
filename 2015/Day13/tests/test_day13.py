'''
David Hanley, Nov 2024
'''
import pytest
from Day13 import Day13

test_data1=[('tests/test1.txt',330)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day13(file_name)
    assert(d.part1() == result)

