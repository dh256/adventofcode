from Console import Console, InfiniteLoopDetectedError
import pytest

test_data=[("test.txt",5)]
test_data2=[("test.txt",8)]

@pytest.mark.parametrize("file_name,accumulator",test_data)
def test_run(file_name,accumulator):
    console = Console(file_name)
    try:
        console.run()
    except InfiniteLoopDetectedError:
        assert console.accumulator == accumulator


@pytest.mark.parametrize("file_name,accumulator",test_data2)
def test_run2(file_name,accumulator):
    console = Console(file_name)
    console.run2()
    assert console.accumulator == accumulator
