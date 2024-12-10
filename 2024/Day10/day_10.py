 
''' 
David Hanley, December 2024
'''
from Day10 import Day10
from time import time
                            
def main():
    d = Day10('input.txt')
    start_time = time()
    result_p1, result_p2 = d.solution()
    print(f'Part 1: {result_p1}')
    print(f'Part 2: {result_p2}')
    print(f'Excution Time: {(time()-start_time):.3f} s')


if __name__ == '__main__':
    main()
            