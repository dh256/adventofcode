import pytest
from Day3 import Day3

test_data=[('tests/input.txt',357,3121910778619)]
                  
@pytest.mark.parametrize('file_name,result1,result2',test_data)
def test_parts1and2(file_name,result1,result2):
    d = Day3(file_name)
    assert(d.parts1and2() == (result1, result2))

