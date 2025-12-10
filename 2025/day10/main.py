import os 
from day10 import Day10
                            
def main():
    file_name: str = os.path.dirname(__file__) + '/input.txt'
    d = Day10(file_name)
    print(f'Part 1: {d.part1()}')
    print(f'Part 2: {d.part2()}')

if __name__ == '__main__':
    main()
            