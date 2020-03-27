import pytest
from Simulation import Simulation

testdata = [
    ("tests/test1.txt",2),
    ("tests/test2.txt",4),
    ("tests/test3.txt",2),
]

@pytest.mark.parametrize("input_file,expected", testdata)
def test_simulation(input_file, expected):
    sim = Simulation(input_file)
    sim.run()
    assert(sim.houses_visited_more_than(0)) == expected