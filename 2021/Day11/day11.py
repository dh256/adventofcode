from octopus import Octopus

octopus = Octopus('input.txt')
print(f'Part 1: {octopus.calc_flashes(100)}')

octopus2 = Octopus('input.txt')
print(f'Part 2: {octopus2.calc_all_flash()}')