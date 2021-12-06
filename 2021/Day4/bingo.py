import re
from colorama import Fore, Style

class Board:
    def __init__(self,id):
        self._id = id
        self.rows = 5
        self.cols = 5
        self.entries = []       # list of board entries

    def add_row(self,row):
        self.entries.append(row)
    
    def __str__(self):
        output_str = f'Board {self._id}\n'
        for row in self.entries:
            for entry in row:
                if entry.marked:
                    output_str += f'{Style.BRIGHT}{Fore.GREEN}{entry.num}{Fore.RESET}{Style.RESET_ALL} '
                else:
                    output_str += f'{Fore.RED}{entry.num}{Fore.RESET} '
            output_str += '\n'
        return output_str

    def __hash__(self) -> int:
        return self._id

    @property
    def id(self):
        return self._id
    
    @property
    def unmarked_sum(self):
        ''' Return sum of all unmarked entries 
        '''
        unmarked_sum = 0
        for row in self.entries:
            for entry in row:
                if not entry.marked:
                    unmarked_sum += entry.num

        return unmarked_sum

    @property
    def bingo(self):
        '''
        Return whether board is BINGO! i.e. one row or one column is all marked
        '''
        for row in self.entries:
            for entry in row:
                if not entry.marked:
                    break
            else:
                return True
         
        # check columns
        for col in range(0,self.cols):
            for row in range(0,self.rows):
                if not self.entries[row][col].marked:
                    break
            else: 
                return True 

    def match(self,num):
        for row in self.entries:
            for entry in row:
                if entry.num == num:
                    entry.mark()
                

class BoardEntry:
    def __init__(self,num):
        self._num = num
        self._marked = False

    @property
    def num(self):
        return self._num

    @property 
    def marked(self):
        return self._marked

    def mark(self):
        self._marked = True

class Bingo:

    def __init__(self,filename):
        with open(filename,'r') as input_file:
            lines = [line.strip('\n') for line in input_file]
            
            # first line is the numbers that will be drawn
            self.numbers = [int(num) for num in re.findall(r'\d+',lines[0])]

            # next sets are the boards - start at line 2, when a blank line is encountered, start a new board
            self.boards = []
            curr_board = 0
            board = Board(curr_board)
            for curr_line in range(2,len(lines)):
                if len(lines[curr_line]) == 0:
                    self.boards.append(board)
                    curr_board += 1
                    board = Board(curr_board)
                else:
                    row = [BoardEntry(int(num)) for num in re.findall(r'\d+',lines[curr_line])]
                    board.add_row(row)
            self.boards.append(board)         
            
    def play(self,last_mode=False):
        # lets play bingo!
        for num in self.numbers:
            # go through each board and mark numbers
            boards_to_remove = []                          # needed for last mode (Part 2)         
            for board in self.boards:
                board.match(num)    
                # check if board is calling bingo
                if board.bingo:
                    if not last_mode or len(self.boards) == 1:      # if first mode or len remaining boards is 1
                        # calculate final score
                        # sum all unmarked numbers on board and multiply by num
                        score = board.unmarked_sum * num
                        return score
                    else:
                        boards_to_remove.append(board.id)

            # if last mode and board(s) to remove, then remove them
            if last_mode and len(boards_to_remove) > 0:
                for id in boards_to_remove:
                    for board_idx in range(len(self.boards)-1,-1,-1):
                        if self.boards[board_idx].id == id:
                            self.boards.pop(board_idx)
