import pytest
from Day5 import Day5

test_data1=[('tests/input.txt',3)]
test_data2=[('tests/input.txt',14),
            ('tests/input2.txt',4),
            ('tests/input3.txt',3),
            ('tests/input4.txt',3)]
                  
@pytest.mark.parametrize('file_name,result',test_data1)
def test_part1(file_name,result):
    d = Day5(file_name)
    assert(d.part1() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_part2(file_name,result):
    d = Day5(file_name)
    assert(d.part2() == result)

