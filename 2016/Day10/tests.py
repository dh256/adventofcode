import pytest
from Factory import Factory

test_data=[("test1.txt",2,(5,2))]

@pytest.mark.parametrize("file_name,bot_number,compare_chips",test_data)
def test_number(file_name,bot_number,compare_chips):
    factory = Factory(file_name)
    assert(bot_number == factory.run(compare_chips)[0])