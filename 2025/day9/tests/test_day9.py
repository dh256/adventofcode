import os
import pytest
from day9 import Day9

test_data=[(os.path.dirname(__file__) + '/input.txt',50,24)]
                  
@pytest.mark.parametrize('file_name,result1,result2',test_data)
def test_parts1and2(file_name: str,result1: int, result2: int):
    d = Day9(file_name)
    assert(d.parts1and2() == (result1,result2))

