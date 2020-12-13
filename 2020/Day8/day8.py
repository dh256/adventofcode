from Console import Console, InfiniteLoopDetectedError

console = Console("input.txt")

# part 1
try:
    console.run()
    raise Exception("Should not get here!")
except InfiniteLoopDetectedError:
    print(console.accumulator)
except Exception:
    print('Part 1 failed')

# part 2
try:
    console.run2()
    print(console.accumulator)
except Exception:
    print('Part 2 failed')