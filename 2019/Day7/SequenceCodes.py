from itertools import permutations

class SequenceCodes:
    def __init__(self,permutation_from,permutation_to,length):
        # Get all permutations of [from..to] and length length 
        permutation_list = []
        for i in range(permutation_from,permutation_to+1):
            permutation_list.append(i) 
            self.codes = permutations(permutation_list, length) 