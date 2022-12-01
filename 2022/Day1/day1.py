from Elf import Elf

def main():
    file_name = 'input.txt'
    elves = Elf(file_name)
    print(f'Part1: {elves.most_calorific}')
    print(f'Part2: {elves.top3_most_calorific}')

if __name__ == '__main__':
    main()