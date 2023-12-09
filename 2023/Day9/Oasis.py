class Oasis:
    def __init__(self,file_name) -> None:
        self.histories: list[int] = []
        with open(file_name, 'r') as input_file:
            histories=[line.strip().split() for line in input_file]
            for h in histories:
                self.histories.append([int(v) for v in h])
        return

    def get_diffs(self, h: list[int]) -> list[list[int]]:
        '''
        Gets all the diffs for the given history
        '''
        diffs: list[list[int]] = [[v for v in h]]
        while len(list(filter(lambda v: v == 0, diffs[-1]))) != len(diffs[-1]):
            next_diffs: list[int] = []
            for i in range(len(diffs[-1])-1):
                next_diffs.append(diffs[-1][i+1]-diffs[-1][i])
            diffs.append(next_diffs)

        # Only need to return last number of each diff
        return diffs

    def sum_of_extrapolated(self, part: int) -> int:
        '''
        Calculate sum of extrapolated values
        '''
        result: int = 0
        for h in self.histories:
            diffs = self.get_diffs(h)
            next_num = 0
            for i in range(2,len(diffs)+1):
                if part == 1:
                    next_num = next_num + diffs[-i][-1]
                else:
                    next_num = diffs[-i][0] - next_num 
            result += next_num
        return result
    