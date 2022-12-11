from MonkeyInTheMiddle import Monkeys

def main():
    monkeys = Monkeys('input.txt')
    print(monkeys.calc_monkey_business(20,True))

    monkeys = Monkeys('input.txt')
    print(monkeys.calc_monkey_business(10000,False))

if __name__ == '__main__':
    main()