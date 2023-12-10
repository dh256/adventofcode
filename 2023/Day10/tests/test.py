from Pipes import Pipes
import pytest

test_data=[('tests/input1.txt',4),('tests/input2.txt',8),
    ('tests/input3.txt',2),
    ('tests/input4.txt',2),
    ('tests/input5.txt',2),
    ('tests/input6.txt',2)]

test_data2=[('tests/input7.txt',4),('tests/input8.txt',8),('tests/input9.txt',10)]

@pytest.mark.parametrize('file_name,result',test_data)
def test_steps_to_farthest(file_name, result):
    pipes = Pipes(file_name)
    assert(pipes.steps_to_farthest() == result)

@pytest.mark.parametrize('file_name,result',test_data2)
def test_enclosed_by_loop(file_name, result):
    pipes = Pipes(file_name)
    assert(pipes.enclosed_by_loop() == result)


