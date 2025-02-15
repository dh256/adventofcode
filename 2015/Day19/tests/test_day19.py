'''
David Hanley, November 2024
'''
import pytest
from Day19 import Day19

test_data1=[('tests/test1.txt',4),(('tests/test2.txt',7))]
test_data2=[('tests/test3.txt',3),('tests/test4.txt',6)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name: str,result: int):
    d = Day19(file_name)
    assert(d.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name: str,result: int):
    d = Day19(file_name)
    assert(d.part2() == result)

