"""
Name: SNAFU.py
Author: David Hanley
Date: 26-Dec-2022

Note:
To Decimal working
To SNAFU not working, struggling to get my head around this
"""
from collections import deque

class SNAFUNumber:
    base: int = 5
    double_neg: chr = '='
    single_neg: chr = '-'
    
    def __init__(self,num: str):
        self.num = num

    def to_decimal(self) -> int:
        '''
        Convert this SNAFU number to decimal
        '''
        mult = 1
        dec_number = 0
        for index in range(len(self.num)-1,-1,-1):
            if self.num[index].isnumeric():
                dec_digit = int(self.num[index])
            else:
                if self.num[index] == SNAFUNumber.double_neg:
                    dec_digit = -2
                else:
                    dec_digit = -1
            dec_number += (dec_digit * mult)
            mult *= SNAFUNumber.base
        return dec_number

    @classmethod
    def carry_snafu_digit(cls, num, index, digit):
        try:
            num[index] += digit
        except IndexError:
            num.append(digit)

    @classmethod
    def insert_snafu_digit(cls, num, index, digit):
        try:
            num[index] = digit
        except IndexError:
            num.append(digit)

    @classmethod
    def to_snafu(cls, number: int):
        '''
        Convert given decimal number returning a SNAFUNumber
        '''
        num = [0]
        curr_index = 0
        while number > 0:
            candidate_dig = number % SNAFUNumber.base
            if candidate_dig in range(0,3):           
                SNAFUNumber.carry_snafu_digit(num, curr_index, candidate_dig)
            else:
                if candidate_dig == 3:
                    SNAFUNumber.carry_snafu_digit(num, curr_index, -2)
                else:
                    SNAFUNumber.carry_snafu_digit(num, curr_index, -1)
                
                SNAFUNumber.carry_snafu_digit(num, curr_index+1, 1)
            
            # round up (only ever curr_index+1 and beyond)
            for index in range(curr_index,len(num)):
                if num[index] == 3:
                    SNAFUNumber.insert_snafu_digit(num, index, -2)
                    SNAFUNumber.carry_snafu_digit(num, index+1, 1)
                elif num[index] == 4:
                    SNAFUNumber.insert_snafu_digit(num, index, -1)
                    SNAFUNumber.carry_snafu_digit(num, index+1, 1)
                    
            number = number // SNAFUNumber.base
            curr_index += 1
            
        # reverse and map -ve nums to required chars
        output = str()
        for digit in num[::-1]:
            if digit == -2:
                output += '='
            elif digit == -1:
                output += '-'
            else:
                output += f'{digit}'
        return output


    def __str__(self) -> str:
        return self.num

class SNAFU:
    def __init__(self, file_name) -> None:
        with open(file_name, 'r') as input_file:
            self.numbers: list(SNAFUNumber) = [SNAFUNumber(line.strip('\n')) for line in input_file]
        
    def calculate_sum(self) -> str:
        '''
        Calculates the sum of all SNAFU numbers as a SNAFU number
        '''
        result = SNAFUNumber.to_snafu(sum([number.to_decimal() for number in self.numbers]))
        return result
                
