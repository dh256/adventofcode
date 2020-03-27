from Moons import Moons

# Part1
moons = Moons("input.txt")
moons.move_moons(1000)
print(f'Total Energy = {moons.total_energy()}')