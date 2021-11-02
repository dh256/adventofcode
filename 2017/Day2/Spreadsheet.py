import re
import itertools

class Spreadsheet:
    def __init__(self,file_name):
        self.sheet = []
        regex = re.compile(r"\d+")
        with open(file_name,"r") as input_file:
            for line in input_file:
                 nums = [int(num) for num in regex.findall(line.strip('\n'))]
                 self.sheet.append(nums)
                
    @property
    def check_sum(self):
        checksum = 0
        for row in self.sheet:
            checksum += max(row) - min(row)
        return checksum

    @property
    def check_sum2(self):
        checksum = 0
        for row in self.sheet:
            result = [i[0] // i[1] for i in itertools.permutations(row,2) if i[0] % i[1] == 0]
            checksum += result[0]
        return checksum
        