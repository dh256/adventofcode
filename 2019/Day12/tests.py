import pytest
from Point3D import Point3D
from Moons import Moons

test_moons=[("test1.txt",[("Io",Point3D(-1,0,2)),("Europa",Point3D(2,-10,-7)),("Ganymede",Point3D(4,-8,8)),("Callisto",Point3D(3,5,-1))]),
                ("test2.txt",[("Io",Point3D(-8,-10,0)),("Europa",Point3D(5,5,10)),("Ganymede",Point3D(2,-7,3)),("Callisto",Point3D(9,-8,-3))])
                ]

total_energy_data=[("test1.txt",10,179),("test2.txt",100,1940)]

move_moons_data=[
    ("test1.txt",1,[Point3D(2,-1,1),Point3D(3,-7,-4),Point3D(1,-7,5),Point3D(2,2,0)]),
    ("test1.txt",10,[Point3D(2,1,-3),Point3D(1,-8,0),Point3D(3,-6,1),Point3D(2,0,4)]),
    ("test2.txt",100,[Point3D(8,-12,-9),Point3D(13,16,-3),Point3D(-29,-11,-1),Point3D(16,-13,23)])
]

energy_data=[
    ("test1.txt",[3,19,20,9],[0,0,0,0]),
    ("test2.txt",[18,20,12,20],[0,0,0,0]),
]

@pytest.mark.parametrize("filename,test_moons",test_moons)
def test_moon_input(filename,test_moons):
    moons = Moons(filename)
    for i in range(0,4):
        assert(moons.moons[i].name == test_moons[i][0])
        assert(moons.moons[i].position == test_moons[i][1])

@pytest.mark.parametrize("filename,potential,kinetic",energy_data)
def test_energy(filename,potential,kinetic):
    moons = Moons(filename)
    for i in range(0,4):
        assert(moons.moons[i].potential_energy() == potential[i])
        assert(moons.moons[i].kinetic_energy() == kinetic[i])

@pytest.mark.parametrize("filename,time,positions",move_moons_data)
def test_move_moons(filename,time,positions):
    moons = Moons(filename)
    moons.move_moons(time)
    for i in range(0,4):
        assert(moons.moons[i].position == positions[i])

@pytest.mark.parametrize("filename,time,total_energy",total_energy_data)
def test_total_energy(filename,time,total_energy):
    moons = Moons(filename)
    moons.move_moons(time)
    assert(moons.total_energy() == total_energy)