import pytest
from day4 import find_number

test_data = [("abcdef","00000",609043),("pqrstuv","00000",1048970)]
@pytest.mark.parametrize("key,prefix,expected",test_data)
def test_find_number(key,prefix,expected):
    assert(find_number(key,prefix) == expected)
    