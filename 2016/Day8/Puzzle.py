import numpy as np
import re

class Puzzle:

    def __init__(self, file_name, screen_width=50, screen_height=6):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = np.zeros(shape=(self.screen_height,self.screen_width),dtype=int)
        with open(file_name, "r") as file_input:
            self.instructions = [line.strip('\n') for line in file_input]

    def run(self):
        # runs puzzle instructions and returns number of pixels lit
        for instruction in self.instructions:
            if "rect" in instruction:
                self.process_rect_instruction(instruction)
            else:           # rotate instruction
                self.process_rotate_instruction(instruction)

        # return number of lit pixels
        return np.count_nonzero(self.screen == 1)

    def process_rotate_instruction(self, instruction):
        '''
        Process a rotate instruction
        '''
        try:
        
            move_row = True             # assume moving a row
            if "column" in instruction:
                move_row = False        # move column instead
            
            # get required movements - 1st number is row/column; 2nd number space to move row/column
            movements = re.findall(r'(\d+)', instruction)
            row_col = int(movements[0])
            spaces = int(movements[1])
            
            # move row/col

            if move_row:
                # buffer to hold new screen pixels
                new_row = np.zeros(shape=self.screen_width,dtype=int)
                
                # for a row, move all pixels spaces to the right up to the point where move would move off end of row
                for i in range(0,self.screen_width - spaces):
                    new_row[i+spaces] = self.screen[row_col][i]
                
                # any pixels that would fall off end wrap back around to start of row e.g 50 -> 0 + space; 49 -> 0 + space-1
                j = 0
                for i in range(self.screen_width - spaces,self.screen_width): 
                    new_row[j] = self.screen[row_col][i]
                    j += 1
                
                # update screen with new pixels
                for i in range(0,self.screen_width): 
                    self.screen[row_col][i] = new_row[i]

            else:
                # buffer to hold new screen pixels
                new_col = np.zeros(shape=self.screen_height,dtype=int)
                
                # for a column, move all pixels spaces down up to the point where move would move off bottom of column
                for i in range(0,self.screen_height - spaces):
                    new_col[i+spaces] = self.screen[i][row_col]
                
                # any pixels that would fall off bottom wrap back around to top of column e.g 50 -> 0 + space; 49 -> 0 + space-1
                j = 0
                for i in range(self.screen_height - spaces,self.screen_height): 
                    new_col[j] = self.screen[i][row_col]
                    j += 1
                
                # update screen with new pixels
                for i in range(0,self.screen_height): 
                    self.screen[i][row_col] = new_col[i]
        
        except Exception as e:
            print(e)

    def process_rect_instruction(self, instruction):
        '''
        Process a rect instruction
        '''
        # extract rect dimensions
        rect_dims = re.findall(r'(\d+)', instruction)
        width = int(rect_dims[0])
        height = int(rect_dims[1])
        
        # turn rect pixels on (starts at 0,0)
        for w in range(0,width):
            for h in range(0,height):
                self.screen[h][w] = 1

    def __str__(self):
        '''
        Output Puzzle Screen
        '''
        output=""
        for row in range(0,self.screen_height):
            for col in range(0,self.screen_width):
                if self.screen[row][col] == 0:
                    output += '.'
                else:
                    output += '#'
            output += '\n'
        return output