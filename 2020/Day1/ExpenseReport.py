import itertools

class ExpenseReport:

    def __init__(self,data_file):
        with open(data_file,'r') as input_file:
            self.entries = [int(line.strip('\n')) for line in input_file]

    def find_entries_sum_to(self,value,num_entries):
        '''
        Find num_entries that add to value and multiply together
        '''
        result = itertools.combinations(self.entries,num_entries)
        for r in result:
            if sum(r) == value:
                final_result = 1
                for i in r:
                    final_result *= i
                return final_result
