import pytest
from MonkeyInTheMiddle import Monkeys 

test_data=[ ('tests/test1.txt',20,True,10605),
            ('tests/test1.txt',20,False,10197),
            ('tests/test1.txt',10000,False,2713310158)]

@pytest.mark.parametrize('file_name,rounds,correct_worry_levels,result',test_data)
def test_calc_monkey_business(file_name,rounds,correct_worry_levels,result):
    monkeys = Monkeys(file_name)
    assert(monkeys.calc_monkey_business(rounds,correct_worry_levels) == result)

