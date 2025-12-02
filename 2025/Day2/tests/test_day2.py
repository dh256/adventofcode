
import pytest
from Day2 import Day2

test_data1=[('tests/input.txt',1227775554,4174379265)]
                  
@pytest.mark.parametrize('file_name,result1,result2',test_data1)
def test_parts1and2(file_name,result1,result2):
    d = Day2(file_name)
    assert(d.parts1and2() == (result1, result2))

