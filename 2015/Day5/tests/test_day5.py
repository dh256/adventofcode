import pytest
from NiceString import NiceStrings

test_data1 = [('tests/test1.txt',2)]
test_data2 = [('tests/test2.txt',2)]


@pytest.mark.parametrize("file_name,nice_strings_count",test_data1)
def test_nice_strings_count1(file_name,nice_strings_count):
    nice_strings = NiceStrings(file_name)
    assert(nice_strings.count_nice_part1() == nice_strings_count)

@pytest.mark.parametrize("file_name,nice_strings_count",test_data2)
def test_nice_strings_count2(file_name,nice_strings_count):
    nice_strings = NiceStrings(file_name)
    assert(nice_strings.count_nice_part2() == nice_strings_count)
