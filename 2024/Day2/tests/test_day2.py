
''' 
David Hanley, December 2024
'''
import pytest
from Day2 import Day2

test_data1=[('tests/test1.txt',2)]
test_data2=[('tests/test1.txt',4)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name: str,result: int):
    d = Day2(file_name)
    assert(d.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day2(file_name)
    assert(d.part2() == result)

