import pytest
from DistressSignal import Signal

test_data=[('tests/test1.txt',13)]
test_data2=[('tests/test1.txt',140)]

@pytest.mark.parametrize('file_name, result',test_data)
def test_right_order_pairs(file_name, result):
    signal = Signal(file_name)
    assert(signal.right_order_pairs() == result)

@pytest.mark.parametrize('file_name, result',test_data2)
def test_pairs_in_right_order(file_name, result):
    signal = Signal(file_name)
    assert(signal.pairs_in_right_order() == result)