from Simulation import Simulation

sim = Simulation("input.txt")
sim.run()
print(sim.houses_visited_more_than(0))