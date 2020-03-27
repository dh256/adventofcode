'''
All tests pass but answer for Part 1 is 104 which is too low
Unclear why this is the case
'''
from NiceString import NiceStrings

nice_strings = NiceStrings("input.txt")
result = nice_strings.count_nice()
print(result)