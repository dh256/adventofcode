import pytest
from RopeBridge import Rope

test_data=[('tests/test1.txt',13)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_tail_visit_at_least_once(file_name,result):
    rope = Rope(file_name)
    rope.move()
    assert(rope.tail_visit_at_least_once == result)