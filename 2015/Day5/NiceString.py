import re

class NiceStrings():
    def __init__(self,filename: str):
        with open(filename,"r") as data:
            self.nice_strings = [NiceString(line.strip('\n')) for line in data]
    
    def count_nice_part1(self) -> int:
        result = [nice_string for nice_string in self.nice_strings if nice_string.is_nice_part1()]
        return len(result)

    def count_nice_part2(self) -> int:
        result = [nice_string for nice_string in self.nice_strings if nice_string.is_nice_part2()]
        return len(result)

class NiceString():
    def __init__(self, str):
        self.str = str

    def is_nice_part1(self) -> bool:
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
        vowels = len(vowels_found) >= 3
    
        # letters appear twice
        letters_twice_found = re.findall(letters_twice_reg_ex, self.str)
        appears_twice = len(letters_twice_found) > 0
        
        # contains
        contains_found = re.findall(contains_reg_ex,self.str)
        contains = len(contains_found) > 0

        return vowels and appears_twice and not contains

    def is_nice_part2(self) -> bool:
        '''
            Nice if:
                contains at least one letter which repeats with exactly one letter between them
                contains a pair of any two letters that appears at least twice in the string without overlapping
        '''
        repeat_with_one_between_reg_ex = r"([a-z])([a-z])\1"
        repeat_with_one_between = len(re.findall(repeat_with_one_between_reg_ex,self.str)) > 0

        pair_appears_twice_no_overlap = False
        for i in range(0,len(self.str)-1):
            search_str = self.str[i:i+2]
            if search_str in self.str[i+2:]:
                pair_appears_twice_no_overlap = True
                break

        return repeat_with_one_between and pair_appears_twice_no_overlap
