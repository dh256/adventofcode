from Memory import Memory

def main():
    memory = Memory('input.txt')
    part1 = memory.restribute(1)

    # reset memory banks
    memory = Memory('input.txt')
    part2 = memory.restribute(2) - part1

    print(f'Part 1: {part1}; Part 2: {part2}')

if __name__ == '__main__':
    main()
