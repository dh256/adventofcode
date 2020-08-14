import pytest
from Signal import Signal

test_data = [("test1.txt","easter",True),
            ("test1.txt","advent",False)]

@pytest.mark.parametrize("input_file,repeating_message,most_common",test_data)
def test_get_repeating_message(input_file,repeating_message,most_common):
    signal = Signal(input_file)
    assert(signal.get_repeating_message(most_common) == repeating_message)
