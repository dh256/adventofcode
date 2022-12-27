"""
Name: test_day25.py
Author: David Hanley
Date: 26-Dec-2022
"""
import pytest
from SNAFU import SNAFU
from SNAFU import SNAFUNumber

test_data_snafu_to_decimal = [(1,'1'),
(2,'2'),
(3,'1='),
(4,'1-'),
(5,'10'),
(6,'11'),
(7,'12'),
(8,'2='),
(9,'2-'),
(10,'20'),
(15,'1=0'),
(20,'1-0'),
(2022,'1=11-2'),
(12345,'1-0---0'),
(314159265,'1121-1110-1=0')
]

test_data_snafu_to_decimal2 = [
('1=-0-2',1747),
('12111',906),
('2=0=',198),
('21',11),
('2=01',201),
('111',31),
('20012',1257),
('112',32),
('1=-1=',353),
('1-12',107),
('12',7),
('1=',3),
('122',37)
]

test_data=[('tests/test1.txt','2=-1=0')]

@pytest.mark.parametrize('dec_num,snafu_num',test_data_snafu_to_decimal)
def test_to_decimal(dec_num,snafu_num):
    num = SNAFUNumber(snafu_num)
    assert(num.to_decimal() == dec_num)

@pytest.mark.parametrize('dec_num,snafu_num',test_data_snafu_to_decimal)
def test_to_snafu(dec_num,snafu_num):
    num = SNAFUNumber.to_snafu(dec_num)
    assert(num == snafu_num)

@pytest.mark.parametrize('snafu_num,dec_num',test_data_snafu_to_decimal2)
def test_to_decimal2(dec_num,snafu_num):
    num = SNAFUNumber(snafu_num)
    assert(num.to_decimal() == dec_num)

@pytest.mark.parametrize('snafu_num,dec_num',test_data_snafu_to_decimal2)
def test_to_snafu2(dec_num,snafu_num):
    num = SNAFUNumber.to_snafu(dec_num)
    assert(num == snafu_num)

@pytest.mark.parametrize('file_name,result',test_data)
def test_calculate_sum(file_name,result):
    snafu = SNAFU(file_name)
    assert(snafu.calculate_sum() == result)
