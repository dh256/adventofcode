 
''' 
David Hanley, December 2024
'''
from Day15 import Day15
from time import time
                            
def main():
    #d = Day15('tests/test1.txt')
    d = Day15('input.txt',1)
    start_time = time()
    print(f'Part 1: {d.solution()}; Excution Time: {(time()-start_time):.3f} s')
    
    d = Day15('input.txt',2)
    start_time = time()
    print(f'Part 2: {d.solution()}; Excution Time: {(time()-start_time):.3f} s')

if __name__ == '__main__':
    main()
            