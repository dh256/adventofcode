from Orbits import Orbits
import pytest

testdata = {
    ("test1.txt",1),
    ("test2.txt",42)    
}

testdata2 = {
    ("test3.txt",4)  
}

@pytest.mark.parametrize("filename,expectedresult",testdata)
def test_orbits(filename, expectedresult):
    assert(Orbits(filename).total_orbits() == expectedresult)

@pytest.mark.parametrize("filename,expectedresult",testdata2)
def test_shortest_distance(filename, expectedresult):
    assert(Orbits(filename).shortest_distance() == expectedresult)