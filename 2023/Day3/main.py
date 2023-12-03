from Engine import Engine 
from Engine import Point

def main():
    engine = Engine('input.txt')
    print(f'{engine.sum_of_part_numbers()}')
    
if __name__ == '__main__':
    main()
            