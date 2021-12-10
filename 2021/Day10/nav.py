class Nav:
    open_brackets = ('(','[','{','<')
    close_brackets = (')',']','}','>')
    open_close_bracket_map = {'(': ')', '<': '>', '{': '}', '[': ']'}
    syntax_error_score_table = {')': 3, ']': 57, '}': 1197, '>': 25137}
    auto_complete_score_table = {')': 1, ']': 2, '}': 3, '>': 4}
    
    def __init__(self,filename):
        with open(filename,'r') as input_file:
            self.lines = [line.strip('\n') for line in input_file]

    def calc_scores(self):
        part1_score = 0
        part2_scores = []
        for line in self.lines:
            open_bracks = []        # holds a stack of open brackets, Last in list First one out
            for c in line: 
                if c in Nav.open_brackets:
                    # push onto end of list
                    open_bracks.append(c)
                else:
                    # does close bracket match last open bracket
                    if Nav.open_close_bracket_map[open_bracks[-1]] == c:
                        # match - remove last item in list
                        open_bracks.pop()
                    else:
                        # not a match, look up score for c and stop processing line
                        part1_score += Nav.syntax_error_score_table[c]
                        break
            else:
                # get here have an incomplete line, need this for part 2
                # find all missing matching close brackets for remaining open brackets
                # and calculate line score, append this to part2_scores list 
                line_score = 0
                for c in open_bracks[::-1]:
                    close_brack = Nav.open_close_bracket_map[c]
                    line_score = line_score * 5 + Nav.auto_complete_score_table[close_brack]
                part2_scores.append(line_score)
        
        # sort part 2 scores and extract middle score
        part2_score = sorted(part2_scores)[len(part2_scores) // 2]

        return (part1_score,part2_score)

    