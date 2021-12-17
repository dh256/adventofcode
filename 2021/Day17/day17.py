from probe import Probe

probe = Probe('input.txt')
highest_y, init_vels = probe.fire()
print(f'Part 1: {highest_y}')
print(f'Part 2: {init_vels}')