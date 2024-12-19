 
''' 
David Hanley, December 202
'''
from Day19 import Day19
from time import time
                            
def main():
    d = Day19('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')
    start_time = time()
    print(f'Part 2: {d.part2()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            