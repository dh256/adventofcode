from Day6 import Day6
import os
                            
def main():
    filename = os.path.dirname(__file__) + '/tests/input.txt'
    d = Day6(filename)
    print(f'Part 1: {d.part1()}')
    #print(f'Part 2: {d.part2()}')

if __name__ == '__main__':
    main()
            