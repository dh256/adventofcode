 
''' 
David Hanley, December 2024
'''
from Day5 import Day5
                            
def main():
    d = Day5('input.txt')
    p1_result, invalid_pus = d.part1()
    print(f'Part 1: {p1_result}')
    print(f'Part 2: {d.part2(invalid_pus)}')

if __name__ == '__main__':
    main()
            