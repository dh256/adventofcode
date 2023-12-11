from Universe import Universe

def main():
    universe = Universe('input.txt',2)
    print(f'Part 1: {universe.sum_shortest_paths()}')
    
    universe = Universe('input.txt',1000000)
    print(f'Part 2: {universe.sum_shortest_paths()}')

if __name__ == '__main__':
    main()
            