import pytest
from Camel import Camel

test_data=[('tests/input.txt',6440)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_total_winnings(file_name,result):
    camel = Camel(file_name)
    assert(camel.total_winnings() == result)

