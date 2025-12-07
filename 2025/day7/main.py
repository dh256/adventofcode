import os 
from day7 import Day7
                            
def main():
    filename = os.path.dirname(__file__) + '/input.txt'
    d = Day7(filename)
    print(f'Part 1: {d.part1()}')
    print(f'Part 2: {d.part2()}')

if __name__ == '__main__':
    main()
            