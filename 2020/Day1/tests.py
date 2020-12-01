import pytest
from ExpenseReport import ExpenseReport

test_data = [("test.txt",2,514579),("test.txt",3,241861950)]

@pytest.mark.parametrize("data_file,entries,answer",test_data)
def test_find_entries_sum_to(data_file,entries,answer):
    report = ExpenseReport(data_file)
    assert(report.find_entries_sum_to(2020,entries) == answer)