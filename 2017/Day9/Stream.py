class Stream:

    def __init__(self,filename):
        with open(filename, 'r') as input_file:
            self.chars = input_file.readline().strip('\n')

    def get_totals(self) -> tuple:
        '''
        Calculates total number of groups and group score
        '''
        in_garbage = False
        miss_next_char = False
        total_score = 0
        curr_group_score = 0
        groups = 0
        garbage_chars = 0       # Part 2
        for c in self.chars:
            if not miss_next_char:
                # Part 2
                if in_garbage:
                    if c not in ('!','>'):
                        garbage_chars += 1

                # Partr 1
                if c == '!' and in_garbage:
                    miss_next_char = True
                elif c == '<' and not in_garbage:
                    in_garbage = True
                elif c == '>' and in_garbage:
                    in_garbage = False
                elif c == '{' and not in_garbage:
                    groups += 1
                    curr_group_score += 1
                    total_score += curr_group_score
                elif c == '}' and not in_garbage:
                    curr_group_score -= 1
            else:
                miss_next_char = False

        return (groups,total_score,garbage_chars)