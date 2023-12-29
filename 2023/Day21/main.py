from Garden import Garden
from datetime import datetime, time


def main():
    garden = Garden('input.txt')
    start = datetime.now()
    print(f'Part 1: {garden.part1(128)} {datetime.now()-start}')

if __name__ == '__main__':
    main()
            