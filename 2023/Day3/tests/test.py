
import pytest
from Engine import Engine

test_data=[('tests/input.txt',4361)]
test_data2=[('tests/input.txt',467835)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_sum_of_part_numbers(file_name,result):
    engine = Engine(file_name)
    assert(engine.sum_of_part_numbers() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_sum_of_gear_ratios(file_name,result):
    engine = Engine(file_name)
    assert(engine.sum_of_gear_ratios() == result)