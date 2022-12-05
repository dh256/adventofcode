import pytest
from CrateStacks import CrateStacks, CraneType

test_data=[('tests/test1.txt',CraneType.CRATE_MOVER_9000,'CMZ'),('tests/test1.txt',CraneType.CRATE_MOVER_9001,'MCD')]

@pytest.mark.parametrize('file_name,crane_type,result',test_data)
def test_function(file_name,crane_type,result):
    crate_stacks = CrateStacks(file_name)
    crate_stacks.perform_moves(crane_type)
    assert(crate_stacks.top == result)