from Map import Map, Slope
import pytest

test_data = [("test1.txt",[Slope(3,1)],7),
("test1.txt",[Slope(3,1),Slope(1,1),Slope(5,1),Slope(7,1),Slope(1,2)],336)]

@pytest.mark.parametrize("input_file,slopes,trees",test_data)
def test_traverse(input_file,slopes,trees):
    map = Map(input_file)
    assert(map.traverse(slopes) == trees)