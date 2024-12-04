 
''' 
David Hanley, December 2024

Current Part 2 answer 17577149 is too low, tests passing
                      98826679 is too high, tests passing  
                      88802350 is correct answer but not sure how I get it. Used AG code
'''
from Day3 import Day3
                            
def main():
    #d = Day3('tests/test2.txt')
    d = Day3('input.txt')
    print(f'Part 1: {d.part1()}')
    print(f'Part 2: {d.part2()}')

if __name__ == '__main__':
    main()
            