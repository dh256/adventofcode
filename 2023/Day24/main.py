from Hailstones import Hailstones

def main():
    min_xy = 200000000000000
    max_xy = 400000000000000
    hailstones = Hailstones('input.txt')
    print(f'Part 1: {hailstones.part1(min_xy,max_xy)}')

if __name__ == '__main__':
    main()
            