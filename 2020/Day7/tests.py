import pytest
from Bags import Bags

test_data1=[("bright white bags contain 1 shiny gold bag.","bright white",[('shiny gold',1)]),
("faded blue bags contain no other bags.","faded blue",None),
("dark olive bags contain 3 faded blue bags, 4 dotted black bags.","dark olive",[("faded blue",3),("dotted black",4)])]
test_data2=[("test.txt",4)]

@pytest.mark.parametrize("bag_desc,colour,contents",test_data1)
def test_bags(bag_desc,colour,contents):
    assert(Bags._get_colour(bag_desc) == colour)
    assert(Bags._get_contents(bag_desc) == contents)
    
@pytest.mark.parametrize("file_name,num_bags",test_data2)
def test_contains(file_name,num_bags):
    bags = Bags(file_name)
    assert(bags.contains() == num_bags)
