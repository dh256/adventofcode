from Universe import Universe

def main():
    universe = Universe('input.txt')
    print(f'Part 1: {universe.sum_shortest_paths()}')

if __name__ == '__main__':
    main()
            