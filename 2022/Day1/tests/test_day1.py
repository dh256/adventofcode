import pytest
from Elf import Elf

test_data=[('tests/test1.txt',1,24000),('tests/test1.txt',3,45000)]

@pytest.mark.parametrize('file_name,n,cals',test_data)
def test_nmost_calorific(file_name,n,cals):
    elves = Elf(file_name)
    assert(elves.topn_most_calorific(n) == cals)
