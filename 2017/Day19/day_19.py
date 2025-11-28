from Day19 import Day19

def main() -> None:
    day19: Day19 = Day19('input.txt')
    result = day19.part1and2()
    print(f'Part 1: {result[0]}')
    print(f'Part 2: {result[1]}')

if __name__ == '__main__':
    main()