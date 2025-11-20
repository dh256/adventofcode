from Day16 import Day16
import pytest

test_data =[('tests/test1.txt',5,'baedc')]

@pytest.mark.parametrize('filename,programs,result',test_data)
def tests_part1(filename,programs,result):
    day16 = Day16(filename,programs)
    assert(day16.part1() == result)