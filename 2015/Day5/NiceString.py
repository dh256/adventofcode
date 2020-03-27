import re

class NiceStrings():
    def __init__(self,filename):
        with open(filename,"r") as data:
            self.nice_strings = [NiceString(line.strip('\n')) for line in data]
    
    def count_nice(self):
        result = [nice_string for nice_string in self.nice_strings if nice_string.is_nice()]
        return len(result)

class NiceString():
    def __init__(self, str):
        self.str = str

    def is_nice(self):
        result = False

        '''
        Nice if:
         - contains 3 vowels and
         - at least one letter that appears twice and
         - does not contain any of the strings ab, cd, pq, or xy (overrides the other two rules)
        - otherwise naughty
        '''
        #reg expressions
        vowels_reg_ex = r"[aeiou]"
        letters_twice_reg_ex = r"([a-z])\1{1}"
        contains_reg_ex = r"ab|cd|pq|xy"

        # vowels
        vowels_found = re.findall(vowels_reg_ex,self.str)
        vowels = len(vowels_found) == 3
    
        # letters appear twice
        letters_twice_found = re.findall(letters_twice_reg_ex, self.str)
        appears_twice = len(letters_twice_found) > 0
        
        # contains
        contains_found = re.findall(contains_reg_ex,self.str)
        contains = len(contains_found) > 0

        return vowels and appears_twice and not contains

    def is_naughty(self):
        return not self.is_nice()

    def __str__(self):
        return self.str