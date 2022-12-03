import pytest
from Rucksack import Rucksack

test_data=[('tests/test1.txt',1,157),('tests/test1.txt',2,70)]

@pytest.mark.parametrize('file_name,item_type,priority_sum',test_data)
def test_priority_sum(file_name,item_type,priority_sum):
    rucksack = Rucksack(file_name)
    assert(rucksack.calc_priority_sum(item_type) == priority_sum)