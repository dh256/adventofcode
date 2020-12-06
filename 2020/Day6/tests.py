import pytest
from CustomForm import Groups

test_data = [("test.txt",11)]
test_data2 = [("test.txt",6)]

@pytest.mark.parametrize("file_name,questions",test_data)
def test_total_number_of_questions_answered_by_anyone(file_name,questions):
    groups = Groups(file_name)
    assert(groups.total_number_of_questions_answered_by_anyone() == questions)

@pytest.mark.parametrize("file_name,questions",test_data2)
def test_total_number_of_questions_answered_by_everyone(file_name,questions):
    groups = Groups(file_name)
    assert(groups.total_number_of_questions_answered_by_everyone() == questions)