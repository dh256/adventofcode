

class BoardingPass:
    row_codes = 7
    col_codes = 3
    
    def __init__(self,pass_code):
        self.row = self.get_row(pass_code[0:7])
        self.col = self.get_col(pass_code[7:])
        self.seat_id = BoardingPass.seat_id(self.row,self.col)

    @staticmethod
    def seat_id(row,col):
        return row * 8 + col

    def get_row(self,row_code):
        return self.binary_split(BoardingPass.row_codes,'F',row_code)

    def get_col(self,col_code):
        return self.binary_split(BoardingPass.col_codes,'L',col_code)

    def binary_split(self,bits,drop_lower_char,code):
        max_val = (1 << bits) - 1
        curr_val = max_val
        bit = bits
        for i in range(0,bits):
            code_char = code[i]
            if code_char == drop_lower_char:
                curr_val = curr_val & (max_val - (1 << (bit-1)))
            bit -= 1
        return curr_val


class BoardingPasses:
    def __init__(self,file_name):
        with open(file_name,"r") as input_file:
            self.boarding_passes = [BoardingPass(line.strip('\n')) for line in input_file]

    def highest_seat_id(self):
        '''
        Return highest seat id across all boarding passes
        '''
        return max(self.boarding_passes,key=lambda b : b.seat_id).seat_id

    def find_my_seat(self):
        # for each row (0 to 127), col (0 to 7) determine if pass exists for this seat
        # if not check if seat with seat_id 1 more and less than empty seat are occuppied
        # if so, return empty_seat_id
        for row in range(0,128):
            for col in range(0,8):
                seats = list(filter(lambda b : b.row == row and b.col == col,self.boarding_passes))
                if len(seats) == 0:
                    empty_seat_id = BoardingPass.seat_id(row,col)
                    # check if seat with seat_id 1 more and less than empty seat are occuppied
                    # if so, return empty_seat_id
                    if len(list(filter(lambda b : b.seat_id == empty_seat_id - 1,self.boarding_passes))) > 0 and len(list(filter(lambda b : b.seat_id == empty_seat_id + 1,self.boarding_passes))) > 0:  
                        return empty_seat_id     