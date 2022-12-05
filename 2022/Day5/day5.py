from CrateStacks import CrateStacks, CraneType

def main():
    crate_stacks = CrateStacks('input.txt')
    crate_stacks.perform_moves(CraneType.CRATE_MOVER_9000)
    print(f'Part 1: {crate_stacks.top}')
    crate_stacks.reset()
    crate_stacks.perform_moves(CraneType.CRATE_MOVER_9001)
    print(f'Part 2: {crate_stacks.top}')

if __name__ == '__main__':
    main()