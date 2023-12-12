from Springs import Springs

import pytest

test_data=[('tests/input.txt',21)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_condition_count_sum(file_name,result):
    springs = Springs(file_name)
    assert(springs.condition_count_sum() == result)

