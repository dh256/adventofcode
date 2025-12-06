import os
import pytest
from day6 import Day6

test_data1=[(os.path.dirname(__file__) + '/input.txt',4277556)]
test_data2=[(os.path.dirname(__file__) + '/input.txt',3263827)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day6(file_name)
    assert(d.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day6(file_name)
    assert(d.part2() == result)
