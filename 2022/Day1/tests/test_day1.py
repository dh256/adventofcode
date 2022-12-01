import pytest
from Elf import Elf

test_data=[('tests/test1.txt',24000)]
test_data2=[('tests/test1.txt',45000)]

@pytest.mark.parametrize('file_name,most_cals',test_data)
def test_most_calorific(file_name, most_cals):
    elves = Elf(file_name)
    assert(elves.most_calorific == most_cals)

@pytest.mark.parametrize('file_name,top3_most_cals',test_data2)
def test_top3_most_calorific(file_name, top3_most_cals):
    elves = Elf(file_name)
    assert(elves.top3_most_calorific == top3_most_cals)