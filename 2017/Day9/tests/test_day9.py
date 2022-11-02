import pytest
from Stream import Stream

test_data_score=[('tests/test1.txt',1),
('tests/test2.txt',6),
('tests/test3.txt',5),
('tests/test4.txt',16),
('tests/test5.txt',1),
('tests/test6.txt',9),
('tests/test7.txt',9),
('tests/test8.txt',3)
]

test_data_groups=[('tests/test9.txt',1),
('tests/test10.txt',3),
('tests/test11.txt',3),
('tests/test12.txt',6),
('tests/test13.txt',1),
('tests/test14.txt',1),
('tests/test15.txt',5),
('tests/test16.txt',2)
]

test_data_non_cancelled_in_garbage = [('tests/test17.txt',0),
('tests/test18.txt',10),
('tests/test19.txt',17)
]

@pytest.mark.parametrize('file_name,groups',test_data_groups)
def test_total_groups(file_name,groups):
    stream = Stream(file_name)
    assert(stream.get_totals()[0] == groups)

@pytest.mark.parametrize('file_name,score',test_data_score)
def test_total_score(file_name,score):
    stream = Stream(file_name)
    assert(stream.get_totals()[1] == score)

@pytest.mark.parametrize('file_name,non_cancelled_in_garbage',test_data_non_cancelled_in_garbage)
def test_total_non_cancelled_in_garbage(file_name,non_cancelled_in_garbage):
    stream = Stream(file_name)
    assert(stream.get_totals()[2] == non_cancelled_in_garbage)
