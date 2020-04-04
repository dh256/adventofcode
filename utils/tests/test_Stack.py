import pytest
from copy import deepcopy
from adventofcode.utils.Stack import Stack

def test_Stack():
    s = Stack()
    s.push(1)
    assert(len(s) == 1)
    s.push(2)
    assert(len(s) == 2)
    assert(s.peek() == 2)
    assert(len(s) == 2) 
    assert(s.pop() == 2)
    assert(len(s) == 1) 
    s.push(3)
    s.push(4)
    s.push(5)
    r = deepcopy(s)
    s.push(6)
    r.push(8)
    assert(s.peek() == 6)
    assert(r.peek() == 8)