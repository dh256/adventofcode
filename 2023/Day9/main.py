from Oasis import Oasis

def main():
    oasis = Oasis('input.txt')
    print(f'Part 1: {oasis.sum_of_extrapolated(1)}')
    print(f'Part 2: {oasis.sum_of_extrapolated(2)}')

if __name__ == '__main__':
    main()
            