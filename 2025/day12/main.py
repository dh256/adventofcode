import os 
from day12 import Day12
                            
def main():
    file_name: str = os.path.dirname(__file__) + '/input.txt'
    d = Day12(file_name)
    print(f'Part 1: {d.part1()}')

if __name__ == '__main__':
    main()
            