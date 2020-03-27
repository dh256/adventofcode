import pytest
from Module import Module

test_data1 = {(12,2), (14,2), (1969,654), (100756,33583)}

@pytest.mark.parametrize("module,expected", test_data1)
def test_total_fuel1(module,expected):
    assert(Module(module).fuel() == expected)

test_data2 = {(14,2), (1969,966), (100756,50346)}
@pytest.mark.parametrize("module,expected", test_data2)
def test_total_fuel2(module,expected):
    assert(Module(module).fuel2() == expected)