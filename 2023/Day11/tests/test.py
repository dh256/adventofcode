from Universe import Universe

import pytest

test_data=[('tests/input.txt',2,374),('tests/input.txt',10,1030),('tests/input.txt',100,8410)]

@pytest.mark.parametrize('file_name,expand,result',test_data)
def test_sum_shortest_paths(file_name,expand,result):
    universe = Universe(file_name,expand)
    assert(universe.sum_shortest_paths() == result)

