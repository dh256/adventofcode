import pytest
from FileSystem import FileSystem

test_data=[('tests/test1.txt',100000,95437)]
test_data2=[('tests/test1.txt',30000000,24933642)]

@pytest.mark.parametrize('file_name,max_size,result',test_data)
def test_total_size_of_directories_up_to_size(file_name,max_size,result):
    fs = FileSystem(file_name)
    assert(fs.total_size_of_directories_up_to_size(max_size) == result)

@pytest.mark.parametrize('file_name,free_space_required,result',test_data2)
def test_smallest_to_delete(file_name,free_space_required,result):
    fs = FileSystem(file_name)
    assert(fs.smallest_to_delete(free_space_required) == result)