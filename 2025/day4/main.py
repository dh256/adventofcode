from day4 import Day4 
import os
                            
def main():
    filename = os.path.dirname(__file__) + '/input.txt'
    d = Day4(filename)
    print(f'Part 1: {d.part1()}')
    print(f'Part 2: {d.part2()}')

if __name__ == '__main__':
    main()
            