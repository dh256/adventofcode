'''
David Hanley, November 2024
'''
from Day20 import Day20
                            
def main():
    d = Day20()
    least_presents = 33100000
    result = d.solution(least_presents)
    print(f'Part 1: {result[0]}')
    print(f'Part 2: {result[1]}')

if __name__ == '__main__':
    main()
            