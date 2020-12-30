import pytest
from Tickets import Tickets

test_data = [('test1.txt',71)]

@pytest.mark.parametrize("file_name,error_rate",test_data)
def test_scanning_error_rate(file_name,error_rate):
    tickets = Tickets(file_name)
    assert tickets.scanning_error_rate() == error_rate

