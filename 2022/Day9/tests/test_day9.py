import pytest
from RopeBridge import Rope

test_data=[('tests/test1.txt',2,13),('tests/test1.txt',10,1)]

@pytest.mark.parametrize('file_name,knots,result',test_data)
def test_tail_visit_at_least_once(file_name,knots,result):
    rope = Rope(file_name,knots)
    rope.move()
    assert(rope.tail_visit_at_least_once == result)

