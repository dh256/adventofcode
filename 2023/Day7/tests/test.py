import pytest
from Camel import Camel

test_data=[('tests/input.txt',1,6440),('tests/input.txt',2,5905)]

@pytest.mark.parametrize('file_name,part,result',test_data)
def test_total_winnings(file_name,part,result):
    camel = Camel(file_name,part)
    assert(camel.total_winnings() == result)

