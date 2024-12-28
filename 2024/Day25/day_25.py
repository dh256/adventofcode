 
''' 
David Hanley, December 2024
'''
from Day25 import Day25
from time import time
                            
def main():
    d = Day25('input.txt')
    start_time = time()
    print(f'Part 1: {d.part1()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            