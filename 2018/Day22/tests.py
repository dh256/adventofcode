import pytest
from day22 import Point, RegionType, Cave

def test_pointeq():
    p1 = Point(0,0)
    p2 = Point(0,0)
    p3 = Point(1,0)
    p4 = Point(0,1)

    assert p1 == p2
    assert p1 != p3
    assert p1 != p4

def test_regiontype():
    e1 = RegionType(0)
    e2 = RegionType(1)
    e3 = RegionType(2)

    assert e2 == RegionType.WET   
    assert e1 == RegionType.ROCKY 
    assert e3 == RegionType.NARROW 

def test_cave():
    depth = 510
    target=Point(10,10)

    cave = Cave(target,depth)
    assert cave.risk_level() == 114