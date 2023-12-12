from Springs import Springs

import pytest

test_data=[('tests/input.txt',1,21),('tests/input.txt',2,525152)]

@pytest.mark.parametrize('file_name,part,result',test_data)
def test_condition_count_sum(file_name,part,result):
    springs = Springs(file_name)
    assert(springs.condition_count_sum(part) == result)

