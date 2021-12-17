import pytest
from probe import Probe

test_data = [('tests/test1.txt',45,112)]

@pytest.mark.parametrize('filename,highest_y,distinct_vels',test_data)
def test_fire(filename,highest_y,distinct_vels):
    probe = Probe(filename)
    assert(probe.fire() == (highest_y, distinct_vels))
