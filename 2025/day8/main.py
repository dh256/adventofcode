import os 
from day8 import Day8
                            
def main():
    filename = os.path.dirname(__file__) + '/input.txt'
    d = Day8(filename)
    #print(f'Part 1: {d.part1(1000)}')
    #print(f'Part 2: {d.part2(1000)}')
    result = d.parts1and2(1000)
    print(f'Part 1: {result[0]}')
    print(f'Part 2: {result[1]}')

if __name__ == '__main__':
    main()
            