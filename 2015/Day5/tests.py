import pytest
from NiceString import NiceString, NiceStrings

test_data = [('ugknbfddgicrmopn',True),('aaa',True),('jchzalrnumimnmhp',False),('haegwjzuvuyypxyu',False),('dvszwmarrgswjxmb',False)]

@pytest.mark.parametrize("test_input,expected",test_data)
def test_is_nice(test_input,expected):
    nice_str = NiceString(test_input)
    assert(nice_str.is_nice() == expected)

def test_nice_strings_count():
    nice_strings = NiceStrings("test.txt")
    assert(nice_strings.count_nice() == 2)