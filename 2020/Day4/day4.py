from Passports import Passports

passports = Passports("input.txt")
valid_passports = passports.valid()
print(f'Part 1: {valid_passports}')

valid_passports2 = passports.valid2()
print(f'Part 2: {valid_passports2}')