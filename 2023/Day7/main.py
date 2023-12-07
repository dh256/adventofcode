from Camel import Camel

def main():
    camel = Camel('tests/input.txt',1)
    print(f'Part 1: {camel.total_winnings()}')
    
    camel = Camel('input.txt',2)
    print(f'Part 2: {camel.total_winnings()}')
    
if __name__ == '__main__':
    main()
            