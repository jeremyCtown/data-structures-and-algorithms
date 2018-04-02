import pytest
from stack import Stack

@pytest.fixture
def empty_stack():
    return Stack()

@pytest.fixture
def small_stack():
    s= Stack()
    s.push(4)
    s.push(5)
    s.push(6)
    s.push(7)
    s.push(8)
    return s

@pytest.fixture
def large_stack():
    s = Stack()

    for num in range(1000):
        s.push(num)

    return s

