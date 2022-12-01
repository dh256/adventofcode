from Elf import Elf

def main():
    file_name = 'input.txt'
    elves = Elf(file_name)
    print(f'Part1: {elves.topn_most_calorific(1)}')
    print(f'Part2: {elves.topn_most_calorific(3)}')

if __name__ == '__main__':
    main()