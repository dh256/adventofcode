import pytest
from Passports import Passports,Passport

test_data = [("test.txt",2)]
test_data2 = [("test2.txt",4)]
test_pid = [("000000001",True),("0123456789",False)]
test_hcl = [("#0011ff",True),("#123ffde",False),("#123ffh",False)]
test_ecl = [("brn",True),("wat",False)]
test_hgt = [("60in",True),("190cm",True),(" cm",False),("190in",False),("190",False)]
test_year = [("2002",range(1920,2003),True),("2003",range(1920,2003),False),("1919",range(1920,2003),False),("1920",range(1920,2003),True)]

@pytest.mark.parametrize("input_file,valid_passports",test_data)
def test_valid(input_file, valid_passports):
    passports = Passports(input_file)
    assert(passports.valid() == valid_passports)

@pytest.mark.parametrize("input_file,valid_passports",test_data2)
def test_valid2(input_file, valid_passports):
    passports = Passports(input_file)
    assert(passports.valid2() == valid_passports)

@pytest.mark.parametrize("value,year_range,valid",test_year)
def test_valid_year(value, year_range, valid):
    passport = Passport()
    assert(passport._valid_year(value,year_range) == valid)

@pytest.mark.parametrize("value,valid",test_pid)
def test_valid_pid(value, valid):
    passport = Passport()
    passport.passport['pid'] = value
    assert(passport._valid_pid(value) == valid)

@pytest.mark.parametrize("value,valid",test_hcl)
def test_valid_hcl(value, valid):
    passport = Passport()
    passport.passport['hcl'] = value
    assert(passport._valid_hcl(value) == valid)

@pytest.mark.parametrize("value,valid",test_ecl)
def test_valid_ecl(value, valid):
    passport = Passport()
    passport.passport['ecl'] = value
    assert(passport._valid_ecl(value) == valid)

@pytest.mark.parametrize("value,valid",test_hgt)
def test_valid_hgt(value, valid):
    passport = Passport()
    passport.passport['hgt'] = value
    assert(passport._valid_hgt(value) == valid)