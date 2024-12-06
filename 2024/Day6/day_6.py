''' 
David Hanley, December 2024
'''
from Day6 import Day6
                            
def main():
    d = Day6('input.txt')
    positions = d.part1()
    print(f'Part 1: {len(positions)}')
    print(f'Part 2: {d.part2(positions)}')

if __name__ == '__main__':
    main()
            