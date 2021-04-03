import re

class Homework():

    def __init__(self,file_name):
        with open(file_name, 'r') as homework_file:
            self._lines = [line.strip('\n') for line in homework_file]

    def sum_of_lines(self):
        sum = 0
        for line in self._lines:
            sum += self._calculate_line(line)
        return sum

    def _calculate_line(self,line):
        '''
        Calculate line. Note brackets change precendence
        '''
        # Remove space characters
        line = line.replace(' ','')
        result = None
        op = None
        curr_pos = 0
        while curr_pos < len(line):
            if line[curr_pos] == '(':
                brackets = self._calculate_line(line[curr_pos+1:])
                if op is None:
                    result = brackets[0]
                elif op == '+':
                    result += brackets[0]
                else:
                    result *= brackets[0]
                curr_pos += brackets[1]
            elif line[curr_pos] == ')':
                return (result,curr_pos+1)
            elif line[curr_pos] in ('*','+'):
                op = line[curr_pos]
            else:
                arg = int(line[curr_pos])
                if op is None:
                    result = arg
                elif op == '+':
                    result += arg
                else:
                    result *= arg
            curr_pos += 1
        return result    