from HillClimbing import Hills 

def main():
    hills = Hills('input.txt')
    print(f'Part 1: {hills.find_location()}')
    print(f'Part 2: {hills.find_location2()}')

if __name__ == '__main__':
    main()