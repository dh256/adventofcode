from Pipes import Pipes
import pytest

test_data=[('tests/input1.txt',4),('tests/input2.txt',8),
    ('tests/input3.txt',2),
    ('tests/input4.txt',2),
    ('tests/input5.txt',2),
    ('tests/input6.txt',2)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_steps_to_farthest(file_name, result):
    pipes = Pipes(file_name)
    assert(pipes.steps_to_farthest() == result)

