from Universe import Universe

import pytest

test_data=[('tests/input.txt',374)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_sum_shortest_paths(file_name,result):
    universe = Universe(file_name)
    assert(universe.sum_shortest_paths() == result)

