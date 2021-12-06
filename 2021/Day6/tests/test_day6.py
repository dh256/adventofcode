import pytest

from fish import Fish

test_data = [('tests/test1.txt',18,26),('tests/test1.txt',80,5934),('tests/test1.txt',256,26984457539)]

@pytest.mark.parametrize('filename,days,num_fish',test_data)
def test_process(filename,days,num_fish):
    fish = Fish(filename)
    assert(fish.simulate(days) == num_fish)
