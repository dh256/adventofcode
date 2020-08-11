import pytest
from Triangles import Triangles

test_data = [("test1.txt",0)]
test_data = [("test2.txt",0)]

@pytest.mark.parametrize("file,expected_possible_triangles",test_data)
def test_get_keycode(file,expected_possible_triangles):
    triangles = Triangles(file)
    possible_triangles = triangles.possible(columns=True)
    assert(possible_triangles == expected_possible_triangles)

