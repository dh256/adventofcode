import pytest
from submarine import Submarine

test_data = [('tests/test1.txt',198)]
test_data2 = [('tests/test1.txt',230)]

@pytest.mark.parametrize('filename,power',test_data)
def test_day2_power(filename,power):
    sub = Submarine(filename)
    assert(sub.power_consumption == power)

@pytest.mark.parametrize('filename,life_support',test_data2)
def test_day2_life_support(filename,life_support):
    sub = Submarine(filename)
    assert(sub.life_support_rating == life_support)