import math

class Module:
    def __init__(self,mass):
        self.mass = mass

    def fuel(self):
        return math.trunc(self.mass / 3) - 2 

    def fuel2(self):
        total_fuel = 0
        new_fuel = self.mass
        while True:
            new_fuel = math.trunc(new_fuel / 3) - 2 
            if new_fuel > 0:
                total_fuel += new_fuel
            else:
                return total_fuel

class Modules:
    def __init__(self,filename):
        with open(filename,"r") as data:
            self.modules = [Module(int(line.strip('\n'))) for line in data]
    
    def total_fuel(self):
        fuel = 0
        for module in self.modules:
            fuel += module.fuel()
        return fuel

    def total_fuel2(self):
        fuel = 0
        for module in self.modules:
            fuel += module.fuel2()
        return fuel
