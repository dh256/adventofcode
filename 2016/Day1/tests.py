import pytest
from Directions import Directions

test_data = [("test1.txt",False,5),("test2.txt",False,2),("test3.txt",False,12),("test4.txt",True,4)]

@pytest.mark.parametrize("input,part2,result",test_data)
def test_easter_bunny(input,part2,result):
    directions = Directions(input)
    assert(directions.easter_bunny_hq(part2) == result)
