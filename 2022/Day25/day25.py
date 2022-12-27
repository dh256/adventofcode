"""
Name: day25.py
Author: David Hanley
Date: 26-Dec-2022
"""
from SNAFU import SNAFU, SNAFUNumber

def main():
    snafu = SNAFU('input.txt')
    print(f'{snafu.calculate_sum()}')

if __name__ == '__main__':
    main()