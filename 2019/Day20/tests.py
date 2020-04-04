import pytest
from Pluto import Pluto

test_data=[
        ("test1.txt",23),
        ("test2.txt",58)
    ]

@pytest.mark.parametrize("filename,shortest_distance",test_data)
def test_shortest_path(filename,shortest_distance):
    pluto = Pluto(filename)
    assert(pluto.find_shortest_distance() == shortest_distance)