 
''' 
David Hanley, December 2024
'''
from Day24 import Day24
from time import time
                            
def main():
    #d = Day24('tests/test1.txt')
    d = Day24('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')
    #start_time = time()
    #print(f'Part 2: {d.part2()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            