from Rucksack import Rucksack

def main():
    rucksack = Rucksack('input.txt')
    print(f'{rucksack.calc_priority_sum(1)}')
    print(f'{rucksack.calc_priority_sum(2)}')

if __name__ == '__main__':
    main()