'''
David Hanley, Nov 2024
'''
import pytest
from Day12 import Day12

test_data1=[('tests/test1.txt',6)]
test_data1=[('tests/test2.txt',3)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day12(file_name)
    assert(d.part1() == result)

'''
@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day12(file_name)
    assert(d.part2() == result)
'''
