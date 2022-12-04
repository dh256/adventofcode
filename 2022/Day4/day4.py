from Space import Space

def main():
    space = Space('input.txt')
    print(f'{space.pairs_contained_within()}')
    print(f'{space.pairs_overlap_at_all()}')

if __name__ == '__main__':
    main()