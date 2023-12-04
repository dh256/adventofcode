
import pytest
from Cards import Cards

test_data=[('tests/input.txt',13)]
test_data2=[('tests/input.txt',30)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_points(file_name,result):
    cards = Cards(file_name)
    assert(cards.calc_points() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_calc_total_cards(file_name,result):
    cards = Cards(file_name)
    assert(cards.calc_total_cards() == result)

