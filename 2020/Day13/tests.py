import pytest

from Bus import Bus

test_data =[('test1.txt',295)]

@pytest.mark.parametrize("file_name,next_bus",test_data)
def test_next_bus(file_name,next_bus):
    bus = Bus(file_name)
    assert bus.next_bus() == next_bus