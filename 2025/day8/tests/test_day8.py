
import pytest
from day8 import Day8
import os

test_data=[(os.path.dirname(__file__) + '/input.txt',10,40,25272)]
                  
@pytest.mark.parametrize('file_name,pairs,part1,part2',test_data)
def test_part1(file_name,pairs,part1,part2):
    d = Day8(file_name)
    result = d.parts1and2(pairs)
    assert(result == (part1, part2))

