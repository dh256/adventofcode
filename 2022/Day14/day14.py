from Cave import Cave

def main():
    cave = Cave('input.txt')
    print(f'{cave.falling_sand()}')

    # reset
    cave = Cave('input.txt')
    print(f'{cave.falling_sand2()}')

if __name__ == '__main__':
    main()