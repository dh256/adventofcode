import pytest
from Simulation import Simulation

testdata = [
    ("tests/test1.txt",1,2),
    ("tests/test2.txt",1,4),
    ("tests/test3.txt",1,2),
    ("tests/test4.txt",2,3),
    ("tests/test2.txt",2,3),
    ("tests/test3.txt",2,11),
]

@pytest.mark.parametrize("input_file,part,expected", testdata)
def test_simulation(input_file, part, expected):
    sim = Simulation(input_file)
    sim.run()
    assert(sim.run(part)) == expected