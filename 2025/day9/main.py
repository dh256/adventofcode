import os
from day9 import Day9
                     
def main():
    file_name: str = os.path.dirname(__file__) + '/input.txt'
    d = Day9(file_name)
    result: tuple[int,int] = d.parts1and2()
    print(f'Part 1: {result[0]}')
    print(f'Part 2: {result[1]}')

if __name__ == '__main__':
    main()
            